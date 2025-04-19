# Lightfeed API Clients

<p align="center">
  <img src="https://www.lightfeed.ai/docs/img/logo.svg" width="128" height="128" alt="Lightfeed Logo">
</p>

<div align="center">
  <a href="https://www.npmjs.com/package/lightfeed">
    <img src="https://img.shields.io/npm/v/lightfeed?style=flat-square&logo=npm" alt="npm">
  </a>
  <a href="https://pypi.org/project/lightfeed/">
    <img src="https://img.shields.io/pypi/v/lightfeed?style=flat-square&logo=pypi&logoColor=white" alt="PyPI">
  </a>
  <a href="https://github.com/lightfeed/lightfeed/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/lightfeed/lightfeed?style=flat-square" alt="License">
  </a>
  <a href="https://discord.gg/txZ2s4pgQJ" alt="Discord">
    <img src="https://img.shields.io/discord/1209342987008614501?style=flat-square&label=discord&logo=discord&logoColor=white&color=5865F2" alt="Discord">
  </a>
</div>

This repository contains the official client libraries for interacting with the Lightfeed API, enabling real-time search and filtering of extracted web data.

## Available Clients

| Client | Package | Documentation |
|--------|---------|---------------|
| TypeScript/Node.js | [npm](https://www.npmjs.com/package/lightfeed) | [README](./typescript/README.md) |
| Python | [PyPI](https://pypi.org/project/lightfeed/) | [README](./python/README.md) |

## Repository Structure

- `/clients/typescript` - TypeScript/Node.js client implementation
- `/clients/python` - Python client implementation
- `/clients/test-clients` - Test projects for local development
- `/.github/workflows` - GitHub Actions workflows for automated releases

## Development

### Prerequisites

- Node.js 14+ (for TypeScript client)
- Python 3.7+ (for Python client)
- npm or yarn
- pip

### Local Development Setup

#### TypeScript Client

```bash
cd clients/typescript
npm install
npm run build
```

#### Python Client

```bash
cd clients/python
pip install -e .
```

## Releases

We use GitHub Actions to automate the release process. The workflows are located in the repository's root `.github/workflows` directory:

- For TypeScript releases, create a tag with the format `ts-v*` (e.g., `ts-v1.0.0`)
- For Python releases, create a tag with the format `py-v*` (e.g., `py-v1.0.0`)

These tags will trigger the corresponding GitHub Actions workflow to build, create a GitHub Release, and publish to npm or PyPI.

### Creating a New Release

1. Update the version number in the respective package files:
   - For TypeScript: Update `version` in `typescript/package.json`
   - For Python: Update `version` in `python/pyproject.toml`

2. Commit these version changes:
   ```bash
   git add clients/typescript/package.json
   git add clients/python/pyproject.toml
   git commit -m "Bump versions: typescript to 1.0.0, python to 1.0.0"
   git push
   ```

3. Create and push tags for the release:
   ```bash
   # For TypeScript
   git tag ts-v1.0.0

   # For Python
   git tag py-v1.0.0

   # Push both tags
   git push origin ts-v1.0.0 py-v1.0.0
   ```

4. The GitHub Actions workflows will automatically run:
   - When you push `ts-v1.0.0`, the TypeScript workflow runs
   - When you push `py-v1.0.0`, the Python workflow runs
   - These workflows build and publish to npm/PyPI and GitHub Packages

5. Create formal GitHub Releases (optional but recommended):
   - Go to GitHub → Releases → Draft new release
   - Select your tag (e.g., `ts-v1.0.0`)
   - Add release notes
   - Publish the release
   - Repeat for the Python tag

## License

This project is licensed under the Apache 2.0 License - see the [LICENSE](../LICENSE) file for details. 