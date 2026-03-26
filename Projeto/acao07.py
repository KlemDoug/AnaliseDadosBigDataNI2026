# AÇÃO 07 — MIGUEL

# Lógica original certinha e intacta, só adicionei o return.

def calcular_total():
    """
    Calcula o total do pedido somando itens digitados pelo garçom.
    """

    total = 0
    print("--- Sistema de Pedidos ---")
    print("Digite 'sair' para finalizar.")

    while True:
        item = input("Nome do prato/bebida: ")

        if item.lower() == "sair":
            break

        try:
            preco = float(input(f"Preço de '{item}': R$ "))
            total += preco  # 100% correto aqui
        except ValueError:
            print("Valor inválido!")

    print(f"Total da conta: R$ {total:.2f}")
    return total  # Essa adição é necessária para integração com ação 08