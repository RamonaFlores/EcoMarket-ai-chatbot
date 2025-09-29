"""
Configuración principal del chatbot de EcoMarket
Integra todos los prompts desde sus archivos respectivos
"""

import json
from typing import Dict, List, Optional
from datetime import datetime, timedelta
import random

# Importar prompts desde los archivos modulares
from prompts.system import get_system_prompt, combine_prompts
from prompts.order import get_order_prompt, format_order_response
from prompts.returns import (
    get_return_prompt, 
    evaluate_return_eligibility,
    format_return_response
)

class EcoMarketChatbot:
    def __init__(self):
        """Inicializa el chatbot con las bases de datos y configuraciones"""
        self.order_database = self.load_order_database()
        self.product_database = self.load_product_database()
        self.return_policies = self.load_return_policies()
        
        # Cargar system prompt principal
        self.system_prompt = combine_prompts("main", "ethical", "context")
        
    def load_order_database(self) -> List[Dict]:
        """Simula base de datos de pedidos - 10 ejemplos como mínimo"""
        return [
            {
                "tracking_number": "ECO12345",
                "customer_name": "María García",
                "status": "en_transito",
                "order_date": "2024-11-25",
                "estimated_delivery": "2024-11-30",
                "items": ["Botella Reutilizable", "Bolsa Eco"],
                "carrier": "EcoExpress"
            },
            {
                "tracking_number": "ECO12346",
                "customer_name": "Juan Pérez",
                "status": "entregado",
                "order_date": "2024-11-20",
                "delivery_date": "2024-11-23",
                "items": ["Kit Solar Portátil"]
            },
            {
                "tracking_number": "ECO12347",
                "customer_name": "Ana Martínez",
                "status": "procesando",
                "order_date": "2024-11-27",
                "estimated_delivery": "2024-12-02",
                "items": ["Jabón Artesanal", "Shampoo Sólido"]
            },
            {
                "tracking_number": "ECO12348",
                "customer_name": "Carlos López",
                "status": "retrasado",
                "order_date": "2024-11-15",
                "estimated_delivery": "2024-11-28",
                "original_delivery": "2024-11-25",
                "delay_reason": "condiciones climáticas",
                "items": ["Compostador Doméstico"]
            },
            {
                "tracking_number": "ECO12349",
                "customer_name": "Laura Rodríguez",
                "status": "preparando",
                "order_date": "2024-11-28",
                "estimated_delivery": "2024-12-03",
                "items": ["Set Cubiertos Bambú", "Pajitas Reutilizables"]
            },
            {
                "tracking_number": "ECO12350",
                "customer_name": "Pedro Sánchez",
                "status": "en_transito",
                "order_date": "2024-11-24",
                "estimated_delivery": "2024-11-29",
                "items": ["Panel Solar USB"],
                "location": "Centro de distribución regional"
            },
            {
                "tracking_number": "ECO12351",
                "customer_name": "Isabel Fernández",
                "status": "entregado",
                "order_date": "2024-11-18",
                "delivery_date": "2024-11-21",
                "items": ["Cepillo Dental Bambú", "Pasta Dental Natural"]
            },
            {
                "tracking_number": "ECO12352",
                "customer_name": "Miguel Torres",
                "status": "devuelto",
                "order_date": "2024-11-10",
                "return_date": "2024-11-17",
                "return_reason": "producto dañado",
                "refund_status": "procesado"
            },
            {
                "tracking_number": "ECO12353",
                "customer_name": "Carmen Ruiz",
                "status": "en_transito",
                "order_date": "2024-11-26",
                "estimated_delivery": "2024-12-01",
                "items": ["Detergente Eco", "Suavizante Natural"],
                "carrier": "GreenDelivery"
            },
            {
                "tracking_number": "ECO12354",
                "customer_name": "Roberto Díaz",
                "status": "procesando",
                "order_date": "2024-11-28",
                "estimated_delivery": "2024-12-04",
                "items": ["Maceta Biodegradable", "Semillas Orgánicas"],
                "payment_pending": False
            }
        ]
    
    def load_product_database(self) -> List[Dict]:
        """Simula base de datos de productos con políticas de devolución"""
        return [
            {
                "name": "Botella Reutilizable",
                "category": "reutilizable",
                "returnable": True,
                "price": 15.99,
                "eco_points": 50
            },
            {
                "name": "Jabón Artesanal",
                "category": "higiene",
                "returnable": False,
                "reason": "producto de higiene personal",
                "price": 8.99,
                "eco_points": 20
            },
            {
                "name": "Kit Solar Portátil",
                "category": "tecnologia",
                "returnable": True,
                "price": 89.99,
                "eco_points": 200
            },
            {
                "name": "Compostador Doméstico",
                "category": "jardineria",
                "returnable": True,
                "price": 45.99,
                "eco_points": 100
            },
            {
                "name": "Shampoo Sólido",
                "category": "higiene",
                "returnable": False,
                "reason": "producto de higiene personal",
                "price": 12.99,
                "eco_points": 30
            },
            {
                "name": "Frutas Orgánicas",
                "category": "perecedero",
                "returnable": False,
                "reason": "producto perecedero",
                "price": 25.99,
                "eco_points": 15
            },
            {
                "name": "Planta Suculenta",
                "category": "plantas",
                "returnable": False,
                "reason": "ser vivo, no retornable después de 48 horas",
                "price": 18.99,
                "eco_points": 40
            },
            {
                "name": "Taza Personalizada",
                "category": "personalizado",
                "returnable": False,
                "reason": "producto personalizado",
                "price": 22.99,
                "eco_points": 35
            },
            {
                "name": "Panel Solar USB",
                "category": "tecnologia",
                "returnable": True,
                "price": 129.99,
                "eco_points": 300
            },
            {
                "name": "Bolsa Eco",
                "category": "reutilizable",
                "returnable": True,
                "price": 9.99,
                "eco_points": 25
            }
        ]
    
    def load_return_policies(self) -> Dict:
        """Políticas de devolución de la empresa"""
        return {
            "return_window": 30,
            "non_returnable_categories": [
                "higiene",
                "perecedero",
                "plantas",
                "personalizado"
            ],
            "conditions": "producto en estado original, con empaque",
            "refund_timeline": "5-7 días hábiles",
            "warranty_period": 365
        }
    
    def check_order_status(self, tracking_number: str) -> str:
        """
        Consulta estado de pedido usando prompts modulares
        
        Args:
            tracking_number: Número de seguimiento del pedido
            
        Returns:
            Respuesta formateada con el estado del pedido
        """
        # Buscar pedido en la base de datos
        order = None
        for o in self.order_database:
            if o["tracking_number"] == tracking_number:
                order = o
                break
        
        if not order:
            # Usar prompt de pedido no encontrado
            template = get_order_prompt("not_found")
            return template.replace("{tracking_number}", tracking_number)
        
        # Obtener el prompt apropiado según el estado
        status = order["status"]
        template = get_order_prompt(status)
        
        # Formatear y retornar la respuesta
        return format_order_response(order, template)
    
    def process_return(self, product_name: str, purchase_date: str, reason: str) -> str:
        """
        Procesa solicitud de devolución usando prompts modulares
        
        Args:
            product_name: Nombre del producto a devolver
            purchase_date: Fecha de compra (YYYY-MM-DD)
            reason: Motivo de la devolución
            
        Returns:
            Respuesta formateada con el proceso de devolución
        """
        # Buscar producto en la base de datos
        product = None
        for p in self.product_database:
            if p["name"].lower() == product_name.lower():
                product = p
                break
        
        if not product:
            # Producto no encontrado
            template = get_return_prompt("not_found")
            return template.replace("{product_name}", product_name)
        
        # Evaluar elegibilidad
        eligibility = evaluate_return_eligibility(product, purchase_date)
        
        # Obtener prompt apropiado
        template = get_return_prompt(eligibility["status"])
        
        # Formatear y retornar respuesta
        return format_return_response(
            product_name,
            purchase_date,
            reason,
            eligibility,
            template
        )
    
    def generate_response(self, query_type: str, **kwargs) -> str:
        """
        Genera respuesta según tipo de consulta
        
        Args:
            query_type: Tipo de consulta (order_status, return_process, etc.)
            **kwargs: Parámetros específicos de la consulta
            
        Returns:
            Respuesta generada por el chatbot
        """
        if query_type == "order_status":
            return self.check_order_status(kwargs.get("tracking_number", ""))
        elif query_type == "return_process":
            return self.process_return(
                kwargs.get("product_name", ""),
                kwargs.get("purchase_date", ""),
                kwargs.get("reason", "")
            )
        else:
            return "¡Hola! 👋 Soy tu asistente de EcoMarket. ¿En qué puedo ayudarte hoy? 😊"
    
    def log_interaction(self, query_type: str, query: dict, response: str):
        """
        Registra la interacción para análisis y mejora continua
        
        Args:
            query_type: Tipo de consulta
            query: Consulta del usuario
            response: Respuesta generada
        """
        interaction = {
            "timestamp": datetime.now().isoformat(),
            "query_type": query_type,
            "query": query,
            "response_length": len(response),
            "response_preview": response[:100] + "..." if len(response) > 100 else response
        }
        
        # En producción, esto se guardaría en una base de datos
        print(f"[LOG] Interacción registrada: {interaction['query_type']}")
        
    def get_system_context(self) -> str:
        """
        Obtiene el contexto del sistema para el modelo
        
        Returns:
            System prompt combinado con contexto actual
        """
        return self.system_prompt