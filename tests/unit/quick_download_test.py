#!/usr/bin/env python3
"""
Test rápido de endpoints de descarga
"""

import requests
import json

def test_endpoints():
    base_url = "http://localhost:8000"
    
    print("🧪 Testing Download Endpoints")
    print("=" * 30)
    
    # 1. Test health
    try:
        response = requests.get(f"{base_url}/health")
        if response.status_code == 200:
            print("✅ API is running")
        else:
            print("❌ API health check failed")
            return
    except:
        print("❌ Cannot connect to API")
        return
    
    # 2. Test list deployments
    try:
        response = requests.get(f"{base_url}/models/deployments/list")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ List deployments endpoint working")
            print(f"   Status: {data.get('status')}")
            print(f"   Message: {data.get('message')}")
            print(f"   Deployments: {len(data.get('deployments', []))}")
            
            # Si hay deployments, mostrar el primero
            if data.get('deployments'):
                first = data['deployments'][0]
                print(f"   First deployment: {first.get('filename')}")
                
                # 3. Test download
                filename = first.get('filename')
                if filename:
                    download_response = requests.get(f"{base_url}/models/deployments/download/{filename}")
                    if download_response.status_code == 200:
                        print(f"✅ Download endpoint working")
                        print(f"   Content-Type: {download_response.headers.get('content-type')}")
                        print(f"   Content-Length: {len(download_response.content)} bytes")
                    else:
                        print(f"❌ Download failed: {download_response.status_code}")
        else:
            print(f"❌ List deployments failed: {response.status_code}")
            print(f"   Response: {response.text}")
            
    except Exception as e:
        print(f"❌ Error testing endpoints: {e}")

if __name__ == "__main__":
    import sys, os
    ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
    if ROOT not in sys.path:
        sys.path.insert(0, ROOT)
    test_endpoints()