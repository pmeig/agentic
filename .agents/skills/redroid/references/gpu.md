# Redroid: GPU

Rendering is **software** (ANGLE on SwiftShader) with `auto` or `guest`. `host` needs a DRM render node (`/dev/dri/renderD128`) and
Mesa GBM: WSL2 has only `/dev/dxg`, so `host` fails (`no suitable EGLConfig found`, surfaceflinger restarts in a loop). Also,
Android's bionic Mesa GBM has no driver for NVIDIA's proprietary stack even on native Linux. Keep `auto`/`guest` on WSL2 and say
so in reports; do not claim acceleration. For GPU rendering on this PC use the Android Emulator (`-gpu host`), not Redroid.
