# AÇÃO 15 – RYAN

#  Adaptei o avaliar_atendimento original.

avaliacoes = []  # preservei do original

def avaliacao():
    """
    Registra a avaliação do cliente.
    """

    print("Obrigado por visitar o Restaurante Tanoshimi!")
    nome = input("Qual o seu nome? ")

    while True:
        try:
            nota = int(input(f"{nome}, que nota você dá ao atendimento (1 a 10)? "))
            if 1 <= nota <= 10:
                break
            else:
                print("Digite um número entre 1 e 10.")
        except ValueError:
            print("Entrada inválida, tente novamente.")

    avaliacoes.append({"nome": nome, "nota": nota})
    print(f"Obrigado pela avaliação, {nome}! Volte sempre!")