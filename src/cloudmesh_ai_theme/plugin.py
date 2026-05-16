from mkdocs.plugins import BasePlugin
from mkdocs.config import config_options


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

        # Branding defaults
        if self.config["logo"]:
            theme["logo"] = self.config["logo"]

        if self.config["favicon"]:
            theme["favicon"] = self.config["favicon"]

        # Inject palette safely (do not overwrite user config)
        theme.setdefault("palette", [
            {
                "scheme": "default",
                "primary": self.config["primary_color"],
                "accent": self.config["primary_color"],
                "toggle": {
                    "icon": "brightness-7",
                    "name": "Switch to dark mode",
                },
            },
            {
                "scheme": "slate",
                "primary": self.config["primary_color"],
                "accent": self.config["primary_color"],
                "toggle": {
                    "icon": "brightness-4",
                    "name": "Switch to light mode",
                },
            },
        ])

        # Inject CSS via MkDocs native mechanism
        if self.config["inject_css"]:
            config.setdefault("extra_css", [])
            config["extra_css"].append("cloudmesh_ai_theme/custom.css")

        return config