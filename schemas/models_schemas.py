from pydantic import BaseModel
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
        schema_extra = {
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
        schema_extra = {
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
        model_prompt: str

        class Config:
            schema_extra = {
                "example": {
                    "model_name": "gpt-4",
                    "model_prompt": "You are a helpful assistant."
                }
            }


class ModelCreateResponse(BaseModel):
    model_name: str
    model_prompt: str
    version: str

    class Config:
        schema_extra = {
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
    prompts: str

    class Config:
        schema_extra = {
            "example": {
                "model_name": "gpt-4",
                "prompts": "What is the capital of France?"
            }
        }


class ModelTrainResponse(BaseModel):
     status:str
     model:str
     version:str
     previous_version:str
     metrics:dict
     feedback:str
     created_at:str


     class Config:
          schema_extra = {
               "example": {
                    "status": "ok",
                    "model": "gpt-4",
                    "version": "1.0.0",
                    "previous_version": "0.9.0",
                    "metrics": {
                         "accuracy": 0.95,
                         "precision": 0.92,
                         "recall": 0.93,
                         "f1": 0.94
                    },
                    "feedback": "Model trained successfully.",
                    "created_at": "2023-10-01T12:00:00Z"
               }
          }

#==========================

#endpoint models '/update_prompt' request and response schemas

#==========================

class ModelAddPromptRequest(BaseModel):
    model_name: str
    new_prompt: str

    class Config:
        schema_extra = {
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
        schema_extra = {
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

#endpoint models '/compare' request and response schemas

#==========================

class ModelCompareRequest(BaseModel):
    model_name: str
    version1: str
    version2: str

    class Config:
        schema_extra = {
            "example": {
                "model_name": "gpt-4",
                "version1": "1.0.0",
                "version2": "1.1.0"
            }
        }


class ModelCompareResponse(BaseModel):
    model_name: str
    version1: str
    version2: str
    version1_metric: dict
    version2_metric: dict
    comparison_result: str

    class Config:
        schema_extra = {
            "example": {
                "model_name": "gpt-4",
                "version1": "1.0.0",
                "version2": "1.1.0",
                "version1_metric": {
                    "accuracy": 0.95,
                    "precision": 0.92,
                    "recall": 0.93,
                    "f1": 0.94
                },
                "version2_metric": {
                    "accuracy": 0.96,
                    "precision": 0.93,
                    "recall": 0.94,
                    "f1": 0.95
                },
                "comparison_result": "Version 1.1.0 shows a slight improvement over 1.0.0 in all metrics."

            }
        }


#==========================

#Endpoints '/models' DELETE

#==========================

#endpoint models '/{model_name}' response schema

#==========================

class ModelDeleteRequest(BaseModel):
    model_name: str

    class Config:
        schema_extra = {
            "example": {
                "model_name": "gpt-4"
            }
        }

class ModelDeleteResponse(BaseModel):
    message: str

    class Config:
        schema_extra = {
            "example": {
                "message": "Model gpt-4 deleted successfully."
            }
        }

