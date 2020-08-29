# Operadores de comparação

# == igual
# != diferente
# >= maior igual
# > maior
# <= menor igual
# < menor

numero = int(input("Digite um número: "))

if (numero % 2) == 0:
    # Executa quando verdadeiro
    print(  f"Número {numero} é par!")
    #quatro espaços = indentação
else:
    # Executa quando falso
    print(  f"Número {numero} é impar!")