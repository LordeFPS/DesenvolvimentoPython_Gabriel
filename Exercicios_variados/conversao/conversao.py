################################
# 
# Convertendo Tipos de Variáveis
# 
################################


# O input() sempre irá retornar para nós uma string (texto).
# Porém as vezes precisamos de outros tipos de dados como um inteiro ou um float (ponto flutuante ou real).
# Para isso devemos usar funções para converter como:
# - int() para interios
# - float() para float
# 
# A escolha vai depender do que você está trabalhando.
# Exemplo:




# converter variável

# de string para inteiro
var = '10' # a aspa indica que a variável é do tipo string. 
var = int(var) # Estou convertendo e salvando na mesma variável

# de inteiro para string
var = 10
var = str(var)

# de float para string
var = 9.50
var = str(var)

# de string para float
var = '10.75'
var = float(var)

# de inteiro para float
var = 10
var = float(var)

# de float para inteiro
# Ficar atento que esta conversão pega somente a parte inteira do número. A parte depois da virgula é perdida

var = 7.85
var = int(var)
print(var)


print('\n')


# pedir 2 números inteiros e fazer a soma deles
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
soma = numero1 + numero2
print("A soma dos números é: ", soma)

# pedir 2 número float e somar os dois
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
soma = numero1 + numero2
print("A soma dos números é: ", soma)

# em via de regra, usamos o float quando queremos trabalhar com dinheiro, preço, peso, altura...
valor = float(input("Digite o preço do produto: "))
quantidade = int(input("Digite a quantidade de produto que você deseja: "))
preco_total = valor * quantidade
print("O valor total a ser pago é: ", preco_total)


# Uma forma de saber que tipo de variável é usando a função type().
# 
# Exemplo:

# para descobrir qual o tipo da variável
variavel = 10 #inteiro
print("Inteiro")
print(type(variavel))

print('\n')

variavel = 10.0 # float
print("Float")
print(type(variavel))

print('\n')

variavel = '10 abc' # string (texto)
print("string")
print(type(variavel))


