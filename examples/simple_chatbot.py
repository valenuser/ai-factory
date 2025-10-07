#!/usr/bin/env python3
"""
Simple example: Create your first AI chatbot in 30 seconds

This example shows how easy it is to create and train a local AI model.
"""

import requests
import json
import time

# AI Factory server URL (start with: ai-factory serve)
BASE_URL = "http://localhost:8000"

def create_simple_chatbot():
    """Create and train a simple chatbot"""
    
    print("🤖 Creating Your First AI Chatbot!")
    print("=" * 40)
    
    # Step 1: Create the model
    print("📝 Step 1: Creating model...")
    
    create_request = {
        "model_name": "friendly-bot",
        "base_prompt": "You are a friendly and helpful AI assistant. Be warm, encouraging, and provide clear answers."
    }
    
    try:
        response = requests.post(f"{BASE_URL}/models/create", json=create_request, timeout=30)
        if response.status_code == 200:
            print("   ✅ Model created successfully!")
        else:
            print(f"   ❌ Error creating model: {response.text}")
            return
    except requests.exceptions.ConnectionError:
        print("   ❌ Cannot connect to AI Factory server.")
        print("   💡 Start the server with: ai-factory serve")
        return
    
    # Step 2: Train with simple examples
    print("\n🎓 Step 2: Training with examples...")
    
    train_request = {
        "model_name": "friendly-bot", 
        "prompts": "Hello, how are you?, What can you help me with?, Tell me a fun fact, What's the weather like?, Help me plan my day"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/models/train", json=train_request, timeout=60)
        if response.status_code == 200:
            result = response.json()
            if result.get('status') == 'success':
                metrics = result.get('metrics', {})
                print(f"   ✅ Training completed!")
                print(f"   📊 Success rate: {metrics.get('successful_responses', 0)}/{metrics.get('total_prompts_tested', 0)}")
                print(f"   ⚡ Average response time: {metrics.get('avg_response_time', 0):.2f}s")
            else:
                print(f"   ⚠️ Training had issues: {result.get('message', 'Unknown')}")
        else:
            print(f"   ❌ Training failed: {response.text}")
    except Exception as e:
        print(f"   ❌ Training error: {str(e)}")
    
    # Step 3: Test the chatbot
    print(f"\n💬 Step 3: Testing your chatbot...")
    print("   🎉 Your AI chatbot 'friendly-bot' is ready!")
    print(f"   🌐 Test it at: {BASE_URL}/docs")
    print("   📋 Use the /models/train endpoint to test different prompts")
    
    print(f"\n🎯 Next Steps:")
    print(f"   1. Visit {BASE_URL}/docs for interactive testing")
    print(f"   2. Try different prompts with your model")
    print(f"   3. Export your model: GET {BASE_URL}/export")
    print(f"   4. Create more models for different purposes!")

if __name__ == "__main__":
    create_simple_chatbot()