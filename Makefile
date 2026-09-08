######################################################################
# Cloudmesh AI Theme Makefile
######################################################################

# Variables
PYTHON       := python3
PIP          := $(PYTHON) -m pip

.PHONY: help install test clean doc view publish

help:
	@echo
	@echo "Makefile for the Cloudmesh AI Theme:"
	@echo
	@echo "  install       - Install in editable mode for local development"
	@echo "  test          - Run the theme verification suite"
	@echo "  clean         - Remove build artifacts and cache"
	@echo "  doc           - Build the documentation site locally"
	@echo "  view          - Start a local server to preview the documentation"
	@echo "  publish       - Deploy the site to GitHub Pages"
	@echo

# --- DEVELOPMENT & TESTING ---

install:
	$(PIP) install -e .

test:
	$(PYTHON) tests/test_theme.py

# --- DOCUMENTATION ---

doc:
	mkdocs build

view:
	mkdocs serve --livereload

publish: doc
	@echo "Deploying to GitHub Pages..."
	mkdocs gh-deploy

# --- CLEANUP ---

clean:
	@echo "Cleaning artifacts..."
	rm -rf site/
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
