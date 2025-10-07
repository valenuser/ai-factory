#!/usr/bin/env python3
"""
🔧 AI Factory - Integration Fix Test
Test específico para el problema de integración create -> deploy
"""

import sys
import os
import asyncio
from pathlib import Path

# Add project root to Python path
PROJECT_ROOT = Path(__file__).parent
sys.path.insert(0, str(PROJECT_ROOT))

async def test_integration_fix():
    """Test de la corrección de integración"""
    print("🔧 AI FACTORY - INTEGRATION FIX TEST")
    print("=" * 50)
    
    try:
        from api.services.model_services import create_model_json, deploy_model_json
        from schemas.models_schemas import ModelCreateRequest
        
        test_model_name = "integration-fix-test"
        test_version = "1.0.fix"
        
        print(f"\n1️⃣ Creating model: {test_model_name}")
        
        # Create model
        request = ModelCreateRequest(
            model_name=test_model_name,
            base_prompt="Integration fix test model",
            version=test_version
        )
        
        create_result = await create_model_json(request)
        
        if create_result.get("status") == "success":
            print(f"✅ Model created successfully")
            print(f"   Message: {create_result.get('message')}")
        else:
            print(f"❌ Model creation failed: {create_result}")
            return
        
        print(f"\n2️⃣ Attempting deploy immediately after create (this was the failing case)")
        
        # Deploy immediately after create (this should work now)
        deploy_result = await deploy_model_json(test_model_name, test_version)
        
        if deploy_result.get("status") == "success":
            print(f"✅ Deploy successful!")
            print(f"   Deployment folder: {deploy_result.get('deployment_folder')}")
            print(f"   Files created: {deploy_result.get('files_created')}")
            
            # Verify deployment folder exists
            deploy_path = Path(deploy_result.get("deployment_folder"))
            if deploy_path.exists():
                file_count = len(list(deploy_path.iterdir()))
                print(f"   Verified: {file_count} files in deployment folder")
            
        elif deploy_result.get("status") == "error":
            print(f"❌ Deploy failed: {deploy_result.get('message')}")
            return
        else:
            print(f"⚠️ Deploy unknown status: {deploy_result}")
        
        print(f"\n3️⃣ Testing with non-existent version (should handle gracefully)")
        
        deploy_result2 = await deploy_model_json(test_model_name, "999.999.999")
        
        if deploy_result2.get("status") == "success":
            print(f"✅ Fallback deploy worked for non-existent version")
        elif "not found" in deploy_result2.get("message", "").lower():
            print(f"✅ Properly handles non-existent version: {deploy_result2.get('message')}")
        else:
            print(f"⚠️ Unexpected result: {deploy_result2}")
        
        print(f"\n🎯 INTEGRATION FIX COMPLETE")
        print("=" * 50)
        
    except Exception as e:
        print(f"❌ Error in integration fix test: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    import sys, os
    ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
    if ROOT not in sys.path:
        sys.path.insert(0, ROOT)
    import asyncio
    asyncio.run(test_integration_fix())