lista = [['edu',12, 1.5,'a@a'],['dudu',15, 4.6,'b@b'],
         ['caja','abacate',20, 8.6,'c@c']]


# mostrar todos os elementos separadamente da lista
lista_convidados = []
for pessoa in lista:
    if pessoa[1] >= 14:
        lista_convidados.append(pessoa)

print(lista_convidados, "\n")

for i in lista_convidados:
    print(i)