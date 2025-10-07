#!/usr/bin/env python3
"""
Test Final de Integración - AI Factory
Verifica que todo el sistema funcione correctamente después de la reorganización.
"""

import requests
import json
import time
import sys
from pathlib import Path

# Agregar el directorio raíz al path
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

def test_server_connectivity():
    """Test de conectividad del servidor"""
    print("🔗 Probando conectividad del servidor...")
    try:
        response = requests.get("http://localhost:8001/health", timeout=5)
        if response.status_code == 200:
            print("✅ Servidor respondiendo correctamente")
            return True
        else:
            print(f"❌ Servidor responde con código {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Error de conectividad: {e}")
        return False

def test_model_endpoints():
    """Test de endpoints de modelos"""
    print("\n🤖 Probando endpoints de modelos...")
    
    # Test GET /models/
    try:
        response = requests.get("http://localhost:8001/models/", timeout=10)
        if response.status_code == 200:
            print("✅ GET /models/ funcionando")
        else:
            print(f"❌ GET /models/ falló con código {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Error en GET /models/: {e}")
        return False
    
    return True

def test_deployment_endpoints():
    """Test de endpoints de deployment"""
    print("\n📦 Probando endpoints de deployment...")
    
    # Test GET /models/deployments/list
    try:
        response = requests.get("http://localhost:8001/models/deployments/list", timeout=10)
        if response.status_code == 200:
            print("✅ GET /models/deployments/list funcionando")
            data = response.json()
            print(f"   📁 Deployments disponibles: {len(data.get('deployments', []))}")
        else:
            print(f"❌ GET /models/deployments/list falló con código {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Error en GET /models/deployments/list: {e}")
        return False
    
    return True

def test_model_creation():
    """Test de creación de modelo simple"""
    print("\n🔨 Probando creación de modelo...")
    
    test_model = {
        "model_name": "test_integration_model",
        "base_model": "llama3.2:1b",
        "system_prompt": "Eres un asistente de prueba para verificación de integración.",
        "temperature": 0.7,
        "max_tokens": 100,
        "training_data": [
            {"input": "¿Qué es integración?", "output": "Integración es el proceso de combinar componentes."},
            {"input": "¿Funciona el sistema?", "output": "Sí, el sistema está funcionando correctamente."}
        ]
    }
    
    try:
        response = requests.post(
            "http://localhost:8001/models/create",
            json=test_model,
            timeout=30
        )
        
        if response.status_code == 200:
            print("✅ Creación de modelo iniciada correctamente")
            result = response.json()
            print(f"   📋 Estado: {result.get('status', 'unknown')}")
            return True
        else:
            print(f"❌ Creación de modelo falló con código {response.status_code}")
            if response.text:
                print(f"   📝 Error: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Error en creación de modelo: {e}")
        return False

def main():
    """Ejecuta todos los tests de integración"""
    print("🚀 INICIANDO TEST FINAL DE INTEGRACIÓN")
    print("=" * 50)
    
    tests_passed = 0
    total_tests = 4
    
    # Test 1: Conectividad
    if test_server_connectivity():
        tests_passed += 1
    
    # Test 2: Endpoints de modelos
    if test_model_endpoints():
        tests_passed += 1
    
    # Test 3: Endpoints de deployment
    if test_deployment_endpoints():
        tests_passed += 1
    
    # Test 4: Creación de modelo
    if test_model_creation():
        tests_passed += 1
    
    # Resultado final
    print("\n" + "=" * 50)
    print(f"🎯 RESULTADO FINAL: {tests_passed}/{total_tests} tests pasados")
    
    if tests_passed == total_tests:
        print("🎉 ¡TODOS LOS TESTS PASARON! Sistema completamente funcional")
        return 0
    else:
        print(f"⚠️  {total_tests - tests_passed} tests fallaron. Revisar configuración.")
        return 1

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)