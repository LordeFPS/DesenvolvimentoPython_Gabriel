
#################
# 
# Uso do print()
# 
################


# A função print() mostra na tela uma mensagem ou o valor das variáveis.<br>
# Assim é só colocar uma variavel dentro do print() ou uma string (texto) desta forma:



# Com um uma string (texto)
print("Sejam bem vindos ao nosso sistema de cadastro de pessoas")
# lembrando que as string devem ser representadas com aspas simples '' ou duplas ""


# Podemos usar caracteres de escape para pular uma linha
print("\n")

# Com uma variável
nome = 'Julio'
print("Seja bem vindo ", nome)

print("\n")

# Pode ser colocado uma operação matemática dentro dela
print("A soma de 1+2 é: ", 1+2)


print("\n")

# Ou até fazer esta operação usando variaveis
valor = 5.50
quantidade = 10
print("Preço total é: ",valor*quantidade)

print("\n")

# Porém o melhor mesmo é fazer desta forma:
valor = 5.50
quantidade = 10
total = valor*quantidade
print("Preço total é: ",total)

print("\n")

# Para mostrar um texto com mais linhas, podemos usar as 3 aspas """ """ desta forma:
print("""
Oi
Meu nome
é
Pedro
""")


