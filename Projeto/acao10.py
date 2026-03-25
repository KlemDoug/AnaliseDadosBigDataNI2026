
import time

def cumprimentos():

    def boas_vindas():
        print("\033[1;31m" + "="*70 + "\033[0m")
        print("🎉 🍣 SEJA BEM VINDO AO TANOSHIMO!! 🍣 🎉")
        print("\033[1;31m" + "="*70 + "\033[0m")
        time.sleep(1)

        cliente=input("Como voce se chama? ")
        print()
    
        print(f'\033[1;32m""🥢 Olá {cliente} Será um prazer acompanha-lo (a) nessa aventura gastronomica! 🥢\033[0m' )
        print("\033[1;33m" + "-"*70 + "\033[0m")
        print(f' Sinta-se a vontade e se delicie com nossos deliciosos pratos.\n E \033[1;34m{cliente}\033[0m não esqueça de deixar a sua \033[1;31mavaliação\033[0m,ela é muito importante para nós.')
        print("\033[1;33m" + "-"*70 + "\033[0m")
        time.sleep(2)
        print("\033[1;31m 😋 BOM APETITE!!! 😋\033[0m")
        print("\033[1;31m" + "="*70 + "\033[0m")

        return cliente
        print()
    def encerramento(cliente):
        print("\033[1;31m" + "="*70 + "\033[0m")
        print(f'\033[1;32m{cliente}\033[0m Esperamos que a sua experiência tenha sido incrível!!!\nAvalei nosso atendimento e volte sempre!! ❤️')
        print("\033[1;31m" + "="*70 + "\033[0m")


    cliente_nome=boas_vindas()
    time.sleep(4)
    encerramento(cliente_nome)