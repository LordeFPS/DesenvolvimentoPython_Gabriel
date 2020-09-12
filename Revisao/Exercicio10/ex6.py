from random import randint
# **Exercícios**

# Usando o for com o e sem o range() resolva:

# Crie um programa que pegue a idade da lista e mostre a seguinte mensagem:
# Para maiores de 18 anos -> "Entrada Liberada"
# Para menores de 18 anos -> "Entrada Proibida"

lista_idade = [randint(15,50) for x in range(20)] # List Comprehension
