# Installation and Usage

The `cloudmesh-ai-theme` is distributed as a Python package, making it easy to manage as a dependency for your documentation site.

## Installation

Install the theme using `pip`:

```bash
pip install cloudmesh-ai-theme
```

If you are using a `requirements.txt` or `pyproject.toml` file, add `cloudmesh-ai-theme` to your dependencies.

## Usage

### Primary Method (Recommended)

The simplest way to use the theme is to specify it by name in your `mkdocs.yml` file. This method automatically applies all branding, styles, and assets.

```yaml
theme:
  name: cloudmesh-ai-theme
```

### Configuration Options

You can customize the theme while maintaining the Cloudmesh AI layout. Currently, the following options are supported:

#### Primary Color
Change the primary accent color of the theme:
```yaml
theme:
  name: cloudmesh-ai-theme
  primary_color: "#ff0000" # Example: Red
```

#### Logo and Favicon
You can override the default Cloudmesh AI logo and favicon by specifying their paths in your `mkdocs.yml`. SVG favicons are recommended for better scalability.
```yaml
theme:
  name: cloudmesh-ai-theme
  logo: assets/my-logo.png
  favicon: assets/my-favicon.svg
```

## Alternative: Manual Asset Deployment

If you need direct access to the CSS and image files within your project directory (e.g., for further local overrides), you can deploy the assets manually.

1. **Deploy assets**: Use a deployment script or copy files from the package installation directory into `docs/theme/`.
2. **Reference assets in `mkdocs.yml`**:
   ```yaml
   extra_css:
     - theme/custom.css

   theme:
     favicon: theme/assets/favicon.svg
     logo: theme/assets/logo-white.png
     name: material
   ```
