from importlib.metadata import version, PackageNotFoundError
from pathlib import Path
import shutil

try:
    __version__ = version("cloudmesh-ai-theme")
except PackageNotFoundError:
    __version__ = "0.0.0"


def install_assets(target_dir="docs/theme"):
    """
    Copy theme assets and CSS into a target MkDocs directory.
    """
    package_dir = Path(__file__).parent
    assets_src = package_dir / "assets"
    css_src = package_dir / "css"

    target_path = Path(target_dir)
    target_path.mkdir(parents=True, exist_ok=True)

    # Copy assets
    if assets_src.exists():
        shutil.copytree(
            assets_src,
            target_path / "assets",
            dirs_exist_ok=True,
        )

    # Copy CSS files
    if css_src.exists():
        for item in css_src.iterdir():
            shutil.copy2(item, target_path / item.name)


if __name__ == "__main__":
    install_assets()