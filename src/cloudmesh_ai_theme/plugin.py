from mkdocs.plugins import BasePlugin
from mkdocs.config import config_options
import shutil
from pathlib import Path
try:
    from importlib import resources
except ImportError:
    import importlib_resources as resources


class CloudmeshAIThemePlugin(BasePlugin):
    """
    Clean MkDocs plugin:
    - Injects branding defaults
    - Configures theme safely
    - Does NOT modify filesystem
    """

    config_scheme = (
        ("primary_color", config_options.Type(str, default="#1e90ff")),
        ("logo", config_options.Type(str, default=None)),
        ("favicon", config_options.Type(str, default=None)),
        ("inject_css", config_options.Type(bool, default=True)),
    )

    def on_config(self, config):
        theme = config.get("theme")

        if not theme:
            config["theme"] = {}
            theme = config["theme"]

        # Ensure Material theme baseline
        theme["name"] = theme.get("name", "material")

        # Enable Material theme features
        features = theme.setdefault("features", [])
        if "content.code.copy" not in features:
            features.append("content.code.copy")

        # Handle Assets (Logo/Favicon)
        # We copy assets to the docs directory so MkDocs can find them
        # Use docs/assets/theme to avoid triggering MkDocs custom theme override (docs/theme)
        docs_dir = Path(config["docs_dir"])
        assets_dst = docs_dir / "assets" / "theme"
        assets_dst.mkdir(parents=True, exist_ok=True)

        # Default assets from package
        default_logo = "logo-white.png"
        default_favicon = "favicon.svg"

        try:
            # Copy assets from package to docs/theme/assets
            for asset in [default_logo, default_favicon]:
                source = resources.files("cloudmesh_ai_theme.assets").joinpath(asset)
                target = assets_dst / asset
                shutil.copy2(source, target)
        except Exception as e:
            print(f"CloudmeshAIThemePlugin: Failed to copy assets: {e}")

        # Set branding
        logo_path = self.config["logo"] or f"assets/theme/{default_logo}"
        favicon_path = self.config["favicon"] or f"assets/theme/{default_favicon}"
        
        theme["logo"] = logo_path
        theme["favicon"] = favicon_path

        # Inject palette safely (do not overwrite user config)
        theme.setdefault("palette", [
            {
                "scheme": "default",
                "primary": self.config["primary_color"],
                "accent": self.config["primary_color"],
            },
            {
                "scheme": "slate",
                "primary": self.config["primary_color"],
                "accent": self.config["primary_color"],
            },
        ])

        return config

    def on_page_content(self, html, page, config, files):
        if not self.config["inject_css"]:
            return html

        try:
            # Read CSS from the package resources
            css_content = resources.files("cloudmesh_ai_theme.css").joinpath("custom.css").read_text(encoding="utf-8")
            style_tag = f"\n<style>\n{css_content}\n</style>\n"
            return style_tag + html
        except Exception as e:
            print(f"CloudmeshAIThemePlugin: Failed to inject CSS: {e}")
            return html
