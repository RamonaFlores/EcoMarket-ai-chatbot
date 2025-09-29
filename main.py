from config import EcoMarketChatbot
def main():
    chatbot = EcoMarketChatbot()
    
    print("="*60)
    print("🌱 ECOMARKET - Sistema de Atención al Cliente con IA")
    print("="*60)
    print()
    
    while True:
        print("\n¿Qué deseas probar?")
        print("1. Consultar estado de pedido")
        print("2. Solicitar devolución")
        print("3. Salir")
        
        choice = input("\nOpción: ").strip()
        
        if choice == "1":
            print("\n📦 CONSULTA DE PEDIDO")
            print("-"*40)
            print("Números de ejemplo: ECO12345, ECO12348, ECO12350, ECO12354")
            tracking = input("Número de seguimiento: ").strip()
            
            print("\n🤖 Respuesta del Chatbot:")
            print("-"*40)
            response = chatbot.generate_response(
                "order_status", 
                tracking_number=tracking
            )
            print(response)
            
        elif choice == "2":
            print("\n↩️ PROCESO DE DEVOLUCIÓN")
            print("-"*40)
            print("Productos de ejemplo:")
            print("• Retornables: Botella Reutilizable, Kit Solar Portátil, Panel Solar USB")
            print("• No retornables: Jabón Artesanal, Shampoo Sólido, Frutas Orgánicas")
            
            product = input("\nNombre del producto: ").strip()
            date = input("Fecha de compra (YYYY-MM-DD): ").strip()
            reason = input("Motivo de devolución: ").strip()
            
            print("\n🤖 Respuesta del Chatbot:")
            print("-"*40)
            response = chatbot.generate_response(
                "return_process",
                product_name=product,
                purchase_date=date,
                reason=reason
            )
            print(response)
            
        elif choice == "3":
            print("\n¡Gracias por usar EcoMarket! 🌱")
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()