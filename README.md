# Cloudmesh AI Theme Guide

Welcome to the guide for the **Cloudmesh AI Theme**. This package provides a consistent look and feel for Cloudmesh AI project documentation, built as an extension of the Material for MkDocs theme.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage-guide)
  - [Primary Method (Recommended)](#primary-method-recommended)
  - [Configuration Options](#configuration-options)
  - [Alternative: Manual Asset Deployment](#alternative-manual-asset-deployment)
- [Development & Contribution](#development--contribution)
  - [Local Development](#local-development)
  - [Running Tests](#running-tests)
- [Maintainer's Guide](#maintainers-guide)
  - [Project Structure](#project-structure)
  - [Version Management](#version-management)
  - [Release Process](#release-process)

---

## Introduction

The `cloudmesh-ai-theme` is a Python package that provides branding for Cloudmesh AI documentation. Instead of copying CSS and images into every project, this package allows you to apply the theme via a configuration change in your `mkdocs.yml`.

It automatically handles:
- **Branding**: Injects the "Cloudmesh AI" site name and a standardized footer.
- **Styling**: Applies custom CSS.
- **Assets**: Provides shared logos and favicons.

---

## Installation

The theme is distributed as a Python package. You can install it using `pip`:

```bash
pip install cloudmesh-ai-theme
```

---

## Usage

### Primary Method (Recommended)

The simplest way to use the theme is to specify it by name in your `mkdocs.yml` file. This method automatically applies all branding, styles, and assets.

```yaml
theme:
  name: cloudmesh-ai-theme
```

### Configuration Options

You can customize the theme while maintaining the Cloudmesh AI layout. Currently, the following options are supported:

#### `primary_color`
Change the primary accent color of the theme.
```yaml
theme:
  name: cloudmesh-ai-theme
  primary_color: "#ff0000" # Example: Red
```

#### `logo` and `favicon`
You can override the default Cloudmesh AI logo and favicon by specifying their paths in your `mkdocs.yml`. SVG favicons are recommended for better scalability and quality.
```yaml
theme:
  name: cloudmesh-ai-theme
  logo: assets/my-logo.png
  favicon: assets/my-favicon.svg
```

### Alternative: Manual Asset Deployment

If you need direct access to the CSS and image files within your project directory (e.g., for further local overrides), you can deploy the assets manually.

1. **Run the deployment command**:
   ```bash
   cloudmesh-ai-theme-install
   ```
   This will copy the assets into `docs/theme/` in your current project.

2. **Reference assets in `mkdocs.yml`**:
   ```yaml
   extra_css:
     - theme/custom.css

   theme:
     favicon: theme/assets/favicon.svg
     logo: theme/assets/logo-white.png
     name: material
   ```

---

## Development & Contribution

### Local Development

To make changes to the theme and see them reflected in your projects immediately, install the package in editable mode:

```bash
cd cloudmesh-ai-theme
pip install -e .
```

### Running Tests

The theme includes a verification suite to ensure that the package builds and renders correctly.

```bash
cd cloudmesh-ai-theme/tests
python test_theme.py
```

---

## Maintainer's Guide

### Project Structure

```text
cloudmesh-ai-theme/
├── .github/workflows/  # CI/CD pipelines
├── src/
│   └── cloudmesh_ai_theme/
│       ├── __init__.py  # Package logic & versioning
│       ├── assets/      # Logos and favicons
│       ├── css/         # Custom stylesheets
│       └── theme/       # MkDocs templates (main.html)
├── tests/              # Verification suite
├── VERSION             # Single source of truth for version
├── pyproject.toml      # Build system & metadata
└── README.md           # This guide
```

### Version Management

The version is managed in the `VERSION` file at the root of the repository. To bump the version:
1. Edit the `VERSION` file (e.g., change `0.1.0` to `0.1.1`).
2. Commit the change:
   ```bash
   git add VERSION
   git commit -m "Bump version to 0.1.1"
   ```

### Release Process

Releases are automated via GitHub Actions. To trigger a new release:
1. Create a git tag following the `v*` pattern:
   ```bash
   git tag v0.1.0
   git push origin v0.1.0
   ```
2. The GitHub Action will automatically build the `.whl` and `.tar.gz` distributions and upload them as artifacts.

#### Publishing to PyPI

The easiest way to upload the package to PyPI is using the provided `Makefile`:

```bash
make pypi
```

This command automatically installs the necessary build tools, builds the distribution, and uploads it to PyPI using `twine`.

**Manual Upload (without Makefile):**
1. Install build tools:
   ```bash
   pip install build twine
   ```
2. Build the distribution:
   ```bash
   python -m build
   ```
3. Upload to PyPI:
   ```bash
   python -m twine upload dist/*
   ```

**Automated Upload (GitHub Actions):**
To automate publishing, add a `pypi-publish` step to the `.github/workflows/release.yml` file and configure a `PYPI_API_TOKEN` in your GitHub repository secrets.
