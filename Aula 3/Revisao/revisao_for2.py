# media de 0 a 5: Reprovado
# media de 5 a 7: Recuperação
# media de 7 a 10: Aprovado

lista_notas = []

for i in range(3):
    nota = float(input("Digite a nota: "))
    lista_notas.append( nota ) # append adiciona a nota na lista_notas


media = sum(lista_notas) / len(lista_notas)


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

for i in lista_notas:
    if i > 5:
        print(i)