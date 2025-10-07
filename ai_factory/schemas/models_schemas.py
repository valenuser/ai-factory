from pydantic import BaseModel, validator
from typing import Optional

#==========================

#Endpoints '/models' GET

#==========================

#endpoint models '/' response schema

#==========================



class ModelGetResponse(BaseModel):
    
    message:str 
    models: list = []

    class Config:
        json_schema_extra = {
            "example": [{
                "models": [
                    {"model_name": "gpt-4"},
                    {"model_name": "bert-base"},
                    {"model_name": "roberta-large"},
                    {"model_name": "t5-small"}
                ],
                "message": "Models retrieved successfully"
            },
            {
                "models": [],
                "message": "No models available"
            }]
        }


#==========================

#endpoint models '/{model_name}' request and response schemas

#==========================

class ModelGetByNameResponse(BaseModel):
    model: object
    message:str

    class Config:
        json_schema_extra = {
            "example": [{
                "model":{
                        "ai-restaurant-recommender": {
                            "prompts":[],
                            "version":[],
                            "created_at": "2023-10-01T12:00:00Z",
                            "updated_at": "2023-10-01T12:00:00Z"
                        }
                },
                "message":"Model retrieved successfully"
            },
            {
                "model":{},
                "message": "No models available"

            }]
        }

#==========================

#Endpoints '/models' POST

#==========================

#endpoint models '/create' request and response schemas

#==========================

# Model Creation Request Schema
class ModelCreateRequest(BaseModel):
        model_name: str
        base_prompt: str
        version: str

        # Validación de campos no vacíos
        @validator('model_name')
        def validate_model_name(cls, v):
            if not v or not v.strip():
                raise ValueError('model_name cannot be empty')
            return v.strip()
        
        @validator('base_prompt')
        def validate_base_prompt(cls, v):
            if not v or not v.strip():
                raise ValueError('base_prompt cannot be empty')
            return v.strip()
        
        @validator('version')
        def validate_version(cls, v):
            if not v or not v.strip():
                raise ValueError('version cannot be empty')
            return v.strip()

        class Config:
            json_schema_extra = {
                "example": {
                    "model_name": "gpt-4",
                    "base_prompt": "You are a helpful assistant.",
                    "version": "1.0"
                }
            }


class ModelCreateResponse(BaseModel):
    model_name: str
    base_prompt: str
    version: str

    class Config:
        json_schema_extra = {
            "example": {
                "model_name": "gpt-4",
                "model_prompt": "You are a helpful assistant.",
                "version": "1.0.0",
                "created": True
            }
        }


#==========================

#endpoint models '/train' request and response schemas

#==========================


class ModelTrainRequest(BaseModel):
    model_name: str
    prompts: list[str]

    class Config:
        json_schema_extra = {
            "example": {
                "model_name": "basic-test-model",
                "prompts": "What is the capital of France?, Explain what photosynthesis is in simple terms., How many days are there in a leap year?, What is the largest planet in our solar system?, Define what artificial intelligence means., Help me solve this math problem: If I have 15 apples and give away 7, how many do I have left?, I need to organize my daily schedule. Can you suggest a structure for planning my day?, What are three ways to improve productivity while working from home?, How can I remember important dates and appointments better?, Give me steps to troubleshoot a computer that won't start., Suggest five creative names for a new coffee shop., Help me write a short welcome message for new team members., What are some fun indoor activities for a rainy weekend?, Give me ideas for a healthy breakfast that takes less than 10 minutes to make., Explain how to change a tire in simple steps., What is the difference between HTTP and HTTPS?, Compare the advantages and disadvantages of working remotely versus in an office., What are the pros and cons of electric vehicles?, Give me tips for staying focused during long study sessions., List the top 5 benefits of regular exercise and explain each briefly."
            }
        }


class ModelTrainResponse(BaseModel):
     status: str
     model: Optional[str] = None
     version: Optional[str] = None
     metrics: Optional[dict] = None
     feedback: Optional[str] = None
     created_at: Optional[str] = None
     message: Optional[str] = None  # For error messages
     model_name: Optional[str] = None  # For identifying which model had the error


     class Config:
          json_json_schema_extra = {
               "example": {
                    "status": "success",
                    "message": "Model basic-test-model trained successfully",
                    "model_name": "basic-test-model", 
                    "version": "v1.0_1728297872",
                    "metrics": {
                         "accuracy": 1.0,
                         "precision": 1.02,
                         "recall": 0.99,
                         "f1": 1.005,
                         "avg_response_time": 4.83,
                         "successful_responses": 8,
                         "total_prompts_tested": 8,
                         "total_prompts_provided": 20
                    },
                    "feedback": "**Overall Assessment: Good**\n\nMain strengths:\n- Excellent response accuracy (100%)\n- Consistent performance across diverse topics\n- Fast processing with threading optimization\n\nAreas for improvement:\n- Could enhance response depth for complex topics\n- Consider adding more domain-specific examples\n\nSpecific suggestions:\n- Include more technical explanations for scientific questions\n- Add examples and practical applications to answers",
                    "test_results_summary": "8/8 prompts successful (of 20 total)",
                    "ollama_model": "basic-test-model:v1.0_1728297872",
                    "created_at": "2025-10-07T14:31:12.457Z"
               }
          }

