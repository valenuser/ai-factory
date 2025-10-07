# 🏭 AI Factory - Guía Fácil para Usuarios

> **¡Crea tus propios modelos de IA en 5 minutos!** 🚀  
> Sin conocimientos técnicos complicados

---

## 🤔 ¿Qué es AI Factory?

**AI Factory** te permite crear tus propios asistentes de IA personalizados, como ChatGPT pero adaptados a lo que TÚ necesites.

**Por ejemplo, puedes crear:**
- 📝 Un asistente para escribir emails profesionales
- 🍳 Un chef virtual que te da recetas con lo que tienes en casa  
- 📚 Un tutor para explicar cualquier tema
- 💼 Un asistente para tu negocio específico

---

## 🎯 ¿Para quién es esto?

✅ **Perfecto si eres:**
- Emprendedor que quiere automatizar tareas
- Estudiante que necesita ayuda personalizada
- Profesional que quiere un asistente específico
- Curioso que quiere experimentar con IA

❌ **NO necesitas ser:**
- Programador experto
- Científico de datos
- Tener conocimientos de IA avanzados

---

## ⚡ Instalación Super Fácil

### Opción 1: Instalar desde Internet (MÁS FÁCIL)
```bash
pip install ai-factory
ai-factory serve
```
**¡Listo!** Abre tu navegador en: `http://localhost:8000`

### Opción 2: Desde código fuente
1. **Descargar:** Descarga este proyecto
2. **Doble clic:** Ejecuta `scripts/install.bat` (Windows) o `install.sh` (Mac/Linux)
3. **¡Funciona!** Se abre automáticamente en tu navegador

---

## 🎮 Cómo Usar (Paso a Paso)

### 🟢 **Paso 1: Abre la Interfaz Web**
1. Ejecuta el programa
2. Ve a: `http://localhost:8000/docs`
3. Verás una pantalla como esta:

```
🏭 AI Factory API
📖 Documentación interactiva
🔗 Endpoints disponibles:
  ✅ POST /models/create    - Crear modelo
  ✅ POST /models/train     - Entrenar modelo  
  ✅ POST /models/deploy    - Desplegar modelo
  ✅ GET  /models/          - Ver todos los modelos
```

### 🟡 **Paso 2: Crear Tu Primer Modelo**

**Ejemplo: Asistente de Cocina**

1. **Hacer clic en:** `POST /models/create`
2. **Llenar el formulario:**
```json
{
  "model_name": "chef-personal",
  "base_model": "llama3.2:1b",
  "system_prompt": "Eres un chef experto que ayuda a crear recetas deliciosas con ingredientes simples. Siempre das instrucciones claras paso a paso.",
  "temperature": 0.7,
  "max_tokens": 500,
  "training_data": [
    {
      "input": "¿Qué puedo hacer con huevos, leche y harina?",
      "output": "¡Perfecto! Con esos ingredientes puedes hacer panqueques deliciosos..."
    }
  ]
}
```

3. **Hacer clic en:** `Execute`
4. **¡Tu modelo se está creando!**

### 🔵 **Paso 3: Probar Tu Modelo**

1. **Hacer clic en:** `GET /models/`
2. **Ver tu modelo:** Aparecerá "chef-personal" en la lista
3. **¡Ya puedes usarlo!**

### 🟣 **Paso 4: Descargar Tu Modelo**

1. **Hacer clic en:** `POST /models/deploy`
2. **Poner:** `chef-personal`
3. **Descargar:** Ve a `/models/deployments/list`
4. **¡Tienes un ZIP con tu IA completa!**

---

## 📱 Ejemplos Listos para Usar

### 🍳 **Asistente de Cocina**
```json
{
  "model_name": "chef-personal", 
  "system_prompt": "Eres un chef que crea recetas con ingredientes simples",
  "training_data": [
    {"input": "tengo pollo y arroz", "output": "Te sugiero un delicioso arroz con pollo..."}
  ]
}
```

