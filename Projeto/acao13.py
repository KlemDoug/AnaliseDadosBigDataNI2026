# AÇÃO 13 – THIAGO

# A lógica original (valor_conta * porcentagem/100) perfeita, mantida.

def comissao_garcom():
    """
    Calcula a comissão do garçom.
    """

    try:
        valor_conta = float(input("Informe o valor total da conta: "))
    except ValueError:
        print("Valor inválido.")
        return

    porcentagem = 10  # igual ao original

    gorjeta = valor_conta * (porcentagem / 100)

    print(f"Comissão do garçom: R$ {gorjeta:.2f}")
    return gorjeta