#!/usr/bin/env python3
"""
AI Factory - API Training Test

Test script to verify the /train endpoint works correctly.
"""

import requests
import json
import time


def test_training_endpoint():
    """Test the /train endpoint via HTTP requests"""
    
    base_url = "http://localhost:8000"
    
    print("🧪 AI Factory - API Training Test")
    print("=" * 40)
    
    # First, check if server is running
    try:
        response = requests.get(f"{base_url}/health")
        if response.status_code != 200:
            print("❌ Server is not running. Start it with: python cli.py serve")
            return
        print("✅ Server is running")
    except requests.ConnectionError:
        print("❌ Cannot connect to server. Start it with: python cli.py serve")
        return
    
    # Step 1: Create a model first
    print("\n📝 Step 1: Creating test model...")
    
    create_data = {
        "model_name": "api-test-classifier",
        "model_prompt": "You are a text classifier. Classify the input as TECH, BUSINESS, or SPORTS."
    }
    
    try:
        create_response = requests.post(
            f"{base_url}/models/create",
            json=create_data,
            headers={"Content-Type": "application/json"}
        )
        
        if create_response.status_code == 200:
            print("✅ Model created successfully")
            print(f"   Response: {create_response.json()}")
        else:
            print(f"❌ Failed to create model: {create_response.status_code}")
            print(f"   Error: {create_response.text}")
            return
            
    except Exception as e:
        print(f"❌ Error creating model: {e}")
        return
    
    # Step 2: Train the model
    print("\n🚀 Step 2: Training model...")
    
    training_data = {
        "model_name": "api-test-classifier",
        "prompts": """The new iPhone features advanced AI capabilities and improved camera technology.

Tesla reports record quarterly earnings and stock price surge.

The Lakers won their game last night with a spectacular final quarter performance.

Microsoft announces new cloud computing services for enterprise customers.

The football match ended in a thrilling 3-2 victory for the home team.

Amazon's AWS division shows strong growth in cloud infrastructure services."""
    }
    
    try:
        print("⏳ Sending training request (this may take 1-2 minutes)...")
        
        start_time = time.time()
        train_response = requests.post(
            f"{base_url}/models/train",
            json=training_data,
            headers={"Content-Type": "application/json"},
            timeout=180  # 3 minutes timeout
        )
        end_time = time.time()
        
        training_time = end_time - start_time
        print(f"⏱️  Training completed in {training_time:.1f} seconds")
        
        if train_response.status_code == 200:
            result = train_response.json()
            print("🎉 Training successful!")
            print("=" * 30)
            print(f"✅ Status: {result.get('status', 'N/A')}")
            print(f"📊 Model: {result.get('model_name', 'N/A')}")
            print(f"🏷️  Version: {result.get('version', 'N/A')}")
            
            if 'metrics' in result:
                metrics = result['metrics']
                print("📈 Metrics:")
                print(f"   • Accuracy: {metrics.get('accuracy', 0):.1%}")
                print(f"   • Precision: {metrics.get('precision', 0):.1%}")
                print(f"   • F1 Score: {metrics.get('f1', 0):.1%}")
                print(f"   • Response Time: {metrics.get('avg_response_time', 0):.2f}s")
            
            if 'feedback' in result:
                feedback = result['feedback']
                print(f"\n🤖 AI Feedback:")
                print(f"   {feedback[:150]}...")
                
            if 'ollama_model' in result:
                print(f"\n🔧 Ollama Model: {result['ollama_model']}")
                print("   Test it with:")
                print(f"   ollama run {result['ollama_model']} 'Apple releases new MacBook Pro'")
        else:
            print(f"❌ Training failed: {train_response.status_code}")
            print(f"   Error: {train_response.text}")
            
    except requests.Timeout:
        print("⏰ Training request timed out (took longer than 3 minutes)")
    except Exception as e:
        print(f"❌ Error during training: {e}")
    
    # Step 3: Get model info
    print("\n📋 Step 3: Checking model info...")
    
    try:
        info_response = requests.get(f"{base_url}/models/api-test-classifier")
        
        if info_response.status_code == 200:
            model_info = info_response.json()
            print("✅ Model info retrieved")
            print(f"   Model data: {json.dumps(model_info, indent=2)}")
        else:
            print(f"❌ Failed to get model info: {info_response.status_code}")
            
    except Exception as e:
        print(f"❌ Error getting model info: {e}")


def main():
    """Main function"""
    print("🏭 AI Factory - API Training Test")
    print("🔧 Make sure the server is running: python cli.py serve")
    print()
    
    input("Press Enter to start the test (Ctrl+C to cancel)...")
    
    try:
        test_training_endpoint()
    except KeyboardInterrupt:
        print("\n👋 Test cancelled by user")
    except Exception as e:
        print(f"\n💥 Unexpected error: {e}")
    
    print("\n✅ Test completed!")


if __name__ == "__main__":
    main()