# Contributing to Lightfeed

Thank you for your interest in contributing to Lightfeed! This document provides guidelines and instructions for contributing to this project.

## Development Workflow

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Submit a pull request

## Code Style

- For Python code, follow [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- For TypeScript code, follow the project's ESLint configuration

## Testing

All new features and bug fixes should include tests. Run tests before submitting a PR:

- For Python: `cd clients/python && pytest`
- For TypeScript: `cd clients/typescript && npm test`

## Release Process

The project uses GitHub Actions for CI/CD and automated releases. We maintain separate versioning for Python and TypeScript clients.

### Versioning

We follow [Semantic Versioning](https://semver.org/):

- MAJOR version for incompatible API changes
- MINOR version for backwards-compatible functionality additions
- PATCH version for backwards-compatible bug fixes

### Preparing a Release

1. Update the version number:
   - For Python: Update `setup.py` or `pyproject.toml` in the `clients/python` directory
   - For TypeScript: Update `package.json` in the `clients/typescript` directory

2. Update the CHANGELOG.md:
   - Move changes from the "Unreleased" section to a new version section
   - Follow the format: `## [X.Y.Z] - YYYY-MM-DD`
   - Group changes by type: Added, Changed, Deprecated, Removed, Fixed, Security
   - Update the link references at the bottom of the file

Example CHANGELOG entry:
```markdown
## [1.1.0] - 2023-05-15
### Added
- New feature X that does Y
### Fixed
- Bug in function Z that caused issue W
```

3. Commit these changes with a message like "Release vX.Y.Z"
4. Push to main: `git push origin main`

### Creating a Release

1. Create and push a tag:
   - For Python releases: `git tag py-vX.Y.Z && git push origin py-vX.Y.Z`
   - For TypeScript releases: `git tag ts-vX.Y.Z && git push origin ts-vX.Y.Z`

2. The GitHub Actions workflow will automatically:
   - Run tests
   - Build the package
   - Publish to PyPI (Python) or npm (TypeScript)
   - Create a GitHub release with notes from the CHANGELOG

### Post-Release

1. Verify the package is available on [PyPI](https://pypi.org/project/lightfeed/) or [npm](https://www.npmjs.com/package/lightfeed)
2. Verify the GitHub release was created correctly
3. Announce the release in appropriate channels

## Troubleshooting Releases

If a release fails:

1. Check the GitHub Actions logs for errors
2. Fix any issues in a new commit
3. Delete the tag: `git tag -d [tag-name] && git push --delete origin [tag-name]`
4. Re-tag and push again

## Additional Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [PyPI Publishing Guide](https://packaging.python.org/guides/publishing-package-distribution-releases-using-github-actions-ci-cd-workflows/)
- [npm Publishing Guide](https://docs.npmjs.com/creating-and-publishing-scoped-public-packages) 