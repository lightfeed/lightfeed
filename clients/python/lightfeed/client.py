"""
Lightfeed API Client Implementation
"""

import json
from typing import Any, Dict, Optional, cast

import requests
from requests.exceptions import RequestException

from lightfeed.models import (
    LightfeedConfig,
    RecordsResponse,
    GetRecordsParams,
    SearchRecordsParams,
    FilterRecordsParams,
    LightfeedError,
)


# Default configuration values
DEFAULT_BASE_URL = "https://api.lightfeed.ai"
DEFAULT_TIMEOUT = 30.0  # 30 seconds


class LightfeedClient:
    """
    Lightfeed API Client
    
    Client for interacting with the Lightfeed API to access your extracted web data.
    """

    def __init__(self, config: LightfeedConfig) -> None:
        """
        Creates a new Lightfeed API client
        
        Args:
            config: Client configuration with API key and optional settings
        """
        self.api_key = config["apiKey"]
        self.base_url = config.get("baseUrl") or DEFAULT_BASE_URL
        self.timeout = config.get("timeout") or DEFAULT_TIMEOUT
        
        # Prepare request headers used for all API calls
        self.headers = {
            "x-api-key": self.api_key,
            "Content-Type": "application/json",
        }

    def get_records(
        self, database_id: str, params: Optional[GetRecordsParams] = None
    ) -> RecordsResponse:
        """
        Get all records from a database with optional filters
        
        Args:
            database_id: The database ID
            params: Optional query parameters
            
        Returns:
            Records response containing results and pagination information
            
        Raises:
            LightfeedError: If the API request fails
        """
        url = f"{self.base_url}/v1/databases/{database_id}/records"
        
        try:
            response = requests.get(
                url, 
                headers=self.headers, 
                params=params, 
                timeout=self.timeout
            )
            response.raise_for_status()
            return cast(RecordsResponse, response.json())
        except RequestException as e:
            raise self._handle_error(e)

    def search_records(
        self, database_id: str, params: SearchRecordsParams
    ) -> RecordsResponse:
        """
        Search records using semantic search with optional filters
        
        Args:
            database_id: The database ID
            params: Search parameters including search text, filters, and pagination
            
        Returns:
            Records response containing results and pagination information
            
        Raises:
            LightfeedError: If the API request fails
        """
        url = f"{self.base_url}/v1/databases/{database_id}/records/search"
        
        try:
            response = requests.post(
                url, 
                headers=self.headers, 
                json=params, 
                timeout=self.timeout
            )
            response.raise_for_status()
            return cast(RecordsResponse, response.json())
        except RequestException as e:
            raise self._handle_error(e)

    def filter_records(
        self, database_id: str, params: FilterRecordsParams
    ) -> RecordsResponse:
        """
        Filter records using complex filter expressions
        
        Args:
            database_id: The database ID
            params: Filter parameters including filter rules, time range, and pagination
            
        Returns:
            Records response containing results and pagination information
            
        Raises:
            LightfeedError: If the API request fails
        """
        url = f"{self.base_url}/v1/databases/{database_id}/records/filter"
        
        try:
            response = requests.post(
                url, 
                headers=self.headers, 
                json=params, 
                timeout=self.timeout
            )
            response.raise_for_status()
            return cast(RecordsResponse, response.json())
        except RequestException as e:
            raise self._handle_error(e)

    def _handle_error(self, error: RequestException) -> LightfeedError:
        """
        Handles and transforms API errors into a consistent format
        
        Args:
            error: The exception from the requests library
            
        Returns:
            A formatted LightfeedError
        """
        if getattr(error, "response", None) is not None:
            response = error.response
            status_code = response.status_code
            
            # Ensure status code is one of the expected ones
            if status_code not in [400, 401, 403, 404, 429, 500]:
                status_code = 500  # Default to internal server error
                
            try:
                error_data = response.json()
                message = error_data.get("message", LightfeedError.get_default_message(status_code))
            except (ValueError, json.JSONDecodeError):
                message = response.text or LightfeedError.get_default_message(status_code)
                
            return LightfeedError(status_code, message)
        
        # For network errors, connection issues, etc.
        return LightfeedError(500, str(error)) 