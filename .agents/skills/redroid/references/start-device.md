# Redroid: start a device

Android runs as a Docker container sharing the host kernel: no VM, boot in about 30 s without snapshot. Used by `qa` as the
Android device of the Maestro e2e (`e2e-maestro-best-practices`, `e2e-run`, `e2e-parallelism-init`). Project scripts, when the
project has them: `e2e/android/redroid/{check-host,start,stop}.sh`.

```bash
docker run -d --privileged --name rd1 redroid/redroid:14.0.0-latest \
  androidboot.use_memfd=true androidboot.redroid_gpu_mode=guest \
  androidboot.redroid_width=1080 androidboot.redroid_height=2280 androidboot.redroid_dpi=420 androidboot.redroid_fps=30
until [ "$(docker exec rd1 getprop sys.boot_completed | tr -d '\r')" = 1 ]; do sleep 2; done   # works before adb is reachable
```

- Image `redroid/redroid:14.0.0-latest` = Android 14. `--privileged` is required. One container per device, one adb serial each.
- `docker logs` ending with `No controlling tty` and a shell prompt is normal; judge by `sys.boot_completed`.
- Settings applied by the project script after boot: soft keyboard off, animations off (`window_animation_scale`,
  `transition_animation_scale`, `animator_duration_scale` = 0), `captive_portal_mode 0`.
- Count: from `e2e-parallelism-init` (ascending from 1, no ceiling), one container per shard of `maestro --shard-split`.
- Always remove with the project `stop.sh` (keeps logs, removes containers, relays and networks by label) in an `always()` step.

Also load `references/prerequisites.md` when the container exits right after launch, and `references/networks-adb.md` for adb.
