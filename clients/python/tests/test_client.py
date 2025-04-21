"""
Tests for the Lightfeed API client
"""

import json
import unittest
from unittest.mock import patch, Mock

import requests
from requests.exceptions import RequestException

from lightfeed import LightfeedClient
from lightfeed.models import Condition, Operator, LightfeedError


class TestLightfeedClient(unittest.TestCase):
    """Test cases for the Lightfeed API client"""

    def setUp(self):
        """Set up the test client"""
        self.client = LightfeedClient({"apiKey": "test-api-key"})

    def test_init(self):
        """Test client initialization with default and custom values"""
        # Test with default values
        self.assertEqual(self.client.api_key, "test-api-key")
        self.assertEqual(self.client.base_url, "https://api.lightfeed.ai")
        self.assertEqual(self.client.timeout, 30.0)

        # Test with custom values
        custom_client = LightfeedClient({
            "apiKey": "custom-api-key",
            "baseUrl": "https://custom-api.example.com",
            "timeout": 10.0
        })
        self.assertEqual(custom_client.api_key, "custom-api-key")
        self.assertEqual(custom_client.base_url, "https://custom-api.example.com")
        self.assertEqual(custom_client.timeout, 10.0)

    @patch("requests.get")
    def test_get_records(self, mock_get):
        """Test the get_records method"""
        # Setup mock response
        mock_response = Mock()
        mock_response.json.return_value = {
            "results": [
                {
                    "id": 1,
                    "data": {"name": "Test Record"},
                    "timestamps": {
                        "first_seen_time": "2023-01-01T00:00:00Z",
                        "last_changed_time": "2023-01-02T00:00:00Z",
                        "last_seen_time": "2023-01-03T00:00:00Z"
                    }
                }
            ],
            "pagination": {
                "limit": 100,
                "next_cursor": None,
                "has_more": False
            }
        }
        mock_get.return_value = mock_response

        # Call the method
        params = {
            "start_time": "2023-01-01T00:00:00Z",
            "limit": 10
        }
        result = self.client.get_records("test-db-id", params)

        # Verify the request
        mock_get.assert_called_once_with(
            "https://api.lightfeed.ai/v1/databases/test-db-id/records",
            headers={
                "x-api-key": "test-api-key",
                "Content-Type": "application/json"
            },
            params=params,
            timeout=30.0
        )

        # Verify the response
        self.assertEqual(result, mock_response.json.return_value)

    @patch("requests.post")
    def test_search_records(self, mock_post):
        """Test the search_records method"""
        # Setup mock response
        mock_response = Mock()
        mock_response.json.return_value = {
            "results": [
                {
                    "id": 1,
                    "data": {"name": "Test Record"},
                    "timestamps": {
                        "first_seen_time": "2023-01-01T00:00:00Z",
                        "last_changed_time": "2023-01-02T00:00:00Z",
                        "last_seen_time": "2023-01-03T00:00:00Z"
                    },
                    "relevance_score": 0.9
                }
            ],
            "pagination": {
                "limit": 100,
                "next_cursor": None,
                "has_more": False
            }
        }
        mock_post.return_value = mock_response

        # Call the method
        params = {
            "search": {
                "text": "test query",
                "threshold": 0.5
            }
        }
        result = self.client.search_records("test-db-id", params)

        # Verify the request
        mock_post.assert_called_once_with(
            "https://api.lightfeed.ai/v1/databases/test-db-id/records/search",
            headers={
                "x-api-key": "test-api-key",
                "Content-Type": "application/json"
            },
            json=params,
            timeout=30.0
        )

        # Verify the response
        self.assertEqual(result, mock_response.json.return_value)

    @patch("requests.post")
    def test_filter_records(self, mock_post):
        """Test the filter_records method"""
        # Setup mock response
        mock_response = Mock()
        mock_response.json.return_value = {
            "results": [
                {
                    "id": 1,
                    "data": {"name": "Test Record", "category": "Test"},
                    "timestamps": {
                        "first_seen_time": "2023-01-01T00:00:00Z",
                        "last_changed_time": "2023-01-02T00:00:00Z",
                        "last_seen_time": "2023-01-03T00:00:00Z"
                    }
                }
            ],
            "pagination": {
                "limit": 100,
                "next_cursor": None,
                "has_more": False
            }
        }
        mock_post.return_value = mock_response

        # Call the method
        params = {
            "filter": {
                "condition": Condition.AND,
                "rules": [
                    {
                        "column": "category",
                        "operator": Operator.EQUALS,
                        "value": "Test"
                    }
                ]
            }
        }
        result = self.client.filter_records("test-db-id", params)

        # Verify the request
        mock_post.assert_called_once_with(
            "https://api.lightfeed.ai/v1/databases/test-db-id/records/filter",
            headers={
                "x-api-key": "test-api-key",
                "Content-Type": "application/json"
            },
            json=params,
            timeout=30.0
        )

        # Verify the response
        self.assertEqual(result, mock_response.json.return_value)

    @patch("requests.get")
    def test_error_handling(self, mock_get):
        """Test error handling"""
        # Create a RequestException with response attributes
        mock_response = Mock()
        mock_response.status_code = 401
        mock_response.json.return_value = {
            "message": "Invalid API key"
        }
        
        # Create the exception with the response
        exception = RequestException("API Error")
        exception.response = mock_response
        
        # Make the request raise the exception
        mock_get.side_effect = exception

        # Call the method and expect an error
        with self.assertRaises(LightfeedError) as context:
            self.client.get_records("test-db-id")

        # Verify the error
        self.assertEqual(context.exception.status, 401)
        self.assertEqual(context.exception.message, "Invalid API key")
        
    @patch("requests.get")
    def test_error_handling_with_unknown_status(self, mock_get):
        """Test error handling with an unknown status code"""
        # Create a RequestException with response attributes and an unexpected status code
        mock_response = Mock()
        mock_response.status_code = 418  # I'm a teapot (not in our expected codes)
        mock_response.json.return_value = {
            "message": "I'm a teapot"
        }
        
        # Create the exception with the response
        exception = RequestException("API Error")
        exception.response = mock_response
        
        # Make the request raise the exception
        mock_get.side_effect = exception

        # Call the method and expect an error
        with self.assertRaises(LightfeedError) as context:
            self.client.get_records("test-db-id")

        # Verify the error is normalized to 500
        self.assertEqual(context.exception.status, 500)
        self.assertEqual(context.exception.message, "I'm a teapot")  # Original message is preserved


if __name__ == "__main__":
    unittest.main() 