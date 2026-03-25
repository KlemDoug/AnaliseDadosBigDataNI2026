
def calcular_conta():
    total = 0
    print("--- 🍔 Bem-vindo ao Sistema de Pedidos ---")
    print("Digite o nome do item (ou 'sair' para finalizar):")

    while True:
        item = input("\nNome do prato/bebida: ")
        
        if item.lower() == 'sair':
            break
            
        try:
            preco = float(input(f"Preço de '{item}': R$ "))
            total += preco
        except ValueError:
            print("❌ Valor inválido! Por favor, use apenas números e ponto (ex: 15.50).")

    print("\n" + "="*30)
    print(f"💰 TOTAL DA CONTA: R$ {total:.2f}")
    print("="*30)
    print("Obrigado e volte sempre!")

# if __name__ == "__main__":
#     calcular_conta()




 