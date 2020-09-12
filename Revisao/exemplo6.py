# Com a lista de preços de uma compra, faça a soma de todos os 
# preços e mostre o valor total da compra.

lista_compra = [10.00, 25.05, 55.30, 29.90, 0.5, 0.75,
                5.95, 16.54, 78.00, 25,90, 4.55, 8.95]

# para resolvermos devemos usar a função sum()
soma = sum(lista_compra)

print(soma)


# Com a lista de tamanho, mostre a altura do menor atleta 
# esportivo.

lista_tamanho = [1.75, 1.78, 1.75, 1.74, 1.69, 1.70,
                 1.73, 1.72, 1.70, 1.79, 1.80, 1.77]

# para resolvermos devemos usar a função min()

print(min(lista_tamanho),"m")

# Com a lista de pesos, mostre o maior peso do peixe pescado 
# em um campeonato de pesca.

lista_peso = [1.00, 1.50, 1.41, 1.01, 1.05, 1.51, 1.75,
              1.69, 0.75, 1.09, 1.45, 2.01, 1.11, 1.15]

# para resolvermos devemos usar a função max()

print(max(lista_peso),"Kg")

# Com a lista de nomes para uma festa, mostre quantas pessoas
# foram convidadas

lista_nomes = ['André', 'Agnaldo', 'Jorge', 'Amanda', 'Flavia',
               'Flavio', 'Paulo', 'Fernada', 'Eduardo','Monica',
               'Felipe', 'Ester', 'Vera', 'Clair', 'Itemar',
               'Noeli', 'Melissa']

# para resolvermos devemos usar a função len()

print(len(lista_nomes),"qtd")


# Com a seguinte lista de tamanho, mostre a altura média
# dos atletas
lista_tamanho = [1.75, 1.78, 1.75, 1.74, 1.69, 1.70,
                 1.73, 1.72, 1.70, 1.79, 1.80, 1.77]

# para resolvermos devemos usar duas funções sum() e len()

print(sum(lista_tamanho)/len(lista_tamanho),"media")