from mkdocs.plugins import BasePlugin
from pathlib import Path
from . import install_assets

class CloudmeshAIThemePlugin(BasePlugin):
    """
    MkDocs plugin to automatically install Cloudmesh AI theme assets.
    """

    def on_config(self, config):
        """
        Install theme assets when the configuration is loaded and update the theme config.
        """
        # Use the docs_dir from config, and put assets in a 'theme' subdirectory
        docs_dir = config.get("docs_dir", "docs")
        target_dir = Path(docs_dir) / "theme"
        
        install_assets(target_dir=str(target_dir))

        # Dynamically update the theme configuration to use the newly created custom_dir
        if "theme" not in config:
            config["theme"] = {}
        
        config["theme"]["custom_dir"] = str(target_dir)
        
        return config
