#!/usr/bin/env python3
"""
Simple test to verify the training function logic
"""

import sys
import os
from pathlib import Path
import asyncio

# Add root directory to path
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from config import config


async def test_basic_functionality():
    """Test basic functionality without Ollama dependency"""
    
    print("🧪 AI Factory - Basic Function Test")
    print("=" * 40)
    
    # Test 1: Configuration
    print("1. Testing configuration...")
    try:
        models_path = config.get_models_data_path()
        print(f"   ✅ Models data path: {models_path}")
        
        config.ensure_directories()
        print("   ✅ Directories created")
        
        # Test Modelfile generation
        modelfile_content = config.generate_modelfile(
            model_name="test-model",
            prompt="You are a test assistant",
            version="1.0.0"
        )
        print("   ✅ Modelfile generation works")
        print(f"   📄 Modelfile preview: {modelfile_content[:100]}...")
        
    except Exception as e:
        print(f"   ❌ Configuration test failed: {e}")
        return False
    
    # Test 2: Import model services
    print("\n2. Testing model services import...")
    try:
        from api.services.model_services import create_model_json, train_model_json
        print("   ✅ Model services imported successfully")
        
    except Exception as e:
        print(f"   ❌ Import failed: {e}")
        return False
    
    # Test 3: Schema validation
    print("\n3. Testing schema validation...")
    try:
        from schemas.models_schemas import ModelCreateRequest, ModelTrainRequest
        
        # Test ModelCreateRequest
        create_req = ModelCreateRequest(
            model_name="test-model",
            base_prompt="Test prompt",
            version="1.0.0"
        )
        print(f"   ✅ ModelCreateRequest: {create_req.model_name}")
        
        # Test ModelTrainRequest  
        train_req = ModelTrainRequest(
            model_name="test-model",
            prompts=["Test prompt 1", "Test prompt 2"]
        )
        print(f"   ✅ ModelTrainRequest: {train_req.model_name}")
        
    except Exception as e:
        print(f"   ❌ Schema test failed: {e}")
        return False
    
    # Test 4: Basic model creation (without Ollama)
    print("\n4. Testing model creation logic...")
    try:
        test_model = ModelCreateRequest(
            model_name="basic-test-model", 
            base_prompt="You are a helpful assistant for testing purposes.",
            version="1.0.0"
        )
        
        result = await create_model_json(test_model)
        print(f"   ✅ Model creation result: {result}")
        
    except Exception as e:
        print(f"   ❌ Model creation test failed: {e}")
        return False
    
    print("\n🎉 All basic tests passed!")
    print("\n📋 Notes:")
    print("   • Configuration works correctly")
    print("   • All imports are successful") 
    print("   • Schema validation works")
    print("   • Model creation logic works")
    print("   • To test full training, you need Ollama installed")
    print("\n⚠️  For full training test, ensure Ollama is installed and run:")
    print("   python examples/training_example.py")
    
    return True


async def show_project_status():
    """Show current project status"""
    print("\n📊 Project Status")
    print("=" * 20)
    
    # Check files exist
    files_to_check = [
        "config.py",
        "api/services/model_services.py", 
        "api/router/models.py",
        "schemas/models_schemas.py",
        "templates/Modelfile.template"
    ]
    
    for file_path in files_to_check:
        if Path(file_path).exists():
            print(f"   ✅ {file_path}")
        else:
            print(f"   ❌ {file_path} - Missing!")
    
    # Check directories
    dirs_to_check = ["data", "models", "exports", "templates", "examples"]
    
    print("\n📁 Directories:")
    for dir_path in dirs_to_check:
        if Path(dir_path).exists():
            print(f"   ✅ {dir_path}/")
        else:
            print(f"   ⚠️  {dir_path}/ - Will be created as needed")


async def main():
    """Main function"""
    await test_basic_functionality()
    await show_project_status()


if __name__ == "__main__":
    import sys, os
    ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
    if ROOT not in sys.path:
        sys.path.insert(0, ROOT)
    asyncio.run(main())