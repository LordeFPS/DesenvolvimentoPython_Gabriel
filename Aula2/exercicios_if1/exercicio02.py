# Exercicio 2
# Faça um programa que peça um número.
# 
# Mostre na tela se este número é negativo ou positivo. (lembrando que números positivos são maiores que zero!)

numero = int(input("Digite um numero: "))

if numero >= 0:
    print(f"Número Positivo: {numero}")
else:
    print(f"Número Negativo: {numero}")
