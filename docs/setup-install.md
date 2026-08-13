# Setup and publishing

## Local setup

No dependencies need to be installed. Run:

```sh
make run
```

Open `http://localhost:8000`. Run `make test` before publishing; it checks that the HTML contains all projects, contains no JavaScript, and references only existing local assets.
If that port is already in use, run `make run PORT=8080` and open the matching address.

## GitHub Pages

The repository includes `.github/workflows/deploy-pages.yml`. In the GitHub repository settings, choose **GitHub Actions** as the Pages source. Every push to `main` will then upload and deploy `site/` directly. The workflow can also be run manually from the Actions tab.
