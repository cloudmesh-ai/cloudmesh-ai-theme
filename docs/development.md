# Development and Contribution

This guide explains how to modify the theme and contribute improvements.

## Local Development

To make changes to the theme and see them reflected in your projects immediately, install the package in editable mode:

```bash
cd cloudmesh-ai-theme
make install
```

## Running Tests

The theme includes a verification suite to ensure that the package builds and renders correctly.

```bash
make test
```

## Previewing Changes

You can preview the theme's own documentation to see how changes affect the layout:

```bash
make view
```

## Contribution Workflow

1. Create a new branch for your feature or fix.
2. Implement your changes in `src/cloudmesh_ai_theme/`.
3. Verify your changes using `make test`.
4. Commit your changes and open a Pull Request.
