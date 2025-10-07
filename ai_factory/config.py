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
    
    @classmethod
    def get_template_path(cls) -> str:
        """Get the absolute path to the Modelfile template"""
        template_dir = cls.PROJECT_ROOT / "templates"
        template_dir.mkdir(exist_ok=True)
        return str(template_dir / "Modelfile.template")
    
    @classmethod
    def generate_modelfile(cls, model_name: str, prompt: str, version: str = "1.0.0") -> str:
        """Generate a Modelfile from the template with the given parameters"""
        template_path = cls.get_template_path()
        
        try:
            with open(template_path, 'r', encoding='utf-8') as file:
                template_content = file.read()
            
            # Use format to replace placeholders
            modelfile_content = template_content.format(
                prompt=prompt,
                model_name=model_name,
                version=version
            )
            
            return modelfile_content
            
        except FileNotFoundError:
            # Fallback simple template if template file doesn't exist
            return f"""FROM llama3.2

SYSTEM \"\"\"
{prompt}
\"\"\"

PARAMETER temperature 0.7
PARAMETER top_p 0.9
PARAMETER num_ctx 4096
"""
    
    @classmethod
    def create_modelfile_for_model(cls, model_name: str, prompt: str, version: str = "1.0.0") -> str:
        """Create and save a Modelfile for a specific model"""
        modelfile_content = cls.generate_modelfile(model_name, prompt, version)
        modelfile_path = cls.get_model_file_path(model_name)
        
        with open(modelfile_path, 'w', encoding='utf-8') as file:
            file.write(modelfile_content)
        
        return modelfile_path


# Initialize configuration
config = Config()