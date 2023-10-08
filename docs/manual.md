# MkDocs Manual

## 🦦 Workflow

1. Enable virtual environment:

   ```sh
   poetry shell
   ```

2. Edit the base markdown files in `docs/base/` directory.
3. Generate the i18n markdown files with `mmg` and serve the site:

   ```sh
   mmg -b ./mmg.yml; mkdocs serve
   ```

4. Open the site in your browser at http://127.0.0.1:8000/.

## 🦦 Cautions

### Relative URL

- Relative URLs start with `/$LANG/`. For the default language, just `/`.
- The images in `./docs/assets` directory have URLs starting with `/assets/`.

### Absolute URL

Examples:

- `https://mmg.ryul1206.dev/latest/` (en)
- `https://mmg.ryul1206.dev/latest/ko/`
- `https://mmg.ryul1206.dev/latest/assets/$IMAGE_NAME`

## 🦦 Publish

Please make sure the package version in `pyproject.toml` is correct before pushing. [Mike](https://github.com/jimporter/mike) will overwrite the existing pages with the pushed version.

### Method 1: By Hand

> Recommended for correcting the existing pages

```sh
mmg -b ./mmg.yml
mike deploy --push --update-aliases $VERSION $TAGS --force
```

- `$VERSION` must be a valid [SemVer](https://semver.org/) version.
- `$TAGS` is a list of tags separated by space.
   - `latest` for the latest stable version, usually `docs` branch.
   - `unstable` for the latest unstable version, usually `dev` branch.

### Method 2: By GitHub Actions

> Recommended for the new version release

- For `latest` tag: Push a new commit to `docs` branch.
- For `unstable` tag: Push a new commit to `dev` branch.
