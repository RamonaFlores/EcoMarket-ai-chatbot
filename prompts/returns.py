"""
Prompts especializados para procesos de devolución
"""

RETURN_PROCESS_BASE_PROMPT = """
Cliente solicita devolución de: {product_name}
Fecha de compra: {purchase_date}
Motivo: {return_reason}

Base de políticas de devolución:
{return_policies_db}

Categorías NO retornables:
- Productos perecederos
- Artículos de higiene personal abiertos
- Productos personalizados
- Plantas vivas después de 48 horas

Proceso de evaluación:
1. VERIFICAR categoría del producto
2. VALIDAR tiempo desde la compra (máximo 30 días)
3. CONFIRMAR estado del producto
4. DETERMINAR elegibilidad

Si ES ELEGIBLE para devolución:
"¡Por supuesto! Entiendo que deseas devolver {product_name}. 
Te ayudaré con el proceso:

1. **Genera tu etiqueta de devolución**: [Link personalizado]
2. **Empaca el producto**: En su empaque original si es posible
3. **Envía dentro de 7 días**: Puedes dejarlo en cualquier punto de entrega
4. **Reembolso en 5-7 días hábiles** después de recibir el producto

¿El motivo de tu devolución es {return_reason}? Esto nos ayuda a mejorar.
¿Necesitas ayuda con algo más del proceso?"

Si NO ES ELEGIBLE:
"Entiendo tu situación con {product_name}. Lamentablemente, este producto 
pertenece a la categoría de {category}, la cual no es elegible para devolución 
según nuestras políticas debido a {specific_reason}.

Sin embargo, me gustaría ayudarte:
- Si el producto está defectuoso, podemos gestionar una garantía
- Si no cumple expectativas, podemos ofrecer crédito para futura compra
- Puedo conectarte con un especialista para explorar otras opciones

¿Qué alternativa prefieres?"
"""

RETURN_ELIGIBLE_PROMPT = """
¡Perfecto! ✅ Tu devolución de **{product_name}** es elegible.

📋 **Detalles de tu devolución:**
• Producto: {product_name}
• Comprado: {purchase_date} ({days_elapsed} días atrás)
• Motivo: {return_reason}
• Ventana de devolución: ✓ Dentro de 30 días

**📦 Proceso súper simple:**

1️⃣ **Genera tu etiqueta** (gratis):
   https://ecomarket.com/return/generate-label
   
2️⃣ **Empaca el producto**:
   • Preferiblemente en su empaque original
   • Si no lo tienes, cualquier caja sirve
   
3️⃣ **Entrega en punto autorizado**:
   • +500 puntos de entrega disponibles
   • Localiza el más cercano: https://ecomarket.com/puntos
   
4️⃣ **Recibe tu reembolso**:
   • 5-7 días hábiles tras recibir el producto
   • Notificación por email en cada paso

**💡 Feedback valioso:**
Tu opinión sobre "{return_reason}" nos ayuda a mejorar. 
¿Podrías compartir más detalles? (opcional)

**🎁 Por las molestias:**
Cupón 10% próxima compra: ECORETURN10

¿Necesitas ayuda con el empaque o tienes alguna pregunta sobre el proceso? 😊
"""

RETURN_NOT_ELIGIBLE_PROMPT = """
Entiendo tu situación con **{product_name}** 💚

Lamentablemente, este producto pertenece a la categoría **{category}**, 
la cual no es elegible para devolución debido a: **{specific_reason}**.

**Sin embargo, puedo ofrecerte estas alternativas:**

🔄 **Si el producto está defectuoso:**
   • Activamos garantía inmediata
   • Reemplazo sin costo
   
💳 **Si no cumple expectativas:**
   • Crédito del 50% para próxima compra
   • Descuento especial en productos similares
   
🤝 **Atención personalizada:**
   • Conectarte con especialista de producto
   • Sesión de asesoría sobre uso óptimo

¿Cuál opción prefieres? También puedo explicarte más sobre cada alternativa.

Tu satisfacción es nuestra prioridad 🌟
"""

