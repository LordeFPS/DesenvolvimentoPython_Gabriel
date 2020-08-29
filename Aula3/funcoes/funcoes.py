# media de 0 a 5: Reprovado
# media de 5 a 7: Recuperação
# media de 7 a 10: Aprovado
def media(lista_funcao ):
    media = sum(lista_funcao) / len(lista_funcao)
    return media

def captura(qualquer_coisa):
    lista = []
    for i in range(qualquer_coisa):
        nota = float(input("Digite a nota: "))
        lista.append( nota ) # append adiciona a nota na lista_notas
    return lista

lista_notas1 = captura(4)
lista_notas2 = captura(2)
lista_notas3 = captura(3)


media1 = media(lista_notas1)
media2 = media(lista_notas2)
media3 = media(lista_notas3)

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