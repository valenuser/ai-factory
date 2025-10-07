# 🛠️ AI Factory - Scripts y Utilidades

Este directorio contiene scripts de utilidad, instalación y demostración para AI Factory.

## 📂 Contenido

### 🚀 **Scripts de instalación**
- `install.bat` - Instalación automática para Windows
- `install.sh` - Instalación automática para Linux/Mac

### 🎮 **Scripts de demostración**
- `demo_download_system.py` - **Demostración completa del sistema de descarga**
- `deploy_demo.py` - Demo del sistema de deployment

### 🔧 **Utilidades**
- `generate_modelfile.py` - Generador de Modelfiles para Ollama

## 🎯 Scripts principales

### **📦 demo_download_system.py**
Demostración completa del flujo de descarga:

```bash
python scripts/demo_download_system.py
```

**¿Qué hace?**
1. ✅ Crea un modelo de prueba
2. 📦 Hace deploy (genera ZIP automáticamente)  
3. 📋 Lista deployments disponibles
4. ⬇️ Descarga el archivo ZIP
5. 🔍 Verifica el contenido del ZIP
6. 📚 Muestra instrucciones de uso

**Salida ejemplo:**
```
🚀 AI Factory - Sistema de Descarga de Deployments
============================================================

📋 Creando modelo de demostración: demo-model-1759853455
✅ Modelo creado exitosamente

📦 Haciendo deploy del modelo (generando ZIP)...
✅ Deploy completado!
   📁 Carpeta: ./deployments/demo-model-1759853455-1.0.0
   📦 ZIP: demo-model-1759853455-1.0.0-deployment.zip

⬇️ Descargando ZIP del modelo...
✅ Descarga completada!
   💾 Tamaño: 3087 bytes
   📄 Archivos en ZIP: main.py, Modelfile, requirements.txt, README.md, docker-compose.yml

🎯 ¡Deployment listo para usar!
```

### **🔧 deploy_demo.py**
Demo básico del sistema de deployment:

```bash
python scripts/deploy_demo.py
```

### **📄 generate_modelfile.py**
Utilidad para generar Modelfiles personalizados:

```bash
python scripts/generate_modelfile.py
```

## 🛠️ Scripts de instalación

### **Windows - install.bat**
```batch
@echo off
echo 🏭 AI Factory - Instalación Windows
python -m pip install --upgrade pip
pip install -r requirements.txt
echo ✅ Instalación completa
pause
```

### **Linux/Mac - install.sh**
```bash
#!/bin/bash
echo "🏭 AI Factory - Instalación Linux/Mac"
python3 -m pip install --upgrade pip
pip3 install -r requirements.txt
echo "✅ Instalación completa"
```

## 🎮 Cómo usar los demos

### **Prerequisitos:**
1. **AI Factory corriendo**: `python -m uvicorn api.main:app --port 8000`
2. **Ollama instalado**: `ollama --version`
3. **Dependencias**: ejecutar script de instalación

### **Flujo recomendado:**
```bash
# 1. Instalar dependencias
scripts/install.bat  # Windows
# o
scripts/install.sh   # Linux/Mac

# 2. Iniciar servidor (en terminal separado)
python -m uvicorn api.main:app --reload --port 8000

# 3. Ejecutar demo completo
python scripts/demo_download_system.py
```

## 📋 Casos de uso

### **Para desarrolladores:**
- **Validar instalación**: Usar scripts de instalación
- **Probar funcionalidad**: Ejecutar `demo_download_system.py`
- **Debuggear deployments**: Usar `deploy_demo.py`

### **Para usuarios finales:**
- **Primera instalación**: `install.bat/sh`
- **Validar que funciona**: `demo_download_system.py`
- **Ver ejemplo real**: Revisar output del demo

### **Para testing:**
- **CI/CD**: Incorporar demos en pipeline
- **Validación rápida**: Ejecutar demos antes de releases
- **Documentación**: Usar output de demos como ejemplos

## 🔧 Personalización

### **Modificar demos:**
Los scripts son fácilmente modificables para:
- Cambiar nombres de modelos de prueba
- Ajustar prompts de ejemplo
- Personalizar output y logging
- Agregar validaciones específicas

### **Crear nuevos scripts:**
Estructura recomendada:
```python
#!/usr/bin/env python3
"""
Título del Script
================
Descripción breve
"""

import requests
import json

def main():
    # Verificar API disponible
    try:
        response = requests.get("http://localhost:8000/health")
        if response.status_code != 200:
            print("❌ API no disponible")
            return
    except:
        print("❌ No se puede conectar a la API")
        return
    
    # Tu lógica aquí
    print("🚀 Script funcionando...")

if __name__ == "__main__":
    main()
```

---

💡 **Tip**: Siempre ejecuta `demo_download_system.py` después de cambios importantes - es la mejor validación end-to-end del sistema.