RETURN_EXPIRED_WINDOW_PROMPT = """
😔 Lo siento, han pasado {days_elapsed} días desde tu compra de **{product_name}**.

Nuestra política de devolución es de **30 días**, y tu compra fue el {purchase_date}.

**Pero aún puedo ayudarte:**

📞 **Casos especiales**: 
   Si hay un defecto de fábrica, la garantía puede aplicar hasta 1 año
   
🎁 **Programa de lealtad**:
   Como cliente valioso, puedo ofrecer 25% descuento en tu próxima compra
   
♻️ **Programa de reciclaje**:
   Recibe crédito devolviendo productos para reciclaje

¿Te gustaría explorar alguna de estas opciones?
"""

PRODUCT_NOT_FOUND_PROMPT = """
🤔 No encuentro "{product_name}" en nuestro catálogo.

¿Quizás te refieres a alguno de estos?
• Botella Reutilizable
• Kit Solar Portátil
• Jabón Artesanal

Por favor, verifica el nombre exacto en tu recibo de compra.
"""

# Diccionario de categorías y razones de no devolución
NON_RETURNABLE_REASONS = {
    "higiene": "productos de higiene personal por razones sanitarias",
    "perecedero": "productos perecederos por su naturaleza",
    "plantas": "ser vivo, no retornable después de 48 horas",
    "personalizado": "producto personalizado hecho a medida"
}

def get_return_prompt(eligibility_status: str) -> str:
    """
    Retorna el prompt apropiado según la elegibilidad de devolución
    
    Args:
        eligibility_status: Estado de elegibilidad (eligible, not_eligible, expired, not_found)
    
    Returns:
        Template de prompt correspondiente
    """
    templates = {
        "base": RETURN_PROCESS_BASE_PROMPT,
        "eligible": RETURN_ELIGIBLE_PROMPT,
        "not_eligible": RETURN_NOT_ELIGIBLE_PROMPT,
        "expired": RETURN_EXPIRED_WINDOW_PROMPT,
        "not_found": PRODUCT_NOT_FOUND_PROMPT
    }
    
    return templates.get(eligibility_status, RETURN_PROCESS_BASE_PROMPT)

def calculate_days_elapsed(purchase_date: str, current_date: str = "2024-11-28") -> int:
    """
    Calcula días transcurridos desde la compra
    
    Args:
        purchase_date: Fecha de compra (YYYY-MM-DD)
        current_date: Fecha actual para cálculo
    
    Returns:
        Número de días transcurridos
    """
    from datetime import datetime
    
    purchase = datetime.strptime(purchase_date, "%Y-%m-%d")
    current = datetime.strptime(current_date, "%Y-%m-%d")
    
    return (current - purchase).days

def evaluate_return_eligibility(product_data: dict, purchase_date: str) -> dict:
    """
    Evalúa la elegibilidad de devolución de un producto
    
    Args:
        product_data: Información del producto
        purchase_date: Fecha de compra
    
    Returns:
        Diccionario con estado de elegibilidad y detalles
    """
    days_elapsed = calculate_days_elapsed(purchase_date)
    
    # Verificar ventana de tiempo
    if days_elapsed > 30:
        return {
            "status": "expired",
            "days_elapsed": days_elapsed,
            "message": "Fuera del período de devolución de 30 días"
        }
    
    # Verificar si es retornable
    if not product_data.get("returnable", True):
        category = product_data.get("category", "desconocida")
        return {
            "status": "not_eligible",
            "category": category,
            "reason": NON_RETURNABLE_REASONS.get(category, "políticas de la empresa"),
            "days_elapsed": days_elapsed
        }
    
    # Producto elegible
    return {
        "status": "eligible",
        "days_elapsed": days_elapsed,
        "message": "Elegible para devolución"
    }

def format_return_response(
    product_name: str,
    purchase_date: str,
    return_reason: str,
    eligibility: dict,
    template: str
) -> str:
    """
    Formatea la respuesta de devolución con los datos reales
    
    Args:
        product_name: Nombre del producto
        purchase_date: Fecha de compra
        return_reason: Motivo de devolución
        eligibility: Resultado de evaluación de elegibilidad
        template: Template de prompt a usar
    
    Returns:
        Respuesta formateada
    """
    response = template
    
    replacements = {
        "{product_name}": product_name,
        "{purchase_date}": purchase_date,
        "{return_reason}": return_reason,
        "{days_elapsed}": str(eligibility.get("days_elapsed", 0)),
        "{category}": eligibility.get("category", ""),
        "{specific_reason}": eligibility.get("reason", "")
    }
    
    for placeholder, value in replacements.items():
        response = response.replace(placeholder, str(value))
    
    return response