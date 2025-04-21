#!/usr/bin/env python
# Test script for the Lightfeed Python client

import os
from dotenv import load_dotenv
from lightfeed import LightfeedClient, Operator

# Load environment variables from .env file
load_dotenv()

def test_client():
    try:
        print("Testing Lightfeed Python client...")
        
        # Initialize client with your API key
        client = LightfeedClient({
            "apiKey": os.getenv("CLIENT_API_KEY")
        })
        
        print("Client instance created successfully")
        print("Client configuration:")
        # Mask all but first 6 characters of API key
        masked_key = client.api_key[:6] + "..."
        print(f"- API key: {masked_key}")
        print(f"- Base URL: {client.base_url}")
        print(f"- Timeout: {client.timeout}")
        
        try:
            # Run search records with same parameters as test-npm.js
            response = client.search_records(os.getenv("DATABASE_ID"), {
                "search": {
                    "text": "AI solutions"
                },
                "filter": {
                    "rules": [
                        {
                            "column": "start_date",
                            "operator": Operator.EQUALS,
                            "value": 2021
                        }
                    ]
                },
                "pagination": {
                    "limit": 2,
                    "cursor": "2025-03-11T19:59:49.150Z_691"
                }
            })
            
            print(f"Found {len(response['results'])} matching records")
            print(response["results"])
            print(response["pagination"])
        except Exception as e:
            print(f"Error searching records: {e}")
        
        print("\nTest successful! The client is correctly installed.")
    except Exception as e:
        print(f"Test failed with error: {e}")

if __name__ == "__main__":
    test_client() 