import os
import shutil
from pathlib import Path

# Read version from VERSION file
VERSION_FILE = Path(__file__).parent.parent / "VERSION"
if VERSION_FILE.exists():
    __version__ = VERSION_FILE.read_text().strip()
else:
    __version__ = "0.1.0"

def install_assets(target_dir="docs/theme"):
    """
    Copies the theme assets and CSS from the package to the target directory.
    """
    package_dir = Path(__file__).parent
    assets_src = package_dir / "assets"
    css_src = package_dir / "css"
    
    target_path = Path(target_dir)
    target_path.mkdir(parents=True, exist_ok=True)
    
    # Copy assets
    if assets_src.exists():
        shutil.copytree(assets_src, target_path / "assets", dirs_exist_ok=True)
        print(f"Copied assets to {target_path}/assets")
        
    # Copy CSS
    if css_src.exists():
        # We want to copy the files inside css/ to the target_path root or a css subfolder
        # To keep it consistent with the submodule approach (theme/custom.css), 
        # we copy the contents of css/ directly into target_path
        for item in css_src.iterdir():
            shutil.copy2(item, target_path / item.name)
            print(f"Copied {item.name} to {target_path}/{item.name}")

if __name__ == "__main__":
    install_assets()