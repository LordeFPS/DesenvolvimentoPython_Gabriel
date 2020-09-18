# Escreva um programa que peça a nota de um aluno e mostre:
# 
# Nota 9 a 10 - Aprovado com louvor
# Nota 7 a 9 - Aprovado
# Nota 5.5 a 7 - Recuperação
# Nota menor que 5.5 - Reprovado

nota = 11

if nota >= 9 and nota <= 10:
    print("Aprovado com louvor")
elif nota >= 7 and nota < 9:
    print("Aprovado")
elif nota >= 5.5 and nota < 7:
    print("Recuperação")
elif nota >= 0 and nota < 5.5:
    print("Reprovado")
else: 
    print("Valor inválido")

# Fim

