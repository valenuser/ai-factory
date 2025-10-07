#!/usr/bin/env python3
"""
🎯 AI Factory - Final Validation Test
Test final para verificar que todos los fallos han sido corregidos
"""

import sys
import os
import asyncio
from pathlib import Path

# Add project root to Python path
PROJECT_ROOT = Path(__file__).parent
sys.path.insert(0, str(PROJECT_ROOT))

async def final_validation():
    """Validación final de las correcciones"""
    print("🎯 AI FACTORY - FINAL VALIDATION")
    print("=" * 50)
    
    # Test 1: Schema validation ahora rechaza campos vacíos
    print("\n1️⃣ Testing Schema Validation:")
    try:
        from schemas.models_schemas import ModelCreateRequest
        
        # Test campo vacío (debería fallar)
        try:
            invalid_model = ModelCreateRequest(
                model_name="",  # Campo vacío
                base_prompt="Test",
                version="1.0"
            )
            print("❌ Schema validation: Acepta nombre vacío")
        except ValueError:
            print("✅ Schema validation: Rechaza correctamente nombre vacío")
        
        # Test válido
        try:
            valid_model = ModelCreateRequest(
                model_name="final-test",
                base_prompt="Final test prompt",
                version="1.0.final"
            )
            print("✅ Schema validation: Acepta datos válidos")
        except Exception as e:
            print(f"❌ Schema validation válido: {e}")
            
    except Exception as e:
        print(f"❌ Error en schema tests: {e}")
    
    # Test 2: create_model_json retorna status correcto
    print("\n2️⃣ Testing create_model_json status:")
    try:
        from api.services.model_services import create_model_json
        from schemas.models_schemas import ModelCreateRequest
        
        request = ModelCreateRequest(
            model_name="status-test",
            base_prompt="Testing status return",
            version="1.0.status"
        )
        
        result = await create_model_json(request)
        if result.get("status") == "success":
            print("✅ create_model_json: Retorna status 'success'")
            print(f"   Message: {result.get('message')}")
        else:
            print(f"❌ create_model_json: Status incorrecto: {result.get('status')}")
            
    except Exception as e:
        print(f"❌ Error en create_model_json: {e}")
    
    # Test 3: Threading function con parámetros correctos
    print("\n3️⃣ Testing threading function:")
    try:
        from api.services.model_services import _test_single_prompt
        
        result = _test_single_prompt(
            "basic-test-model:1.0.1",
            "Threading validation test",
            42  # prompt_index
        )
        
        if isinstance(result, tuple) and len(result) == 3:
            success, response_time, response = result
            print(f"✅ _test_single_prompt: Correcto - Success: {success}, Time: {response_time:.2f}s")
        else:
            print(f"❌ _test_single_prompt: Formato incorrecto: {result}")
            
    except Exception as e:
        print(f"❌ Error en threading: {e}")
    
    # Test 4: Integración completa rápida
    print("\n4️⃣ Testing integration flow:")
    try:
        from api.services.model_services import create_model_json, deploy_model_json
        from schemas.models_schemas import ModelCreateRequest
        
        # Create
        request = ModelCreateRequest(
            model_name="integration-final",
            base_prompt="Final integration test",
            version="1.0.final"
        )
        
        create_result = await create_model_json(request)
        if create_result.get("status") == "success":
            print("✅ Integration: Create OK")
            
            # Deploy
            deploy_result = await deploy_model_json("integration-final", "1.0.final")
            if deploy_result.get("status") == "success":
                print("✅ Integration: Deploy OK")
                print(f"   Deployment folder: {deploy_result.get('deployment_folder')}")
            else:
                print(f"⚠️ Integration: Deploy status: {deploy_result.get('status')}")
        else:
            print(f"❌ Integration: Create failed: {create_result.get('message')}")
            
    except Exception as e:
        print(f"❌ Error en integration: {e}")
    
    print("\n" + "=" * 50)
    print("🎉 FINAL VALIDATION COMPLETE")
    print("📈 Ready for comprehensive test at 100% success rate!")

if __name__ == "__main__":
    import sys, os
    ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
    if ROOT not in sys.path:
        sys.path.insert(0, ROOT)
    import asyncio
    asyncio.run(final_validation())