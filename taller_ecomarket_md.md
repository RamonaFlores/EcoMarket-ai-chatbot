# Taller Práctico #1: Optimización de Atención al Cliente con IA Generativa

## Caso de Estudio: EcoMarket

**Empresa:** EcoMarket - Comercio electrónico de productos sostenibles  
**Problema:** Alto volumen de consultas (miles diarias) con tiempo de respuesta de 24 horas  
**Objetivo:** Acelerar y mejorar la calidad de respuestas en el servicio al cliente

---

## Fase 1: Selección y Justificación del Modelo de IA

### Modelo Seleccionado

**Large Language Model (LLM) con arquitectura modular basada en prompts**

La solución implementada utiliza un enfoque de prompt engineering estructurado que puede integrarse con cualquier LLM de propósito general (GPT-4, Claude, Llama, etc.), sin requerir fine-tuning especializado.

### Justificación de la Selección

#### 1. Arquitectura Propuesta

La implementación sigue una arquitectura de tres capas:

```
├── System Prompts (Capa de Identidad y Comportamiento)
│   ├── Prompt principal con personalidad y valores
│   ├── Contexto y personalización
│   └── Guías éticas y manejo de errores
│
├── Task-Specific Prompts (Capa de Dominio)
│   ├── Prompts de estado de pedidos
│   └── Prompts de devoluciones
│
└── Data Integration Layer (Capa de Datos)
    ├── Base de datos de pedidos (simulada)
    ├── Catálogo de productos
    └── Políticas de devolución
```

#### 2. Ventajas del Enfoque Seleccionado

**Costo:**
- No requiere entrenamiento ni fine-tuning costoso
- Utiliza modelos pre-entrenados existentes
- Escalamiento económico mediante prompt engineering
- Posibilidad de usar modelos open-source

**Escalabilidad:**
- Sistema modular que permite agregar nuevos tipos de consultas fácilmente
- Separación clara entre lógica de negocio y respuestas
- Fácil actualización de políticas sin reentrenar modelos

**Facilidad de Integración:**
- Integración directa con bases de datos existentes mediante Python
- No requiere infraestructura ML compleja
- Implementación rápida (días vs. meses)
- Compatible con múltiples proveedores de LLM

**Calidad de Respuesta:**
- Prompts especializados por tipo de consulta
- Respuestas empáticas y personalizadas
- Manejo de casos edge mediante prompts específicos
- Control total sobre tono y estilo de comunicación

#### 3. Por qué este modelo y no otro

**vs. Fine-tuned LLM:**
- Menor costo inicial y de mantenimiento
- Mayor flexibilidad para cambios de políticas
- No requiere conjunto de datos de entrenamiento extenso
- Actualizaciones inmediatas sin reentrenamiento

**vs. Sistema de reglas tradicional:**
- Mayor naturalidad en las respuestas
- Capacidad de manejar variaciones en las consultas
- Menor rigidez en la comprensión del lenguaje natural

**vs. Modelo de propósito único:**
- Aprovecha capacidades generales del LLM
- Reduce tiempo de desarrollo
- Facilita mantenimiento y actualizaciones

### Integración con Base de Datos

El sistema implementa:
- Búsqueda directa en bases de datos simuladas (10+ pedidos, 10+ productos)
- Evaluación programática de elegibilidad de devoluciones
- Formateo dinámico de respuestas con datos reales
- Validación de información antes de responder

---

## Fase 2: Evaluación de Fortalezas, Limitaciones y Riesgos Éticos

### Fortalezas

#### Operativas
1. **Reducción del tiempo de respuesta:** De 24 horas a respuesta inmediata para el 80% de consultas repetitivas
2. **Disponibilidad 24/7:** Sin limitaciones de horario ni ubicación geográfica
3. **Consistencia:** Respuestas uniformes que siguen las políticas establecidas
4. **Escalabilidad ilimitada:** Puede manejar miles de consultas simultáneas sin degradación

#### Técnicas
1. **Modularidad:** Sistema de prompts organizado en archivos separados (`system.py`, `order.py`, `returns.py`)
2. **Mantenibilidad:** Fácil actualización de prompts sin afectar el código base
3. **Trazabilidad:** Sistema de logging para análisis y mejora continua
4. **Verificación:** Validación contra base de datos antes de responder

#### Experiencia del Cliente
1. **Personalización:** Uso del nombre del cliente y contexto de compra
2. **Empatía programada:** Diferentes tonos según la situación (retraso, devolución, entrega exitosa)
3. **Claridad:** Respuestas estructuradas con información accionable
4. **Proactividad:** Ofrece alternativas y siguientes pasos

