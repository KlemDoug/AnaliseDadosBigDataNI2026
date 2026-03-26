# AÇÃO 06 — DIOGO

# A lógica original estava muito boa, apenas ajustei o escopo e fluxo.
from acao02 import mesas_restaurante

def buscar_pedido():
    """
    Busca um pedido pelo número do cartão/ID.
    """

    try:
        id_procurado = int(input("Digite o número do cartão/ID do pedido: "))
    except ValueError:
        print("Entrada inválida.")
        return

    # No original, você percorria um dicionário idpedido -> correção:
    # Alterei para usarmos o sistema de mesas da ação 02.
    for mesa, status in mesas_restaurante.items():
        # No original, 'idpedido' viria de outra ação.
        # Aqui integra com a ação 05.
        if isinstance(status, dict) and status.get("id_pedido") == id_procurado:
            print("\n=== CONSUMO LOCALIZADO ===")
            print(f"Mesa: {mesa}")
            print(f"Número do cartão: {id_procurado}")
            return

    print("\nConsumo não encontrado.")