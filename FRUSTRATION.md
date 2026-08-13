# Frustration log

## 2026-08-13 — Default npm cache was not writable

The site initializer could not finish dependency installation because the user npm cache contained files owned by another account. Reusing the generated project with the bundled Node runtime and a project-specific temporary npm cache avoids changing global ownership.

## 2026-08-13 — macOS window capture permission was unavailable

Clipboard Markup could be launched safely with a clean temporary home directory, but both the system screenshot utility and ScreenCaptureKit were denied screen-capture permission. Use a project visual based on the app icon for now, and replace it with a real app screenshot after granting screen-recording access or adding a checked-in screenshot to that project.

## 2026-08-13 — “Static” was interpreted as static build output

The initial portfolio used React and Vite even though it deployed static files. For a small GitHub Pages portfolio, “static site” should mean authored directly as HTML and CSS unless the user requests a framework. The project now publishes its finished `site/` folder with no package installation, compilation, or client runtime.
