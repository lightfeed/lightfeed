"""
Lightfeed API Client Library

This library provides a convenient way to interact with the Lightfeed API to access 
your extracted web data programmatically.
"""

from lightfeed.client import LightfeedClient
from lightfeed.models import (
    LightfeedConfig,
    Record,
    Timestamps,
    GetRecordsParams,
    SearchRecordsParams,
    FilterRecordsParams,
    TimeRange,
    SearchParams,
    Filter,
    Condition,
    Operator,
    ColumnRule,
    RuleGroup,
    PaginationParams,
    RecordsResponse,
    Pagination,
)

__all__ = [
    "LightfeedClient",
    "LightfeedConfig",
    "Record",
    "Timestamps",
    "GetRecordsParams",
    "SearchRecordsParams",
    "FilterRecordsParams",
    "TimeRange",
    "SearchParams",
    "Filter",
    "Condition",
    "Operator",
    "ColumnRule",
    "RuleGroup",
    "PaginationParams",
    "RecordsResponse",
    "Pagination",
]

__version__ = "0.1.0" 