#!/usr/bin/env python3
"""
Test the API endpoint with the new threading implementation
"""
import requests
import json
import time

def test_api_endpoint():
    """Test the /train endpoint with threading"""
    url = "http://127.0.0.1:8000/models/train"
    
    payload = {
        "model_name": "basic-test-model",
        "prompts": "Explica qué es Python, Define machine learning, ¿Qué es AI?, Explica algoritmos, ¿Qué son las redes neuronales?"
    }
    
    print("🌐 API THREADING TEST")
    print("=" * 50)
    print(f"URL: {url}")
    print(f"Model: {payload['model_name']}")
    print(f"Prompts: {payload['prompts']}")
    print("=" * 50)
    
    try:
        print("🚀 Sending request...")
        start_time = time.time()
        
        response = requests.post(url, json=payload, timeout=60)
        
        end_time = time.time()
        execution_time = end_time - start_time
        
        print(f"⏱️ API Response time: {execution_time:.2f}s")
        print(f"📊 Status Code: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            print(f"✅ Status: {result.get('status', 'unknown')}")
            
            if result.get('status') == 'success':
                metrics = result.get('metrics', {})
                print(f"🎯 Success rate: {metrics.get('successful_responses', 0)}/{metrics.get('total_prompts_tested', 0)}")
                print(f"📈 Accuracy: {metrics.get('accuracy', 0)}")
                print(f"⚡ Avg response time: {metrics.get('avg_response_time', 0):.2f}s")
                print(f"📝 Summary: {result.get('test_results_summary', 'N/A')}")
                print("\n🏆 SUCCESS: Threading implementation working via API!")
            else:
                print(f"❌ Training failed: {result.get('message', 'Unknown error')}")
        else:
            print(f"❌ HTTP Error: {response.status_code}")
            print(f"Response: {response.text}")
            
    except requests.exceptions.Timeout:
        print("⏰ Request timeout - this might indicate slower performance")
    except requests.exceptions.ConnectionError:
        print("🔌 Connection error - make sure server is running on port 8000")
    except Exception as e:
        print(f"💥 Unexpected error: {str(e)}")

if __name__ == "__main__":
    test_api_endpoint()