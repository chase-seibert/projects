# Built by Chase

A static portfolio of apps, tools, and experiments built by Chase Seibert.

![Built by Chase project gallery](docs/images/site.png)

## Local preview

```sh
make run
```

Open [http://localhost:8000](http://localhost:8000). No installation or build step is required.
Use `make run PORT=8080` to choose another port when needed.

## Publishing

Pushes to `main` automatically publish the finished `site/` folder through GitHub Pages. See [docs/setup-install.md](docs/setup-install.md) for the one-time repository settings and publishing details.

## Updating the gallery

Project content lives directly in `site/index.html`. Add screenshots to `site/apps/`, update the HTML, then run `make test`.
