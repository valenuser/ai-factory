<div align="center">

# 🏭 AI Factory

**La plataforma definitiva para entrenar, comparar y desplegar modelos de IA locales**

[![PyPI version](https://badge.fury.io/py/ai-factory.svg)](https://badge.fury.io/py/ai-factory)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **¡Crea tus propios modelos de IA personalizados en 5 minutos!** 🤖✨  
> Sin conocimientos técnicos complicados - 100% local y gratuito

## 📚 **GUÍAS FÁCILES PARA USUARIOS** 📚

[![🚀 Inicio Rápido](https://img.shields.io/badge/🚀-Inicio%20Rápido%20(2%20min)-brightgreen?style=for-the-badge)](./docs/GUIA_FACIL.md)
[![📖 API Completa](https://img.shields.io/badge/📖-API%20Completa-blue?style=for-the-badge)](./docs/API_COMPLETA.md)  
[![🛠️ CLI Completa](https://img.shields.io/badge/🛠️-CLI%20Completa-red?style=for-the-badge)](./docs/CLI_COMPLETA.md)

**¿Primera vez?** 👆 **¡Usa las guías de arriba!** Son súper fáciles de seguir.

</div>

---

AI Factory es una plataforma completa para crear, entrenar, versionar y desplegar modelos de inteligencia artificial personalizados de forma local. Con threading optimizado, sistema de descargas y una interfaz FastAPI moderna.

## 🚀 Características principales

- ✅ **Creación y entrenamiento** de modelos locales con Ollama
- ⚡ **Threading optimizado** con mejoras de rendimiento 2.91x  
- 📦 **Sistema de deployment** con generación automática de ZIP
- 📥 **Descarga de deployments** directamente desde la API
- 🔄 **Versionado automático** y comparación de modelos
- 📊 **Testing exhaustivo** con suite de pruebas completa
- 🌐 **Interfaz Swagger** para uso sin código

## 📁 Estructura del proyecto

```
ai-factory/
├── 📂 ai_factory/             # Código fuente principal
│   ├── api/                   # FastAPI application
│   ├── cli.py                 # Interfaz de línea de comandos
│   ├── schemas/               # Pydantic schemas
│   └── utils/                 # Utilidades
├── 📂 tests/                  # Suite de testing completa
│   ├── unit/                  # Tests unitarios
│   ├── integration/           # Tests de integración
│   └── performance/           # Tests de rendimiento
├── 📂 docs/                   # Documentación completa
├── 📂 examples/               # Ejemplos de uso
├── 📂 scripts/                # Scripts de utilidades
└── 📂 deployments/            # Deployments generados
```

## ⚡ Instalación Súper Fácil

### 🎯 **Instalación Express (Recomendada)**

```bash
pip install ai-factory
ai-factory serve
```

**¡Listo!** Ve a: `http://localhost:8000/docs`

### 🛠️ **Prerequisitos**

- **Python 3.8+** (si no tienes: [descargar aquí](https://python.org))
- **Ollama** para los modelos ([descargar aquí](https://ollama.ai))

### 📦 **Instalación desde código fuente**

```bash
# Clonar repositorio
git clone <repo-url>
cd ai-factory

# Usar script automático
# Windows: doble clic en scripts/install.bat
# Mac/Linux: ./scripts/install.sh

# O manualmente:
pip install -r requirements.txt
python -m uvicorn ai_factory.api.main:app --reload --port 8000
```

> **💡 ¿Problemas?** Ve a la [**Guía de Solución de Problemas**](./docs/CLI_COMPLETA.md)

## 🚀 Uso rápido

### 1. **Interfaz web (recomendado)**

Visita: `http://localhost:8000/docs`

### 2. **API Endpoints principales**

#### 📝 **Crear modelo**

```http
POST /models/create
{
  "model_name": "mi-modelo",
  "base_prompt": "Eres un asistente especializado en...",
  "version": "1.0.0"
}
```

#### 🎯 **Entrenar modelo**

```http
POST /models/train
{
  "model_name": "mi-modelo", 
  "prompts": ["Ejemplo 1", "Ejemplo 2"]
}
```

#### 📦 **Deploy modelo**

```http
POST /models/deploy
{
  "model_name": "mi-modelo",
  "version": "1.0.0"
}
```

#### 📥 **Descargar deployment**

```http
# 1. Listar deployments
GET /models/deployments/list

# 2. Descargar ZIP
GET /models/deployments/download/{filename}
```

## 🔥 Casos de Uso Reales

### 💬 Chatbot Personalizado

```bash
# Crear chatbot de soporte técnico
curl -X POST http://localhost:8000/models/create \
  -H "Content-Type: application/json" \
  -d '{
    "model_name": "soporte-tech",
    "base_prompt": "Eres un experto en soporte técnico. Responde de forma clara y precisa.",
    "version": "1.0.0"
  }'
```

### 📊 Comparar Versiones de Modelos

```bash
# Ver qué versión funciona mejor
curl http://localhost:8000/models/mi-modelo/compare

# Respuesta con ranking automático:
{
  "model_name": "mi-modelo",
  "versions": [
    {
      "version": "1.0.2",
      "score": 85.5,
      "rank": 1,
      "metrics": {"accuracy": 0.92, "f1_score": 0.88, "avg_response_time": 1.2}
    }
  ],
  "recommendation": {
    "best_version": "1.0.2",
    "reason": "Mayor accuracy y mejor tiempo de respuesta",
    "confidence": 0.94
  }
}
```

### 🚀 Deploy Inteligente

```bash
# Deploy de la mejor versión automáticamente
curl -X POST http://localhost:8000/models/mi-modelo/deploy \
  -H "Content-Type: application/json" \
  -d '{"auto_select_best": true}'

# O deploy de versión específica
curl -X POST http://localhost:8000/models/mi-modelo/deploy \
  -H "Content-Type: application/json" \
  -d '{"version": "1.0.2", "port": 8080}'
```

## 🧪 Testing

### Ejecutar tests

```bash
# Tests unitarios
python -m pytest tests/unit/ -v

# Tests de integración  
python -m pytest tests/integration/ -v

# Tests de rendimiento
python -m pytest tests/performance/ -v

# Test completo
python tests/test_certificacion_final.py
```

### Scripts de demostración

```bash
# Demo completo del sistema
python scripts/demo_download_system.py

# Test de deployments
python tests/integration/test_deployment_download.py
```

## 📚 Documentación Completa

| Recurso | Descripción |
|---------|-------------|
| [📖 Guía Fácil](docs/GUIA_FACIL.md) | Tutorial paso a paso |
| [🔧 CLI Completa](docs/CLI_COMPLETA.md) | Todos los comandos disponibles |
| [🌐 API Completa](docs/API_COMPLETA.md) | Referencia completa de endpoints |

## 🏗️ Arquitectura

```
AI Factory
├── 🤖 Entrenamiento → Crea modelos personalizados  
├── 📊 Comparación → Rankea versiones automáticamente  
├── 🚀 Despliegue → Deploy con un comando
└── 📈 Monitoreo → Métricas en tiempo real
```

## ⚡ Características avanzadas

### **Threading optimizado**

- Procesamiento paralelo con 4 workers
- Mejora de rendimiento 2.91x verificada
- Testing automatizado de prompts en paralelo

### **Sistema de deployments**

- Generación automática de aplicaciones FastAPI standalone
- Archivos ZIP descargables con todo incluido
- Documentación completa y Docker support

### **Suite de testing**

- Tests unitarios, integración y rendimiento
- Validación exhaustiva con 18 tests críticos
- Reportes detallados de cobertura y métricas

## 🚀 Ejemplo de flujo completo

### **Crear → Entrenar → Deploy → Descargar**

```bash
# 1. Crear modelo
curl -X POST "http://localhost:8000/models/create" \
  -H "Content-Type: application/json" \
  -d '{"model_name": "mi-asistente", "base_prompt": "Eres un asistente especializado", "version": "1.0.0"}'

# 2. Entrenar con ejemplos  
curl -X POST "http://localhost:8000/models/train" \
  -H "Content-Type: application/json" \
  -d '{"model_name": "mi-asistente", "prompts": ["Ejemplo 1", "Ejemplo 2"]}'

# 3. Deploy (genera ZIP automáticamente)
curl -X POST "http://localhost:8000/models/deploy" \
  -H "Content-Type: application/json" \
  -d '{"model_name": "mi-asistente", "version": "1.0.0"}'

# 4. Listar y descargar
curl "http://localhost:8000/models/deployments/list"
curl -o mi-asistente.zip "http://localhost:8000/models/deployments/download/mi-asistente-1.0.0-deployment.zip"
```

## 🔧 Arquitectura técnica

### **Stack tecnológico:**

- **FastAPI** - API REST moderna con Swagger UI
- **Ollama** - Motor local de modelos de IA  
- **Pydantic v2** - Validación robusta de schemas
- **Threading** - Procesamiento paralelo optimizado
- **JSON** - Persistencia simple sin BD externa

### **Flujo interno:**

```
Usuario → FastAPI → Pydantic → Services → Ollama → Response
```

### **Persistencia:**

- `data/models_data.json` - Modelos y metadatos
- `deployments/` - Paquetes generados  
- `exports/` - Exportaciones de usuario

## 🛠️ Desarrollo Local

```bash
# Clonar repositorio
git clone https://github.com/valenuser/ai-factory.git
cd ai-factory

# Instalar dependencias
pip install -e .

# Ejecutar tests
pytest tests/

# Iniciar en modo desarrollo
ai-factory start --dev
```

## 🤝 Contribuir

1. Fork el repositorio
2. Crear rama feature: `git checkout -b feature/nueva-funcionalidad`
3. Hacer cambios y tests: `python tests/test_certificacion_final.py`
4. Commit: `git commit -am 'Agregar nueva funcionalidad'`
5. Push: `git push origin feature/nueva-funcionalidad`
6. Crear Pull Request

## 📄 Licencia

Este proyecto está bajo licencia MIT. Ver `LICENSE` para más detalles.

## 🆘 Soporte

- 📧 Email: soporte@ai-factory.dev
- 💬 Discord: [Únete a la comunidad](https://discord.gg/ai-factory)
- 🐛 Issues: [GitHub Issues](https://github.com/valenuser/ai-factory/issues)

---

<div align="center">

🏭 **AI Factory** - Plataforma local para IA personalizada | Made with ❤️ for developers

**⭐ Si AI Factory te ayuda, ¡dale una estrella en GitHub!**

</div>