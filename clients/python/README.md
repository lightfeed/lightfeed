# Lightfeed API Client for Python

Official Python client library for interacting with the Lightfeed API. This library enables easy access to your extracted web data.

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

## API Methods

### get_records

Retrieves records from a database with optional filtering by time range.

```python
client.get_records(database_id: str, params: Optional[GetRecordsParams]) -> RecordsResponse
```

### search_records

Performs semantic search on your database records with optional filtering.

```python
client.search_records(database_id: str, params: SearchRecordsParams) -> RecordsResponse
```

### filter_records

Applies complex filtering conditions to database records.

```python
client.filter_records(database_id: str, params: FilterRecordsParams) -> RecordsResponse
```

## Pagination

All methods that return multiple records support pagination. You can use the `next_cursor` from the response to fetch the next page of results.

```python
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

The client library throws custom errors that include details about what went wrong.

```python
from lightfeed import LightfeedError

try:
    records = client.get_records("your-database-id")
except LightfeedError as e:
    print(f"Error {e.status}: {e.message}")
    if e.details:
        print(f"Details: {e.details}")
```

## Requirements

- Python 3.7+
- requests

## Development

```bash
# Clone the repo
git clone https://github.com/lightfeed/lightfeed-api-clients.git
cd lightfeed-api-clients/clients/python

# Install in development mode
pip install -e .

# Run tests
pytest
```

## Type Hints

The library provides comprehensive type hints for better IDE support and static type checking.

```python
from lightfeed.models import (
    LightfeedConfig,
    Record,
    SearchParams,
    Filter,
    Condition,
    Operator
)
```

## Documentation

For more detailed documentation, please refer to the [main README](../../README.md) or visit the [Lightfeed API documentation](https://www.lightfeed.ai/docs/apis/).

## License

This project is licensed under the MIT License - see the LICENSE file for details. 