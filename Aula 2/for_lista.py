# # Forma básica
# for i in range(<numero>):
#     <codigo a ser executado>

# Exemplo de uso:
# mostre na tela números de 1 a 20

# for i in range(5): # O range fica o número de vezes que ele irá executar
#     print("ola mundo")

# Introdução a lista
# Solicite ao usuário o nome do aluno
# as 4 notas e mostre a média junto com o 
# nome do aluno usando o f-string

nome = input("Digite o nome do aluno: ")

qdd_nota = int(input("Digite a quantidade de notas: "))
lista = [] # Iniciando uma lista vazia
print(lista)

for i in range(qdd_nota):
    nota = float(input(f"Digite a nota {i+1}: "))
    lista.append(nota) # Adicionando elemento em uma lista
    print(lista)



media = (sum(lista)) / qdd_nota

print(f"O aluno {nome}, teve a méida {media:.2f}")