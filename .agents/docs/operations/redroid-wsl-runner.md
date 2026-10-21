# Redroid on the remote WSL2 runner

## Purpose

Use this handoff when diagnosing the self-hosted GitHub Actions runner on the remote Windows PC. This document is for host-side investigation; it does not authorize changing the runner, stopping WSL, triggering CI, or editing the external repositories.

## Observed CI evidence

- Repository: `pmeig/budget`, branch `claude/budget-spending-stats-page-0y95ko`.
- Failed run: [39611160947](https://github.com/pmeig/budget/actions/runs/39611160947).
- The workflow pins `pmeig/github-actions/actions/android/redroid` at `6aac8b50c142c0ec80a1eb4d8af923009d05bbd2`.
- Runner kernel reported: `6.6.87.2-microsoft-standard-WSL2`.
- Runner reported 24,034 MB total and 17,200 MB available memory; the requested two Redroid devices fit the action's resource calculation.
- The Redroid container exited with status `129` about 14 seconds after launch. ADB found no device. The container log showed `No controlling tty`, a shell prompt, and no Android boot completion.
- The workflow already requests `androidboot.redroid_gpu_mode=auto` and `androidboot.use_memfd=true`.

The log does not include `/proc/filesystems`, the running kernel configuration, or relevant host `dmesg` output, so the kernel diagnosis below is a strong lead, not a proven cause.

## Primary investigation: WSL kernel support

Redroid's [WSL2 deployment guide](https://github.com/remote-android/redroid-doc/blob/master/deploy/wsl.md) requires a custom WSL kernel with BinderFS and DMA-BUF support. The Microsoft WSL 6.6 standard configuration checked for this investigation has Binder IPC and DMA-BUF heaps disabled. The runner's reported kernel identity is consistent with WSL2, but the exact running configuration must be checked on the runner.

On the remote runner, inspect before changing anything:

1. Record `uname -a` and the WSL kernel version.
2. Check whether `binder` appears in `/proc/filesystems`.
3. If available, inspect `/proc/config.gz` for `CONFIG_ANDROID_BINDER_IPC`, `CONFIG_ANDROID_BINDERFS`, `CONFIG_DMABUF_HEAPS`, and `CONFIG_DMABUF_HEAPS_SYSTEM`.
4. Review `dmesg` for binder, DMA-BUF, ashmem, memfd, and Redroid-related errors.

If required support is missing, prepare a custom WSL kernel from source matching the runner's WSL kernel version. Start from the corresponding Microsoft WSL config and enable at least:

```text
CONFIG_ANDROID=y
CONFIG_ANDROID_BINDER_IPC=y
CONFIG_ANDROID_BINDERFS=y
CONFIG_ANDROID_BINDER_DEVICES="binder,hwbinder,vndbinder"
CONFIG_DMABUF_HEAPS=y
CONFIG_DMABUF_HEAPS_SYSTEM=y
```

Keep IPv6 enabled and apply the additional IPv6 options required by the Redroid WSL2 guide. Ashmem is optional when Redroid's `androidboot.use_memfd=true` path works; memfd does not replace BinderFS or DMA-BUF.

## Safe installation and rollback

- Back up the existing `%USERPROFILE%\.wslconfig` and the current kernel image before installing anything.
- Add the custom kernel path to the existing `[wsl2]` section; preserve all existing settings, including `memory`, `processors`, and GPU settings.
- Use a maintenance window. `wsl --shutdown` stops every running WSL distribution, including the runner; do not run it while a job is active.
- Restart WSL and the runner only after confirming the maintenance window. Verify the new kernel with `uname -a` and confirm BinderFS is available before scheduling CI.
- Keep the old kernel and `.wslconfig` backup available for rollback.

Do not trigger a workflow or E2E run without explicit authorization. Read-only kernel diagnostics can be collected first.

## GPU investigation

Redroid documents `androidboot.redroid_gpu_mode` values `auto`, `host`, and `guest`; `host` requests GPU rendering, while `guest` uses software rendering. The current action requests `auto`, but it does not explicitly pass WSL's `/dev/dxg` device or `/usr/lib/wsl` libraries.

The prior Android Emulator action used `/dev/dxg`, WSL libraries, and Mesa D3D12 environment settings. Do not assume that setup works for Redroid: its Android renderer and kernel requirements differ.

After the kernel prerequisites are satisfied:

1. Inspect whether `/dev/dxg` and `/usr/lib/wsl/lib` exist on the remote WSL runner.
2. Check Redroid's current documented GPU path and whether the required device and driver stack are supported in this WSL configuration.
3. Do not switch to `host` solely because Docker can see `/dev/dxg`. Confirm that Android boots and that the renderer is actually using the GPU.
4. Preserve `auto` as the fallback until a supported Redroid GPU path is verified. If GPU rendering is unavailable, report that explicitly rather than claiming acceleration.

## Completion criteria

- The remote runner boots the intended custom WSL kernel and exposes the required BinderFS and DMA-BUF support.
- An authorized CI run shows the Redroid container staying active, ADB connecting, and `sys.boot_completed` returning `1`.
- GPU acceleration is reported only after the Redroid renderer itself is verified; device visibility alone is insufficient.
- The original kernel and WSL configuration remain available for rollback.

## References

- [Redroid WSL2 deployment guide](https://github.com/remote-android/redroid-doc/blob/master/deploy/wsl.md)
- [Redroid configuration and troubleshooting](https://github.com/remote-android/redroid-doc)
- [Microsoft WSL2 Linux kernel](https://github.com/microsoft/WSL2-Linux-Kernel)
