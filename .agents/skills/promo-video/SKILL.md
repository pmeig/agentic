---
name: promo-video
description: sales: promotional video script, storyboard, app recording, ffmpeg montage, captions, export.
---

# Promotional video

## 1. Concept and script

- One video = **one idea** and one call to action. Hook in the first 3 seconds (problem or result), proof by showing the real
  product, end on the action. Lengths: 15 / 30 / 60 s cuts of the same story; formats 9:16, 1:1, 16:9.
- Write `promotion/video/<name>/storyboard.md`: a table of shots (number, duration, image or recording, on-screen text, voice-over,
  caption, sound). Voice-over about 2.5 words per second; captions lines of at most 42 characters.
- Use the demo account and seeded data; no real personal data, token or email visible.

## 2. Record the real app

- **Web**: Playwright with `recordVideo` (size 1280x720 or the target viewport) or scripted screenshots; drive the flow by script
  so the take is repeatable (`e2e-playwright-best-practices`); slow the pointer, hide devtools, fixed window size.
- **Android**: emulator with `adb shell screenrecord` or `scrcpy --record`, touches visible (`adb shell settings put system show_touches 1`),
  a script or a Maestro flow to drive it (`e2e-maestro-best-practices`), animations on, demo mode in the status bar
  (`adb shell cmd statusbar demo` or the System UI demo mode).
- **iOS**: `xcrun simctl io booted recordVideo`, status bar override with `xcrun simctl status_bar booted override`.
- Several short takes beat one long one; record at 60 fps when possible and at the target resolution (portrait for 9:16).
- Ask `front` for the demo account, data and the exact flow; ask `qa` for a stable environment.

## 3. Montage with ffmpeg (repeatable commands, kept in the folder)

Keep every command in `promotion/video/<name>/build.sh` (strict mode, quoted variables; `shell-bash-best-practices`; WSL when
the Windows PATH has no ffmpeg), sources in `source/`, exports in `export/`.

- Cut: `ffmpeg -ss <start> -to <end> -i in.mp4 -c copy cut.mp4` (re-encode when the cut is not on a keyframe).
- Concatenate: concat demuxer with a list file; crossfade with `xfade`; speed up a slow part with `setpts` / `atempo`.
- Reframe to 9:16: `crop`/`scale` and `pad`, or a blurred copy as background; check that the touch area is not cropped.
- Titles and lower thirds: `drawtext` (font file with its licence) or PNG overlays made by the `designer`; end card with the call to action.
- Captions: write an `.srt` from the script, burn in with `subtitles=` for social formats and keep the `.srt` for platforms that take it.
- Audio: loudness `loudnorm` (about -14 LUFS for social), duck the music under the voice (`sidechaincompress`), royalty-free music
  with its licence noted.
- Export: H.264 + AAC, `-pix_fmt yuv420p -movflags +faststart`, `-crf 18-23`; 1080x1920 (9:16), 1080x1080, 1920x1080; a thumbnail
  frame or a `designer` thumbnail.
- For richer motion graphics, propose a code-driven tool (Remotion or similar) or ask the lead for a human editor; do not fake it.

## 4. Review before export

Watch the draft frame by frame at key moments (stills inline for the lead), check: hook, readable text on a phone, captions in sync,
no secrets or personal data, no flashing, audio level, call to action, correct claims. Deliver: video files, `.srt`, thumbnails,
the brief and the licence list.

## Monthly refresh

Last refreshed: 2026-10. At first use in a later month: re-check the sources, update only internet-derived guidance, keep user/project rules, update this date, report changes.
Sources: https://ffmpeg.org/ffmpeg-all.html , https://developer.android.com/tools/adb , https://scrcpy.org/ ,
https://support.google.com/youtube/answer/1722171 , https://playwright.dev/docs/videos
