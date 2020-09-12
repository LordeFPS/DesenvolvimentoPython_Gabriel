# Adicione o nome de 3 pessoas na lista de convidados
lista_convidados = ['André', 'Agnaldo', 'Jorge', 'Amanda', 'Flavia',
               'Flavio', 'Paulo', 'Fernada', 'Eduardo','Monica',
               'Felipe', 'Ester', 'Vera', 'Clair', 'Itemar',
               'Noeli', 'Melissa']

# for i in range(3):
#     nome = input("Digite um nome: ")
#     lista_convidados.append(nome)

# print(lista_convidados)


# Na lista numérica, faltou um número. Adicione este número
# na posição correta.
lista_numeros = [10, 11, 13, 14, 15, 16, 17, 18, 19, 20]

# lista_numeros.insert(2,12)

# print(lista_numeros)


# Na lista de convidados, é necessário remover os dois ultimos
# nomes, pois os convites foram recusados!

lista_convidados = ['André', 'Agnaldo', 'Jorge', 'Amanda', 'Flavia',
                    'Flavio', 'Paulo', 'Fernada', 'Eduardo','Monica',
                    'Felipe', 'Ester', 'Vera', 'Clair', 'Itemar',
                    'Noeli', 'Melissa']

# função POP remove sempre a ultima posição da lista 
# nome1 = lista_convidados.pop()
# nome2 = lista_convidados.pop()

# print(lista_convidados)
# print(f'''
# Nomes removidos
# {nome1}
# {nome2}
# '''
# )


# Na lista de números eu preciso remover o número da 
# posição 3
lista_numeros = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# função POP também remove uma posição específica da lista 
# lista_numeros.pop(3)

# print(lista_numeros)



# Na lista de condicados, é necessário remover a Flavia e o Paulo,
# pois os convites foram recusados!

lista_convidados = ['André', 'Agnaldo', 'Jorge', 'Amanda', 'Flavia',
               'Flavio', 'Paulo', 'Fernada', 'Eduardo','Monica',
               'Felipe', 'Ester', 'Vera', 'Clair', 'Itemar',
               'Noeli', 'Melissa']

# lista_convidados.remove("Flavia")
# lista_convidados.remove('Paulo')

# print(lista_convidados)

# Na lista de tamanho dos atletas, ordene de menor para o maior
lista_tamanho = [1.75, 1.78, 1.75, 1.74, 1.69, 1.70,
                 1.73, 1.72, 1.70, 1.79, 1.80, 1.77]

# Usando a mesma lista de tamanhos já ordenados, inverta a orden da lista, do maior
# para o menor

lista_tamanho.sort()

print(lista_tamanho)
