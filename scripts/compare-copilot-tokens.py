#!/usr/bin/env python3
"""Run the same Copilot CLI prompt in disposable worktrees for two refs.

Usage: python scripts/compare-copilot-tokens.py --base main --compare chore/optimisation
Metrics are reported only if the installed CLI actually emits parseable usage fields.
"""
import argparse, datetime, json, os, shlex, subprocess, sys, time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
KEYS = {"usage", "input_tokens", "output_tokens", "total_tokens", "prompt_tokens", "completion_tokens", "cache_read_input_tokens", "cache_creation_input_tokens", "total_cost_usd", "cost"}

def run(cmd, cwd, timeout=None):
    return subprocess.run(cmd, cwd=cwd, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=timeout, check=False)

def git(*args):
    p = run(["git", *args], ROOT)
    if p.returncode: raise RuntimeError(p.stderr.strip() or "git command failed")
    return p.stdout.strip()

def usage(value):
    found=[]
    if isinstance(value, dict):
        if KEYS.intersection(value): found.append(value)
        for v in value.values(): found.extend(usage(v))
    elif isinstance(value, list):
        for v in value: found.extend(usage(v))
    return found

def parse_usage(text):
    found=[]
    for line in text.splitlines():
        try: found.extend(usage(json.loads(line.strip())))
        except (json.JSONDecodeError, TypeError): pass
    return max(found, key=len) if found else None

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--prompt', default='prompts/token-test-copilot.md')
    ap.add_argument('--base', default='main'); ap.add_argument('--compare', default='chore/optimisation')
    ap.add_argument('--output-dir', default='token-comparison-results'); ap.add_argument('--timeout', type=int, default=3600)
    ap.add_argument('--copilot-command', default=os.environ.get('COPILOT_COMMAND','copilot'))
    ap.add_argument('--dry-run', action='store_true'); a=ap.parse_args()
    pp=Path(a.prompt); pp=pp if pp.is_absolute() else ROOT/pp
    if not pp.is_file(): ap.error('Prompt file not found: '+str(pp))
    prompt=pp.read_text(encoding='utf-8'); out=Path(a.output_dir); out=out if out.is_absolute() else ROOT/out
    out=out/('copilot-'+datetime.datetime.now().strftime('%Y%m%d-%H%M%S')); out.mkdir(parents=True,exist_ok=False)
    records=[]; worktrees=[]
    try:
        for label,ref in [('base',a.base),('compare',a.compare)]:
            commit=git('rev-parse','--verify',ref+'^{commit}'); wt=out/('worktree-'+label)
            p=run(['git','worktree','add','--detach',str(wt),commit],ROOT)
            if p.returncode: raise RuntimeError(p.stderr.strip())
            worktrees.append(wt); (wt/'TOKEN-BENCHMARK-PROMPT.md').write_text(prompt,encoding='utf-8')
            rec={'label':label,'ref':ref,'commit':commit,'started_at':datetime.datetime.now().isoformat()}
            if a.dry_run: rec.update(status='dry-run',duration_seconds=0,usage=None)
            else:
                cmd=shlex.split(a.copilot_command)+['-p',prompt]; start=time.monotonic()
                try:
                    p=subprocess.run(cmd,cwd=wt,text=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=a.timeout,check=False)
                    rec.update(status='completed' if p.returncode==0 else 'failed',return_code=p.returncode,duration_seconds=round(time.monotonic()-start,2),usage=parse_usage(p.stdout+'\n'+p.stderr))
                    (out/(label+'.stdout.log')).write_text(p.stdout,encoding='utf-8'); (out/(label+'.stderr.log')).write_text(p.stderr,encoding='utf-8')
                except subprocess.TimeoutExpired as e:
                    rec.update(status='timeout',duration_seconds=round(time.monotonic()-start,2),usage=None)
                    (out/(label+'.stdout.log')).write_text(str(e.stdout or ''),encoding='utf-8'); (out/(label+'.stderr.log')).write_text(str(e.stderr or ''),encoding='utf-8')
            records.append(rec)
            if not a.dry_run and rec['status']!='completed': break
    finally:
        for wt in reversed(worktrees): run(['git','worktree','remove','--force',str(wt)],ROOT)
    report={'tool':'GitHub Copilot CLI','created_at':datetime.datetime.now().isoformat(),'base_ref':a.base,'compare_ref':a.compare,'prompt':str(pp),'note':'null usage means no parseable metrics were emitted; it does not mean zero usage.','runs':records}
    (out/'comparison.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print('Results:',out)
    for r in records: print(r['label'],r['ref'],r['status'],'duration=',r.get('duration_seconds'),'usage=',json.dumps(r.get('usage')))
    if not a.dry_run and any(r.get('usage') is None for r in records): print('Copilot output exposed no recognized usage metrics; consult your Copilot usage dashboard.',file=sys.stderr)
    return 0 if a.dry_run or all(r['status']=='completed' for r in records) else 1

if __name__=='__main__':
    try: raise SystemExit(main())
    except (RuntimeError,OSError,ValueError) as e: print('error:',e,file=sys.stderr); raise SystemExit(2)
