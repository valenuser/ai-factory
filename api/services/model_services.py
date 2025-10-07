import json
from schemas.models_schemas import ModelCreateRequest, ModelAddPromptRequest
from config import config
import datetime

async def get_models_json():
    models_file = config.get_models_data_path()
    
    try:
        with open(models_file, 'r') as file:
            models_data = file.read()

            if len(models_data) == 0:
                return {
                    "models": [],
                    "message": "No models available"
                }

            models_data = json.loads(models_data)

            data = []

            for model_info in models_data:
                data.append({
                    "model_name": model_info
                })

            return {
                "models": data,
                "message": "Models retrieved successfully"
            }
    except FileNotFoundError:
        # Create file if it doesn't exist
        config.ensure_directories()
        with open(models_file, 'w') as file:
            json.dump({}, file)
        return {
            "models": [],
            "message": "No models available"
        }
    except json.JSONDecodeError:
        return {
            "models": [],
            "message": "Error reading models data"
        }
    

async def get_model_by_name_json(model_name:str):
    models_file = config.get_models_data_path()
    
    try:
        with open(models_file, 'r') as file:
            models_data = file.read()

            if len(models_data) == 0:
                return {
                    "model": {},
                    "message": "No model available"
                }
            
            models_data = json.loads(models_data)

            models_keys = models_data.keys()

            if model_name in models_keys:
                return {
                    "model":{
                        f"{model_name}":{
                            "prompts":models_data[model_name]["prompts"],
                            "version":models_data[model_name]["version"],
                            "created_at":models_data[model_name]["created_at"],
                            "updated_at":models_data[model_name]["updated_at"]
                        }
                    },
                    "message":"Model retrieved successfully"
                }
            
            return {
                    "model": {},
                    "message": "No model available"
                }
    except FileNotFoundError:
        config.ensure_directories()
        return {
            "model": {},
            "message": "No model available"
        }
    except json.JSONDecodeError:
        return {
            "model": {},
            "message": "Error reading models data"
        }





async def delete_model_json(model:str):
    models_file = config.get_models_data_path()
    
    try:
        with open(models_file, 'r+') as file:
            try:
                content = file.read().strip()
                models_data = json.loads(content) if content else {}
            except json.JSONDecodeError:
                models_data = {}

            if not models_data:
                return {"status": "error", "message": "No hay modelos para eliminar"}

            if model not in models_data:
                return {"status": "error", "message": f"Modelo '{model}' no encontrado"}

            # Filtramos todas las claves excepto la que queremos eliminar
            filtered_data = {k: v for k, v in models_data.items() if k != model}

            # Volvemos al inicio del archivo y borramos el contenido
            file.seek(0)
            file.truncate(0)

            # Guardamos el nuevo contenido
            json.dump(filtered_data, file, indent=2, ensure_ascii=False)

        return {"status": "ok", "deleted": model}
    except FileNotFoundError:
        config.ensure_directories()
        return {"status": "error", "message": "No models file found"}


async def create_model_json(model:ModelCreateRequest):

    data_model = model.model_dump()
    models_file = config.get_models_data_path()
    
    try:
        with open(models_file,'r+') as file:
            try:
                content = file.read()
                models_data = json.loads(content) if content else {}
            except json.JSONDecodeError as error:

                return {
                    "model_name":data_model["model_name"],
                    "model_prompt": data_model["model_prompt"],
                    "message":"Problem creating the model, please try again"
                }
            
            date = str(datetime.datetime.now())
            
            models_data[data_model["model_name"]] = {

                    "prompts":[f"{data_model['model_prompt']}"],
                    "version": [],
                    "created_at": date,
                    "updated_at":date
            }

            # Volvemos al inicio del archivo y borramos el contenido
            file.seek(0)
            file.truncate(0)

            # Guardamos el nuevo contenido
            json.dump(models_data, file, indent=2, ensure_ascii=False)

            return {
                data_model["model_name"]:models_data[data_model["model_name"]]
            }
    except FileNotFoundError:
        # Create file if it doesn't exist
        config.ensure_directories()
        with open(models_file, 'w') as file:
            date = str(datetime.datetime.now())
            models_data = {
                data_model["model_name"]: {
                    "prompts":[f"{data_model['model_prompt']}"],
                    "version": [],
                    "created_at": date,
                    "updated_at":date
                }
            }
            json.dump(models_data, file, indent=2, ensure_ascii=False)
            return {
                data_model["model_name"]:models_data[data_model["model_name"]]
            }
        

async def add_prompt_json(data:ModelAddPromptRequest):
    data_model = data.model_dump()
    models_file = config.get_models_data_path()
    
    try:
        with open(models_file,'r+') as file:
            try:
                content = file.read()
                models_data = json.loads(content) if content else {}
                
            except json.JSONDecodeError as error:

                return {
                    "model_name": data_model["model_name"],
                    "message": "Problem adding new prompt, please try again",
                    "added": False
                }
            
            date = str(datetime.datetime.now())
            
            models_data[data_model["model_name"]]["prompts"].append(data_model["new_prompt"])

            models_data[data_model["model_name"]]["updated_at"] = date

            # Volvemos al inicio del archivo y borramos el contenido
            file.seek(0)
            file.truncate(0)

            # Guardamos el nuevo contenido
            json.dump(models_data, file, indent=2, ensure_ascii=False)

            return {
                    "model_name": data_model["model_name"],
                    "new_prompt":data_model["new_prompt"],
                    "added": True
                }
    except FileNotFoundError:
        config.ensure_directories()
        return {
            "model_name": data_model["model_name"],
            "message": "Models file not found",
            "added": False
        }