# Promotional video: montage

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
