# Lightfeed API Client

Official client library for interacting with the Lightfeed API. This SDK enables real-time search and filtering of your extracted web data, with support for both Typescript and Python environments.

## Features

- Simple and intuitive interface for accessing Lightfeed APIs
- Semantic search and advanced filtering capabilities
- Full TypeScript/Python type definitions for better developer experience
- Comprehensive error handling
- Support for pagination

## Installation

### TypeScript / Node.js

```bash
npm install lightfeed
```

### Python

```bash
pip install lightfeed
```

## Quick Start

### TypeScript / Node.js

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

Both TypeScript and Python clients provide the same core functionality through the following methods:

#### `getRecords` / `get_records`

Retrieves records from a database with optional filtering by time range.

**Parameters:**
- `databaseId` (string): The ID of your Lightfeed database
- `params` (optional): Query parameters
  - `start_time` (string, optional): Start of time range (ISO 8601)
  - `end_time` (string, optional): End of time range (ISO 8601)
  - `limit` (number, optional): Maximum records to return (default: 100, max: 500)
  - `cursor` (string, optional): Pagination cursor

**Returns:** Records response containing results and pagination information

For detailed specifications and examples, see [Get Records API](https://www.lightfeed.ai/docs/apis/v1-database/records/)

```typescript
// TypeScript
client.getRecords(databaseId: string, params?: GetRecordsParams): Promise<RecordsResponse>

// Python
client.get_records(database_id: str, params: Optional[GetRecordsParams]) -> RecordsResponse
```

#### `searchRecords` / `search_records`

Performs semantic search on your database records with optional filtering.

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

```typescript
// TypeScript
client.searchRecords(databaseId: string, params: SearchRecordsParams): Promise<RecordsResponse>

// Python
client.search_records(database_id: str, params: SearchRecordsParams) -> RecordsResponse
```

#### `filterRecords` / `filter_records`

Applies complex filtering conditions to database records.

**Parameters:**
- `databaseId` (string): The ID of your Lightfeed database
- `params`: Filter parameters
  - `filter` (object): Filtering conditions using rules and operators
  - `time_range` (object, optional): Time range constraints
  - `pagination` (object, optional): Pagination options

**Returns:** Records response containing filtered results

For detailed specifications and examples, see [Filter Records API](https://www.lightfeed.ai/docs/apis/v1-database/filter/)

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

```python
# Python example
def get_all_records(database_id):
    all_records = []
    cursor = None
    has_more = True
    
    while has_more:
        params = {
            "limit": 100
        }
        
        if cursor:
            params["cursor"] = cursor
            
        response = client.get_records(database_id, params)
        
        all_records.extend(response["results"])
        cursor = response["pagination"]["next_cursor"]
        has_more = response["pagination"]["has_more"]
    
    return all_records
```

## Error Handling

The client libraries automatically handle HTTP errors from the API and convert them into structured `LightfeedError` objects. This provides a consistent error handling experience regardless of the underlying error type.

Each error object contains:
- `status`: The HTTP status code (matches standard HTTP status codes)
- `message`: A descriptive error message

The status codes follow standard HTTP conventions:

- `400`: Invalid request parameters
- `401`: Invalid or missing API key
- `403`: Permission denied
- `404`: Resource not found
- `429`: Rate limit exceeded
- `500`: Internal server error

### TypeScript Example

```typescript
try {
  const records = await client.getRecords('your-database-id');
} catch (error) {
  // The client automatically converts API errors to LightfeedError objects
  console.error(`Error ${error.status}: ${error.message}`);
  
  // You can handle specific error types based on status code
  switch (error.status) {
    case 401:
      console.log('Authentication failed. Please check your API key');
      break;
    case 404:
      console.log('Database not found');
      break;
    case 429:
      console.log('Rate limit exceeded. Please retry after a delay');
      break;
    default:
      console.log('An unexpected error occurred');
  }
}
```

### Python Example

```python
from lightfeed import LightfeedError

try:
    records = client.get_records("your-database-id")
except LightfeedError as e:
    # The client automatically converts API errors to LightfeedError objects
    print(f"Error {e.status}: {e.message}")
    
    # You can handle specific error types based on status code
    if e.status == 401:
        print("Authentication failed. Please check your API key")
    elif e.status == 404:
        print("Database not found")
    elif e.status == 429:
        print("Rate limit exceeded. Please retry after a delay")
    else:
        print("An unexpected error occurred")
```

## Documentation

For comprehensive documentation and guides, visit the [Lightfeed Documentation](https://www.lightfeed.ai/docs).

## Community

Join our [Discord community](https://discord.gg/txZ2s4pgQJ) to:
- Connect with other Lightfeed users
- Get help with implementation questions
- Share use cases and best practices
- Stay updated on new features and releases

## Support

If you need direct assistance with your implementation:
- Email us at support@lightfeed.ai
- Open an issue in this repository
- Post your question in our [Discord community](https://discord.gg/txZ2s4pgQJ)
