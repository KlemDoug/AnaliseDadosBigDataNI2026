###################################################
#               PROJETO TANOSHIMI                 #
###################################################

# Importação das funções de cada colaborador
from acao01 import exibir_cardapio
from acao02 import abrir_mesa
from acao03 import add_item_pedido
from acao04 import vincular_garcom
from acao05 import gerar_id_pedido
from acao06 import buscar_pedido
from acao07 import calcular_total
from acao08 import finalizar_caixa
from acao09 import liberar_mesa
from acao10 import cumprimentos
from acao11 import desconto_usuario
from acao12 import status_salao
from acao13 import comissao_garcom
from acao14 import exportar_log
from acao15 import avaliacao

# Execução
def menu():
    print("ATENDIMENTO TANOSHIMI")
    opcoes = [
        "Exibir cardápio",
        "Abrir mesa",
        "Adicionar item ao pedido",
        "Vincular garçom à mesa",
        "Gerar ID do pedido",
        "Buscar pedido",
        "Calcular total",
        "Finalizar caixa",
        "Liberar mesa",
        "Cumprimentos",
        "Desconto do usuário",
        "Status do salão",
        "Comissão do garçom",
        "Exportar log",
        "Avaliação"
    ]

    for i, texto in enumerate(opcoes, start=1):
        print(f"{i} - {texto}")
    print("0 - Sair")


def main():
    while True:
        menu()
        opcao = input("\nEscolha uma opção: ")

        match opcao:
            case "1": exibir_cardapio()
            case "2": abrir_mesa()
            case "3": add_item_pedido()
            case "4": vincular_garcom()
            case "5": gerar_id_pedido()
            case "6": buscar_pedido()
            case "7": calcular_total()
            case "8": finalizar_caixa()
            case "9": liberar_mesa()
            case "10": cumprimentos()
            case "11": desconto_usuario()
            case "12": status_salao()
            case "13": comissao_garcom()
            case "14": exportar_log()
            case "15": avaliacao()
            case "0":
                print("Saindo...")
                break
            case _:
                print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()