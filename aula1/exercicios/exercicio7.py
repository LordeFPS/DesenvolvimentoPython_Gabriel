# Solicite ao usuário o nome do aluno
# as 4 notas e mostre a média junto com o 
# nome do aluno usando o f-string

nome = input("Digite o nome do aluno: ")

nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))
nota4 = float(input("Digite a nota 4: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

print(f"O aluno {nome}, teve a méida {media:.2f}")