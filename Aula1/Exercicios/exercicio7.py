# Solicite ao usuário o nome do aluno
# as 4 notas e mostre a média junto com o 
# nome do aluno usando o f-string

aluno = str(input("Nome do aluno: "))

cont = 0
nota_soma = 0

for i in range(4):
    nota = float(input(f"Digite valor da nota {cont + 1}: "))
    nota_soma = nota_soma + nota
    cont = cont + 1
    media = nota_soma / cont

print(f"Nome do aluno: {aluno}\nMedia: {media:.2f}") #2f deixa apenas 2 numero depois da vírgula
