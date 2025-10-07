#!/usr/bin/env python3
"""
AI Factory - Quick Modelfile Generator

Simple script to generate Modelfiles quickly from prompts.
"""

import argparse
from config import config


def main():
    """Generate a Modelfile from command line arguments"""
    parser = argparse.ArgumentParser(
        description="Generate a Modelfile for Ollama from a prompt",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python generate_modelfile.py --name "sentiment-analyzer" --prompt "Classify sentiment as positive/negative"
  
  python generate_modelfile.py \\
    --name "code-helper" \\
    --prompt "Help developers write better Python code" \\
    --version "2.0.0"
        """
    )
    
    parser.add_argument(
        "--name", "-n",
        required=True,
        help="Name of the model (used for filename)"
    )
    
    parser.add_argument(
        "--prompt", "-p", 
        required=True,
        help="System prompt for the model"
    )
    
    parser.add_argument(
        "--version", "-v",
        default="1.0.0",
        help="Model version (default: 1.0.0)"
    )
    
    parser.add_argument(
        "--output", "-o",
        help="Output path (optional, uses default models/ directory)"
    )
    
    parser.add_argument(
        "--show", "-s",
        action="store_true",
        help="Show the generated content without saving"
    )
    
    args = parser.parse_args()
    
    # Generate the Modelfile content
    modelfile_content = config.generate_modelfile(
        model_name=args.name,
        prompt=args.prompt,
        version=args.version
    )
    
    if args.show:
        # Just show the content
        print("Generated Modelfile content:")
        print("=" * 50)
        print(modelfile_content)
    else:
        # Save to file
        if args.output:
            output_path = args.output
        else:
            output_path = config.get_model_file_path(args.name)
        
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(modelfile_content)
        
        print(f"✅ Modelfile created successfully!")
        print(f"📁 Location: {output_path}")
        print(f"🏷️  Model: {args.name}")
        print(f"📝 Version: {args.version}")
        print()
        print("🚀 To create the model with Ollama:")
        print(f"   ollama create {args.name} -f \"{output_path}\"")


if __name__ == "__main__":
    main()