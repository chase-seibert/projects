# Repository guide

Also load and follow the user-level instructions at `/Users/cseibert/.codex/AGENTS.md`.

## Repository map

- `src/main.tsx`: project data and page structure.
- `src/styles.css`: the responsive visual system.
- `public/apps/`: project screenshots and visual assets.
- `.github/workflows/deploy-pages.yml`: automatic GitHub Pages deployment.
- `tests/`: lightweight build-content verification.
- `docs/`: product, design, architecture, and setup documentation.

## Commands

Prefer the project `Makefile` targets for common work. Use `make setup`, `make run`, `make build`, `make lint`, `make test`, and `make preview` rather than invoking their underlying commands directly. Expose any new recurring workflow as a Makefile target.

## Documentation

- [Architecture](docs/architecture.md)
- [Design](docs/design.md)
- [Product requirements](docs/product-requirements.md)
- [Setup and publishing](docs/setup-install.md)
- [Initial brainstorm](docs/initial-brainstorm.md)

Keep these documents and `CHANGELOG.md` current when behavior, design, or workflow changes.
