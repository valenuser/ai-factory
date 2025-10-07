# API Completa de AI Factory

## Descripción General

AI Factory proporciona una API REST completa para gestionar modelos de IA. Todos los endpoints están disponibles cuando el servidor está ejecutándose.

## Iniciar el Servidor

```bash
# Opción 1: Comando simple
ai-factory serve

# Opción 2: Con configuración personalizada  
ai-factory serve --host 0.0.0.0 --port 8000

# Opción 3: Usando Python directamente
python -m ai_factory.cli serve
```

**📍 URLs importantes:**
- **Documentación interactiva**: http://localhost:8000/docs
- **API principal**: http://localhost:8000
- **Interfaz alternativa**: http://localhost:8000/redoc

## Endpoints Disponibles

### 1. Health Check

**GET** `/health`

Verifica que la API esté funcionando.

**Respuesta:**
```json
{
  "status": "🚀 api_factory is running"
}
```

### 2. Gestión de Modelos

#### Listar Modelos
**GET** `/models/`

**Respuesta:**
```json
{
  "message": "Models retrieved successfully",
  "models": [
    {"model_name": "mi-modelo"},
    {"model_name": "otro-modelo"}
  ]
}
```

#### Crear Modelo
**POST** `/models/create`

**Request Body:**
```json
{
  "model_name": "mi-nuevo-modelo",
  "base_prompt": "Eres un asistente útil",
  "version": "1.0"
}
```

#### Obtener Modelo Específico
**GET** `/models/{model_name}`

**Respuesta:**
```json
{
  "model": {
    "mi-modelo": {
      "prompts": ["Prompt inicial"],
      "version": [],
      "created_at": "2025-10-07T21:00:00",
      "updated_at": "2025-10-07T21:00:00"
    }
  },
  "message": "Model retrieved successfully"
}
```

#### Entrenar Modelo
**POST** `/models/train`

**Request Body:**
```json
{
  "model_name": "mi-modelo",
  "prompts": [
    "¿Cuál es la capital de España?",
    "Explica qué es la inteligencia artificial"
  ]
}
```

**Respuesta:**
```json
{
  "status": "success",
  "model": null,
  "version": "1.0.1",
  "metrics": {
    "accuracy": 1.0,
    "precision": 1.0,
    "recall": 0.99,
    "f1": 0.995,
    "avg_response_time": 2.1
  }
}
```

#### Agregar Prompt
**POST** `/models/add_prompt`

**Request Body:**
```json
{
  "model_name": "mi-modelo",
  "new_prompt": "Eres también experto en ciencias"
}
```

#### Eliminar Modelo
**DELETE** `/models/{model_name}`

#### 🆕 Comparar Versiones de Modelo
**GET** `/models/{model_name}/compare`

Compara todas las versiones entrenadas de un modelo y proporciona recomendaciones automáticas.

**Respuesta:**
```json
{
  "model_name": "mi-modelo",
  "total_versions": 2,
  "comparison": {
    "versions": [
      {
        "version": "1.0.1",
        "prompts_count": 3,
        "metrics": {
          "accuracy": 0.95,
          "f1_score": 0.93,
          "avg_response_time": 2.1
        },
        "ranking": 1,
        "trained_at": "2024-10-07T15:30:00Z"
      },
      {
        "version": "1.0.2", 
        "prompts_count": 5,
        "metrics": {
          "accuracy": 0.92,
          "f1_score": 0.89,
          "avg_response_time": 3.5
        },
        "ranking": 2,
        "trained_at": "2024-10-07T16:15:00Z"
      }
    ]
  },
  "recommendation": {
    "best_version": "1.0.1",
    "reason": "Mejor accuracy (95%) y f1-score (93%), con tiempo de respuesta más rápido (2.1s)",
    "confidence": 0.89,
    "deploy_recommendation": "Altamente recomendado para deployment en producción"
  },
  "status": "success"
}
```

#### 🆕 Información de Deployment
**GET** `/models/{model_name}/deploy-info`

Obtiene información y recomendaciones antes de hacer un deployment. Idéntica respuesta que `/compare` pero enfocada en decisión de deployment.

**Uso recomendado:** Llama a este endpoint ANTES de crear un deployment para elegir la mejor versión.

### 3. Deployments

#### Crear Deployment
**POST** `/models/deploy`

**Request Body:**
```json
{
  "model_name": "mi-modelo",
  "version": "1.0"
}
```

**Respuesta:**
```json
{
  "status": "success",
  "message": "Deployment package created successfully",
  "deployment_folder": "./deployments/mi-modelo-1.0",
  "zip_file": "deployments/mi-modelo-1.0-deployment.zip",
  "zip_filename": "mi-modelo-1.0-deployment.zip"
}
```

