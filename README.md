# Cloudmesh AI Theme

This repository contains the shared theme assets for all Cloudmesh AI projects.

## Contents
- `css/custom.css`: Shared custom styles for MkDocs.
- `assets/`: Shared logos and favicons.

## How to use as a Submodule

To integrate this theme into a Cloudmesh AI project:

1. **Add the submodule**:
   ```bash
   git submodule add https://github.com/cloudmesh-ai/cloudmesh-ai-theme.git theme
   ```

2. **Update `mkdocs.yml`**:
   Reference the CSS and assets using the `theme/` path:
   ```yaml
   extra_css:
     - theme/custom.css

   theme:
     favicon: theme/assets/favicon.ico
     logo: theme/assets/logo-white.png
     name: material
   ```

3. **Updating the theme**:
   To pull the latest changes from the theme repository:
   ```bash
   git submodule update --remote