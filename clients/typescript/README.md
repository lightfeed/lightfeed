# Lightfeed Node SDK

Official Node.js client library for interacting with the Lightfeed API. Extract, search, and filter web data with a simple and intuitive interface.

## Features

- Simple and intuitive interface for accessing Lightfeed APIs
- Semantic search and advanced filtering capabilities
- Full type definitions for better developer experience
- Comprehensive error handling
- Support for pagination

## Installation

```bash
npm install @lightfeed/sdk
```

## Quick Start

```typescript
import { LightfeedClient } from '@lightfeed/sdk';

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

**Parameters:**
- `databaseId` (string): The ID of your Lightfeed database
- `params` (optional): Query parameters
  - `start_time` (string, optional): Start of time range (ISO 8601)
  - `end_time` (string, optional): End of time range (ISO 8601)
  - `limit` (number, optional): Maximum records to return (default: 100, max: 500)
  - `cursor` (string, optional): Pagination cursor

**Returns:** Records response containing results and pagination information

For detailed specifications and examples, see [Get Records API](https://www.lightfeed.ai/docs/apis/v1-database/records/)

#### `searchRecords`

Performs semantic search on your database records with optional filtering.

```typescript
client.searchRecords(databaseId: string, params: SearchRecordsParams): Promise<RecordsResponse>
```

**Parameters:**
- `databaseId` (string): The ID of your Lightfeed database
- `params`: Search parameters
  - `search.text` (string): The text to search for
  - `search.threshold` (number, optional): Minimum relevance score (0-1)
  - `filter` (object, optional): Filtering conditions
  - `time_range` (object, optional): Time range constraints
  - `pagination` (object, optional): Pagination options

**Returns:** Records response containing results with relevance scores

For detailed specifications and examples, see [Search Records API](https://www.lightfeed.ai/docs/apis/v1-database/search/)

#### `filterRecords`

Applies complex filtering conditions to database records.

```typescript
client.filterRecords(databaseId: string, params: FilterRecordsParams): Promise<RecordsResponse>
```

**Parameters:**
- `databaseId` (string): The ID of your Lightfeed database
- `params`: Filter parameters
  - `filter` (object): Filtering conditions using rules and operators
  - `time_range` (object, optional): Time range constraints
  - `pagination` (object, optional): Pagination options

**Returns:** Records response containing filtered results

For detailed specifications and examples, see [Filter Records API](https://www.lightfeed.ai/docs/apis/v1-database/filter/)

## Authentication

All API requests require authentication using your Lightfeed API key. You can generate an API key in the Lightfeed dashboard under "API Keys".

```typescript
const client = new LightfeedClient({
  apiKey: 'YOUR_API_KEY'
});
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
- Open an issue in the [GitHub repository](https://github.com/lightfeed/sdk)
- Join our [Discord community](https://discord.gg/txZ2s4pgQJ) 