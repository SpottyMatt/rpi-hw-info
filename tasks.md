# Task List: Convert to PyPI Package and Setup GitHub Actions Workflow

## Project Restructuring
- [x] Create proper package directory structure 
- [x] Refactor the existing script into modular components
- [x] Create necessary package files (pyproject.toml, README.md updates)
- [x] Ensure Python 2.7+ compatibility

## Package Setup
- [x] Create pyproject.toml with Poetry configuration
- [x] Create __init__.py with package exports
- [x] Create __main__.py for CLI entry point
- [x] Create detector.py with core functionality
- [x] Create models.py for RPi model definitions
- [x] Update README.md with new package information

## GitHub Actions Workflow
- [x] Create GitHub Actions workflow file for PyPI publishing
- [x] Configure PyPI Trusted Publishers integration (OIDC)

## Versioning
- [x] Configure Python Semantic Release for automatic versioning
- [x] Set up Conventional Commits-based versioning in CI
- [x] Add --version flag to CLI tool
- [x] Create version test
- [x] Document Conventional Commits format in README

## Testing
- [x] Create basic tests
- [ ] Verify package installation and functionality
- [ ] Verify CLI tool functionality

## Documentation
- [x] Create CHANGELOG.md
- [x] Update README.md with usage examples for the package
- [x] Document migration from v1.0.0 to v2.0.0 