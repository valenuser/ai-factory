@echo off
REM AI Factory Easy Installer for Windows
REM Run this in Command Prompt or PowerShell

echo 🚀 AI Factory Easy Installer for Windows
echo ==========================================

REM Check Python
echo 📦 Checking Python installation...
python --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo ❌ Python is not installed or not in PATH!
    echo 📥 Please install Python 3.8+ from https://python.org
    echo 💡 Make sure to check "Add Python to PATH" during installation
    pause
    exit /b 1
) else (
    for /f "tokens=2" %%i in ('python --version 2^>^&1') do echo ✅ Python %%i found
)

REM Check pip
echo 📦 Checking pip...
pip --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo ❌ pip is not available!
    echo 📥 Installing pip...
    python -m ensurepip --default-pip
) else (
    echo ✅ pip found
)

REM Check Ollama
echo 🤖 Checking Ollama installation...
ollama --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo ❌ Ollama is not installed!
    echo 📥 Please download and install Ollama from https://ollama.com
    echo 💡 After installation, restart this script
    start https://ollama.com
    pause
    exit /b 1
) else (
    for /f "tokens=*" %%i in ('ollama --version 2^>^&1') do echo ✅ %%i
)

REM Install AI Factory
echo 🏭 Installing AI Factory...
pip install -e .
if %ERRORLEVEL% NEQ 0 (
    echo ❌ Installation failed!
    pause
    exit /b 1
)

REM Verify installation
ai-factory --help >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo ⚠️ Command 'ai-factory' not found in PATH
    echo 💡 You can still use: python cli.py serve
) else (
    echo ✅ AI Factory installed successfully!
)

REM Download base model
echo 📦 Downloading base AI model (this may take a few minutes)...
ollama pull llama3.2:1b
if %ERRORLEVEL% NEQ 0 (
    echo ⚠️ Could not download llama3.2:1b
    echo 💡 You can download it later with: ollama pull llama3.2:1b
)

REM Success message
echo.
echo 🎉 AI Factory Installation Complete!
echo ==================================
echo.
echo 🚀 Quick Start:
echo    1. Start the server: ai-factory serve
echo    2. Open browser: http://localhost:8000/docs
echo    3. Create your first model!
echo.
echo 📚 Resources:
echo    • Quick Guide: type QUICKSTART.md
echo    • Examples: dir examples\
echo    • Documentation: README.md
echo.
echo 🆘 Need Help?
echo    • Run: ai-factory --help
echo    • Check: python examples\simple_chatbot.py
echo.
echo Happy AI building! 🤖
pause