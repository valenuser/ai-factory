#!/usr/bin/env python3
"""
Demostración del Sistema de Descarga de Deployments
==================================================

Este script demuestra el nuevo flujo completo:
1. Crear un modelo
2. Hacer deploy (genera ZIP automáticamente)
3. Listar deployments disponibles
4. Descargar el ZIP del modelo
"""

import requests
import json
import time

def demo_complete_flow():
    base_url = "http://localhost:8000"
    
    print("🚀 AI Factory - Sistema de Descarga de Deployments")
    print("=" * 60)
    print()
    
    # Modelo de ejemplo
    model_name = f"demo-model-{int(time.time())}"
    version = "1.0.0"
    
    print(f"📋 Creando modelo de demostración: {model_name}")
    
    # 1. Crear modelo
    create_data = {
        "model_name": model_name,
        "base_prompt": "You are a helpful AI assistant for demonstration purposes.",
        "version": version
    }
    
    try:
        response = requests.post(f"{base_url}/models/create", json=create_data)
        if response.status_code == 200:
            print("✅ Modelo creado exitosamente")
        else:
            print("⚠️ Modelo puede que ya exista, continuando...")
    except Exception as e:
        print(f"⚠️ Error creando modelo: {e}")
    
    # 2. Hacer deploy
    print(f"\n📦 Haciendo deploy del modelo (generando ZIP)...")
    deploy_data = {
        "model_name": model_name,
        "version": version
    }
    
    try:
        response = requests.post(f"{base_url}/models/deploy", json=deploy_data)
        if response.status_code == 200:
            deploy_result = response.json()
            print("✅ Deploy completado!")
            print(f"   📁 Carpeta: {deploy_result.get('deployment_folder')}")
            print(f"   📦 ZIP: {deploy_result.get('zip_filename')}")
            print(f"   📄 Archivos: {', '.join(deploy_result.get('files_created', []))}")
            
            zip_filename = deploy_result.get('zip_filename')
        else:
            print(f"❌ Error en deploy: {response.status_code}")
            return
    except Exception as e:
        print(f"❌ Error en deploy: {e}")
        return
    
    # 3. Listar deployments disponibles
    print(f"\n📋 Listando deployments disponibles...")
    try:
        response = requests.get(f"{base_url}/models/deployments/list")
        if response.status_code == 200:
            list_result = response.json()
            deployments = list_result.get('deployments', [])
            print(f"✅ {len(deployments)} deployments encontrados:")
            
            for i, deployment in enumerate(deployments, 1):
                print(f"   {i}. {deployment.get('model_name')} v{deployment.get('version')}")
                print(f"      📄 Archivo: {deployment.get('filename')}")
                print(f"      💾 Tamaño: {deployment.get('size_mb')} MB")
        else:
            print(f"❌ Error listando deployments: {response.status_code}")
            return
    except Exception as e:
        print(f"❌ Error listando deployments: {e}")
        return
    
    # 4. Descargar ZIP
    print(f"\n⬇️ Descargando ZIP del modelo...")
    try:
        download_url = f"{base_url}/models/deployments/download/{zip_filename}"
        response = requests.get(download_url)
        
        if response.status_code == 200:
            # Guardar archivo
            local_filename = f"downloaded_{zip_filename}"
            with open(local_filename, 'wb') as f:
                f.write(response.content)
            
            print("✅ Descarga completada!")
            print(f"   📁 Guardado como: {local_filename}")
            print(f"   💾 Tamaño: {len(response.content)} bytes")
            print(f"   🔗 URL de descarga: {download_url}")
            
            # Verificar ZIP
            import zipfile
            if zipfile.is_zipfile(local_filename):
                with zipfile.ZipFile(local_filename, 'r') as zf:
                    files = zf.namelist()
                    print(f"   📄 Archivos en ZIP: {', '.join(files)}")
            
        else:
            print(f"❌ Error descargando: {response.status_code}")
            return
            
    except Exception as e:
        print(f"❌ Error en descarga: {e}")
        return
    
    # 5. Mostrar instrucciones finales
    print(f"\n🎯 ¡Deployment listo para usar!")
    print(f"   1. Descomprimir: {local_filename}")
    print(f"   2. Instalar dependencias: pip install -r requirements.txt")
    print(f"   3. Crear modelo Ollama: ollama create {model_name}:{version} -f Modelfile")
    print(f"   4. Ejecutar API: python main.py")
    print(f"   5. Visitar: http://localhost:8080/docs")
    
    print(f"\n📚 Documentación completa en README.md dentro del ZIP")
    
    # Cleanup
    try:
        import os
        os.remove(local_filename)
        print(f"\n🧹 Archivo de demo eliminado: {local_filename}")
    except:
        pass

if __name__ == "__main__":
    # Verificar que la API esté disponible
    try:
        response = requests.get("http://localhost:8000/health")
        if response.status_code != 200:
            print("❌ La API no está disponible. Inicia el servidor primero:")
            print("   python -m uvicorn api.main:app --reload --port 8000")
            exit(1)
    except:
        print("❌ No se puede conectar a la API. Inicia el servidor primero:")
        print("   python -m uvicorn api.main:app --reload --port 8000")
        exit(1)
    
    demo_complete_flow()