"""
AI Factory - Tool to create, train, version and deploy AI models locally
"""

__version__ = "1.0.0"
__author__ = "Valentin"
__email__ = "vpavonlopez@gmail.com"

# Import main components for easy access
from ai_factory.config import config
from ai_factory.api.main import app

__all__ = ["config", "app", "__version__"]