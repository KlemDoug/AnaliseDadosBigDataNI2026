'''
5. Média do Aluno com Optativa:

Escreva um programa que leia as notas das duas avaliações normais e a nota da avaliação 
optativa dos estudantes de uma turma. Caso o estudante não tenha feito a optativa, deve 
ser fornecido o valor -1. Calcular a média do semestre considerando que a prova optativa 
substitui a nota mais baixa entre as duas primeiras avaliações. Escrever a média e 
mensagens que indiquem se o estudante foi aprovado, reprovado ou se está em 
recuperação, de acordo com as informações abaixo: 

Aprovado: média >= 6.0 
Reprovado: média < 3.0 
Recuperação: média >= 3.0 e < 6.0 

Observação: nota optativa - o estudante decide fazer uma prova extra para melhorar o 
resultado final. 
'''

# nota1=float(input('Primeira Nota:'))
# nota2=float(input('Segunda Nota:'))
# optativa=float(input('Tem nota optativa?'))

# if optativa == -1:
#     media=(nota1+nota2)/2
# else:
#     if optativa > nota1:
#         media=(optativa+nota2)/2
#     else:
#         media=(optativa+nota1)/2

# if media >= 6.0:
#     resultado='APROVADO'
# elif media >= 3.0:
#     resultado='RECUPERAÇÃO'
# else:
#     resultado='REPROVADO'

# print(f'Média final: {media}; resultado: {resultado}')

'''
1. Cálculo de Lâmpadas: 
Escreva um programa para calcular e imprimir o número de lâmpadas necessárias para 
iluminar um determinado cômodo de uma residência. Dados de entrada: a potência da 
lâmpada utilizada (em watts), as dimensões (largura e comprimento, em metros) do 
cômodo. Considere que a potência necessária é de 3 watts por metro quadrado e a cada 
3m² existe um bocal para uma lâmpada. 
'''

# POTENCIA = 3
# # lampadas = 0
# largura = float(input('Largura:'))
# comprimento=float(input('Comprimento:'))

# area=largura*comprimento

# lampadas=area/POTENCIA

# print(f'São necessárias {round(lampadas)} lâmpadas para iluminar um cômodo de {area} m2.')

CONTADOR = 0

while contador != 0: # A condição de parada: Enquanto o contador for menor que 5 
    try: 
        print(f"Número {contador + 1} de {limite}:") 
        num = float(input("Digite um número: ")) 
        dobro = num * 2 
        triplo = num * 3 
        quádruplo = num * 4 
        print(f"  Resultado: Dobro={dobro}, Triplo={triplo}, Quádruplo={quádruplo}\n") 
        contador = contador - 1 # IMPORTANTÍSSIMO! Incrementa o contador para evitar loop infinito 
    except ValueError: 
        print("Entrada inválida. Tente novamente.") 
# Não incrementamos o contador para dar nova chance ao usuário 
