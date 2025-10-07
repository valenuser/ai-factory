#!/bin/bash
# AI Factory Easy Installer
# Works on Linux, macOS, and Windows (with Git Bash)

set -e

echo "🚀 AI Factory Easy Installer"
echo "============================="

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Check Python
echo -e "${BLUE}📦 Checking Python installation...${NC}"
if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
elif command -v python &> /dev/null; then
    PYTHON_CMD="python"
else
    echo -e "${RED}❌ Python is not installed!${NC}"
    echo -e "${YELLOW}📥 Please install Python 3.8+ from https://python.org${NC}"
    exit 1
fi

PYTHON_VERSION=$($PYTHON_CMD --version 2>&1 | cut -d' ' -f2)
echo -e "${GREEN}✅ Python $PYTHON_VERSION found${NC}"

# Check pip
echo -e "${BLUE}📦 Checking pip...${NC}"
if command -v pip &> /dev/null; then
    PIP_CMD="pip"
elif command -v pip3 &> /dev/null; then
    PIP_CMD="pip3"
else
    echo -e "${RED}❌ pip is not installed!${NC}"
    echo -e "${YELLOW}📥 Installing pip...${NC}"
    $PYTHON_CMD -m ensurepip --default-pip
    PIP_CMD="pip"
fi
echo -e "${GREEN}✅ pip found${NC}"

# Check Ollama
echo -e "${BLUE}🤖 Checking Ollama installation...${NC}"
if command -v ollama &> /dev/null; then
    OLLAMA_VERSION=$(ollama --version 2>&1)
    echo -e "${GREEN}✅ $OLLAMA_VERSION${NC}"
else
    echo -e "${YELLOW}⚠️ Ollama is not installed${NC}"
    echo -e "${BLUE}📥 Installing Ollama...${NC}"
    
    # Detect OS and install Ollama
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        curl -fsSL https://ollama.com/install.sh | sh
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        if command -v brew &> /dev/null; then
            brew install ollama
        else
            echo -e "${YELLOW}💡 Please install Ollama from https://ollama.com${NC}"
            echo -e "${YELLOW}   Or install Homebrew first: /bin/bash -c \"\$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\"${NC}"
        fi
    else
        echo -e "${YELLOW}💡 Please download and install Ollama from https://ollama.com${NC}"
        echo -e "${YELLOW}   Then run this installer again.${NC}"
        exit 1
    fi
    
    # Verify installation
    if command -v ollama &> /dev/null; then
        echo -e "${GREEN}✅ Ollama installed successfully${NC}"
    else
        echo -e "${RED}❌ Ollama installation failed${NC}"
        exit 1
    fi
fi

# Install AI Factory
echo -e "${BLUE}🏭 Installing AI Factory...${NC}"
$PIP_CMD install -e .

# Verify installation
if command -v ai-factory &> /dev/null; then
    echo -e "${GREEN}✅ AI Factory installed successfully!${NC}"
else
    echo -e "${YELLOW}⚠️ Command 'ai-factory' not found in PATH${NC}"
    echo -e "${YELLOW}💡 You can still use: python cli.py serve${NC}"
fi

# Pull a base model for Ollama
echo -e "${BLUE}📦 Downloading base AI model (this may take a few minutes)...${NC}"
ollama pull llama3.2:1b 2>/dev/null || {
    echo -e "${YELLOW}⚠️ Could not download llama3.2:1b${NC}"
    echo -e "${YELLOW}💡 You can download it later with: ollama pull llama3.2:1b${NC}"
}

# Success message
echo ""
echo -e "${GREEN}🎉 AI Factory Installation Complete!${NC}"
echo "=================================="
echo ""
echo -e "${BLUE}🚀 Quick Start:${NC}"
echo "   1. Start the server: ai-factory serve"
echo "   2. Open browser: http://localhost:8000/docs"
echo "   3. Create your first model!"
echo ""
echo -e "${BLUE}📚 Resources:${NC}"
echo "   • Quick Guide: cat QUICKSTART.md"
echo "   • Examples: ls examples/"
echo "   • Documentation: README.md"
echo ""
echo -e "${BLUE}🆘 Need Help?${NC}"
echo "   • Run: ai-factory --help"
echo "   • Check: python examples/simple_chatbot.py"
echo ""
echo -e "${GREEN}Happy AI building! 🤖${NC}"