# Lightfeed Python SDK

Official Python client library for interacting with the Lightfeed API. Extract, search, and filter web data with a simple and intuitive interface.

## Features

- Simple and intuitive interface for accessing Lightfeed APIs
- Semantic search and advanced filtering capabilities
- Full type definitions for better developer experience
- Comprehensive error handling
- Support for pagination

## Installation

```bash
pip install lightfeed
```

## Quick Start

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

```python
{
  "apiKey": str,        # required
  "baseUrl": str,       # optional, defaults to 'https://api.lightfeed.ai'
  "timeout": float      # optional, defaults to 30.0 seconds
}
```

### Methods

#### `get_records`

Retrieves records from a database with optional filtering by time range.

```python
client.get_records(database_id: str, params: Optional[GetRecordsParams]) -> RecordsResponse
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

#### `search_records`

Performs semantic search on your database records with optional filtering.

```python
client.search_records(database_id: str, params: SearchRecordsParams) -> RecordsResponse
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

#### `filter_records`

Applies complex filtering conditions to database records.

```python
client.filter_records(database_id: str, params: FilterRecordsParams) -> RecordsResponse
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

```python
client = LightfeedClient({
  "apiKey": "YOUR_API_KEY"
})
```

## Error Handling

The client library handles HTTP errors from the API and converts them into structured `LightfeedError` objects.

```python
from lightfeed import LightfeedError

try:
    records = client.get_records("your-database-id")
except LightfeedError as e:
    print(f"Error {e.status}: {e.message}")
    
    # Handle specific error types
    if e.status == 401:
        print("Authentication failed. Please check your API key")
    elif e.status == 404:
        print("Database not found")
    # ...
```

## Documentation

For comprehensive documentation and guides, visit the [Lightfeed Documentation](https://www.lightfeed.ai/docs).

## Support

If you need assistance with your implementation:
- Email us at support@lightfeed.ai
- Open an issue in the [GitHub repository](https://github.com/lightfeed/lightfeed)
- Join our [Discord community](https://discord.gg/txZ2s4pgQJ) 