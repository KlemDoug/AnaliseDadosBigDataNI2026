# Define a função que será responsável por exibir o cardápio do restaurante
def exibir_cardapio():
    # Cria um dicionário chamado 'cardapio' que armazena as categorias de pratos
    # Cada chave é uma categoria (ex: "Entradas") e o valor é uma lista de dicionários
    cardapio = {
        # Categoria de ENTRADAS com pratos típicos da culinária japonesa
        "Entradas": [
            # Dicionário com as informações de cada prato: nome e preço
            {"nome": "Edamame", "preco": 15.00},
            {"nome": "Gyoza", "preco": 18.00},
            {"nome": "Agedashi Tofu", "preco": 20.00},
            {"nome": "Tempura de Vegetais", "preco": 22.00},
        ],

        # Categoria de PRATOS PRINCIPAIS com opções mais substanciais
        "Pratos Principais": [
            {"nome": "Sushi Variado", "preco": 45.00},
            {"nome": "Sashimi Premium", "preco": 50.00},
            {"nome": "Donburi de Frango Teriyaki", "preco": 35.00},
            {"nome": "Ramen Tonkotsu", "preco": 40.00},
            {"nome": "Okonomiyaki (Panqueca Japonesa)", "preco": 32.00},
            {"nome": "Udon ao Sumo", "preco": 38.00},
        ],

        # Categoria de SOBREMESAS com doces tradicionais japoneses
        "Sobremesas": [
            {"nome": "Mochi de Frutas Vermelhas", "preco": 12.00},
            {"nome": "Dorayaki (Bolo de Feijão Vermelho)", "preco": 10.00},
            {"nome": "Tempura de Banana com Sorvete", "preco": 15.00},
            {"nome": "Anko Taiyaki (Bolo em Forma de Peixe)", "preco": 8.00},
        ],
    }

    # Imprime um título formatado para o cardápio
    print("\n" + "="*50)
    print("           🍜 CARDÁPIO TANOSHIMI 🍜")
    print("="*50 + "\n")

    # Itera sobre cada categoria do cardápio usando o método .items()
    # 'categoria' recebe a chave (ex: "Entradas") e 'pratos' recebe a lista de dicionários
    for categoria, pratos in cardapio.items():
        # Imprime o nome da categoria em maiúsculas com uma formatação visual
        print(f"\n📌 {categoria.upper()}")
        print("-" * 50)

        # Itera sobre cada prato dentro da categoria
        # 'indice' é o número do prato começando do 1
        # 'prato' é o dicionário com as informações do prato
        for indice, prato in enumerate(pratos, start=1):
            # Extrai o nome do prato do dicionário
            nome = prato["nome"]
            # Extrai o preço do prato do dicionário
            preco = prato["preco"]

            # Imprime o prato formatado com número, nome e preço
            # f-string permite inserir variáveis diretamente na string
            # :6.2f formata o preço com 2 casas decimais
            print(f"{indice}. {nome:<35} R$ {preco:6.2f}")

    # Imprime uma linha de separação final para delimitar o fim do cardápio
    print("\n" + "="*50 + "\n")

# # Testa a função executando-a diretamente
# if __name__ == "__main__":
#     exibir_cardapio()