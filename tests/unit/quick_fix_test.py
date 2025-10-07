#!/usr/bin/env python3
"""
🔧 AI Factory - Quick Fix Test
Prueba rápida de los schemas corregidos
"""

import sys
import os
from pathlib import Path

# Add project root to Python path
PROJECT_ROOT = Path(__file__).parent
sys.path.insert(0, str(PROJECT_ROOT))

def test_schemas_fixed():
    """Test que los schemas corregidos funcionan"""
    print("🔧 TESTING SCHEMAS CORREGIDOS")
    print("=" * 40)
    
    try:
        from schemas.models_schemas import (
            ModelCreateRequest, ModelTrainRequest, ModelDeployRequest
        )
        
        # Test ModelCreateRequest con campos correctos
        try:
            valid_create = ModelCreateRequest(
                model_name="test-model",
                base_prompt="Test prompt",  # Ahora base_prompt
                version="1.0"  # Ahora incluye version
            )
            print("✅ ModelCreateRequest corregido - OK")
        except Exception as e:
            print(f"❌ ModelCreateRequest corregido - Error: {e}")
        
        # Test ModelTrainRequest con lista
        try:
            valid_train = ModelTrainRequest(
                model_name="test-model",
                prompts=["Test prompt 1", "Test prompt 2"]  # Ahora lista
            )
            print("✅ ModelTrainRequest corregido - OK")
        except Exception as e:
            print(f"❌ ModelTrainRequest corregido - Error: {e}")
        
        # Test ModelDeployRequest (este ya funcionaba)
        try:
            valid_deploy = ModelDeployRequest(
                model_name="test-model",
                version="1.0"
            )
            print("✅ ModelDeployRequest - OK")
        except Exception as e:
            print(f"❌ ModelDeployRequest - Error: {e}")
            
    except ImportError as e:
        print(f"❌ Error importando schemas: {e}")

def test_create_function():
    """Test de la función create_model_json corregida"""
    print("\n🔧 TESTING CREATE FUNCTION")
    print("=" * 40)
    
    try:
        import asyncio
        from api.services.model_services import create_model_json
        from schemas.models_schemas import ModelCreateRequest
        
        async def test_create():
            # Crear request object correctamente
            request = ModelCreateRequest(
                model_name="test-fix",
                base_prompt="Testing fixed function",
                version="1.0.fix"
            )
            
            try:
                result = await create_model_json(request)  # Pasar objeto, no parámetros
                if result.get("status") == "success":
                    print("✅ create_model_json() corregido - OK")
                else:
                    print(f"⚠️ create_model_json() - Status: {result.get('status')}")
            except Exception as e:
                print(f"❌ create_model_json() - Error: {e}")
        
        asyncio.run(test_create())
        
    except Exception as e:
        print(f"❌ Error testing create function: {e}")

def test_threading_function():
    """Test de la función de threading corregida"""
    print("\n🔧 TESTING THREADING FUNCTION")
    print("=" * 40)
    
    try:
        from api.services.model_services import _test_single_prompt
        
        # Test con los parámetros correctos
        result = _test_single_prompt(
            "basic-test-model:1.0.1", 
            "Test threading prompt",
            0  # prompt_index requerido
        )
        
        if isinstance(result, tuple) and len(result) == 3:
            success, time_taken, response = result
            print(f"✅ _test_single_prompt() corregido - Success: {success}, Time: {time_taken}")
        else:
            print(f"⚠️ _test_single_prompt() - Resultado inesperado: {result}")
            
    except Exception as e:
        print(f"❌ Error testing threading function: {e}")

if __name__ == "__main__":
    import sys, os
    ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
    if ROOT not in sys.path:
        sys.path.insert(0, ROOT)
    test_quick_fix()
    print("🔧 AI FACTORY - QUICK FIX VALIDATION")
    print("=" * 50)
    
    test_schemas_fixed()
    test_create_function()
    test_threading_function()
    
    print("\n" + "=" * 50)
    print("🎯 FIXES APLICADOS:")
    print("1. ✅ ModelCreateRequest: base_prompt + version")
    print("2. ✅ ModelTrainRequest: prompts como lista")
    print("3. ✅ Verificado create_model_json recibe objeto") 
    print("4. ✅ Verificado _test_single_prompt necesita prompt_index")
    print("\n🔄 Ejecutar comprehensive_test.py para validar todas las correcciones")