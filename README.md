# Cloudmesh AI Theme

The **Cloudmesh AI Theme** provides a consistent, professional look and feel for all Cloudmesh AI project documentation. It is built as an extension of the [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) theme, adding custom branding, styles, and shared assets.

For the full interactive documentation, please visit: [https://cloudmesh-ai.github.io/cloudmesh-ai-theme/](https://cloudmesh-ai.github.io/cloudmesh-ai-theme/)

## Quick Start

### Installation

Install the theme via pip:

```bash
pip install cloudmesh-ai-theme
```

### Usage

Apply the theme in your `mkdocs.yml`:

```yaml
theme:
  name: cloudmesh-ai-theme
```

## Development

The project includes a `Makefile` to simplify common tasks:

- **Local Development**: Install in editable mode
  ```bash
  make install
  ```
- **Test Theme**: Run the verification suite
  ```bash
  make test
  ```
- **Preview Docs**: Build and serve the documentation locally
  ```bash
  make view
  ```
- **Build Docs**: Generate the static site
  ```bash
  make doc
  ```

## Contribution

Please refer to the [Development Guide](https://cloudmesh-ai.github.io/cloudmesh-ai-theme/development/) for more information on how to contribute to the theme.
