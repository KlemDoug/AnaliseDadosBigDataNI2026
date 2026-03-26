# AÇÃO 04 — BRUNO

# No original havia um dicionário temporário: eu preservei a ideia.
from acao02 import mesas_restaurante

def vincular_garcom():
    """
    Vincula um garçom a uma mesa.
    """

    funcionario = input("Digite o ID do garçom: ")
    mesa = input("Digite o número da mesa: ")

    # Alinhei no formato usado na ação 02.
    identificador = f"Mesa {mesa}"

    # ✓ Correção: verificar se mesa existe.
    if identificador not in mesas_restaurante:
        print("Mesa não encontrada.")
        return

    # Atualiza o dicionário real da ação 02.
    mesas_restaurante[identificador] = False  # ocupada

    print(f"Garçom {funcionario} vinculado à {identificador}.")