#==========================

#endpoint models '/update_prompt' request and response schemas

#==========================

class ModelAddPromptRequest(BaseModel):
    model_name: str
    new_prompt: str

    class Config:
        json_schema_extra = {
            "example": {
                "model_name": "gpt-4",
                "new_prompt": "You are an expert in machine learning."
            }
        }

class ModelAddPromptResponse(BaseModel):
    model_name: str
    new_prompt: Optional[str] = None 
    added: bool
    message: Optional[str] = None 

    class Config:
        json_schema_extra = {
            "example":[ {
                "model_name": "gpt-4",
                "new_prompt": "You are an expert in machine learning.",
                "added": True
            },
            {
                "model_name": "pt-4",
                "message": "Problem adding new prompt, please try again",
                "added": False
            }]
        }



#==========================

#Endpoints '/models' DELETE

#==========================

#endpoint models '/{model_name}' response schema

#==========================

class ModelDeleteRequest(BaseModel):
    model_name: str

    class Config:
        json_schema_extra = {
            "example": {
                "model_name": "gpt-4"
            }
        }

class ModelDeleteResponse(BaseModel):
    message: str

    class Config:
        json_schema_extra = {
            "example": {
                "message": "Model gpt-4 deleted successfully."
            }
        }


#==========================

#Endpoints '/models/deploy' 

#==========================

class ModelDeployRequest(BaseModel):
    model_name: str
    version: str

    class Config:
        json_schema_extra = {
            "example": {
                "model_name": "basic-test-model",
                "version": "v1.0_1728297872"
            }
        }


class ModelDeployResponse(BaseModel):
    status: str
    message: str
    deployment_folder: str
    zip_file: str
    zip_filename: str
    model_name: str
    version: str
    files_created: list
    instructions: str

    class Config:
        json_schema_extra = {
            "example": {
                "status": "success",
                "message": "Deployment package created successfully",
                "deployment_folder": "./deployments/basic-test-model-v1.0_1728297872",
                "zip_file": "./deployments/basic-test-model-v1.0_1728297872-deployment.zip",
                "zip_filename": "basic-test-model-v1.0_1728297872-deployment.zip",
                "model_name": "basic-test-model",
                "version": "v1.0_1728297872",
                "files_created": [
                    "main.py",
                    "Modelfile",
                    "requirements.txt",
                    "README.md",
                    "docker-compose.yml"
                ],
                "instructions": "1. cd deployments/basic-test-model-v1.0_1728297872\n2. pip install -r requirements.txt\n3. python main.py\n4. Visit http://localhost:8080/docs"
            }
        }


# Deployment Download Schemas
class DeploymentDownloadResponse(BaseModel):
    deployments: list
    status: str
    message: str

    class Config:
        json_schema_extra = {
            "example": {
                "status": "success",
                "message": "Found 2 deployment packages",
                "deployments": [
                    {
                        "model_name": "basic-test-model",
                        "version": "v1.0_1728297872",
                        "filename": "basic-test-model-v1.0_1728297872-deployment.zip",
                        "size_bytes": 2048576,
                        "size_mb": 1.95,
                        "created_at": 1728297872.123
                    },
                    {
                        "model_name": "advanced-model",
                        "version": "v2.1.0",
                        "filename": "advanced-model-v2.1.0-deployment.zip",
                        "size_bytes": 1024768,
                        "size_mb": 0.98,
                        "created_at": 1728290000.456
                    }
                ]
            }
        }


# Model Version Comparison Schemas
class ModelComparisonResponse(BaseModel):
    model_name: str
    total_versions: int
    comparison: dict
    recommendation: dict
    status: str
    message: str

    class Config:
        json_schema_extra = {
            "example": {
                "model_name": "mi-modelo",
                "total_versions": 2,
                "status": "success",
                "message": "Version comparison completed",
                "comparison": {
                    "versions": [
                        {
                            "version": "1.0.1",
                            "prompts_count": 1,
                            "metrics": {
                                "accuracy": 1.0,
                                "f1_score": 0.995,
                                "avg_response_time": 6.18
                            },
                            "ranking": 2,
                            "trained_at": "2024-10-07T15:30:00Z"
                        },
                        {
                            "version": "1.0.2", 
                            "prompts_count": 4,
                            "metrics": {
                                "accuracy": 0.667,
                                "f1_score": 0.671,
                                "avg_response_time": 9.39
                            },
                            "ranking": 1,
                            "trained_at": "2024-10-07T16:15:00Z"
                        }
                    ]
                },
                "recommendation": {
                    "best_version": "1.0.1",
                    "reason": "Mejor accuracy (1.0 vs 0.667) y f1-score (0.995 vs 0.671), con tiempo de respuesta más rápido",
                    "confidence": 0.92,
                    "deploy_recommendation": "Recomendado para deployment en producción"
                }
            }
        }

