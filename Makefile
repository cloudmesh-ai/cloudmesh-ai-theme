.PHONY: help pypi test view clean

# Default target
all: test

help:
	@echo "Available targets:"
	@echo "  all    - Run tests (default)"
	@echo "  pypi   - Install build tools, build package, and upload to PyPI"
	@echo "  test   - Run theme verification tests"
	@echo "  view   - Start mkdocs serve for the test site"
	@echo "  clean  - Remove build artifacts"

# Build and upload to PyPI
pypi:
	pip install build twine
	python3 -m build
	python3 -m twine upload dist/*

# Run theme verification tests
test:
	python3 tests/test_theme.py

# Start mkdocs serve for the test site
view:
	pip install -e .
	mkdocs serve --livereload -f tests/mkdocs.yml

# Clean build artifacts
clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info