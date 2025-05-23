"""
Lightfeed API Client type definitions
"""

from enum import Enum, auto, IntEnum
from typing import Dict, List, Optional, Union, Any, TypedDict, Literal


class LightfeedConfig(TypedDict, total=False):
    """API client configuration"""
    
    apiKey: str  # Lightfeed API key (required)
    baseUrl: Optional[str]  # API base URL (defaults to https://api.lightfeed.ai)
    timeout: Optional[float]  # Request timeout in seconds (defaults to 30)


class Timestamps(TypedDict):
    """Timestamp object for records"""
    
    first_seen_time: str  # ISO 8601 timestamp when the record was first seen
    last_changed_time: str  # ISO 8601 timestamp when the record was last changed
    last_seen_time: str  # ISO 8601 timestamp when the record was last seen


class Record(TypedDict, total=False):
    """Record returned by the API"""
    
    id: int  # Unique identifier for the record
    data: Dict[str, Any]  # The record's structured data
    timestamps: Timestamps  # Timing information for the record
    relevance_score: Optional[float]  # Relevance score (only present if semantic search is applied)


class Pagination(TypedDict):
    """Pagination metadata"""
    
    limit: int  # The requested limit parameter value from the original request
    next_cursor: Optional[str]  # Token to use for fetching the next page
    has_more: bool  # Indicates whether more results are available


class RecordsResponse(TypedDict):
    """API response with records and pagination"""
    
    results: List[Record]  # List of records
    pagination: Pagination  # Pagination information


class GetRecordsParams(TypedDict, total=False):
    """Query parameters for retrieving records"""
    
    start_time: Optional[str]  # Start of last seen time range (ISO 8601 timestamp)
    end_time: Optional[str]  # End of last seen time range (ISO 8601 timestamp)
    limit: Optional[int]  # Maximum number of records to return (default: 100, max: 500)
    cursor: Optional[str]  # Cursor for pagination (from previous response)


class TimeRange(TypedDict, total=False):
    """Time range for filtering records"""
    
    start_time: Optional[str]  # Start of last seen time range (ISO 8601 timestamp)
    end_time: Optional[str]  # End of last seen time range (ISO 8601 timestamp)


class PaginationParams(TypedDict, total=False):
    """Pagination parameters for search/filter"""
    
    limit: Optional[int]  # Maximum number of records to return (default: 100, max: 500)
    cursor: Optional[str]  # Cursor for pagination (from previous response)


class SearchParams(TypedDict, total=False):
    """Semantic search parameters"""
    
    text: str  # The text to search for
    threshold: Optional[float]  # Minimum relevance score threshold (0 to 1, defaults to 0.2)


class Condition(str, Enum):
    """Condition type for filter rules"""
    
    AND = "AND"
    OR = "OR"


class Operator(str, Enum):
    """Comparison operators for filter rules"""
    
    EQUALS = "equals"
    NOT_EQUALS = "not_equals"
    GREATER_THAN = "greater_than"
    LESS_THAN = "less_than"
    GREATER_THAN_OR_EQUALS = "greater_than_or_equals"
    LESS_THAN_OR_EQUALS = "less_than_or_equals"
    CONTAINS = "contains"
    NOT_CONTAINS = "not_contains"
    STARTS_WITH = "starts_with"
    ENDS_WITH = "ends_with"
    IS_EMPTY = "is_empty"
    IS_NOT_EMPTY = "is_not_empty"


class ColumnRule(TypedDict, total=False):
    """Simple filter rule for a single column"""
    
    column: str  # The column name to filter on
    operator: Operator  # The comparison operator
    value: Optional[Any]  # The value to compare with


# Need this forward reference for the RuleGroup
RuleGroup_TypeHint = Dict[str, Union[Condition, List[Union['RuleGroup_TypeHint', ColumnRule]]]]


class RuleGroup(TypedDict):
    """Group of filter rules with a logical condition"""
    
    condition: Condition  # Logical operator to combine rules (AND/OR)
    rules: List[Union[RuleGroup_TypeHint, ColumnRule]]  # List of rules or rule groups


# Type alias for filter definition
Filter = RuleGroup


class SearchRecordsParams(TypedDict, total=False):
    """Parameters for search records API"""
    
    search: SearchParams  # Semantic search parameters
    filter: Optional[Filter]  # Filter to apply (optional)
    time_range: Optional[TimeRange]  # Time range to filter by (optional)
    pagination: Optional[PaginationParams]  # Pagination parameters (optional)


class FilterRecordsParams(TypedDict, total=False):
    """Parameters for filter records API"""
    
    filter: Filter  # Filter to apply
    time_range: Optional[TimeRange]  # Time range to filter by (optional)
    pagination: Optional[PaginationParams]  # Pagination parameters (optional)


# Define valid error status codes
class ErrorStatus(IntEnum):
    """Valid API error status codes"""
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    RATE_LIMIT_EXCEEDED = 429
    INTERNAL_SERVER_ERROR = 500


class LightfeedError(Exception):
    """Error from the Lightfeed API"""
    
    def __init__(self, status: int, message: str):
        """
        Initialize a Lightfeed API error
        
        Args:
            status: HTTP status code (400, 401, 403, 404, 429, or 500)
            message: Error message from the API
        """
        # Validate the status code is one of the expected ones
        if status not in [400, 401, 403, 404, 429, 500]:
            status = 500  # Default to internal server error for unexpected codes
            
        self.status = status
        self.message = message
        super().__init__(f"Lightfeed API Error ({status}): {message}")

    def __repr__(self) -> str:
        return f"LightfeedError(status={self.status}, message='{self.message}')"
        
    @staticmethod
    def get_default_message(status: int) -> str:
        """
        Get the default error message for a given status code
        
        Args:
            status: HTTP status code
            
        Returns:
            Default error message for the status code
        """
        messages = {
            400: "Invalid request parameters",
            401: "Invalid or missing API key",
            403: "The API key doesn't have permission to access the resource",
            404: "The requested resource doesn't exist",
            429: "Rate limit exceeded",
            500: "Something went wrong on our end"
        }
        return messages.get(status, "Unknown error") 