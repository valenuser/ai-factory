#!/usr/bin/env python3
"""
AI Factory - Modelfile Generation Example

This example shows how to use the Modelfile template to create custom models.
"""

import sys
from pathlib import Path

# Add parent directory to path to import config
sys.path.append(str(Path(__file__).parent.parent))
from config import config


def example_usage():
    """Demonstrate how to use the Modelfile template"""
    
    print("🏭 AI Factory - Modelfile Generation Example")
    print("=" * 50)
    
    # Example 1: Simple text classifier
    print("📝 Example 1: Text Sentiment Classifier")
    prompt1 = """You are a sentiment analysis expert. Analyze the given text and classify it as:
- POSITIVE: for positive sentiment
- NEGATIVE: for negative sentiment  
- NEUTRAL: for neutral sentiment

Respond only with the classification and a brief explanation."""
    
    modelfile1 = config.generate_modelfile(
        model_name="sentiment-classifier",
        prompt=prompt1,
        version="1.0.0"
    )
    
    print("Generated Modelfile content:")
    print("-" * 30)
    print(modelfile1[:300] + "...")
    print()
    
    # Example 2: Code reviewer
    print("📝 Example 2: Code Review Assistant")
    prompt2 = """You are an expert code reviewer. Review the provided code and:
1. Identify potential bugs or issues
2. Suggest improvements for readability
3. Check for security vulnerabilities
4. Recommend best practices

Provide constructive feedback in a clear, organized format."""
    
    # Create and save the Modelfile
    modelfile_path = config.create_modelfile_for_model(
        model_name="code-reviewer",
        prompt=prompt2,
        version="1.1.0"
    )
    
    print(f"✅ Modelfile created at: {modelfile_path}")
    print()
    
    # Example 3: Simple format usage
    print("📝 Example 3: Direct Template Usage")
    template_path = config.get_template_path()
    
    try:
        with open(template_path, 'r', encoding='utf-8') as file:
            template = file.read()
        
        # Direct format usage
        custom_modelfile = template.format(
            prompt="You are a helpful assistant that explains complex topics simply.",
            model_name="simple-explainer", 
            version="2.0.0"
        )
        
        print("✅ Direct format() method works perfectly!")
        print(f"Template path: {template_path}")
        
    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    example_usage()