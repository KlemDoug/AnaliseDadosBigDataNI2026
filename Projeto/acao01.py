# AÇÃO 01 – MATHEUS

# Função original estava correta conceitualmente: tinha que exibir o cardápio.

# Melhorias:

# - O cardápio era redefinido dentro da ação 03, causando duplicação.
# - A função estava sendo executada automaticamente no final do arquivo.
# - Por isso, eu mantive a estrutura; só removi duplicações e execuções automáticas.

def exibir_cardapio():
    """
    Exibe o cardápio completo organizado por categorias.
    A lógica original estava correta, só precisava ser isolada.
    """
    
    # O dicionário original foi preservado (correto)
    cardapio = {
        "Entradas": [
            {"nome": "Edamame", "preco": 15.00},
            {"nome": "Gyoza", "preco": 18.00},
            {"nome": "Agedashi Tofu", "preco": 20.00},
            {"nome": "Tempura de Vegetais", "preco": 22.00},
        ],
        "Pratos Principais": [
            {"nome": "Sushi Variado", "preco": 45.00},
            {"nome": "Sashimi Premium", "preco": 50.00},
            {"nome": "Donburi de Frango Teriyaki", "preco": 35.00},
            {"nome": "Ramen Tonkotsu", "preco": 40.00},
            {"nome": "Okonomiyaki", "preco": 32.00},
            {"nome": "Udon ao Sumo", "preco": 38.00},
        ],
        "Sobremesas": [
            {"nome": "Mochi", "preco": 12.00},
            {"nome": "Dorayaki", "preco": 10.00},
            {"nome": "Tempura de Banana", "preco": 15.00},
            {"nome": "Taiyaki", "preco": 8.00},
        ],
    }

    # Esta parte está perfeita, apenas mantida e comentada
    print("\n" + "="*50)
    print(" 🍜 CARDÁPIO TANOSHIMI 🍜")
    print("="*50 + "\n")

    for categoria, pratos in cardapio.items():
        print(f"\n📌 {categoria.upper()}")
        print("-" * 50)

        for i, prato in enumerate(pratos, 1):
            print(f"{i}. {prato['nome']:<35} R$ {prato['preco']:6.2f}")

    print("\n" + "="*50)
