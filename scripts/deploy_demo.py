#!/usr/bin/env python3
"""
🚀 AI Factory Deploy Demo
Demonstrates the complete deploy functionality
"""

import asyncio
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from api.services.model_services import deploy_model_json

async def main():
    """Demo of the deploy functionality"""
    
    print("🏭 AI Factory - Deploy Demo")
    print("=" * 60)
    print()
    
    # Deploy basic-test-model version 1.0.1
    print("📦 Deploying basic-test-model v1.0.1...")
    result = await deploy_model_json("basic-test-model", "1.0.1")
    
    if result["status"] == "success":
        print(f"✅ {result['message']}")
        print(f"📁 Deployment folder: {result['deployment_folder']}")
        print(f"📋 Files created: {', '.join(result['files_created'])}")
        print()
        print("🚀 Instructions to run your deployed model:")
        print(result['instructions'])
    else:
        print(f"❌ Deploy failed: {result['message']}")
    
    print()
    print("=" * 60)
    print("🎉 Deploy Demo Complete!")
    print()
    print("📖 Available endpoints in AI Factory:")
    print("   • GET  /models/          - List all models")
    print("   • POST /models/create    - Create a new model")
    print("   • POST /models/train     - Train a model (with threading)")
    print("   • POST /models/deploy    - Deploy model as standalone package")
    print("   • GET  /models/{name}    - Get specific model details")
    print("   • POST /models/add_prompt - Add training prompts")
    print()
    print("🌐 API Documentation: http://localhost:8000/docs")

if __name__ == "__main__":
    asyncio.run(main())