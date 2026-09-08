# Maintainer's Guide

This section is for developers responsible for the long-term maintenance of the theme.

## Project Structure

```text
cloudmesh-ai-theme/
├── .github/workflows/  # CI/CD pipelines
├── src/
│   └── cloudmesh_ai_theme/
│       ├── __init__.py  # Package logic & versioning
│       ├── assets/      # Logos and favicons
│       ├── css/         # Custom stylesheets
│       └── theme/       # MkDocs templates (main.html)
├── docs/               # Documentation source
├── tests/              # Verification suite
├── VERSION             # Single source of truth for version
├── pyproject.toml      # Build system & metadata
├── Makefile            # Project automation
└── README.md           # GitHub landing page
```

## Version Management

The version is managed in the `VERSION` file at the root of the repository. To bump the version:
1. Edit the `VERSION` file (e.g., change `7.0.5` to `7.0.6`).
2. Commit the change:
   ```bash
   git add VERSION
   git commit -m "Bump version to 7.0.6"
   ```

## Release Process

Releases are automated via GitHub Actions. To trigger a new release:
1. Create a git tag following the `v*` pattern:
   ```bash
   git tag v7.0.6
   git push origin v7.0.6
   ```
2. The GitHub Action will automatically build the distributions and upload them.

### Publishing to PyPI
The theme is published to PyPI to allow easy installation via pip. This is typically handled by the release workflow or can be done manually using `twine`.
