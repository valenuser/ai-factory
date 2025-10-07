#!/usr/bin/env python3
"""
Test the new Swagger example in the actual API
"""
import requests
import json
import time

def test_swagger_example():
    """Test using the exact example from Swagger documentation"""
    url = "http://127.0.0.1:8000/models/train"
    
    # This is the exact example from our Swagger documentation
    payload = {
        "model_name": "basic-test-model",
        "prompts": "What is the capital of France?, Explain what photosynthesis is in simple terms., How many days are there in a leap year?, What is the largest planet in our solar system?, Define what artificial intelligence means., Help me solve this math problem: If I have 15 apples and give away 7, how many do I have left?, I need to organize my daily schedule. Can you suggest a structure for planning my day?, What are three ways to improve productivity while working from home?, How can I remember important dates and appointments better?, Give me steps to troubleshoot a computer that won't start., Suggest five creative names for a new coffee shop., Help me write a short welcome message for new team members., What are some fun indoor activities for a rainy weekend?, Give me ideas for a healthy breakfast that takes less than 10 minutes to make., Explain how to change a tire in simple steps., What is the difference between HTTP and HTTPS?, Compare the advantages and disadvantages of working remotely versus in an office., What are the pros and cons of electric vehicles?, Give me tips for staying focused during long study sessions., List the top 5 benefits of regular exercise and explain each briefly."
    }
    
    print("📖 SWAGGER EXAMPLE TEST")
    print("=" * 60)
    print(f"URL: {url}")
    print(f"Model: {payload['model_name']}")
    print(f"Total prompts in example: {len(payload['prompts'].split(','))} prompts")
    print("=" * 60)
    
    try:
        print("🚀 Sending Swagger example request...")
        start_time = time.time()
        
        response = requests.post(url, json=payload, timeout=90)
        
        end_time = time.time()
        execution_time = end_time - start_time
        
        print(f"⏱️ Total execution time: {execution_time:.2f}s")
        print(f"📊 Status Code: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            print(f"✅ Status: {result.get('status', 'unknown')}")
            
            if result.get('status') == 'success':
                metrics = result.get('metrics', {})
                print(f"\n📈 TRAINING RESULTS:")
                print(f"  🎯 Success rate: {metrics.get('successful_responses', 0)}/{metrics.get('total_prompts_tested', 0)}")
                print(f"  📊 Accuracy: {metrics.get('accuracy', 0)}")
                print(f"  ⚡ Avg response time: {metrics.get('avg_response_time', 0):.2f}s")
                print(f"  📦 Total prompts provided: {metrics.get('total_prompts_provided', 0)}")
                print(f"  🔧 Model version: {result.get('version', 'N/A')}")
                print(f"  📝 Summary: {result.get('test_results_summary', 'N/A')}")
                
                feedback = result.get('feedback', '')
                if feedback:
                    print(f"\n🤖 AI FEEDBACK:")
                    print(f"  {feedback[:200]}...")
                
                print(f"\n🏆 SUCCESS: Swagger example worked perfectly!")
                print(f"💡 Users can copy this exact example from /docs")
                
            else:
                print(f"❌ Training failed: {result.get('message', 'Unknown error')}")
        else:
            print(f"❌ HTTP Error: {response.status_code}")
            print(f"Response: {response.text}")
            
    except requests.exceptions.Timeout:
        print("⏰ Request timeout - example might have too many prompts")
    except requests.exceptions.ConnectionError:
        print("🔌 Connection error - make sure server is running on port 8000")
    except Exception as e:
        print(f"💥 Unexpected error: {str(e)}")

if __name__ == "__main__":
    test_swagger_example()