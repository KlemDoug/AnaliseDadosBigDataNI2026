# AÇÃO 11 – RAFAELLA

def desconto_usuario():
    """
    Aplica o desconto de aniversário.
    """

    try:
        valor_compra = float(input("Digite o valor da compra: "))
    except ValueError:
        print("Valor inválido.")
        return

    faz_aniversario = input("Hoje é seu aniversário? (SIM/NAO): ").upper()

    if faz_aniversario == "SIM":
        desconto = valor_compra * 0.15  # cálculo estava totalmente correto aqui
        valor_final = valor_compra - desconto
        print(f"Você ganhou um desconto de R$ {desconto:.2f}!")
    elif faz_aniversario == "NAO":
        valor_final = valor_compra
        print("Nenhum desconto aplicado.")
    else:
        print("Resposta inválida.")
        return

    print(f"Total final: R$ {valor_final:.2f}")
    return valor_final