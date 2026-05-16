import subprocess
import os
from pathlib import Path

def test_install_assets_import():
    """
    Verifies that the package can be imported and install_assets can be called.
    """
    try:
        from cloudmesh_ai_theme import install_assets
        print("Successfully imported install_assets from cloudmesh_ai_theme")
        
        # Test calling it with a temporary directory
        test_assets_dir = Path("test_assets_output")
        install_assets(target_dir=str(test_assets_dir))
        
        if test_assets_dir.exists():
            print("install_assets successfully created target directory")
            # Cleanup
            import shutil
            shutil.rmtree(test_assets_dir)
            return True
        return False
    except ImportError as e:
        print(f"Import failed: {e}")
        return False

def test_theme_build():
    """
    Verifies that the theme can be installed and used to build a site.
    """
    root_dir = Path(__file__).parent.parent
    test_dir = Path(__file__).parent
    
    print("Installing theme...")
    subprocess.run(["pip", "install", "."], cwd=root_dir, check=True)
    
    # Ensure the package root is in PYTHONPATH for the mkdocs build
    os.environ["PYTHONPATH"] = str(root_dir) + os.pathsep + os.environ.get("PYTHONPATH", "")
    
    print("Building test site...")
    result = subprocess.run(
        ["mkdocs", "build"], 
        cwd=test_dir, 
        capture_output=True, 
        text=True
    )
    
    if result.returncode != 0:
        print("Build failed!")
        print(result.stderr)
        return False
    
    print("Build succeeded. Verifying output...")
    site_dir = test_dir / "site"
    index_html = site_dir / "index.html"
    
    if not index_html.exists():
        print("index.html not found!")
        return False
        
    content = index_html.read_text()
    if "Cloudmesh AI" not in content:
        print("Branding 'Cloudmesh AI' not found in output!")
        return False
        
    print("Theme verification successful!")
    return True

if __name__ == "__main__":
    success = True
    if not test_install_assets_import():
        print("Import test failed!")
        success = False
    
    if not test_theme_build():
        print("Build test failed!")
        success = False
        
    if success:
        print("SUCCESS")
    else:
        print("FAILURE")
        exit(1)
