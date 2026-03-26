# AÇÃO 02 — GLAUCIO

# O dicionário abaixo estava correto e foi preservado.
mesas_restaurante = {f"Mesa {i}": True for i in range(1, 10)}

def atualizar_mesa(numero_mesa, status_novo):
    """
    Atualiza a disponibilidade de uma mesa.
    (Esta função estava essencialmente correta.)
    """
    identificador = f"Mesa {numero_mesa}"

    # Isto já estava certo: verificação se a mesa existe.
    if identificador in mesas_restaurante:
        mesas_restaurante[identificador] = status_novo

        # Melhoria: tornar a mensagem mais clara.
        estado = "LIBERADA" if status_novo else "OCUPADA"
        print(f"Status da {identificador} atualizado para: {estado}.")
    else:
        print("Erro: Mesa não encontrada no sistema.")


def conferir_disponibilidade():
    """
    Exibe todas as mesas e seus status.
    (A lógica estava certa, só faltava indentação.)
    """
    print("\n--- MAPA DE RESERVAS ---")

    # ✓ Isto estava certo, só faltava recuo.
    for mesa, disponivel in mesas_restaurante.items():
        status = "Disponível" if disponivel else "Ocupada"
        print(f"{mesa}: {status}")

    print("------------------------\n")


def abrir_mesa():
    """
    Função necessária para integrar com o main.py
    Criada mantendo sua lógica já usada nas outras funções.
    """
    numero = input("Número da mesa que deseja abrir: ")

    identificador = f"Mesa {numero}"

    # Verificação adicionada para evitar erros de chave.
    if identificador not in mesas_restaurante:
        print("Mesa inexistente.")
        return

    if mesas_restaurante[identificador] == False:
        print("Mesa já está ocupada.")
        return

    # Mesma lógica que já existia em atualizar_mesa()
    atualizar_mesa(numero, False)