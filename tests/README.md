# 🧪 AI Factory - Testing Suite

Este directorio contiene la suite completa de pruebas para AI Factory, organizada por categorías.

## 📂 Estructura de tests

### 📋 **tests/unit/** - Tests unitarios
- `test_basic.py` - Tests básicos de funcionalidad core
- `test_prompts.py` - Tests de validación de prompts
- `quick_fix_test.py` - Tests rápidos de fixes
- `quick_download_test.py` - Tests rápidos de descarga

### 🔄 **tests/integration/** - Tests de integración
- `comprehensive_test.py` - **Suite principal** (72 tests, 10 categorías)
- `final_validation.py` - Validación final del sistema
- `integration_fix_test.py` - Tests de integración específicos
- `test_deploy.py` - Tests del sistema de deploy
- `test_deploy_endpoint.py` - Tests de endpoints de deploy
- `test_deployment_download.py` - Tests completos de descarga
- `test_swagger_example.py` - Tests de documentación Swagger

### ⚡ **tests/performance/** - Tests de rendimiento
- `performance_test.py` - **Test principal de performance**
- `test_threading.py` - Tests del sistema de threading
- `test_api_threading.py` - Tests de threading de la API

## 🚀 Cómo ejecutar los tests

### Tests individuales
```bash
# Test básico rápido
python tests/unit/test_basic.py

# Test completo de performance  
python tests/performance/performance_test.py

# Suite completa de integración
python tests/integration/comprehensive_test.py
```

### Tests con pytest
```bash
# Todos los tests unitarios
pytest tests/unit/ -v

# Todos los tests de integración
pytest tests/integration/ -v

# Todos los tests de performance
pytest tests/performance/ -v

# Todo junto
pytest tests/ -v
```

## 📊 Test principal: comprehensive_test.py

El test más importante es `tests/integration/comprehensive_test.py` que incluye:

### 🔍 **10 categorías de testing:**
1. **File Structure** - Validación de estructura de archivos
2. **Imports** - Verificación de dependencias
3. **Schema Validation** - Tests de esquemas Pydantic
4. **Services** - Tests de servicios aislados
5. **API Endpoints** - Tests de endpoints FastAPI
6. **Threading Performance** - Validación de mejoras 2.91x
7. **Deploy System** - Sistema completo de deployment
8. **Error Handling** - Manejo robusto de errores
9. **Integration Complete** - Flujo completo end-to-end
10. **Final Validation** - Validación final del sistema

### 📈 **Métricas reportadas:**
- ✅ **Success Rate**: 100% (72/72 tests)
- ⚡ **Threading Performance**: 2.91x speedup verificado
- 🔧 **Error Handling**: Robusto en todos los escenarios
- 🎯 **Integration**: Flujo completo funcional

## 🎯 Tests por funcionalidad

### **Sistema de Deploy**
- `tests/integration/test_deploy.py`
- `tests/integration/test_deploy_endpoint.py`
- `tests/integration/test_deployment_download.py`

### **Sistema de Threading**
- `tests/performance/test_threading.py`
- `tests/performance/test_api_threading.py`
- `tests/performance/performance_test.py`

### **Validación de Schemas**
- `tests/unit/test_prompts.py`
- Incluido en `comprehensive_test.py`

### **API Endpoints**
- `tests/integration/test_swagger_example.py`
- Incluido en `comprehensive_test.py`

## 🔧 Configuración de tests

### **Prerequisitos para testing:**
- Servidor FastAPI corriendo en puerto 8000
- Ollama instalado y funcionando
- Dependencias instaladas (`pip install -r requirements.txt`)

### **Variables de entorno para tests:**
```bash
# Puerto de la API (opcional)
export API_PORT=8000

# Base URL de tests (opcional) 
export API_BASE_URL=http://localhost:8000
```

## 📋 Checklist de testing

Antes de hacer push/release, ejecutar:

```bash
# 1. Tests unitarios básicos
✅ python tests/unit/test_basic.py

# 2. Tests de performance  
✅ python tests/performance/performance_test.py

# 3. Suite completa de integración
✅ python tests/integration/comprehensive_test.py

# 4. Validación final
✅ python tests/integration/final_validation.py
```

Si todos los tests pasan con **100% success rate**, el sistema está listo.

## 🐛 Debugging tests

### **Tests fallan?**
1. Verificar que Ollama esté corriendo: `ollama --version`
2. Verificar que la API esté disponible: `curl http://localhost:8000/health`
3. Revisar logs en el output del test
4. Ejecutar test individual para debugging

### **Performance tests lentos?**
- Los tests de threading pueden tomar 30-60 segundos
- Es normal para validar mejoras de performance reales
- Usar `quick_*` tests para validaciones rápidas

---

💡 **Tip**: Siempre ejecuta `comprehensive_test.py` antes de releases importantes - es el test más completo y confiable.