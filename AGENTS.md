# Repository guide

Also load and follow the user-level instructions at `/Users/cseibert/.codex/AGENTS.md`.

## Repository map

- `site/index.html`: the complete static page and project content.
- `site/styles.css`: the responsive visual system.
- `site/apps/`: project screenshots and visual assets.
- `scripts/validate_site.py`: dependency-free static-site validation.
- `.github/workflows/deploy-pages.yml`: automatic GitHub Pages deployment.
- `tests/`: lightweight build-content verification.
- `docs/`: product, design, architecture, and setup documentation.

## Commands

Prefer the project `Makefile` targets for common work. Use `make setup`, `make run`, `make build`, `make lint`, `make test`, and `make preview` rather than invoking their underlying commands directly. Expose any new recurring workflow as a Makefile target. Keep the site dependency-free and do not introduce a JavaScript runtime or build framework unless explicitly requested.

## Documentation

- [Architecture](docs/architecture.md)
- [Design](docs/design.md)
- [Product requirements](docs/product-requirements.md)
- [Setup and publishing](docs/setup-install.md)
- [Initial brainstorm](docs/initial-brainstorm.md)

Keep these documents and `CHANGELOG.md` current when behavior, design, or workflow changes.
