# Escreva um programa que peça para 
# o usuário o valor de a, b e
# calcule o delta

# delta = b² - 4ac
# 
valor_a = int(input("Valor de a: "))
valor_b = int(input("Valor de b: "))
valor_c = int(input("Valor de c: "))

delta = (valor_b ** 2) - (4 * valor_a * valor_c)

print(f"Valor de delta: {delta}")
