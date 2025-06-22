# Task List: Configure Semantic Release for Version 2.0.0

## Context
- Currently on `pypi` branch with version 2.0.0 already set in `__init__.py`
- Need to configure semantic-release to publish version 2.0.0 
- Project has breaking changes that warrant a major version bump
- Current semantic-release config only allows releases from `master` branch

## Tasks

### 1. Analysis & Planning
- [x] Analyze current semantic-release configuration
- [x] Check current branch and version status
- [x] Research semantic-release breaking change patterns
- [x] Identify optimal approach for 2.0.0 release

### 2. Configuration Updates
- [x] Update semantic-release branch configuration to include `pypi` branch
- [x] Ensure version variables are correctly configured
- [x] Test semantic-release configuration

### 3. Breaking Change Commit
- [x] Create a breaking change commit to trigger major version bump
- [x] Verify semantic-release detects the breaking change
- [x] Create temporary tag v1.9.9 to enable proper version bumping

### 4. Release Execution
- [ ] Test semantic-release in dry-run mode
- [ ] Execute actual release to create 2.0.0
- [ ] Verify release was published correctly

### 5. Enhanced CI/CD Features
- [x] Create expected release preview workflow
- [x] Add TestPyPI pre-release publishing capability
- [x] Add PR comment automation for release previews

### 6. Cleanup & Verification
- [ ] Verify GitHub release was created
- [ ] Verify PyPI package was published
- [ ] Clean up any temporary changes

## Notes
- Version 2.0.0 is already set in `rpi_hw_info/__init__.py`
- Release workflow is configured for `master` branch but we're on `pypi`
- Need to ensure breaking change is properly communicated in commit message 