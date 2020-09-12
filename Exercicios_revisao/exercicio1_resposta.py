
# Vamos nos ater nas operações básicas.

# Exercicio 1

# Crie um programa que peça 2 números ao usuário (converta para inteiro), 
# faça todas as operações básicas do 
# python e motre o resultado usando o f-string.

numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite outro número: "))
soma = numero1 + numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2
subtracao = numero1 - numero2
expoente = numero1 ** numero2

print(f'''
soma = {soma}
multiplicação = {multiplicacao}
divisao = {divisao}
subtracao = {subtracao}
expoente = {expoente}
''')


# Exercicio 2
# Crie um programa que peça ao usuário 3 números (converta para float) e 
# mostre a média deles usando o f-string.


numero1 = float(input("Digite um número: "))
numero2 = float(input("Digite outro número: "))
numero3 = float(input("Digite outro número: "))

media = (numero1+numero2+numero3)/3
print(f"A média é: {media}")

# Execicio 3
# Crie um programa que peça um número inteiro e eleve este número ao 
# quadrado e mostre usando f-string

numero1 = int(input("Digite um número: "))
print(f'{numero1**2}')