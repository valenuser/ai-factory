#!/usr/bin/env python3
"""
AI Factory - Model Training Example

This example demonstrates how to use the train_model_json function
to train a model with prompts and generate metrics.
"""

import sys
from pathlib import Path
import asyncio
import json

# Add parent directory to path to import modules
sys.path.append(str(Path(__file__).parent.parent))

from config import config
from api.services.model_services import create_model_json, train_model_json
from schemas.models_schemas import ModelCreateRequest


async def example_model_training():
    """Complete example of creating and training a model"""
    
    print("🏭 AI Factory - Model Training Example")
    print("=" * 50)
    
    # Step 1: Create a base model first
    print("📝 Step 1: Creating base model...")
    
    model_request = ModelCreateRequest(
        model_name="sentiment-analyzer",
        model_prompt="You are a sentiment analysis expert. Classify text as POSITIVE, NEGATIVE, or NEUTRAL. Provide brief reasoning."
    )
    
    create_result = await create_model_json(model_request)
    print(f"✅ Model created: {create_result}")
    print()
    
    # Step 2: Prepare training prompts
    training_prompts = """
    This movie was absolutely amazing! I loved every minute of it.
    
    The service at this restaurant was terrible and the food was cold.
    
    It's an okay product, nothing special but does what it's supposed to do.
    
    Best purchase I've ever made! Highly recommend to everyone.
    
    Meh, could be better, could be worse. Average experience overall.
    
    Worst customer service experience in my life. Never going back.
    
    The weather today is nice, perfect for a walk in the park.
    """
    
    print("📝 Step 2: Training prompts prepared:")
    prompt_lines = [p.strip() for p in training_prompts.split('\n') if p.strip()]
    for i, prompt in enumerate(prompt_lines, 1):
        print(f"   {i}. {prompt[:50]}...")
    print()
    
    # Step 3: Train the model
    print("🚀 Step 3: Training model (this may take a while)...")
    print("⏳ Creating Modelfile, building in Ollama, testing prompts...")
    
    try:
        training_result = await train_model_json(
            model_name="sentiment-analyzer",
            prompts=training_prompts
        )
        
        print("🎉 Training completed!")
        print("=" * 30)
        
        if training_result["status"] == "success":
            print(f"✅ Status: {training_result['status']}")
            print(f"📊 Model: {training_result['model_name']}")
            print(f"🏷️  Version: {training_result['version']}")
            print(f"🎯 Test Results: {training_result['test_results_summary']}")
            print()
            print("📈 Metrics:")
            metrics = training_result['metrics']
            print(f"   • Accuracy: {metrics['accuracy']:.1%}")
            print(f"   • Precision: {metrics['precision']:.1%}")
            print(f"   • Recall: {metrics['recall']:.1%}")
            print(f"   • F1 Score: {metrics['f1']:.1%}")
            print(f"   • Avg Response Time: {metrics['avg_response_time']:.2f}s")
            print()
            print("🤖 AI Feedback:")
            print(f"   {training_result['feedback'][:200]}...")
            print()
            print(f"🔧 Ollama Model Created: {training_result['ollama_model']}")
            print("   You can now test it with:")
            print(f"   ollama run {training_result['ollama_model']} 'I love this product!'")
            
        else:
            print(f"❌ Training failed: {training_result.get('message', 'Unknown error')}")
            
    except Exception as e:
        print(f"💥 Error during training: {str(e)}")
    
    print()
    print("📁 Check the models_data.json file to see the complete training results!")


async def show_training_data():
    """Show the training data structure"""
    print("\n📊 Training Data Structure Example")
    print("=" * 40)
    
    try:
        models_file = config.get_models_data_path()
        with open(models_file, 'r', encoding='utf-8') as file:
            models_data = json.load(file)
        
        for model_name, model_info in models_data.items():
            print(f"🤖 Model: {model_name}")
            
            if "version" in model_info and model_info["version"]:
                print("📋 Training Versions:")
                for version_entry in model_info["version"]:
                    for version_num, version_data in version_entry.items():
                        print(f"   🏷️  Version {version_num}:")
                        print(f"      Status: {version_data.get('status', 'N/A')}")
                        print(f"      Accuracy: {version_data.get('metrics', {}).get('accuracy', 'N/A')}")
                        print(f"      Created: {version_data.get('created_at', 'N/A')}")
                        print()
            else:
                print("   No training data available")
            print("-" * 30)
            
    except FileNotFoundError:
        print("❌ No models_data.json found. Run training first.")
    except Exception as e:
        print(f"❌ Error reading training data: {e}")


async def main():
    """Main function with menu options"""
    print("🏭 AI Factory - Model Training System")
    print("=" * 50)
    print("1. Run complete training example")
    print("2. Show existing training data")
    print("3. Exit")
    
    while True:
        try:
            choice = input("\nSelect option (1-3): ").strip()
            
            if choice == "1":
                await example_model_training()
                break
            elif choice == "2":
                await show_training_data()
                break
            elif choice == "3":
                print("👋 Goodbye!")
                break
            else:
                print("❌ Invalid option. Please choose 1, 2, or 3.")
                
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")


if __name__ == "__main__":
    asyncio.run(main())