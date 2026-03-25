#Ação 13 - Comissão Garçons.

def comissao_garcom(valor_conta, porcentagem=10):
    gorjeta = valor_conta * (porcentagem / 100)
    return round(gorjeta, 2)

conta = 150.00
gorjeta = comissao_garcom(conta, 10)

print(f"Valor da gorjeta: R$ {gorjeta}")