# media de 0 a 5: Reprovado
# media de 5 a 7: Recuperação
# media de 7 a 10: Aprovado

nota1 = float(input("Digite a nota: "))
nota2 = float(input("Digite a nota: "))
nota3 = float(input("Digite a nota: "))
nota4 = float(input("Digite a nota: "))

media = (nota1+nota2+nota3+nota4)/4
if media >= 0 and media < 5:
    # Executa quando verdadeiro
    print(f"Aluno Reprovado {media}")
elif media >= 5 and media < 7:
    # executa quano em cima for falso e este elif 
    # for verdadeiro
    print(f"Aluno Recuperação {media}")
elif media >= 7  and media <= 10:
    # executa quano em cima for falso e este elif 
    # for verdadeiro
    print(f"Aluno Aprovado {media}")
else:
    # Executa quando falso
    print("Valor inválido")