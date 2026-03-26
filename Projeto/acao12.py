# AÇÃO 12 – DANY

# Seu código original ficou ilegível por conta da lista estar fora da função, mas a intenção em listar mesas estava correta.
from acao02 import mesas_restaurante
def status_salao():
    """
    Mostra o status geral das mesas.
    """

    print("\n===== STATUS DO SALÃO =====")

    # Agora usa os dados reais de mesas_restaurante
    for mesa, status in mesas_restaurante.items():
        texto = "Disponível" if status else "Ocupada"
        print(f"{mesa}: {texto}")

    print("===========================\n")