# Lightfeed API Client for Node.js

<p align="center">
  <img src="https://www.lightfeed.ai/docs/img/logo.svg" width="128" height="128" alt="Lightfeed Logo">
</p>

<div align="center">
  <a href="https://www.npmjs.com/package/lightfeed">
    <img src="https://img.shields.io/npm/v/lightfeed?style=flat-square&logo=npm" alt="npm">
  </a>
  <a href="https://github.com/lightfeed/lightfeed/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/lightfeed/lightfeed?style=flat-square" alt="License">
  </a>
  <a href="https://discord.gg/txZ2s4pgQJ" alt="Discord">
    <img src="https://img.shields.io/discord/1209342987008614501?style=flat-square&label=discord&logo=discord&logoColor=white&color=5865F2" alt="Discord">
  </a>
</div>

Official Node.js client library for interacting with the Lightfeed API. Extract, search, and filter web data with a simple and intuitive interface.

## Features

- Simple and intuitive interface for accessing Lightfeed APIs
- Semantic search and advanced filtering capabilities
- Full type definitions for better developer experience
- Comprehensive error handling
- Support for pagination

## Installation

```bash
npm install lightfeed
```

## Quick Start

```typescript
import { LightfeedClient } from 'lightfeed';

// Initialize client with your API key
const client = new LightfeedClient({
  apiKey: 'YOUR_API_KEY'
});

// Retrieve records
async function getRecentRecords() {
  try {
    const response = await client.getRecords('your-database-id', {
      start_time: '2024-01-01T00:00:00Z',
      limit: 100
    });
    
    console.log(`Retrieved ${response.results.length} records`);
    console.log(response.results);
  } catch (error) {
    console.error('Error retrieving records:', error);
  }
}

// Search records
async function searchForCompanies() {
  try {
    const response = await client.searchRecords('your-database-id', {
      search: {
        text: 'innovative AI solutions',
        threshold: 0.3
      },
      filter: {
        condition: 'AND',
        rules: [
          {
            column: 'industry',
            operator: 'equals',
            value: 'Technology'
          }
        ]
      }
    });
    
    console.log(`Found ${response.results.length} matching records`);
  } catch (error) {
    console.error('Error searching records:', error);
  }
}
```

## API Documentation

### Configuration

```typescript
interface LightfeedConfig {
  apiKey: string;
  baseUrl?: string;  // defaults to 'https://api.lightfeed.ai'
  timeout?: number;  // defaults to 30000 (30 seconds)
}
```

### Methods

#### `getRecords`

Retrieves records from a database with optional filtering by time range.

```typescript
client.getRecords(databaseId: string, params?: GetRecordsParams): Promise<RecordsResponse>
```

#### `searchRecords`

Performs semantic search on your database records with optional filtering.

```typescript
client.searchRecords(databaseId: string, params: SearchRecordsParams): Promise<RecordsResponse>
```

#### `filterRecords`

Applies complex filtering conditions to database records.

```typescript
client.filterRecords(databaseId: string, params: FilterRecordsParams): Promise<RecordsResponse>
```

## Error Handling

The client library handles HTTP errors from the API and converts them into structured `LightfeedError` objects.

```typescript
try {
  const records = await client.getRecords('your-database-id');
} catch (error) {
  console.error(`Error ${error.status}: ${error.message}`);
  
  // Handle specific error types
  switch (error.status) {
    case 401:
      console.log('Authentication failed. Please check your API key');
      break;
    case 404:
      console.log('Database not found');
      break;
    // ...
  }
}
```

## Documentation

For comprehensive documentation and guides, visit the [Lightfeed Documentation](https://www.lightfeed.ai/docs).

## Support

If you need assistance with your implementation:
- Email us at support@lightfeed.ai
- Open an issue in the [GitHub repository](https://github.com/lightfeed/lightfeed)
- Join our [Discord community](https://discord.gg/txZ2s4pgQJ) 