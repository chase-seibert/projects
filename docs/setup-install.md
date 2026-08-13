# Setup and publishing

## Local setup

Install Node.js 22.13 or newer, then run:

```sh
make setup
make run
```

Run `make test` before publishing. It builds the static site and checks that all initial projects and destinations are present.

## GitHub Pages

The repository includes `.github/workflows/deploy-pages.yml`. In the GitHub repository settings, choose **GitHub Actions** as the Pages source. Every push to `main` will then build and deploy `dist/` automatically. The workflow can also be run manually from the Actions tab.
