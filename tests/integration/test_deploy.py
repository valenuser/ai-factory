#!/usr/bin/env python3
"""
Test script for the deploy functionality
"""
import sys
import os
import asyncio
import json

# Add the project directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from api.services.model_services import deploy_model_json

async def test_deploy():
    """Test the deploy functionality"""
    print("🧪 Testing Deploy Function...")
    print("=" * 50)
    
    # Test 1: Deploy existing model
    print("\n📦 Test 1: Deploying assistant-test v1.0")
    result1 = await deploy_model_json("assistant-test", "v1.0")
    print(f"Status: {result1['status']}")
    print(f"Message: {result1['message']}")
    print(f"Deployment Folder: {result1['deployment_folder']}")
    print(f"Files Created: {result1['files_created']}")
    
    if result1['status'] == 'success':
        print("\n✅ Deployment successful!")
        print(f"📁 Check folder: {result1['deployment_folder']}")
        print("\n📋 Instructions:")
        print(result1['instructions'])
    else:
        print(f"\n❌ Deployment failed: {result1['message']}")
    
    print("\n" + "=" * 50)
    
    # Test 2: Deploy another model
    print("\n📦 Test 2: Deploying chatbot-demo v2.1")
    result2 = await deploy_model_json("chatbot-demo", "v2.1")
    print(f"Status: {result2['status']}")
    print(f"Message: {result2['message']}")
    print(f"Deployment Folder: {result2['deployment_folder']}")
    print(f"Files Created: {result2['files_created']}")
    
    print("\n" + "=" * 50)
    
    # Test 3: Try to deploy non-existent model
    print("\n📦 Test 3: Deploying non-existent model")
    result3 = await deploy_model_json("non-existent", "v1.0")
    print(f"Status: {result3['status']}")
    print(f"Message: {result3['message']}")

if __name__ == "__main__":
    asyncio.run(test_deploy())