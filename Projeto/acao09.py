#Limpar os dados da mesa e a torna disponivel para o proximo cliente.


import random 

def limpar_mesa(finalizar_caixa,consumo_total):
    """
    Limpa os dados de consumo e redefine o status da mesa para disponível.
    """
    mesapaga=finalizar_caixa
 
    if consumo_total == mesapaga:
        status_mesa = "Disponível"
        print("Mesa limpa e pronta para o próximo cliente!")
    else:
        print(f"Erro: Ainda há um débito de R${consumo_total:.2f}. Finalize o pagamento antes de limpar.")
    
    return status_mesa

