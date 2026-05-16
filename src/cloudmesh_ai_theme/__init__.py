from importlib.metadata import version, PackageNotFoundError
from pathlib import Path

def get_version():
    # 1. Try to read from VERSION file in the package root (installed)
    try:
        version_file = Path(__file__).parent / "VERSION"
        if version_file.exists():
            return version_file.read_text().strip()
    except Exception:
        pass

    # 2. Try to read from VERSION file in the project root (development)
    try:
        # __file__ is .../src/cloudmesh_ai_theme/__init__.py
        # Project root is two levels up from src/
        project_root_version = Path(__file__).parent.parent.parent / "VERSION"
        if project_root_version.exists():
            return project_root_version.read_text().strip()
    except Exception:
        pass

    # 3. Fallback to importlib.metadata
    try:
        return version("cloudmesh-ai-theme")
    except PackageNotFoundError:
        return "0.0.0"

__version__ = get_version()