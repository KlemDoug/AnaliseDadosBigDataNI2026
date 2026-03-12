# CONDICIONAIS II:

carro=False
combustivel=False

# Qual a condição pra que este carro funcione?
#   not(F)==V        not(F)==V
if not carro and not combustivel: # <<< ambas as condições são verdadeiras: é o que eu quero
    print("Meu fusquinha está rodando.")
else:
    print("Não sobrou nada pro fusquinha.")

print('*'*15)

if not carro and not combustivel: # <<< ambas as condições são verdadeiras: é o que eu quero
    print("Meu fusquinha está rodando.")
elif carro==False or combustivel==False:
    print("Não sobrou nada pro fusquinha.")
else:
    print('Erro de execução.')

print('*'*15)

#Melhorias: 

semana = int(input("Informe o dia da semana:")) 
 
if semana == 1:  
    print("Domingo") 
elif semana == 2: 
    print("Segunda-feira") 
elif semana == 3: 
    print("Terça-feira") 
elif semana == 4: 
    print("Quarta-feira") 
elif semana == 5: 
    print("Quinta-feira") 
elif semana == 6: 
    print("Sexta-feira") 
elif semana == 7: 
    print("Sábado") 
else: # O 'else' funciona como o 'default' 
    print("Dia inválido")

#MATCH CASE (SEM tratamento de exceção):
mes = int(input("Informe o mês:"))
 
match mes: 
    case 1: 
        print("Janeiro") 
    case 2: 
        print("Fevereiro") 
    case 3: 
        print("Março") 
    case 6: 
        print("Junho") 
    case _: # O underline ( _ ) funciona como o 'default' ou 'else' 
        print("Mês inválido")

#MATCH CASE (COM tratamento de exceção):
try:
    mes = int(input("Informe o mês:"))
    match mes: 
        case 1: 
            print("Janeiro") 
        case 2: 
            print("Fevereiro") 
        case 3: 
            print("Março") 
        case 4: 
            print("Abril") 
        case 5: 
            print("Maio") 
        case 6: 
            print("Junho") 
        case 7: 
            print("Julho")  
        case 8: 
            print("Agosto") 
        case 9: 
            print("Setembro") 
        case 10: 
            print("Outubro")
        case 11: 
            print("Novembro") 
        case 12: 
            print("Dezembro")  
        case _: # O underline ( _ ) funciona como o 'default' ou 'else' 
            print("Mês inválido")
except ValueError: 
    print("Entrada inválida. Por favor, digite um número inteiro.") 



# TRATAMENTO DE EXCEÇÕES:
        
try: 
    numero_mes = int(input("Digite um número de 1 a 12: ")) 
 
    match numero_mes: 
        case 1: 
            print("O número 1 corresponde a Janeiro.") 
        # Inclua todos os outros meses aqui! 
        case 12: 
            print("O número 12 corresponde a Dezembro.") 
        case _: 
            print(f"Número {numero_mes} inválido. Digite entre 1 e 12.") 
 
except ValueError: 
    print("Entrada inválida. Por favor, digite um número inteiro.") 
