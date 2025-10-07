from fastapi import APIRouter, Body, HTTPException
from fastapi.responses import FileResponse
from ...schemas.models_schemas import ModelGetResponse, ModelGetByNameResponse ,ModelCreateRequest, ModelTrainRequest, ModelTrainResponse, ModelAddPromptRequest, ModelAddPromptResponse, ModelDeployRequest, ModelDeployResponse, DeploymentDownloadResponse, ModelComparisonResponse
from ...config import config

from ..services.model_services import get_models_json, get_model_by_name_json, delete_model_json, create_model_json, add_prompt_json, model_train_json, deploy_model_json, list_deployments, compare_model_versions_json

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
    file_path = config.get_models_data_path()
    
    # Ensure file exists
    config.ensure_directories()
    
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


#compare all versions of a model
@router.get("/{model_name}/compare", response_model=ModelComparisonResponse)
async def compare_model_versions(model_name: str):
    """
    Compare all versions of a model and get recommendations.
    
    This endpoint will:
    1. Analyze all trained versions of the specified model
    2. Compare metrics (accuracy, f1-score, response time)
    3. Rank versions by performance
    4. Provide recommendation for best version to deploy
    
    Perfect for deciding which version to deploy to production!
    """
    
    comparison_data = await compare_model_versions_json(model_name)
    
    return comparison_data




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
async def train_model(prompts: ModelTrainRequest):
    """
    Train a model with provided prompts and generate metrics
    
    This endpoint will:
    1. Process the provided prompts
    2. Create a new model version in Ollama
    3. Test the model with all prompts
    4. Calculate performance metrics
    5. Get AI feedback on model quality
    6. Save results to models_data.json
    """
    
    response = await model_train_json(prompts)
    return response



#update model prompt by name
@router.post("/add_prompt", response_model=ModelAddPromptResponse)
async def update_model_prompt(data:ModelAddPromptRequest):

    response = await add_prompt_json(data)

    return response








# Get deployment information and recommendations
@router.get("/{model_name}/deploy-info", response_model=ModelComparisonResponse)
async def get_deployment_info(model_name: str):
    """
    Get deployment information and version recommendations.
    
    Shows comparison of all versions and recommends the best one for deployment.
    Use this endpoint before deploying to make an informed decision.
    """
    return await compare_model_versions_json(model_name)


# Deploy a specific version of a model
@router.post("/deploy", response_model=ModelDeployResponse)
async def deploy_model(request: ModelDeployRequest):
    """
    Deploy a model as a standalone FastAPI package.
    
    💡 TIP: Use GET /{model_name}/deploy-info first to see version comparison!
    
    Creates a complete deployment folder with:
    - FastAPI application (main.py)
    - Modelfile for Ollama
    - Requirements and documentation
    - Docker configuration
    """
    return await deploy_model_json(
        model_name=request.model_name,
        version=request.version
    )


#==============================
# Models Endpoints DELETE
#==============================

#delete model by name
@router.delete("/{model_name}",description="⚠️ **Advertencia:** esta acción eliminará permanentemente el modelo y todas sus versiones. **No se puede deshacer.**",)
async def delete_model(model_name: str):

    response = await delete_model_json(model_name)

    return response


#==============================
# Deployment Download Endpoints
#==============================

@router.get("/deployments/list", response_model=DeploymentDownloadResponse)
async def get_deployments():
    """
    List all available deployment packages for download.
    
    Returns a list of all deployment ZIP files with metadata including:
    - Model name and version
    - File size information
    - Creation timestamp
    """
    return await list_deployments()


@router.get("/deployments/download/{filename}")
async def download_deployment(filename: str):
    """
    Download a specific deployment package ZIP file.
    
    The filename should be obtained from the /deployments/list endpoint.
    """
    from pathlib import Path
    from fastapi import HTTPException
    import os
    
    # Security: ensure filename ends with .zip and doesn't contain path traversal
    if not filename.endswith("-deployment.zip") or ".." in filename or "/" in filename or "\\" in filename:
        raise HTTPException(status_code=400, detail="Invalid filename format")
    
    deployment_path = Path(f"./deployments/{filename}")
    
    if not deployment_path.exists():
        raise HTTPException(status_code=404, detail="Deployment package not found")
    
    return FileResponse(
        path=str(deployment_path),
        filename=filename,
        media_type="application/zip"
    )