### Limitaciones

#### Limitaciones Técnicas

1. **Dependencia de datos estructurados:**
   - Requiere información precisa en la base de datos
   - Si los datos están desactualizados, las respuestas serán incorrectas
   - No puede "intuir" información faltante

2. **Casos complejos no cubiertos:**
   - El sistema está diseñado para el 80% de consultas repetitivas
   - Casos que requieren juicio humano complejo necesitan escalamiento
   - Situaciones ambiguas pueden generar respuestas inadecuadas

3. **Limitaciones del contexto:**
   - No mantiene memoria entre sesiones (sin implementar)
   - Requiere que el usuario proporcione información completa (número de pedido, nombre del producto)

#### Limitaciones de Empatía

1. **Empatía simulada vs. genuina:**
   - Aunque los prompts incluyen lenguaje empático, el modelo no "siente" realmente
   - En situaciones emocionales intensas (cliente muy molesto), la respuesta puede percibirse como insincera
   - El 20% de casos complejos que requieren conexión humana genuina no son manejables

2. **Contexto emocional limitado:**
   - El sistema no detecta frustración creciente a través de múltiples interacciones
   - No puede ajustar su tono basándose en señales emocionales sutiles

### Riesgos Éticos

#### 1. Alucinaciones

**Riesgo:** El modelo podría generar información falsa sobre pedidos o productos.

**Mitigación implementada:**
- Principio de VERIFICACIÓN en el system prompt: "Siempre valida información en la base de datos antes de responder"
- Búsqueda programática en base de datos antes de formatear respuestas
- Prompt explícito: "No inventes información. Si no sabes algo, admítelo profesionalmente"
- Respuestas predefinidas para casos de "no encontrado"

**Riesgo residual:** 
- Si la base de datos tiene errores, el sistema propagará información incorrecta
- En casos edge no contemplados, el modelo podría especular

#### 2. Sesgo

**Riesgo:** El modelo podría ofrecer un trato preferencial o discriminatorio a ciertos grupos de clientes.

**Mitigación implementada:**
- Guía ética explícita: "Trata a todos los clientes con el mismo respeto. No discrimines por ningún motivo. Aplica políticas consistentemente"
- Prompts estructurados que no permiten desviación de políticas
- Sistema de evaluación programática (ej: elegibilidad de devolución) basado en reglas objetivas

**Riesgo residual:**
- El LLM base podría tener sesgos en su entrenamiento
- Sesgos implícitos en el lenguaje de los prompts (español con referencias culturales específicas)

#### 3. Privacidad de Datos

**Riesgo:** Manejo inadecuado de información sensible del cliente (direcciones, historial de compras, datos de pago).

**Mitigación implementada:**
- Principio de privacidad en guidelines éticos: "Solo accede a información necesaria para la consulta. No compartas datos entre clientes"
- Sistema de búsqueda que requiere identificador específico (número de pedido)
- No se muestra información de pago en las respuestas

**Riesgos pendientes:**
- El código actual no implementa encriptación
- No hay autenticación del cliente antes de mostrar información del pedido
- Logs podrían contener información sensible sin anonimización

**Recomendaciones:**
- Implementar verificación de identidad (código enviado por email, últimos 4 dígitos de tarjeta)
- Enmascarar datos sensibles en logs
- Cumplir con regulaciones de protección de datos (GDPR, CCPA)

#### 4. Impacto Laboral

**Riesgo:** Reemplazo de agentes de servicio al cliente con consecuencias sociales y económicas.

**Filosofía implementada:**
- El sistema está diseñado para **complementar, no reemplazar**
- Enfoque en el 80% de consultas repetitivas para liberar a agentes humanos
- Escalamiento explícito a humanos: "Transfiere a agente humano cuando: Cliente muy molesto, problema técnico complejo, solicitud fuera de políticas"

**Estrategia recomendada:**
- Reasignar agentes humanos al 20% de casos complejos
- Entrenamiento para manejar escalaciones del chatbot
- Transición gradual con transparencia hacia los empleados
- Potencial para crear nuevos roles (supervisión de IA, mejora de prompts)

#### 5. Transparencia

**Riesgo:** Engañar al cliente haciéndole creer que está hablando con un humano.

