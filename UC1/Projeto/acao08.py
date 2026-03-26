# AÇÃO 08 — ALICE
from acao07 import calcular_total
def finalizar_caixa():
    """
    Finaliza o pagamento usando o total calculado.
    """

    # Essa linha a seguir depende originalmente da função calcular_total().
    valor_da_conta = calcular_total()
    
    print("\nFormas de pagamento:")
    print("1 - Crédito")
    print("2 - Débito")
    print("3 - Pix")
    print("4 - Dinheiro")

    pagamento = input("Escolha a forma de pagamento (1-4): ")

    # ✓ A lógica condicional precisou de leve correção
    if pagamento in ["1", "2", "3"]:
        print("Pagamento confirmado!")
    elif pagamento == "4":
        try:
            valor_pago = float(input("Valor entregue pelo cliente: "))
            troco = valor_pago - valor_da_conta
            print(f"Troco: R$ {troco:.2f}")
        except:
            print("Valor inválido.")
    else:
        print("Opção inválida.")