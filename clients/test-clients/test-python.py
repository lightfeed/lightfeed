#!/usr/bin/env python
# Test script for the Lightfeed Python client

from lightfeed import LightfeedClient

def test_client():
    try:
        print("Testing Lightfeed Python client...")
        
        # Initialize client with your API key
        client = LightfeedClient({
            "apiKey": "test-api-key"
        })
        
        print("Client instance created successfully")
        print("Client configuration:")
        print(f"- API key: {client.api_key}")
        print(f"- Base URL: {client.base_url}")
        print(f"- Timeout: {client.timeout}")
        
        # Mock API calls for testing
        # In a real scenario, you would use actual API keys and database IDs
        print("\nTest successful! The client is correctly installed.")
    except Exception as e:
        print(f"Test failed with error: {e}")

if __name__ == "__main__":
    test_client() 