**Mitigación implementada:**
- Identidad clara: "Eres un asistente virtual de EcoMarket"
- Prompt de transparencia: "Identifícate como asistente de IA si te preguntan"
- Nombre distintivo: "EcoAssist" (no un nombre humano)

**Mejora recomendada:**
- Mensaje inicial explícito: "Hola, soy EcoAssist, tu asistente virtual impulsado por IA"
- Opción visible en todo momento para conectar con un humano

#### 6. Riesgos de Sostenibilidad

**Aspecto único del caso:** EcoMarket tiene valores de sostenibilidad.

**Consideración ética:**
- Uso de LLMs tiene impacto ambiental (consumo energético en inferencia)
- Paradoja: Empresa sostenible usando tecnología con huella de carbono

**Mitigación propuesta:**
- Usar modelos más pequeños y eficientes cuando sea posible
- Proveedores cloud con energía renovable
- Compensación de huella de carbono
- Transparencia con clientes sobre el equilibrio tecnología-sostenibilidad

---

## Fase 3: Aplicación de Ingeniería de Prompts

### Arquitectura del Sistema de Prompts

El sistema implementa una jerarquía de prompts que se combinan para generar respuestas óptimas:

```python
# Estructura de combinación de prompts
system_prompt = combine_prompts("main", "ethical", "context")
task_prompt = get_order_prompt(status)  # o get_return_prompt(eligibility)
response = format_response(data, template)
```

### 1. System Prompts Base

#### Prompt Principal (`MAIN_SYSTEM_PROMPT`)

**Propósito:** Define la identidad, conocimiento base y principios operativos del asistente.

**Componentes clave:**
- **Identidad:** Nombre (EcoAssist), personalidad (amable, profesional), valores (sostenibilidad)
- **Principios Operativos:**
  1. Verificación antes de responder
  2. Precisión (no inventar información)
  3. Empatía contextual
  4. Criterios de escalamiento
  5. Promoción de sostenibilidad
- **Formato de Respuesta:** Estructura de 5 pasos (saludo, confirmación, respuesta, opciones, cierre)

**Ejemplo de instrucción:**
```
PRINCIPIOS OPERATIVOS:
1. VERIFICACIÓN: Siempre valida información en la base de datos antes de responder
2. PRECISIÓN: No inventes información. Si no sabes algo, admítelo profesionalmente
3. EMPATÍA: Reconoce las emociones del cliente y responde apropiadamente
```

#### Prompt Ético (`ETHICAL_GUIDELINES_PROMPT`)

**Propósito:** Garantizar comportamiento ético y responsable.

**Dimensiones cubiertas:**
- Veracidad (nunca inventar información)
- Equidad (trato consistente)
- Privacidad (protección de datos)
- Transparencia (identificación como IA)
- Sostenibilidad (promoción de opciones eco-amigables)

#### Prompt de Manejo de Errores (`ERROR_HANDLING_PROMPT`)

**Propósito:** Respuestas apropiadas cuando algo falla.

**Tipos de error contemplados:**
1. Base de datos no disponible
2. Información inconsistente
3. Error de proceso
4. Límite de capacidad

**Patrón de respuesta:** Mantener calma → No exponer detalles técnicos → Ofrecer alternativa → Registrar para mejora

### 2. Prompts Especializados: Consulta de Pedidos

#### Prompt Base de Pedidos (`ORDER_STATUS_BASE_PROMPT`)

**Estructura instruccional:**
```
1. BUSCAR el número de pedido en la base de datos
2. VERIFICAR el estado actual y fechas relevantes
3. CALCULAR tiempo estimado si está en tránsito
4. IDENTIFICAR si hay retrasos o problemas
5. PREPARAR respuesta empática y completa
```

#### Prompts por Estado

**Pedido en Tránsito (`ORDER_STATUS_IN_TRANSIT`):**
- Saludo personalizado con nombre del cliente
- Estado actual y ubicación
- Fecha estimada de entrega
- Lista de productos
- Link de rastreo
- Tip proactivo (notificación de llegada)

**Ejemplo mejorado:**
```
¡Hola {customer_name}! 📦 

**Tu pedido {tracking_number} está en camino**

🔍 **Estado actual**: En tránsito - {location}
📅 **Fecha estimada de entrega**: {estimated_delivery}
🚚 **Transportista**: {carrier}

**Productos en tu pedido:**
{items_list}

🔗 **Rastrea en tiempo real**: https://ecomarket.com/track/{tracking_number}
```

