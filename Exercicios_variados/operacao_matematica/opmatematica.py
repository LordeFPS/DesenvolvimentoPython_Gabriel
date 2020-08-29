###############################
# 
# Operações Matemáticas Básicas
# 
###############################

# O python possui 7 operadores matemáticos. Vamos ver os 5 primeiros.
# 
# SOMA
# O operado usado para soma é o sinal de mais +
# 2 + 2 = 4

# Subtração
# O operador para subtração é o sinal de menos -
# 5 - 3 = 2

# Divizão
# O operador para divizão é a barra /
# 10 / 2 = 10

# Multiplicação
# O operador para multiplicação é o asterisco *
# 2 * 5 = 10
# Quando aparecer a seguinte situação: 2x isso é a mesma coisa que: 2*x

# Expoente
# Você se lemba o que é um expoente?
# O expoente é uma conta matemática em que o primeiro número multiplica por ele mesmo uma quantidade de vezes.
# Exempo é o 4² (lea-se 4 elevado a 2 ou 4 ao quadrado)
# 4² -> 4 * 4 = 16
# 4³ -> 4 * 4 * 4 = 64
# O operador para o expoente são dois asteriscos **
# 4² -> 4 ** 2 = 16
# 4³ -> 4 ** 3 = 64



# exemplo de soma:
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
soma = numero1 + numero2
print("A soma dos números é: ", soma)

print("\n")

# exemplo de multiplicação:
valor = float(input("Digite o preço do produto: "))
quantidade = int(input("Digite a quantidade de produto que você deseja: "))
preco_total = valor * quantidade
print("O valor total a ser pago é: ", preco_total)

print('\n')

# exemplo de divisão
quantidade = int(input("Digite a quantidade de laranjas que você tem: "))
pessoas = int(input("Digite a quantidade de pessoas: "))
divisao = quantidade / pessoas
print("Cada pessoa deve ficar com ", divisao, " laranjas")

# exemplo de subtração
predio_alto = float(input("Digite o tamanho do prédio alto: "))
predio_baixo = float(input("Digite o tamanho do prédio baixo: "))
diferenca = predio_alto - predio_baixo
print("O prédio mais alto ", diferenca, " metros mais alto que o prédio baixo")

# exemplo de expoente
numero = int(input("Digite o número para ser elevado ao quadrado: "))
quadrado = numero ** 2
print("O quadrado de ", numero, " é: ",quadrado)
