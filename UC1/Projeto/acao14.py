# AÇÃO 14 – MYLENA

#A função 'não existia' chamando as outras funções no original, então foi criada seguindo essa intenção (já estava correta).
from acao02 import mesas_restaurante
def exportar_log():
    """
    Exporta um arquivo de texto contendo as informações mais importantes.
    """

    with open("log_restaurante.txt", "w", encoding="utf-8") as arq:
        arq.write("LOG DO TANOSHIMI\n\n")
        
        # Exportando o status das mesas (baseado no que seu código tentava fazer)
        for mesa, status in mesas_restaurante.items():
            estado = "Disponível" if status else "Ocupada"
            arq.write(f"{mesa}: {estado}\n")

    print("Log exportado com sucesso!")