**Pedido Retrasado (`ORDER_STATUS_DELAYED`):**
- Disculpa sincera
- Explicación del motivo del retraso
- Nueva fecha estimada
- **Compensación:** Cupón de 15% descuento (ECOSORRY15)
- Opción de cancelación

**Diferencia con prompt básico:**
Un prompt básico solo informaría el retraso. El prompt mejorado:
1. Muestra empatía explícita
2. Ofrece compensación proactiva
3. Empodera al cliente con opciones
4. Mantiene transparencia sobre acciones tomadas

### 3. Prompts Especializados: Devoluciones

#### Sistema de Evaluación Programática

La elegibilidad de devolución se evalúa mediante código Python, no solo prompts:

```python
def evaluate_return_eligibility(product_data, purchase_date):
    days_elapsed = calculate_days_elapsed(purchase_date)
    
    if days_elapsed > 30:
        return {"status": "expired", ...}
    
    if not product_data.get("returnable"):
        return {"status": "not_eligible", ...}
    
    return {"status": "eligible", ...}
```

**Ventaja:** Elimina riesgo de alucinaciones en decisiones de negocio críticas.

#### Prompt de Devolución Elegible (`RETURN_ELIGIBLE_PROMPT`)

**Estructura:**
1. Confirmación positiva clara
2. Detalles de la devolución (producto, fecha, motivo)
3. Proceso paso a paso con enlaces
4. Solicitud de feedback (mejora continua)
5. Compensación por las molestias (cupón 10%)

**Ejemplo de instrucciones accionables:**
```
**📦 Proceso súper simple:**

1️⃣ **Genera tu etiqueta** (gratis):
   https://ecomarket.com/return/generate-label
   
2️⃣ **Empaca el producto**:
   • Preferiblemente en su empaque original
   • Si no lo tienes, cualquier caja sirve
```

#### Prompt de Devolución No Elegible (`RETURN_NOT_ELIGIBLE_PROMPT`)

**Desafío:** Dar una negativa sin frustrar al cliente.

**Estrategia del prompt:**
1. Empatía ("Entiendo tu situación")
2. Explicación clara de la política
3. **Tres alternativas** en lugar de solo decir "no":
   - Activación de garantía si hay defecto
   - Crédito del 50% para futura compra
   - Conexión con especialista

**Diferencia crítica:**
- Prompt básico: "Este producto no es retornable por política de la empresa"
- Prompt mejorado: "Lamentablemente no es retornable debido a [razón específica], sin embargo puedo ofrecerte estas alternativas..."

### 4. Características Avanzadas de los Prompts

#### Personalización Dinámica

El sistema usa placeholders que se reemplazan con datos reales:

```python
replacements = {
    "{customer_name}": order_data.get('customer_name').split()[0],  # Solo primer nombre
    "{tracking_number}": order_data.get('tracking_number'),
    "{items_list}": "\n".join([f"• {item}" for item in items]),
    "{delay_reason}": order_data.get('delay_reason'),
}
```

#### Formateo Consistente

Todos los prompts siguen convenciones visuales:
- Emojis para categorización visual (📦 pedidos, ↩️ devoluciones, ✅ éxito)
- Negritas para información crítica
- Bullets para listas
- Secciones claramente delimitadas

#### Manejo de Casos Edge

**Pedido no encontrado:**
```python
ORDER_NOT_FOUND = """
😞 Lo siento, no encuentro ningún pedido con el número {tracking_number}.

Esto puede ocurrir por:
• Error al escribir el número de seguimiento
• El pedido fue realizado con otro email
• El pedido tiene más de 6 meses

**¿Qué puedes hacer?**
1. Verifica el email de confirmación
2. Revisa que el número sea correcto
3. Si el problema persiste, conecta con un agente humano
```

**Características:**
- No culpa al cliente ("error al escribir" vs "escribiste mal")
- Ofrece múltiples explicaciones posibles
- Proporciona pasos de solución
- Escalamiento suave a humano

### 5. Evaluación de Efectividad de Prompts

#### Prompts Básicos vs. Mejorados

| Aspecto | Prompt Básico | Prompt Mejorado Implementado |
|---------|---------------|------------------------------|
| Tono | Transaccional | Empático y conversacional |
| Información | Estado del pedido | Estado + contexto + siguiente paso |
| Personalización | Genérica | Nombre del cliente, detalles específicos |
| Accionabilidad | "Tu pedido está en camino" | Link de rastreo + tip proactivo |
| Manejo de problemas | Solo informa | Disculpa + explicación + compensación |

