#!/usr/bin/env python3
"""
Test script para probar el nuevo sistema de threading en train_model_json
"""
import asyncio
import time
from api.services.model_services import train_model_json

async def test_training_with_threading():
    """Test the threaded training system"""
    print("🚀 Testing threaded training system...")
    
    # Preparar datos de prueba con múltiples prompts
    model_name = "basic-test-model"
    test_prompts = "Explica qué es Python, ¿Qué es machine learning?, Define inteligencia artificial, ¿Cómo funciona una red neuronal?, Explica el concepto de algoritmo"
    
    print(f"📝 Model: {model_name}")
    print(f"📋 Prompts: {test_prompts}")
    print("=" * 60)
    
    # Medir tiempo de ejecución
    start_time = time.time()
    
    try:
        # Ejecutar el entrenamiento
        result = await train_model_json(model_name, test_prompts)
        
        end_time = time.time()
        execution_time = end_time - start_time
        
        print("=" * 60)
        print(f"⏱️ Total execution time: {execution_time:.2f} seconds")
        print(f"📊 Status: {result.get('status', 'unknown')}")
        
        if result.get('status') == 'success':
            metrics = result.get('metrics', {})
            print(f"✅ Success rate: {metrics.get('successful_responses', 0)}/{metrics.get('total_prompts_tested', 0)}")
            print(f"📈 Accuracy: {metrics.get('accuracy', 0)}")
            print(f"⚡ Avg response time: {metrics.get('avg_response_time', 0):.2f}s")
            print(f"📝 Test summary: {result.get('test_results_summary', 'N/A')}")
        else:
            print(f"❌ Training failed: {result.get('message', 'Unknown error')}")
            
    except Exception as e:
        print(f"💥 Exception during training: {str(e)}")
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"⏱️ Time before failure: {execution_time:.2f} seconds")

if __name__ == "__main__":
    print("🧪 AI Factory Threading Test")
    print("=" * 60)
    asyncio.run(test_training_with_threading())