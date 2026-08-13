# Architecture

Built by Chase is a static React site compiled by Vite. Project metadata is a typed array in `src/main.tsx`; the page maps that data into accessible project cards. Styles are kept in one responsive stylesheet, while image assets are served unchanged from `public/apps/`.

There is no server, database, authentication, or runtime API. `npm run build` emits the complete site to `dist/`. GitHub Actions uploads that directory as a Pages artifact and deploys it.

Vite derives its production base path from `GITHUB_REPOSITORY`, so the same source works at the repository-scoped GitHub Pages URL and at `/` during local development.
