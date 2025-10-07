"""
AI Factory - Configuration Module

This module handles all file paths and configurations in a portable way.
"""

import os
from pathlib import Path


class Config:
    """Central configuration for AI Factory with portable paths"""
    
    # Base directories
    PROJECT_ROOT = Path.cwd()
    DATA_DIR = PROJECT_ROOT / "data"
    MODELS_DIR = PROJECT_ROOT / "models"
    EXPORTS_DIR = PROJECT_ROOT / "exports"
    
    # File paths
    MODELS_DATA_FILE = DATA_DIR / "models_data.json"
    
    # Ensure directories exist
    @classmethod
    def ensure_directories(cls):
        """Create necessary directories if they don't exist"""
        cls.DATA_DIR.mkdir(exist_ok=True)
        cls.MODELS_DIR.mkdir(exist_ok=True)
        cls.EXPORTS_DIR.mkdir(exist_ok=True)
    
    @classmethod
    def get_models_data_path(cls) -> str:
        """Get the absolute path to models_data.json"""
        cls.ensure_directories()
        return str(cls.MODELS_DATA_FILE)
    
    @classmethod
    def get_export_path(cls, filename: str) -> str:
        """Get the absolute path for export files"""
        cls.ensure_directories()
        return str(cls.EXPORTS_DIR / filename)
    
    @classmethod
    def get_model_file_path(cls, model_name: str) -> str:
        """Get the absolute path for a model's Modelfile"""
        cls.ensure_directories()
        return str(cls.MODELS_DIR / f"{model_name}.Modelfile")


# Initialize configuration
config = Config()