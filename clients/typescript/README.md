# Lightfeed API Client for Node.js/TypeScript

Official Node.js/TypeScript client library for interacting with the Lightfeed API. This library enables easy access to your extracted web data.

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

## API Methods

### getRecords

Retrieves records from a database with optional filtering by time range.

```typescript
client.getRecords(databaseId: string, params?: GetRecordsParams): Promise<RecordsResponse>
```

### searchRecords

Performs semantic search on your database records with optional filtering.

```typescript
client.searchRecords(databaseId: string, params: SearchRecordsParams): Promise<RecordsResponse>
```

### filterRecords

Applies complex filtering conditions to database records.

```typescript
client.filterRecords(databaseId: string, params: FilterRecordsParams): Promise<RecordsResponse>
```

## Pagination

All methods that return multiple records support pagination. You can use the `next_cursor` from the response to fetch the next page of results.

```typescript
async function getAllRecords(databaseId: string) {
  let allRecords = [];
  let cursor = null;
  let hasMore = true;
  
  while (hasMore) {
    const response = await client.getRecords(databaseId, { 
      limit: 100,
      cursor 
    });
    
    allRecords = [...allRecords, ...response.results];
    cursor = response.pagination.next_cursor;
    hasMore = response.pagination.has_more;
  }
  
  return allRecords;
}
```

## Error Handling

The client library throws custom errors that include details about what went wrong.

```typescript
try {
  const records = await client.getRecords('your-database-id');
} catch (error) {
  console.error(`Error ${error.status}: ${error.message}`);
  console.error('Details:', error.details);
}
```

## Requirements

- Node.js 14+
- TypeScript 4.5+ (for TypeScript users)

## Development

```bash
# Clone the repo
git clone https://github.com/lightfeed/lightfeed-api-clients.git
cd lightfeed-api-clients/clients/typescript

# Install dependencies
npm install

# Run tests
npm test

# Build
npm run build
```

## Documentation

For more detailed documentation, please refer to the [main README](../../README.md) or visit the [Lightfeed API documentation](https://www.lightfeed.ai/docs/apis/).

## License

This project is licensed under the MIT License - see the LICENSE file for details. 