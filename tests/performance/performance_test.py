#!/usr/bin/env python3
"""
Comparison test: Sequential vs Threading performance
"""
import asyncio
import time
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed

def test_single_prompt_sync(model_name: str, prompt: str, index: int):
    """Test individual prompt (for sequential comparison)"""
    try:
        start_time = time.time()
        result = subprocess.run([
            "ollama", "run", model_name, prompt
        ], capture_output=True, text=True, timeout=15)
        response_time = time.time() - start_time
        return index, response_time, result.returncode == 0
    except:
        return index, 15.0, False

async def compare_performance():
    """Compare sequential vs parallel execution"""
    model_name = "basic-test-model"
    prompts = [
        "¿Qué es Python?",
        "Explica machine learning",
        "Define inteligencia artificial", 
        "¿Cómo funciona una red neuronal?",
        "¿Qué es un algoritmo?"
    ]
    
    print("🔥 PERFORMANCE COMPARISON TEST")
    print("=" * 50)
    print(f"Model: {model_name}")
    print(f"Testing {len(prompts)} prompts")
    print("=" * 50)
    
    # Test 1: Sequential execution
    print("\n🐌 SEQUENTIAL EXECUTION:")
    sequential_start = time.time()
    sequential_times = []
    
    for i, prompt in enumerate(prompts):
        print(f"  Running prompt {i+1}...")
        index, response_time, success = test_single_prompt_sync(model_name, prompt, i)
        sequential_times.append(response_time)
        print(f"    ⏱️ {response_time:.2f}s {'✅' if success else '❌'}")
    
    sequential_total = time.time() - sequential_start
    sequential_avg = sum(sequential_times) / len(sequential_times)
    
    # Test 2: Parallel execution
    print(f"\n🚀 PARALLEL EXECUTION (4 threads):")
    parallel_start = time.time()
    parallel_times = []
    
    with ThreadPoolExecutor(max_workers=4) as executor:
        future_to_index = {
            executor.submit(test_single_prompt_sync, model_name, prompt, i): i 
            for i, prompt in enumerate(prompts)
        }
        
        results = {}
        for future in as_completed(future_to_index):
            index = future_to_index[future]
            try:
                prompt_index, response_time, success = future.result()
                results[prompt_index] = (response_time, success)
                print(f"  ✅ Prompt {prompt_index+1} completed: {response_time:.2f}s")
                parallel_times.append(response_time)
            except Exception as e:
                print(f"  ❌ Prompt {index+1} failed: {str(e)}")
    
    parallel_total = time.time() - parallel_start
    parallel_avg = sum(parallel_times) / len(parallel_times) if parallel_times else 0
    
    # Results comparison
    print("\n" + "=" * 50)
    print("📊 RESULTS COMPARISON:")
    print("=" * 50)
    print(f"Sequential execution:")
    print(f"  ⏱️ Total time: {sequential_total:.2f}s")
    print(f"  📈 Average per prompt: {sequential_avg:.2f}s")
    
    print(f"\nParallel execution:")
    print(f"  ⏱️ Total time: {parallel_total:.2f}s")  
    print(f"  📈 Average per prompt: {parallel_avg:.2f}s")
    
    speedup = sequential_total / parallel_total if parallel_total > 0 else 0
    time_saved = sequential_total - parallel_total
    
    print(f"\n🎯 PERFORMANCE GAIN:")
    print(f"  🚀 Speedup: {speedup:.2f}x faster")
    print(f"  ⏰ Time saved: {time_saved:.2f}s ({time_saved/sequential_total*100:.1f}%)")
    
    if speedup > 2:
        print("  🏆 EXCELLENT: More than 2x speedup!")
    elif speedup > 1.5:
        print("  ✅ GOOD: Significant speedup achieved!")
    else:
        print("  ⚠️ MODERATE: Some improvement, but could be better")

if __name__ == "__main__":
    asyncio.run(compare_performance())