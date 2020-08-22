# Faça um programa que peça 2 números
# e retorne a soma, multiplicação, divisão, subtração

numero1 = int(input("Valor1: "))
numero2 = int(input("Valor2: "))

# print('''
# ---------- Menu ---------
# -- (1) - Soma          --
# -- (2) - Subtração     --
# -- (3) - Multiplicação --
# -- (4) - Divisão       --
# -------------------------
# '''
# )

# Não muito indicado pois os valores se perdem no code ↓↓↓
# print(f"Soma: {numero1+numero2}\nSubtração: {numero1-numero2}")
# print(f"Multiplicação: {numero1*numero2}\nDivisão: {numero1/numero2}")

# Se possível fazer desta forma ↓↓↓
soma = numero1 + numero2
subtração = numero1 - numero2
multiplicacao = numero1 * numero2
divisão = numero1 / numero2

print (f""" 
Soma: {soma}
Subtração: {subtração}
Multiplicação: {multiplicacao}
Divisão: {divisão}
"""
)