# AÇÃO 05 — RAFAEL

# Ter a biblioteca random importada para gerar números aleatórios aqui fora não é um problema. O algoritmo de randint já estava correto.

from random import randint

def gerar_id_pedido():
    """
    Gera um ID aleatório único para a identificação do pedido.
    """
    
    qtd = int(input("Quantos itens no pedido? "))

    # Originalmente você usava uma lista de pedidos.
    lista_ids = []

    while len(lista_ids) < qtd:
        novo = randint(100, 500)

        # Verificação de duplicados estava correta.
        if novo not in lista_ids:
            lista_ids.append(novo)

    # Impressão da relação item com o id do pedido correta também e foi mantida.
    for i, idd in enumerate(lista_ids, start=1):
        print(f"Item {i} → ID: {idd}")