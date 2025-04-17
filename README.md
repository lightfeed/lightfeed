# Lightfeed API Client Libraries

Official client libraries for interacting with the Lightfeed API. These libraries enable easy access to your extracted web data, with support for both Node.js (TypeScript) and Python environments.

## Features

- Simple and intuitive interface for accessing Lightfeed APIs
- Full TypeScript/Python type definitions for better developer experience
- Comprehensive error handling
- Support for pagination
- Semantic search and advanced filtering capabilities

## Installation

### Node.js / TypeScript

```bash
npm install lightfeed
```

### Python

```bash
pip install lightfeed
```

## Quick Start

### Node.js / TypeScript

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

### Python

```python
from lightfeed import LightfeedClient, Condition, Operator

# Initialize client with your API key
client = LightfeedClient({
    "apiKey": "YOUR_API_KEY"
})

# Retrieve records
def get_recent_records():
    try:
        response = client.get_records("your-database-id", {
            "start_time": "2024-01-01T00:00:00Z",
            "limit": 100
        })
        
        print(f"Retrieved {len(response['results'])} records")
        print(response["results"])
    except Exception as e:
        print(f"Error retrieving records: {e}")

# Search records
def search_for_companies():
    try:
        response = client.search_records("your-database-id", {
            "search": {
                "text": "innovative AI solutions",
                "threshold": 0.3
            },
            "filter": {
                "condition": Condition.AND,
                "rules": [
                    {
                        "column": "industry",
                        "operator": Operator.EQUALS,
                        "value": "Technology"
                    }
                ]
            }
        })
        
        print(f"Found {len(response['results'])} matching records")
    except Exception as e:
        print(f"Error searching records: {e}")
```

## API Documentation

### Configuration

#### TypeScript
```typescript
interface LightfeedConfig {
  apiKey: string;
  baseUrl?: string;  // defaults to 'https://api.lightfeed.ai'
  timeout?: number;  // defaults to 30000 (30 seconds)
}
```

#### Python
```python
{
  "apiKey": str,        # required
  "baseUrl": str,       # optional, defaults to 'https://api.lightfeed.ai'
  "timeout": float      # optional, defaults to 30.0 seconds
}
```

### Methods

Both TypeScript and Python clients provide the same set of methods:

#### getRecords / get_records

Retrieves records from a database with optional filtering by time range.

```typescript
// TypeScript
client.getRecords(databaseId: string, params?: GetRecordsParams): Promise<RecordsResponse>

// Python
client.get_records(database_id: str, params: Optional[GetRecordsParams]) -> RecordsResponse
```

#### searchRecords / search_records

Performs semantic search on your database records with optional filtering.

```typescript
// TypeScript
client.searchRecords(databaseId: string, params: SearchRecordsParams): Promise<RecordsResponse>

// Python
client.search_records(database_id: str, params: SearchRecordsParams) -> RecordsResponse
```

#### filterRecords / filter_records

Applies complex filtering conditions to database records.

```typescript
// TypeScript
client.filterRecords(databaseId: string, params: FilterRecordsParams): Promise<RecordsResponse>

// Python
client.filter_records(database_id: str, params: FilterRecordsParams) -> RecordsResponse
```

## Authentication

All API requests require authentication using your Lightfeed API key. You can generate an API key in the Lightfeed dashboard under "API Keys".

```typescript
// TypeScript
const client = new LightfeedClient({
  apiKey: 'YOUR_API_KEY'
});

// Python
client = LightfeedClient({
  "apiKey": "YOUR_API_KEY"
})
```

## Pagination

All methods that return multiple records support pagination. You can use the `next_cursor` from the response to fetch the next page of results.

```typescript
// TypeScript example
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

The client libraries throw custom errors that include details about what went wrong.

```typescript
// TypeScript
try {
  const records = await client.getRecords('your-database-id');
} catch (error) {
  console.error(`Error ${error.status}: ${error.message}`);
  console.error('Details:', error.details);
}

// Python
try:
    records = client.get_records("your-database-id")
except LightfeedError as e:
    print(f"Error {e.status}: {e.message}")
    if e.details:
        print(f"Details: {e.details}")
```

## Requirements

### Node.js / TypeScript

- Node.js 14+
- TypeScript 4.5+ (for TypeScript users)

### Python

- Python 3.7+
- requests

## Development

```bash
# Clone the repo
git clone https://github.com/lightfeed/lightfeed-api-clients.git
cd lightfeed-api-clients

# TypeScript client
cd clients/typescript
npm install
npm test

# Python client
cd clients/python
pip install -e ".[dev]"
pytest
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, please email support@lightfeed.ai or visit our [documentation](https://www.lightfeed.ai/docs).
