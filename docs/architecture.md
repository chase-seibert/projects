# Architecture

Built by Chase is a dependency-free static website. The complete page and project cards live in `site/index.html`, styles live in `site/styles.css`, and image assets live in `site/apps/`.

There is no JavaScript, package manager, compilation, server application, database, authentication, or runtime API. A small standard-library Python check verifies the HTML structure and local asset references.

GitHub Actions uploads the finished `site/` directory directly to Pages. Relative asset paths allow the same files to work at the repository-scoped GitHub Pages URL and in the local preview.