### 📧 **Escritor de Emails**
```json
{
  "model_name": "email-profesional",
  "system_prompt": "Escribes emails profesionales y educados",
  "training_data": [
    {"input": "email para pedir aumento", "output": "Estimado/a [Nombre], espero se encuentre bien..."}
  ]
}
```

### 🎓 **Tutor Personal**
```json
{
  "model_name": "tutor-matematicas",
  "system_prompt": "Explicas matemáticas de forma simple y clara",
  "training_data": [
    {"input": "¿qué es una ecuación?", "output": "Una ecuación es como una balanza..."}
  ]
}
```

---

## ❓ Preguntas Frecuentes

### **¿Es gratis?**
✅ **SÍ, completamente gratis y de código abierto**

### **¿Necesito internet?**
✅ **NO, funciona 100% en tu computadora (después de instalarlo)**

### **¿Es seguro?**
✅ **SÍ, tus datos nunca salen de tu computadora**

### **¿Puedo crear modelos comerciales?**
✅ **SÍ, licencia MIT permite uso comercial**

### **¿Funciona en Windows/Mac/Linux?**
✅ **SÍ, en todos los sistemas operativos**

---

## � Comparar Versiones de tu Modelo

### **¿Tienes múltiples versiones y no sabes cuál usar?**

Cuando entrenas un modelo varias veces o agregas más prompts, AI Factory crea **versiones diferentes**. ¿Cómo saber cuál es la mejor?

### **🔍 Comparar Automáticamente**

**1. Ver comparación de todas las versiones:**
```bash
# En tu navegador, ve a:
GET /models/tu-modelo/compare
```

**2. Ver recomendación para deployment:**
```bash
# Antes de deployar, consulta:
GET /models/tu-modelo/deploy-info  
```

### **📊 Lo que verás:**

**Métricas lado a lado:**
- ✅ **Accuracy:** Qué tan preciso es
- ✅ **F1-Score:** Calidad general  
- ✅ **Tiempo respuesta:** Qué tan rápido responde

**Recomendación automática:**
- 🥇 **Mejor versión** para usar
- 💡 **Razón** por qué es la mejor
- 🎯 **Nivel de confianza** (0-100%)
- 🚀 **Recomendación de deployment**

### **🤖 Ejemplo Práctico:**

```json
{
  "recommendation": {
    "best_version": "1.0.1",
    "reason": "Mejor accuracy (95%) y tiempo rápido (2.1s)",
    "confidence": 92,
    "deploy_recommendation": "Altamente recomendado para producción"
  }
}
```

### **💡 Consejo Pro:**
**Siempre usa `/deploy-info` antes de hacer deployment.** Te ahorrará dolores de cabeza eligiendo la versión correcta.

---

## �🆘 Ayuda Rápida

### **Si algo no funciona:**

1. **Problema:** No se instala
   - **Solución:** Verifica que tienes Python 3.8+
   - **Comando:** `python --version`

2. **Problema:** No abre el navegador
   - **Solución:** Abre manualmente: `http://localhost:8000/docs`

3. **Problema:** Error al crear modelo
   - **Solución:** Verifica que Ollama esté instalado: `ollama --version`

### **Necesitas más ayuda:**
- 📧 Contactar: [email del desarrollador]
- 🐛 Reportar bug: [GitHub issues]
- 💬 Comunidad: [Discord/Telegram]

---

## 🎉 ¡Listo para Empezar!

**En resumen:**
1. `pip install ai-factory` ← Instalar
2. `ai-factory serve` ← Ejecutar  
3. Ir a `localhost:8000/docs` ← Usar
4. ¡Crear tu primer IA personalizada! 🤖

---

**¿Te gusta AI Factory?** ⭐ Deja una estrella en GitHub y compártelo con tus amigos!

**¡Ahora tienes tu propia fábrica de IA!** 🏭✨