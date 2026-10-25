#!/usr/bin/env python3
"""Compare Copilot CLI runs on two git refs in disposable worktrees."""
import argparse,datetime,json,os,shlex,subprocess,sys,time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
KEYS={'usage','input_tokens','output_tokens','total_tokens','prompt_tokens','completion_tokens','cache_read_input_tokens','cache_creation_input_tokens','total_cost_usd','cost'}
def run(c,cwd,timeout=None): return subprocess.run(c,cwd=cwd,text=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=timeout,check=False)
def git(*a):
 p=run(['git',*a],ROOT)
 if p.returncode: raise RuntimeError(p.stderr.strip() or 'git failed')
 return p.stdout.strip()
def scan(x):
 r=[]
 if isinstance(x,dict):
  if KEYS.intersection(x): r.append(x)
  for v in x.values(): r.extend(scan(v))
 elif isinstance(x,list):
  for v in x: r.extend(scan(v))
 return r
def parse(s):
 r=[]
 for line in s.splitlines():
  try:r.extend(scan(json.loads(line.strip())))
  except (ValueError,TypeError):pass
 return max(r,key=len) if r else None
def main():
 ap=argparse.ArgumentParser(description=__doc__); ap.add_argument('--prompt',default='prompts/token-test-copilot.md'); ap.add_argument('--base',default='main'); ap.add_argument('--compare',default='chore/optimisation'); ap.add_argument('--output-dir',default='token-comparison-results'); ap.add_argument('--timeout',type=int,default=3600); ap.add_argument('--copilot-command',default=os.environ.get('COPILOT_COMMAND','copilot')); ap.add_argument('--dry-run',action='store_true'); a=ap.parse_args()
 pp=Path(a.prompt); pp=pp if pp.is_absolute() else ROOT/pp
 if not pp.is_file(): ap.error('Prompt file not found: '+str(pp))
 prompt=pp.read_text(encoding='utf-8'); out=Path(a.output_dir); out=out if out.is_absolute() else ROOT/out; out=out/('copilot-'+datetime.datetime.now().strftime('%Y%m%d-%H%M%S')); out.mkdir(parents=True,exist_ok=False); recs=[]; wts=[]
 try:
  for label,ref in [('base',a.base),('compare',a.compare)]:
   commit=git('rev-parse','--verify',ref+'^{commit}'); wt=out/('worktree-'+label); p=run(['git','worktree','add','--detach',str(wt),commit],ROOT)
   if p.returncode: raise RuntimeError(p.stderr.strip())
   wts.append(wt); (wt/'TOKEN-BENCHMARK-PROMPT.md').write_text(prompt,encoding='utf-8'); rec={'label':label,'ref':ref,'commit':commit,'started_at':datetime.datetime.now().isoformat()}
   if a.dry_run: rec.update(status='dry-run',duration_seconds=0,usage=None)
   else:
    start=time.monotonic(); cmd=shlex.split(a.copilot_command)+['-p',prompt]
    try:
     p=subprocess.run(cmd,cwd=wt,text=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=a.timeout,check=False); rec.update(status='completed' if p.returncode==0 else 'failed',return_code=p.returncode,duration_seconds=round(time.monotonic()-start,2),usage=parse(p.stdout+'\n'+p.stderr)); (out/(label+'.stdout.log')).write_text(p.stdout,encoding='utf-8'); (out/(label+'.stderr.log')).write_text(p.stderr,encoding='utf-8')
    except subprocess.TimeoutExpired as e:
     rec.update(status='timeout',duration_seconds=round(time.monotonic()-start,2),usage=None); (out/(label+'.stdout.log')).write_text(str(e.stdout or ''),encoding='utf-8'); (out/(label+'.stderr.log')).write_text(str(e.stderr or ''),encoding='utf-8')
   recs.append(rec)
   if not a.dry_run and rec['status']!='completed': break
 finally:
  for wt in reversed(wts): run(['git','worktree','remove','--force',str(wt)],ROOT)
 report={'tool':'GitHub Copilot CLI','created_at':datetime.datetime.now().isoformat(),'base_ref':a.base,'compare_ref':a.compare,'prompt':str(pp),'note':'null usage means no parseable usage metrics were emitted, not zero usage.','runs':recs}; (out/'comparison.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf-8'); print('Results:',out)
 for r in recs: print(r['label'],r['ref'],r['status'],'duration=',r.get('duration_seconds'),'usage=',json.dumps(r.get('usage')))
 if not a.dry_run and any(r.get('usage') is None for r in recs): print('No recognized token/cost fields in Copilot output; consult Copilot usage dashboard.',file=sys.stderr)
 return 0 if a.dry_run or all(r['status']=='completed' for r in recs) else 1
if __name__=='__main__':
 try: raise SystemExit(main())
 except (RuntimeError,OSError,ValueError) as e: print('error:',e,file=sys.stderr); raise SystemExit(2)
