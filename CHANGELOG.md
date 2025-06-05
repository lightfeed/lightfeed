# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Added

## [py-0.1.6 & ts-0.1.6] - 2025-06-04
### Changed
- Changed timestamp fields to created_at, changed_at and synced_at

## [py-0.1.5 & ts-0.1.5] - 2025-05-22
### Fixed
- Fixed operator types in filter

## [py-0.1.4 & ts-0.1.4] - 2025-05-11
### Added
- Initial CI/CD setup
- Automated release workflows for Python and TypeScript clients
- CHANGELOG tracking

## [py-0.1.3 & ts-0.1.3] - 2024-04-21
### Fixed
- Fixed Search and Filter APIs to use the correct endpoints 

## [py-0.1.2 & ts-0.1.2] - 2024-04-18
### Added
- Initial release of the Lightfeed TypeScript client
- Core API client implementation with TypeScript types
- `LightfeedClient` class with configurable API key, base URL, and timeout
- Methods for interacting with Lightfeed API:
  - `getRecords()`: Retrieve records with time range filtering
  - `searchRecords()`: Semantic search with filtering capabilities
  - `filterRecords()`: Apply complex filters to database records
- Comprehensive error handling with `LightfeedError` class
- Pagination support for all record retrieval methods
- Full TypeScript type definitions for request and response objects
- Unit tests for core functionality
- Detailed documentation with usage examples
