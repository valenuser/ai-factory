# CLI Completa de AI Factory

## Descripción General

AI Factory incluye una interfaz de línea de comandos (CLI) completa que permite gestionar todos los aspectos del sistema sin necesidad de programación.

## Instalación

Una vez instalado AI Factory, los comandos CLI están disponibles globalmente:

```bash
pip install ai-factory
```

## Comandos Disponibles

### `ai-factory check`

Verifica que todas las dependencias estén instaladas correctamente.

```bash
ai-factory check
```

**Salida esperada:**
```
🔍 Checking dependencies...
✅ Ollama detected: ollama version is 0.12.3
📁 Initializing workspace...
✅ Data directory: /path/to/data
✅ Models directory: /path/to/models
🎉 All dependencies are ready!
```

**Opciones:**
- `--verbose, -v`: Muestra información detallada de verificación

### `ai-factory serve`

Inicia el servidor API de AI Factory.

```bash
ai-factory serve
```

**Opciones:**
- `--host HOST`: Dirección IP del servidor (default: 127.0.0.1)
- `--port PORT`: Puerto del servidor (default: 8000)
- `--reload`: Reinicia automáticamente al detectar cambios (desarrollo)

**Ejemplos:**
```bash
# Servidor local básico
ai-factory serve

# Servidor accesible desde red
ai-factory serve --host 0.0.0.0 --port 8080

# Modo desarrollo con auto-reload
ai-factory serve --reload
```

**Salida esperada:**
```
🔍 Checking dependencies...
✅ Ollama detected: ollama version is 0.12.3
📁 Initializing workspace...
✅ Data directory: /path/to/data
✅ Models directory: /path/to/models
🚀 Starting AI Factory Server...
📡 Server available at: http://127.0.0.1:8000
📖 API Documentation: http://127.0.0.1:8000/docs
🛑 To stop: Ctrl+C
```

### `ai-factory info`

Muestra información detallada del sistema y configuración.

```bash
ai-factory info
```

**Salida esperada:**
```
🤖 AI Factory - Información del Sistema
=====================================

📦 Versión: 1.0.0
🐍 Python: 3.11.4
📁 Directorio de datos: /path/to/data
📁 Directorio de modelos: /path/to/models

🔧 Dependencias:
✅ Ollama: 0.12.3
✅ FastAPI: 0.118.0
✅ Uvicorn: 0.37.0

📊 Estado:
- Modelos creados: 5
- Deployments disponibles: 3
- Espacio usado: 1.2 GB
```

**Opciones:**
- `--json`: Muestra la información en formato JSON
- `--system`: Incluye información detallada del sistema operativo

## Flujo de Trabajo Típico

### 1. Verificación Inicial
```bash
ai-factory check
```

### 2. Iniciar Servidor
```bash
ai-factory serve --host 0.0.0.0 --port 8000
```

### 3. Verificar Estado (en otra terminal)
```bash
ai-factory info
```

## Configuración Avanzada

### Variables de Entorno

AI Factory reconoce estas variables de entorno:

```bash
# Directorio de datos personalizado
export AI_FACTORY_DATA_DIR=/mi/directorio/datos

# Directorio de modelos personalizado  
export AI_FACTORY_MODELS_DIR=/mi/directorio/modelos

# Puerto por defecto
export AI_FACTORY_DEFAULT_PORT=8080
```

### Archivos de Configuración

AI Factory puede usar archivos de configuración:

**config.json:**
```json
{
  "data_dir": "/path/to/data",
  "models_dir": "/path/to/models", 
  "default_port": 8000,
  "ollama_timeout": 30
}
```

## Solución de Problemas

### Error: "ai-factory: command not found"

**Solución 1: Verificar instalación**
```bash
pip list | grep ai-factory
```

**Solución 2: Usar módulo Python**
```bash
python -m ai_factory.cli check
python -m ai_factory.cli serve
python -m ai_factory.cli info
```

**Solución 3: Reinstalar**
```bash
pip uninstall ai-factory
pip install ai-factory
```

### Error: "Ollama not found"

```bash
# Verificar instalación de Ollama
ollama --version

# Si no está instalado:
# Windows: Descargar desde https://ollama.ai
# Linux/macOS: curl -fsSL https://ollama.ai/install.sh | sh
```

### Servidor no inicia

**Verificar puerto disponible:**
```bash
ai-factory serve --port 8001
```

**Verificar permisos:**
```bash
sudo ai-factory serve --port 80  # Solo si necesitas puerto 80
```

## Integración con Scripts

### Bash Script Ejemplo
```bash
#!/bin/bash

echo "Iniciando AI Factory..."
ai-factory check || exit 1

echo "Iniciando servidor en background..."
ai-factory serve --host 0.0.0.0 --port 8000 &
SERVER_PID=$!

echo "Servidor iniciado con PID: $SERVER_PID"

# Tu código aquí...

echo "Deteniendo servidor..."
kill $SERVER_PID
```

### Python Script Ejemplo
```python
import subprocess
import time
import sys

def start_ai_factory():
    # Verificar dependencias
    result = subprocess.run(['ai-factory', 'check'], capture_output=True)
    if result.returncode != 0:
        print("❌ Dependencias no disponibles")
        sys.exit(1)
    
    # Iniciar servidor
    server = subprocess.Popen(['ai-factory', 'serve', '--port', '8000'])
    
    # Esperar a que inicie
    time.sleep(5)
    
    return server

if __name__ == "__main__":
    server = start_ai_factory()
    try:
        # Tu código aquí...
        pass
    finally:
        server.terminate()
```

## Comandos de Sistema

### Información Detallada del Sistema
```bash
ai-factory info --system --json > system_info.json
```

### Backup de Configuración
```bash
cp ~/.ai-factory/config.json backup_config.json
```

### Logs del Servidor
```bash
ai-factory serve --port 8000 > server.log 2>&1 &
```

## Actualizaciones

### Verificar Versión Actual
```bash
ai-factory info | grep "Versión"
```

### Actualizar a Última Versión
```bash
pip install --upgrade ai-factory
```

### Verificar Nuevas Funcionalidades
```bash
ai-factory --help
```