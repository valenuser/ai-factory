#!/usr/bin/env python3
"""
AI Factory CLI - Command Line Interface for AI Factory
"""

import argparse
import sys
import os
import uvicorn
import subprocess
import platform
from pathlib import Path
from config import config


def check_ollama_installation():
    """Check if Ollama is installed and accessible"""
    try:
        # Try to run ollama --version
        result = subprocess.run(
            ["ollama", "--version"], 
            capture_output=True, 
            text=True, 
            timeout=10
        )
        
        if result.returncode == 0:
            version = result.stdout.strip()
            print(f"✅ Ollama detected: {version}")
            return True
        else:
            return False
            
    except (subprocess.TimeoutExpired, FileNotFoundError, subprocess.SubprocessError):
        return False


def show_ollama_installation_guide():
    """Show Ollama installation instructions"""
    system = platform.system().lower()
    
    print("❌ Ollama is not installed or not accessible!")
    print("🤖 Ollama is required to run AI Factory")
    print()
    print("📥 Install Ollama:")
    print("   🌐 Website: https://ollama.com")
    print("   📚 Documentation: https://github.com/ollama/ollama")
    print()
    
    if system == "windows":
        print("🪟 Windows Installation:")
        print("   1. Download from: https://ollama.com/download/windows")
        print("   2. Run the installer and follow the setup wizard")
        print("   3. Restart your terminal after installation")
        print("   4. Verify with: ollama --version")
    elif system == "darwin":  # macOS
        print("🍎 macOS Installation:")
        print("   1. Download from: https://ollama.com/download/mac")
        print("   2. Or use Homebrew: brew install ollama")
        print("   3. Verify with: ollama --version")
    elif system == "linux":
        print("🐧 Linux Installation:")
        print("   1. Run: curl -fsSL https://ollama.com/install.sh | sh")
        print("   2. Or download from: https://ollama.com/download/linux")
        print("   3. Verify with: ollama --version")
    
    print()
    print("🔄 After installation, try running 'ai-factory serve' again")
    print()


def serve_command(args):
    """Start the FastAPI server"""
    print("🔍 Checking dependencies...")
    
    # Check if Ollama is installed
    if not check_ollama_installation():
        show_ollama_installation_guide()
        sys.exit(1)
    
    # Initialize directories and configuration
    print("📁 Initializing workspace...")
    config.ensure_directories()
    print(f"✅ Data directory: {config.DATA_DIR}")
    print(f"✅ Models directory: {config.MODELS_DIR}")
    
    print("🚀 Starting AI Factory Server...")
    print(f"📡 Server available at: http://{args.host}:{args.port}")
    print(f"📖 API Documentation: http://{args.host}:{args.port}/docs")
    print("🛑 To stop: Ctrl+C")
    print("-" * 50)
    
    try:
        if args.reload:
            # Para reload, usar import string
            uvicorn.run(
                "api.main:app", 
                host=args.host, 
                port=args.port, 
                reload=True,
                log_level=args.log_level
            )
        else:
            # Para producción, importar directamente
            from api.main import app
            uvicorn.run(
                app, 
                host=args.host, 
                port=args.port, 
                reload=False,
                log_level=args.log_level
            )
    except ImportError as e:
        print(f"❌ Error: Could not import application: {e}")
        print("💡 Make sure you're in the correct project directory")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error starting server: {e}")
        sys.exit(1)


def check_command(args):
    """Check system dependencies"""
    print("🔍 AI Factory - Dependency Check")
    print("=" * 40)
    
    # Check Ollama
    ollama_ok = check_ollama_installation()
    if not ollama_ok:
        print("❌ Ollama: Not found")
        show_ollama_installation_guide()
    else:
        print("✅ Ollama: Available")
    
    # Check Python version
    python_version = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
    print(f"✅ Python: {python_version}")
    
    # Check project directories and files
    config.ensure_directories()
    print(f"✅ Data directory: {config.DATA_DIR}")
    print(f"✅ Models directory: {config.MODELS_DIR}")
    
    # Check project files
    project_files = ["api", "cli.py", "requirements.txt", "setup.py", "config.py"]
    missing_files = [f for f in project_files if not Path(f).exists()]
    
    if missing_files:
        print(f"⚠️  Missing files: {', '.join(missing_files)}")
    else:
        print("✅ Project files: Complete")
    
    print()
    if ollama_ok and not missing_files:
        print("🎉 All dependencies are ready! You can run 'ai-factory serve'")
    else:
        print("🚨 Please fix the issues above before running the server")


def info_command(args):
    """Display project information"""
    print("🏭 AI Factory - Local AI Model Management")
    print("=" * 50)
    print("📋 Description: Tool to create, train, version and deploy")
    print("               AI models locally")
    print("🔧 Technologies: FastAPI + Ollama + Python")
    print("📁 Project: ", Path.cwd())
    print("🌐 Documentation: http://localhost:8000/docs (when running)")
    print()
    
    # Show directory structure
    config.ensure_directories()
    print("📂 Directory Structure:")
    print(f"   📁 Data: {config.DATA_DIR}")
    print(f"   📁 Models: {config.MODELS_DIR}")
    print(f"   📁 Exports: {config.EXPORTS_DIR}")
    print()
    
    print("📚 Available commands:")
    print("   ai-factory serve    - Start server")
    print("   ai-factory check    - Check dependencies")
    print("   ai-factory info     - Show this information")
    print("   ai-factory --help   - Detailed help")


def create_parser():
    """Create the CLI argument parser"""
    parser = argparse.ArgumentParser(
        prog="ai-factory",
        description="AI Factory - Local AI Model Management",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Usage examples:
  ai-factory check                    # Check system dependencies
  ai-factory serve                    # Start with default configuration
  ai-factory serve --port 9000        # Start on custom port
  ai-factory serve --host 0.0.0.0     # Allow external access
  ai-factory serve --reload           # Development mode with auto-reload
  ai-factory info                     # Project information
        """
    )
    
    # Subcommands
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # 'serve' command
    serve_parser = subparsers.add_parser(
        "serve", 
        help="Start the FastAPI server"
    )
    serve_parser.add_argument(
        "--host", 
        default="127.0.0.1", 
        help="Server IP address (default: 127.0.0.1)"
    )
    serve_parser.add_argument(
        "--port", 
        type=int, 
        default=8000, 
        help="Server port (default: 8000)"
    )
    serve_parser.add_argument(
        "--reload", 
        action="store_true", 
        help="Enable auto-reload for development"
    )
    serve_parser.add_argument(
        "--log-level", 
        choices=["critical", "error", "warning", "info", "debug"], 
        default="info",
        help="Logging level (default: info)"
    )
    serve_parser.set_defaults(func=serve_command)
    
    # 'check' command
    check_parser = subparsers.add_parser(
        "check", 
        help="Check system dependencies"
    )
    check_parser.set_defaults(func=check_command)
    
    # 'info' command
    info_parser = subparsers.add_parser(
        "info", 
        help="Show project information"
    )
    info_parser.set_defaults(func=info_command)
    
    return parser


def main():
    """Main CLI function"""
    parser = create_parser()
    args = parser.parse_args()
    
    # If no command is specified, show help
    if not args.command:
        parser.print_help()
        return
    
    # Execute the corresponding command
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()