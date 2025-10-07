#!/usr/bin/env python3
"""
Test para verificar que la separación de prompts por coma funciona correctamente
"""

def test_prompt_separation():
    """Test the prompt separation logic"""
    
    print("🧪 Testing Prompt Separation by Comma")
    print("=" * 40)
    
    # Test cases
    test_cases = [
        {
            "name": "Prompts separated by commas",
            "input": "What is the capital of France?, How many days in a year?, What is 2+2?",
            "expected_count": 3
        },
        {
            "name": "Prompts with extra spaces",
            "input": "First prompt , Second prompt,  Third prompt  ,Fourth prompt",
            "expected_count": 4
        },
        {
            "name": "Single prompt",
            "input": "What is artificial intelligence?",
            "expected_count": 1
        },
        {
            "name": "Empty prompts (should be filtered)",
            "input": "Valid prompt, , Another valid, , ,Last valid",
            "expected_count": 3
        }
    ]
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\n{i}. {test_case['name']}")
        print(f"   Input: '{test_case['input']}'")
        
        # Apply the same logic as in train_model_json
        prompts_array = [prompt.strip() for prompt in test_case['input'].split(',') if prompt.strip()]
        
        print(f"   Result: {prompts_array}")
        print(f"   Count: {len(prompts_array)} (expected: {test_case['expected_count']})")
        
        if len(prompts_array) == test_case['expected_count']:
            print("   ✅ PASS")
        else:
            print("   ❌ FAIL")
    
    print(f"\n🎯 Real Training Example:")
    real_prompts = "What is the capital of France?, Help me solve this math problem: If I have 15 apples and give away 7, how many do I have left?, Suggest three creative names for a coffee shop."
    
    real_array = [prompt.strip() for prompt in real_prompts.split(',') if prompt.strip()]
    
    print(f"Input: {real_prompts}")
    print(f"Separated into {len(real_array)} prompts:")
    for j, prompt in enumerate(real_array, 1):
        print(f"   {j}. '{prompt}'")

if __name__ == "__main__":
    import sys, os
    ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
    if ROOT not in sys.path:
        sys.path.insert(0, ROOT)
    test_prompt_separation()