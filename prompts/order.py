"""
Prompts especializados para consultas de estado de pedidos
"""

ORDER_STATUS_BASE_PROMPT = """
Contexto: El cliente solicita información sobre el pedido {tracking_number}.

Base de datos de pedidos:
{order_database}

Instrucciones paso a paso:
1. BUSCAR el número de pedido en la base de datos
2. VERIFICAR el estado actual y fechas relevantes
3. CALCULAR tiempo estimado si está en tránsito
4. IDENTIFICAR si hay retrasos o problemas
5. PREPARAR respuesta empática y completa

Formato de respuesta:
- Saludo personalizado usando el nombre del cliente si está disponible
- Estado actual del pedido de forma clara
- Fecha estimada de entrega
- Si hay retraso: disculpa sincera + explicación + compensación si aplica
- Link de rastreo: https://ecomarket.com/track/{tracking_number}
- Cierre amable ofreciendo ayuda adicional

Si el pedido no existe, responde amablemente que no encuentras ese número y 
ofrece verificar el email de confirmación o contactar a soporte especializado.
"""

ORDER_STATUS_IN_TRANSIT = """
¡Hola {customer_name}! 📦 

**Tu pedido {tracking_number} está en camino**

📍 **Estado actual**: En tránsito - {location}
📅 **Fecha estimada de entrega**: {estimated_delivery}
🚚 **Transportista**: {carrier}

**Productos en tu pedido:**
{items_list}

🔗 **Rastrea en tiempo real**: https://ecomarket.com/track/{tracking_number}

💡 **Tip**: Recibirás una notificación cuando el paquete esté por llegar.

¿Necesitas actualizar tu dirección de entrega o tienes alguna pregunta? 😊
"""

ORDER_STATUS_DELAYED = """
Hola {customer_name} 🤗

Lamento informarte que tu pedido {tracking_number} está experimentando un retraso.

⚠️ **Estado**: Retrasado
📅 **Nueva fecha estimada**: {estimated_delivery} (original: {original_delivery})
📝 **Motivo**: {delay_reason}

**Lo que estamos haciendo:**
• Priorizando tu envío
• Monitoreando constantemente
• Coordinando con el transportista

**Como compensación por las molestias:**
🎁 Cupón 15% descuento en tu próxima compra: ECOSORRY15
📧 Te hemos enviado un email con más detalles

¿Prefieres cancelar el pedido para un reembolso completo? Puedo ayudarte con eso.
"""

ORDER_STATUS_DELIVERED = """
¡Excelente {customer_name}! ✅

Tu pedido {tracking_number} fue entregado exitosamente.

📅 **Fecha de entrega**: {delivery_date}
📦 **Productos entregados**:
{items_list}

**¿Todo perfecto?**
⭐ Nos encantaría conocer tu opinión: https://ecomarket.com/review/{tracking_number}

**¿Algún problema?**
Si hay algo que no está bien, tienes 30 días para devoluciones. 
Solo dímelo y te ayudo con el proceso.

Gracias por elegir productos sostenibles 🌱
"""

ORDER_STATUS_PROCESSING = """
¡Hola {customer_name}! 👋

Tu pedido {tracking_number} está siendo preparado con cariño.

⏳ **Estado**: Procesando en nuestro almacén
📅 **Fecha de pedido**: {order_date}
📦 **Envío estimado**: {estimated_delivery}

**¿Qué sigue?**
1. ✅ Pago confirmado
2. 📦 Preparando productos (actual)
3. 🚚 Envío
4. 🏠 Entrega

**Productos que recibirás:**
{items_list}

Te notificaremos apenas tu pedido salga del almacén.

¿Necesitas agregar algo más a tu pedido? Aún estamos a tiempo 😊
"""

ORDER_NOT_FOUND = """
😔 Lo siento, no encuentro ningún pedido con el número {tracking_number}.

Esto puede ocurrir por:
• Error al escribir el número de seguimiento
• El pedido fue realizado con otro email
• El pedido tiene más de 6 meses

**¿Qué puedes hacer?**
1. Verifica el email de confirmación de tu pedido
2. Revisa que el número sea correcto
3. Si el problema persiste, nuestro equipo especializado puede ayudarte

¿Te gustaría que te conecte con un agente humano? 🤝
"""

def get_order_prompt(status: str) -> str:
    """
    Retorna el prompt apropiado según el estado del pedido
    
    Args:
        status: Estado del pedido (in_transit, delayed, delivered, processing, not_found)
    
    Returns:
        Template de prompt correspondiente
    """
    templates = {
        "base": ORDER_STATUS_BASE_PROMPT,
        "in_transit": ORDER_STATUS_IN_TRANSIT,
        "en_transito": ORDER_STATUS_IN_TRANSIT,
        "delayed": ORDER_STATUS_DELAYED,
        "retrasado": ORDER_STATUS_DELAYED,
        "delivered": ORDER_STATUS_DELIVERED,
        "entregado": ORDER_STATUS_DELIVERED,
        "processing": ORDER_STATUS_PROCESSING,
        "procesando": ORDER_STATUS_PROCESSING,
        "not_found": ORDER_NOT_FOUND,
        "preparando": ORDER_STATUS_PROCESSING,
        "devuelto": ORDER_STATUS_DELIVERED  # Simplificado para el ejemplo
    }
    
    return templates.get(status, ORDER_STATUS_BASE_PROMPT)

def format_order_response(order_data: dict, template: str) -> str:
    """
    Formatea la respuesta del pedido con los datos reales
    
    Args:
        order_data: Diccionario con información del pedido
        template: Template de prompt a usar
    
    Returns:
        Respuesta formateada
    """
    # Formatear lista de items
    items_list = "\n".join([f"• {item}" for item in order_data.get('items', [])])
    
    # Reemplazar placeholders
    response = template
    replacements = {
        "{customer_name}": order_data.get('customer_name', '').split()[0],
        "{tracking_number}": order_data.get('tracking_number', ''),
        "{location}": order_data.get('location', 'en camino a tu dirección'),
        "{estimated_delivery}": order_data.get('estimated_delivery', ''),
        "{carrier}": order_data.get('carrier', 'EcoExpress'),
        "{items_list}": items_list,
        "{delivery_date}": order_data.get('delivery_date', ''),
        "{order_date}": order_data.get('order_date', ''),
        "{original_delivery}": order_data.get('original_delivery', ''),
        "{delay_reason}": order_data.get('delay_reason', ''),
    }
    
    for placeholder, value in replacements.items():
        response = response.replace(placeholder, str(value))
    
    return response