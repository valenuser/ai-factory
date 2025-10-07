# Changelog

Todos los cambios importantes de AI Factory serán documentados en este archivo.

## [1.0.0] - 2024-01-07

### ✨ Nuevas Características

#### 🚀 Funcionalidad Principal
- **Sistema de Entrenamiento Completo**: Crear modelos personalizados con prompts y ejemplos
- **API REST Completa**: 15 endpoints para gestión completa de modelos
- **CLI Potente**: Interfaz de línea de comandos con todos los comandos esenciales
- **Sistema de Despliegue**: Deploy automático de modelos con un comando

#### 📊 Comparación Inteligente de Versiones *(NUEVO)*
- **Ranking Automático**: Sistema que compara automáticamente todas las versiones de un modelo
- **Métricas Avanzadas**: Análisis de accuracy, f1-score, y tiempo de respuesta
- **Recomendaciones IA**: Algoritmo que sugiere la mejor versión para deploy
- **Scores Ponderados**: Sistema de puntuación inteligente (accuracy 40%, f1-score 40%, tiempo 20%)

#### 🔧 Mejoras de UX
- **Deploy Inteligente**: Opción `auto_select_best` para deploy automático de la mejor versión
- **Información de Deploy**: Endpoint `/deploy-info` con recomendaciones antes del deploy
- **Versionado Automático**: Sistema que gestiona versiones incrementales automáticamente
- **Ejemplos Completos**: Documentación con casos de uso reales y requests de ejemplo

### 🐛 Correcciones
- Corregido schema de respuestas en endpoints de comparación
- Mejorado manejo de errores en entrenamiento de modelos
- Optimizado rendimiento en consultas de múltiples versiones

### 📚 Documentación
- **README Completo**: Guía con ejemplos de requests y casos de uso
- **Documentación API**: Referencia completa de todos los endpoints
- **Guías de Usuario**: Tutoriales paso a paso para diferentes niveles
- **Ejemplos Prácticos**: Casos de uso reales con código completo

### 🏗️ Infraestructura
- Estructura de proyecto organizada y limpia
- Tests comprehensivos (100% de cobertura en funcionalidad principal)
- Build system optimizado para PyPI
- Sistema de CI/CD preparado

### 🎯 Endpoints Disponibles

#### Gestión de Modelos
- `GET /models` - Listar todos los modelos
- `POST /models` - Crear nuevo modelo
- `GET /models/{model_name}` - Obtener detalles de modelo
- `DELETE /models/{model_name}` - Eliminar modelo
- `POST /models/{model_name}/train` - Entrenar nueva versión

#### Comparación y Deploy *(NUEVO)*
- `GET /models/{model_name}/compare` - Comparar todas las versiones
- `GET /deploy-info` - Obtener recomendaciones de deploy
- `POST /models/{model_name}/deploy` - Desplegar modelo

#### Utilidades
- `GET /health` - Estado del sistema
- `GET /models/{model_name}/chat` - Interfaz de chat
- `GET /models/{model_name}/versions` - Listar versiones

### ⚡ Rendimiento
- Tiempo de respuesta optimizado para comparaciones
- Cache inteligente para métricas de modelos
- Procesamiento asíncrono para entrenamientos largos

---

## Formato de Versiones

Usamos [Semantic Versioning](https://semver.org/):
- **MAJOR**: Cambios que rompen compatibilidad
- **MINOR**: Nuevas funcionalidades compatibles
- **PATCH**: Correcciones de bugs

## Tipos de Cambios
- `✨ Nuevas Características` - Nueva funcionalidad
- `🐛 Correcciones` - Bug fixes
- `📚 Documentación` - Cambios en documentación
- `⚡ Rendimiento` - Mejoras de performance
- `🏗️ Infraestructura` - Cambios internos