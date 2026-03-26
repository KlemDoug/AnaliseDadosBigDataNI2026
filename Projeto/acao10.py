# AÇÃO 10 – LUCIENE
import time

def cumprimentos():
    """
    Exibe mensagens de boas-vindas e encerramento.
    """

    # ✔ Função original preservada
    def boas_vindas():
        print("=" * 70)
        print("🎉 🍣 SEJA BEM-VINDO AO TANOSHIMI!! 🍣 🎉")
        print("=" * 70)
        time.sleep(1)

        # Entrada do nome estava correta
        cliente = input("Como você se chama? ")

        print(f"\n🥢 Olá {cliente}! É um prazer acompanhá-lo(a) nessa aventura gastronômica!")
        print("-" * 70)
        print("Sinta-se à vontade para apreciar nossos pratos!")
        return cliente

    # Também preservei essa parte
    def encerramento(cliente):
        time.sleep(1)
        print("=" * 70)
        print(f"{cliente}, esperamos que sua experiência tenha sido incrível!")
        print("Avalie nosso atendimento e volte sempre! ❤️")
        print("=" * 70)

    # Organizei a chamada das funções
    nome_cliente = boas_vindas()
    encerramento(nome_cliente)