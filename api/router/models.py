from fastapi import APIRouter, Body
from fastapi.responses import FileResponse
from schemas.models_schemas import ModelGetResponse, ModelGetByNameResponse ,ModelCreateRequest, ModelTrainRequest, ModelTrainResponse, ModelAddPromptRequest, ModelAddPromptResponse, ModelCompareRequest,ModelCompareResponse

from api.services.model_services import get_models_json, get_model_by_name_json, delete_model_json, create_model_json, add_prompt_json

router = APIRouter()


#==============================
# Models Endpoints GET
#==============================

#show all models in the json file
@router.get("/", response_model=ModelGetResponse)
async def get_models():

    models_data = await get_models_json()


    return models_data


#export models_Data as file
@router.get("/export")
def export_json():

    file_path = 'models_data.json'

    return FileResponse(
        path= file_path,
        filename="models_data.json",  # nombre del archivo que descargará el usuario
        media_type="application/json"
    )


#show model by name
@router.get("/{model_name}", response_model=ModelGetByNameResponse)
async def get_model_by_name(model_name: str):

    model_data = await get_model_by_name_json(model_name)


    return model_data




#==============================
# Models Endpoints POST
#==============================

#create new model with name and prompt
@router.post("/create", response_model=ModelCreateRequest)
async def create_model(model:ModelCreateRequest):
    response = await create_model_json(model)

    return response


#train model with prompts
@router.post("/train", response_model=ModelTrainResponse)
def train_model(prompts:ModelTrainRequest):
    return {
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



#update model prompt by name
@router.post("/add_prompt", response_model=ModelAddPromptResponse)
async def update_model_prompt(data:ModelAddPromptRequest):

    response = await add_prompt_json(data)

    return response



#compare two versions of a model
@router.post("/compare", response_model=ModelCompareResponse)
def compare_versions(data:ModelCompareRequest):
    return {
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




#deploy a specific version of a model
@router.post("/deploy")
def deploy_model(model_name:str, version:str):
    return {"message": f"Deploying version {version} of model {model_name}"}


#==============================
# Models Endpoints DELETE
#==============================

#delete model by name
@router.delete("/{model_name}",description="⚠️ **Advertencia:** esta acción eliminará permanentemente el modelo y todas sus versiones. **No se puede deshacer.**",)
async def delete_model(model_name: str):

    response = await delete_model_json(model_name)

    return response