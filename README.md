# EcoMarket AI Customer Service Solution

## 📋 Descripción
Solución de IA Generativa para optimizar el servicio de atención al cliente de EcoMarket, 
una empresa de e-commerce especializada en productos sostenibles. El sistema utiliza un 
enfoque modular con prompts especializados para manejar consultas de pedidos y devoluciones.

## 🎯 Objetivo
Reducir el tiempo de respuesta de 24 horas a segundos, manejando automáticamente el 80% 
de consultas repetitivas mientras mantiene calidad y empatía en las respuestas.

## 🏗️ Arquitectura

### Sistema Modular de Prompts
- **System Prompts**: Definición de comportamiento base del asistente
- **Order Prompts**: Manejo especializado de consultas de pedidos
- **Return Prompts**: Procesamiento de solicitudes de devolución
- **Base de Datos**: Simulación de datos de pedidos y productos
- **Clasificador**: Categorización inteligente de consultas

### Componentes Principales
- **EcoMarketChatbot**: Clase principal que orquesta todas las funcionalidades
- **Base de Datos Simulada**: 10+ pedidos de ejemplo y catálogo de productos
- **Sistema de Validación**: Verificación de elegibilidad para devoluciones
- **Logging**: Registro de interacciones para análisis

## 🚀 Características

### ✅ Funcionalidades Implementadas
- ✅ Consulta de estado de pedidos en tiempo real
- ✅ Procesamiento de solicitudes de devolución
- ✅ Validación de políticas de devolución (30 días)
- ✅ Categorización de productos (retornables/no retornables)
- ✅ Respuestas contextuales y empáticas
- ✅ Sistema de logging de interacciones
- ✅ Interfaz de línea de comandos interactiva

### 📦 Tipos de Consultas Soportadas
1. **Estado de Pedidos**
   - Pedidos en tránsito, entregados, procesando
   - Manejo de retrasos y excepciones
   - Información de seguimiento y entrega

2. **Procesos de Devolución**
   - Evaluación de elegibilidad automática
   - Políticas por categoría de producto
   - Procesamiento de reembolsos

### ⚠️ Limitaciones Actuales
- Base de datos simulada (no conectada a sistemas reales)
- Interfaz solo de línea de comandos
- Sin integración con APIs de pago o envío
- Requiere supervisión humana para casos complejos

### 🛡️ Mitigación de Riesgos Éticos
- **Anti-alucinación**: Validación con base de datos simulada
- **Transparencia**: Respuestas claras sobre limitaciones
- **Escalamiento**: Identificación de casos que requieren intervención humana
- **Privacidad**: Manejo responsable de datos de clientes

## 📁 Estructura del Proyecto

```
EcoMarket-ai-chatbot/
├── main.py                 # Punto de entrada principal
├── config.py              # Configuración y lógica del chatbot
├── requirements.txt       # Dependencias del proyecto
├── prompts/              # Sistema modular de prompts
│   ├── system.py         # Prompts base del sistema
│   ├── order.py          # Prompts para consultas de pedidos
│   └── returns.py        # Prompts para procesos de devolución
└── README.md             # Documentación del proyecto
```

## 💻 Instalación y Uso

### Prerrequisitos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Instalación
```bash
# Clonar repositorio
git clone https://github.com/tuusuario/ecomarket-ai-chatbot.git
cd ecomarket-ai-chatbot

# Instalar dependencias
pip install -r requirements.txt
```

### Ejecución
```bash
# Ejecutar el chatbot
python main.py
```

### Ejemplos de Uso

#### Consulta de Pedido
```
Números de ejemplo disponibles:
- ECO12345 (en tránsito)
- ECO12348 (retrasado)
- ECO12350 (en tránsito)
- ECO12354 (procesando)
```

#### Solicitud de Devolución
```
Productos de ejemplo:
• Retornables: Botella Reutilizable, Kit Solar Portátil, Panel Solar USB
• No retornables: Jabón Artesanal, Shampoo Sólido, Frutas Orgánicas
```

## 🔧 Configuración

### Base de Datos de Pedidos
El sistema incluye 10 pedidos de ejemplo con diferentes estados:
- **En tránsito**: ECO12345, ECO12350, ECO12353
- **Entregado**: ECO12346, ECO12351
- **Procesando**: ECO12347, ECO12354
- **Retrasado**: ECO12348
- **Preparando**: ECO12349
- **Devuelto**: ECO12352

### Catálogo de Productos
Incluye productos con diferentes políticas de devolución:
- **Retornables**: Tecnología, reutilizables, jardinería
- **No retornables**: Higiene personal, perecederos, plantas, personalizados

## 🚀 Próximas Mejoras

### Funcionalidades Planificadas
- [ ] Integración con APIs reales de e-commerce
- [ ] Interfaz web con FastAPI
- [ ] Base de datos persistente (PostgreSQL)
- [ ] Sistema de autenticación de clientes
- [ ] Integración con sistemas de pago
- [ ] Dashboard de métricas y analytics
- [ ] Soporte multiidioma
- [ ] Integración con WhatsApp/Telegram

### Mejoras Técnicas
- [ ] Tests automatizados
- [ ] CI/CD pipeline
- [ ] Docker containerization
- [ ] Monitoreo con Prometheus
- [ ] Logging estructurado
- [ ] Rate limiting y seguridad

## 📊 Métricas de Éxito

### Objetivos Actuales
- ⏱️ Tiempo de respuesta: < 2 segundos
- 🎯 Precisión en consultas: > 95%
- 😊 Satisfacción del cliente: > 4.5/5
- 🔄 Reducción de escalamiento: 80%

## 🤝 Contribución

### Cómo Contribuir
1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -am 'Agrega nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

### Estándares de Código
- Usar Black para formateo de código
- Seguir PEP 8 para estilo de Python
- Documentar funciones y clases
- Incluir tests para nuevas funcionalidades

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 📞 Soporte

Para soporte técnico o consultas sobre el proyecto:
- 📧 Email: soporte@ecomarket.com
- 💬 Issues: [GitHub Issues](https://github.com/tuusuario/ecomarket-ai-chatbot/issues)
- 📖 Documentación: [Wiki del Proyecto](https://github.com/tuusuario/ecomarket-ai-chatbot/wiki)