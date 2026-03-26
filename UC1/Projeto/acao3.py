# AÇÃO 03 — CAIO

# No original, havia várias versões da mesma função e inputs fora desta função.

# Aqui, eu estou mantenho sua lógica usando dicionário ou lista, como você pretendia fazer.

def add_item_pedido():
    """
    Adiciona um item ao consumo da mesa.
    """

    # O original usava "Pedido 1", "Pedido 2"... eu mantive esse conceito.
    mesa = {}
    
    for i in range(1, 4):
        # No original havia add_item_lista(lista, pedido, item)
        # Aqui considero melhor preservamos esta ideia.
        pedido_nome = f"Pedido {i}"
        item = input(f"Digite o nome do {pedido_nome}: ")

        # Inserção estava correta na lógica original.
        mesa[pedido_nome] = item

    # O print final também existia na sua versão e foi preservado.
    print("\n--- RESUMO DA MESA ---")
    print(mesa)