#### Listar Deployments
**GET** `/models/deployments/list`

**Respuesta:**
```json
{
  "status": "success",
  "message": "Found 2 deployment packages",
  "deployments": [
    {
      "model_name": "mi-modelo",
      "version": "1.0.1",
      "filename": "mi-modelo-1.0.1-deployment.zip",
      "size_bytes": 3011,
      "size_mb": 0.0
    }
  ]
}
```

#### Descargar Deployment
**GET** `/models/deployments/download/{filename}`

Descarga el archivo ZIP del deployment.

### 4. Utilidades

#### Exportar Modelos
**GET** `/models/export`

Descarga todos los datos de modelos como archivo JSON.

## Códigos de Estado HTTP

- **200**: Operación exitosa
- **201**: Recurso creado exitosamente  
- **400**: Request inválido
- **404**: Recurso no encontrado
- **422**: Error de validación
- **500**: Error interno del servidor

## Autenticación

Actualmente la API no requiere autenticación, pero se recomienda usar en entornos seguros.

## Límites y Consideraciones

- Timeout por defecto: 30 segundos para entrenamientos
- Tamaño máximo de prompts: 10,000 caracteres
- Máximo 100 prompts por entrenamiento
- Los deployments se almacenan en `./deployments/`

## Ejemplos de Uso

### Crear y Entrenar un Modelo Completo

```python
import requests

BASE_URL = "http://localhost:8000"

# 1. Crear modelo
response = requests.post(f"{BASE_URL}/models/create", json={
    "model_name": "asistente-personal",
    "base_prompt": "Eres un asistente personal útil",
    "version": "1.0"
})

# 2. Entrenar primera versión
response = requests.post(f"{BASE_URL}/models/train", json={
    "model_name": "asistente-personal", 
    "prompts": [
        "¿Cómo organizar mi día?",
        "Dame consejos de productividad"
    ]
})
print(f"Primera versión: {response.json()['version']}")

# 3. Agregar más prompts
requests.post(f"{BASE_URL}/models/add_prompt", json={
    "model_name": "asistente-personal",
    "prompt": "También ayuda con gestión del tiempo"
})

# 4. Entrenar nueva versión
response = requests.post(f"{BASE_URL}/models/train", json={
    "model_name": "asistente-personal", 
    "prompts": [
        "¿Cómo organizar mi día?",
        "Dame consejos de productividad",
        "Ayúdame con gestión del tiempo"
    ]
})
print(f"Segunda versión: {response.json()['version']}")

# 🆕 5. COMPARAR VERSIONES ANTES DE DEPLOYAR
response = requests.get(f"{BASE_URL}/models/asistente-personal/deploy-info")
comparison = response.json()

print(f"\n📊 Comparación de versiones:")
print(f"Total versiones: {comparison['total_versions']}")
print(f"Mejor versión: {comparison['recommendation']['best_version']}")
print(f"Razón: {comparison['recommendation']['reason']}")
print(f"Confianza: {comparison['recommendation']['confidence']:.1%}")

# 6. Deployar la versión recomendada
best_version = comparison['recommendation']['best_version']
response = requests.post(f"{BASE_URL}/models/deploy", json={
    "model_name": "asistente-personal",
    "version": best_version  # 🎯 Usar la versión recomendada
})

print(f"🚀 Deployed version {best_version}")
```

### 🆕 Flujo Optimizado con Comparación de Versiones

```python
# Flujo recomendado para deployment inteligente:

# 1. Crear y entrenar múltiples versiones...
# 2. Comparar todas las versiones
comparison = requests.get(f"{BASE_URL}/models/mi-modelo/compare").json()

# 3. Mostrar recomendación al usuario
recommendation = comparison['recommendation']
print(f"🤖 Recomendación automática:")
print(f"   Mejor versión: {recommendation['best_version']}")
print(f"   Confianza: {recommendation['confidence']:.1%}")
print(f"   Razón: {recommendation['reason']}")

# 4. Deployar con confianza
if recommendation['confidence'] > 0.8:
    # Deploy automático para alta confianza
    deploy_version = recommendation['best_version']
else:
    # Pedir confirmación al usuario para baja confianza
    deploy_version = input(f"Versión recomendada: {recommendation['best_version']}. ¿Continuar? (y/n): ")

requests.post(f"{BASE_URL}/models/deploy", json={
    "model_name": "mi-modelo",
    "version": deploy_version
})
```

## Documentación Interactiva

Para explorar la API de forma interactiva:

1. Inicia el servidor: `ai-factory serve`
2. Visita: http://localhost:8000/docs
3. Prueba los endpoints directamente desde el navegador