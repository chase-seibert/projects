# Frustration log

## 2026-08-13 — Default npm cache was not writable

The site initializer could not finish dependency installation because the user npm cache contained files owned by another account. Reusing the generated project with the bundled Node runtime and a project-specific temporary npm cache avoids changing global ownership.

## 2026-08-13 — macOS window capture permission was unavailable

Clipboard Markup could be launched safely with a clean temporary home directory, but both the system screenshot utility and ScreenCaptureKit were denied screen-capture permission. Use a project visual based on the app icon for now, and replace it with a real app screenshot after granting screen-recording access or adding a checked-in screenshot to that project.