#### Métricas de Calidad Implementadas

El sistema incluye logging para mejora continua:

```python
def log_interaction(self, query_type, query, response):
    interaction = {
        "timestamp": datetime.now().isoformat(),
        "query_type": query_type,
        "response_length": len(response),
        "response_preview": response[:100]
    }
```

**Métricas que se pueden analizar:**
- Tipos de consultas más frecuentes
- Longitud de respuestas por categoría
- Casos que requieren escalamiento
- Patrones de interacción

### 6. Principios de Ingeniería de Prompts Aplicados

#### Claridad y Especificidad
```python
# ❌ Prompt vago
"Dame información del pedido"

# ✅ Prompt específico implementado
"Actúa como un agente de servicio al cliente amable. Proporciona el estado 
actual del pedido con el número de seguimiento '{{tracking_number}}'. 
Incluye una estimación de la fecha de entrega y un enlace para rastrear 
el paquete en tiempo real."
```

#### Definición de Rol
```python
IDENTIDAD:
- Nombre: EcoAssist
- Personalidad: Amable, profesional, empático y conocedor
- Valores: Sostenibilidad, transparencia, servicio excepcional
```

#### Provisión de Contexto
```python
CONTEXT_ENRICHMENT_PROMPT = """
Antes de responder, analiza el contexto del cliente:
- Historial de compras previas
- Interacciones anteriores
- Sentimiento actual (positivo/neutro/negativo)
- Urgencia de la solicitud
```

#### Instrucciones Paso a Paso
```python
Instrucciones paso a paso:
1. BUSCAR el número de pedido en la base de datos
2. VERIFICAR el estado actual y fechas relevantes
3. CALCULAR tiempo estimado si está en tránsito
4. IDENTIFICAR si hay retrasos o problemas
5. PREPARAR respuesta empática y completa
```

#### Ejemplos y Contraejemplos
```python
FORMATO DE RESPUESTA:
1. Saludo personalizado (si aplica)
2. Confirmación de entendimiento
3. Respuesta principal con información verificada
4. Opciones adicionales o siguientes pasos
5. Cierre amable con oferta de ayuda adicional
```

#### Restricciones y Limitaciones
```python
LIMITACIONES:
- No compartas información de otros clientes
- No modifiques precios o políticas establecidas
- No hagas promesas que no puedas cumplir
- No discutas temas fuera del ámbito de EcoMarket
```

---

## Conclusiones

### Logros de la Implementación

1. **Sistema modular escalable:** Fácil agregar nuevos tipos de consultas
2. **Balance entre automatización y humanización:** 80% automatizado, 20% escalado a humanos
3. **Enfoque ético proactivo:** Consideraciones de privacidad, transparencia y equidad desde el diseño
4. **Ingeniería de prompts estructurada:** Jerarquía clara de prompts reutilizables
5. **Verificación programática:** Decisiones críticas (elegibilidad de devolución) en código, no en prompts

### Áreas de Mejora Futura

1. **Seguridad:** Implementar autenticación antes de mostrar información del pedido
2. **Memoria conversacional:** Sistema para recordar contexto entre sesiones
3. **Análisis de sentimiento:** Detectar frustración del cliente y ajustar tono
4. **Testing automatizado:** Suite de pruebas para validar respuestas
5. **Métricas de satisfacción:** Integrar feedback del cliente post-interacción

### Impacto Esperado

- **Tiempo de respuesta:** De 24 horas a <1 minuto para el 80% de consultas
- **Costo operativo:** Reducción del 60-70% en costos de soporte para consultas repetitivas
- **Satisfacción del cliente:** Mejora esperada del 30-40% por disponibilidad 24/7
- **Capacidad de agentes humanos:** Liberados para enfocarse en casos complejos de mayor valor

---

## Repositorio

**Estructura de archivos:**
```
EcoMarket-ai-chatbot/
├── prompts/
│   ├── system.py      # System prompts base
│   ├── order.py       # Prompts de pedidos
│   └── returns.py     # Prompts de devoluciones
├── config.py          # Configuración y lógica principal
└── main.py           # Interfaz de línea de comandos
```

**Ejecutar el sistema:**
```bash
python main.py
```

**Consultas de prueba incluidas:**
- Pedidos: ECO12345, ECO12348, ECO12350, ECO12354
- Productos retornables: Botella Reutilizable, Kit Solar Portátil
- Productos no retornables: Jabón Artesanal, Frutas Orgánicas
