# ###############################################################

# No python há 7 operdeores matemáticos

# *   multiplicação
# /   divisão
# -   subtração
# +   adição
# **  expoente
# //  divisão interira
# %   módulo ou resto da divisão inteira


# As 4 operações básicas são simples e intuitivas. Mas pode ocorer uma pequena confusão
# quanto as outras operações.

# O Expoente.

# O expoente nada mais é que a operação de multiplicação onde um número é multiplicado
# por ele meno várias vezes.
# Exemplo:
# 5² seria 5 x 5 = 25         # cinco ao quadrado (²)
# 5³ seria 5 x 5 x 5 = 125    # cinco ao cubo     (³)

# No python usamos os ** como operador de expoente.
# Exemplo:
# 5² seria 5 ** 2  = 25
# 5³ seria 5 ** 3  = 125

# A divisão inteira

# Na divisão inteira o resultado sempre será um número inteiro. 
# A parte fracionada (depois da virgula) é ignorada.
# Exemplo:
# Divisão normal    20 / 3 = 6.6666666...
# Divisão inteira   20 // 3 = 6

# Note que a parte .6666 é perdida.


# O Módulo ou resto da divisão inteira
# Ele é o resto de uma da divisão interia. 
# Quando os números são multiplos o resto é zero! 
# Vamos ver:

# 20 % 3 = 2    -Sobra 2 nesta divisão. 
# 20 % 10 = 0   -Não sobra nada pois 20 é multiplo de 10!


# ###############################################################

# Conversão de variáveis

# Quando recebemos dados vindo da função input(), este dado é do tipo
# string (texto). Para podermos trabalhar com ele há a necessidade de aplicar
# a converção para o dado mais adequado.

# Como sabemos, a string é reconhecida por iniciar e terminar com aspas. A Conversão
# é feita usando as seguintes funções:

# int()   - Converte para números inteiros
# float() - converte para números reais
# str()   - converte para string 

# Oura funções:
# list()  - converte para listas (vamos ver isso mais para frente)
# tuple() - converte para tuplas (é uma lista que não pode ser mudada)
# dict()  - converte para dicionário (vamos ver isso na proxima aula)

# Para converter se fáz a seguinte operação:

var = '15' # Este é uma string, um texto, tem que ser convertida para inteiro
numero = int(var) # Estou convertendo o var para número e atribuindo (salvando em uma variável)

var = '1.99'
numero_real = float(var)

###############################################################

# F-String
# O f-string é uma forma fácil para adicionar as variáveis em string.

# Veja só... Tenho 3 variáveis e quero adicionálas em uma string e mostra-las

nome_pessoa = "Eduardo da Costa"
quantidade = 10
preço = 10.5

# Usando f-string:

texto = f'Cliente: {nome}, comprou {quantidade} de maçã no preço de {preço} a unidade.'

# Note que podemos fazer operações matemáticas dentro das chaves
texto2 = f'Valor total da compra {quantidade*preço}'

print(texto)
print(texto2)


# O f-string pode ser feito dentro do print()

print(f'Cliente: {nome}, comprou {quantidade} de maçã no preço de {preço} a unidade.')
print(f'Valor total da compra {quantidade*preço}')



# Vamos nos ater nas operações básicas.

# Exercicio 1

# Crie um programa que peça 2 números ao usuário (converta para inteiro), 
# faça todas as operações básicas do 
# python e motre o resultado usando o f-string.


# Exercicio 2
# Crie um programa que peça ao usuário 3 números (converta para float) e 
# mostre a média deles usando o f-string.

# Execicio 3
# Crie um programa que peça um número inteiro e eleve este número ao 
# quadrado e mostre usando f-string

