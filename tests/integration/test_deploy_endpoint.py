#!/usr/bin/env python3
"""
Test script to call the deploy endpoint via HTTP
"""

import requests
import json

def test_deploy_endpoint():
    """Test the /models/deploy endpoint"""
    
    url = "http://127.0.0.1:8000/models/deploy"
    
    # Test data
    payload = {
        "model_name": "basic-test-model",
        "version": "1.0.2"
    }
    
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }
    
    print("🧪 Testing Deploy Endpoint via HTTP")
    print("=" * 50)
    print(f"URL: {url}")
    print(f"Payload: {json.dumps(payload, indent=2)}")
    print()
    
    try:
        # Make the POST request
        response = requests.post(url, json=payload, headers=headers)
        
        print(f"Status Code: {response.status_code}")
        print()
        
        if response.status_code == 200:
            result = response.json()
            print("✅ Success! Deployment Response:")
            print(f"Status: {result['status']}")
            print(f"Message: {result['message']}")
            print(f"Deployment Folder: {result['deployment_folder']}")
            print(f"Files Created: {result['files_created']}")
            print()
            print("📋 Instructions:")
            print(result['instructions'])
        else:
            print(f"❌ Error: {response.status_code}")
            print(response.text)
            
    except requests.exceptions.ConnectionError:
        print("❌ Connection Error: Make sure the FastAPI server is running on http://127.0.0.1:8000")
    except Exception as e:
        print(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    test_deploy_endpoint()