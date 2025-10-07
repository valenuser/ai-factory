#!/usr/bin/env python3
"""
Test de Sistema de Descarga de Deployments
===========================================

Prueba completa del sistema de descarga de paquetes de deployment.
Incluye creación, deploy, listado y descarga de archivos ZIP.
"""

import asyncio
import requests
import json
import os
import zipfile
from pathlib import Path
import time

BASE_URL = "http://localhost:8000"

class DeploymentDownloadTester:
    def __init__(self):
        self.test_model_name = f"download-test-model-{int(time.time())}"
        self.test_version = "1.0.0"
        self.zip_filename = None
        
    async def test_complete_flow(self):
        """Test completo del flujo de descarga"""
        print("🧪 Testing Deployment Download System")
        print("=" * 50)
        
        # 1. Crear modelo de prueba
        await self.test_create_model()
        
        # 2. Hacer deploy del modelo (generar ZIP)
        await self.test_deploy_model()
        
        # 3. Listar deployments disponibles
        await self.test_list_deployments()
        
        # 4. Descargar el archivo ZIP
        await self.test_download_zip()
        
        # 5. Verificar contenido del ZIP
        await self.test_verify_zip_content()
        
        # 6. Cleanup
        await self.cleanup()
        
        print("\n✅ All deployment download tests passed!")
        
    async def test_create_model(self):
        """Crear modelo de prueba"""
        print("\n1️⃣ Creating test model...")
        
        create_data = {
            "model_name": self.test_model_name,
            "base_prompt": "You are a helpful AI assistant specialized in testing deployment downloads.",
            "version": self.test_version
        }
        
        try:
            response = requests.post(f"{BASE_URL}/models/create", json=create_data)
            response.raise_for_status()
            
            result = response.json()
            if result.get("status") == "success":
                print(f"   ✅ Model created: {self.test_model_name}")
            else:
                print(f"   ❌ Failed to create model: {result.get('message')}")
                return False
                
        except requests.exceptions.RequestException as e:
            print(f"   ❌ Request failed: {e}")
            return False
            
        return True
        
    async def test_deploy_model(self):
        """Deploy modelo y generar ZIP"""
        print("\n2️⃣ Deploying model (generating ZIP)...")
        
        deploy_data = {
            "model_name": self.test_model_name,
            "version": self.test_version
        }
        
        try:
            response = requests.post(f"{BASE_URL}/models/deploy", json=deploy_data)
            response.raise_for_status()
            
            result = response.json()
            if result.get("status") == "success":
                self.zip_filename = result.get("zip_filename")
                print(f"   ✅ Deployment created")
                print(f"   📁 Folder: {result.get('deployment_folder')}")
                print(f"   📦 ZIP: {self.zip_filename}")
                print(f"   📄 Files: {len(result.get('files_created', []))} files created")
                return True
            else:
                print(f"   ❌ Deployment failed: {result.get('message')}")
                return False
                
        except requests.exceptions.RequestException as e:
            print(f"   ❌ Request failed: {e}")
            return False
            
    async def test_list_deployments(self):
        """Listar deployments disponibles"""
        print("\n3️⃣ Listing available deployments...")
        
        try:
            response = requests.get(f"{BASE_URL}/models/deployments/list")
            response.raise_for_status()
            
            result = response.json()
            if result.get("status") == "success":
                deployments = result.get("deployments", [])
                print(f"   ✅ Found {len(deployments)} deployments")
                
                # Buscar nuestro deployment
                our_deployment = None
                for deployment in deployments:
                    if deployment.get("model_name") == self.test_model_name:
                        our_deployment = deployment
                        break
                
                if our_deployment:
                    print(f"   📦 Our deployment found:")
                    print(f"      - Filename: {our_deployment['filename']}")
                    print(f"      - Size: {our_deployment['size_mb']} MB")
                    print(f"      - Version: {our_deployment['version']}")
                    return True
                else:
                    print(f"   ❌ Our deployment not found in list")
                    return False
                    
            else:
                print(f"   ❌ Failed to list deployments: {result.get('message')}")
                return False
                
        except requests.exceptions.RequestException as e:
            print(f"   ❌ Request failed: {e}")
            return False
            
    async def test_download_zip(self):
        """Descargar archivo ZIP"""
        print("\n4️⃣ Downloading ZIP file...")
        
        if not self.zip_filename:
            print("   ❌ No ZIP filename available")
            return False
            
        try:
            response = requests.get(f"{BASE_URL}/models/deployments/download/{self.zip_filename}")
            response.raise_for_status()
            
            # Guardar el archivo descargado
            download_path = Path(f"./test_downloads/{self.zip_filename}")
            download_path.parent.mkdir(exist_ok=True)
            
            with open(download_path, 'wb') as f:
                f.write(response.content)
            
            file_size = os.path.getsize(download_path)
            print(f"   ✅ ZIP downloaded successfully")
            print(f"   📁 Saved to: {download_path}")
            print(f"   📊 Size: {file_size / 1024:.1f} KB")
            
            # Verificar que es un ZIP válido
            if zipfile.is_zipfile(download_path):
                print(f"   ✅ File is a valid ZIP archive")
                return True
            else:
                print(f"   ❌ Downloaded file is not a valid ZIP")
                return False
                
        except requests.exceptions.RequestException as e:
            print(f"   ❌ Download failed: {e}")
            return False
            
    async def test_verify_zip_content(self):
        """Verificar contenido del ZIP"""
        print("\n5️⃣ Verifying ZIP content...")
        
        zip_path = Path(f"./test_downloads/{self.zip_filename}")
        if not zip_path.exists():
            print("   ❌ ZIP file not found")
            return False
            
        try:
            with zipfile.ZipFile(zip_path, 'r') as zipf:
                files_in_zip = zipf.namelist()
                expected_files = ["main.py", "Modelfile", "requirements.txt", "README.md", "docker-compose.yml"]
                
                print(f"   📄 Files in ZIP: {len(files_in_zip)}")
                for file in files_in_zip:
                    print(f"      - {file}")
                
                # Verificar archivos esperados
                missing_files = [f for f in expected_files if f not in files_in_zip]
                if missing_files:
                    print(f"   ❌ Missing files: {missing_files}")
                    return False
                
                # Verificar que main.py contiene nuestro modelo
                main_py_content = zipf.read("main.py").decode('utf-8')
                if self.test_model_name in main_py_content:
                    print(f"   ✅ main.py contains correct model name")
                else:
                    print(f"   ❌ main.py does not contain model name")
                    return False
                
                print(f"   ✅ ZIP content verification passed")
                return True
                
        except Exception as e:
            print(f"   ❌ ZIP verification failed: {e}")
            return False
            
    async def cleanup(self):
        """Limpiar archivos de prueba"""
        print("\n6️⃣ Cleaning up...")
        
        try:
            # Eliminar modelo de prueba
            response = requests.delete(f"{BASE_URL}/models/{self.test_model_name}")
            if response.status_code == 200:
                print("   ✅ Test model deleted")
            
            # Eliminar archivos de descarga
            download_dir = Path("./test_downloads")
            if download_dir.exists():
                import shutil
                shutil.rmtree(download_dir)
                print("   ✅ Test downloads cleaned")
                
        except Exception as e:
            print(f"   ⚠️ Cleanup warning: {e}")

async def main():
    """Función principal"""
    print("🚀 Starting Deployment Download Test Suite")
    print(f"🌐 Testing against: {BASE_URL}")
    
    # Verificar que la API esté funcionando
    try:
        response = requests.get(f"{BASE_URL}/health")
        if response.status_code != 200:
            print("❌ API not available. Please start the server first.")
            return
    except:
        print("❌ Cannot connect to API. Please start the server first.")
        return
    
    # Ejecutar tests
    tester = DeploymentDownloadTester()
    await tester.test_complete_flow()

if __name__ == "__main__":
    import sys, os
    ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
    if ROOT not in sys.path:
        sys.path.insert(0, ROOT)
    asyncio.run(main())