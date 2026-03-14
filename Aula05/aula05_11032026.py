# LAÇOS DE REPETIÇÃO:

# >>> FOR

intervalo1 = range(10)
print(intervalo1)

print('***')

for numero in range(1,10,2):
    print('CONTANDO:')
    print('número:')
    print(numero)

for i in range(5):
    try:
        # i representa o número atual da repetição (0, 1, 2...)
        print(f"Número {i + 1} de 5:")
        num = float(input("Digite um número: "))

        dobro = num * 2
        triplo = num * 3
        quádruplo = num * 4

        print(f" Resultado: Dobro={dobro}, Triplo={triplo}, Quádruplo={quádruplo}\n")

    except ValueError:
        print("Entrada inválida. Tente novamente.")

# >>> WHILE

loolap=float(input('Qual o valor do evento (inteira)?')) #Dependnedo do input, cai num loop infinito

while loolap > 300:
    print('Mas não vou mesmo!!!')

print('Estarei lá!')
##

loolap=300.000000000000000000000000000000000001

while loolap > 300:
    loolap=float(input('Qual o valor do evento (inteira)?')) #Dependnedo do input, cai num loop infinito
    print('Mas não vou mesmo!!!')

print('Estarei lá!')
##

loolap=300

while loolap >= 300:
    loolap=float(input('Qual o valor do evento (inteira)?')) #Dependnedo do input, cai num loop infinito
    print('Mas não vou mesmo!!!')

print('Estarei lá!')

print(299.99999==300)