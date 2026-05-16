from setuptools import setup, find_packages

setup(
    package_dir={"": "."},
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "cloudmesh_ai_theme": ["assets/*", "css/*", "theme/*", "theme.yml"],
    },
)