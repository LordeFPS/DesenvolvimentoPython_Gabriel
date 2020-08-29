
# ---
# 
#Variáveis Boobleans
# 
# ---

# Variáveis booleanas possuem 2 valores válidos
# True (verdadeiro) e False (falso)
# 
# O valor True pode ser substituido pelo valor 1
# enquanto o False pode ser substituido pelo valor 0
# 




# Exemplo de variável booleana

entrada = True

saida = False

dineiro_banco = True

saldavel = True


# Para fazer a conversão para booleano é utilizado a funão bool()




# Convertendo numero 1 para booleano
var = 1
var = bool(var)
print(var)

print("\n")

# Convertendo numero 0 para booleano
var = 0
var = bool(var)
print(var)


# Interesante é a conversão de variáveis para o booleano.
# Variáveis None ou vazias resultam e False
# enquanto variáveis com algum valor apresentam valor True




# Criando variáveis vazias
inteiro = 0
real = 0.0
texto = ""


print(type(inteiro),bool(inteiro))
print(type(real),bool(real))
print(type(texto),bool(texto))

print("\n")

# O None é um valor nulo. Não tem tipo e muito menos valor
nulo = None

print(type(nulo),bool(nulo))

print("\n")

# Convertendo variáveis com valor
inteiro = 10
real = -5.0
texto = "0"


print(type(inteiro),bool(inteiro))
print(type(real),bool(real))
print(type(texto),bool(texto))


# ---
# 
#Operadores de comparação
# 
# ---

# Os operadores comparam 2 variávei e retornam True ou False.
# Eles são muito usados no laço condicional para determinar qual ação deve ser tomada.
# 
# Existe 6 operadores de comparação:
# 
# >     Maior
# <     Menor
# >=   Maior menor
# <=   Menor igual
# ==   igual (são 2 sinais de iguais)
# !=   Difierente
# 
# Cuidado com o sinal de igual. É muito comum haver a confusão.
# 1 sial de igual é atribuição de valor para uma vairável.
# Ex:
# valor = 10
# 
# 
# 2 siais de igual é a comparação se os 2 valores são iguais!
# 10 == 10 
# True
# 




# Exemplo de uso:

numero = 10
valor = 10
dinheiro = 15
nota = 9

# Maior - Verifica se a primeira variável é maior que a segunda. 
print("Maior >")
print("nota (9) > valor (10)? ",nota > valor)
print("valor (10) > nota (9)? ", valor > nota)
print("numero (10) > valor (10)? ", numero > valor) # Note que 10 não é maior que 10 por isso será falso.

print('\n')

# Maior igual - Verifica se a primeira variável é maior ou igual que a segunda. 
print("Maior igual >=")
print("nota (9) >= valor (10)? ",nota >= valor)
print("valor (10) >= nota (9)? ", valor >= nota)
print("numero (10) >= valor (10)? ", numero >= valor) # Note que agora o resultado é True.

print('\n')

# Menor - Verifica se a primeira variável é menor que a segunda. 
print("Menor <")
print("nota (9) < valor (10)? ",nota < valor)
print("valor (10) < nota (9)? ", valor < nota)
print("numero (10) < valor (10)? ", numero < valor) # Note que 10 não é menor que 10 por isso será falso.

print('\n')

# Menor igual - Verifica se a primeira variável é menor ou igual que a segunda. 
print("Menor igual <=")
print("nota (9) <= valor (10)? ",nota <= valor)
print("valor (10) <= nota (9)? ", valor <= nota)
print("numero (10) <= valor (10)? ", numero <= valor) # Note que agora o resultado é True.

print('\n')

# Igual - Verifica se a primeira variável é igual à segunda. 
print("Igual ==")
print("nota (9) == valor (10)? ",nota == valor)
print("valor (10) == nota (9)? ", valor == nota)
print("numero (10) == valor (10)? ", numero == valor)

print('\n')

# Diferente - Verifica se a primeira variável é diferente que a segunda. 
print("Diferente !=")
print("nota (9) != valor (10)? ",nota != valor)
print("valor (10) != nota (9)? ", valor != nota)
print("numero (10)!= valor (10)? ", numero != valor)

print('\n')


# Como saber a diferença ente maior e menor?
# 
# É simples procure um 4 ou 7, olha só:
# 
# Maior > é parecido com o número 7
# 
# Menor < é parecido com o número 4

# ---
# 
#Laço condicional 1
# 
# ---
# Controle de Fluxo ou Estrutura de Decisão

# O controle de fluxo serve para orientar o programa a executar um código especifico dependendo da condição.
# 
# No Python existe só um (if), sendo assim muito mais simples de se trabalhar.
# 
# O "if" pode ser tradusido como "se"
# se for menor que 10 anos deve usar cadeirinha.
# se bebeu, não dirija.
# 
# O if terá a seguinte estrutura:
# 
# if <condição>:
# ....<ação se for verdadeiro>
# else:
# ....<ação se for falso>
# 
# 
# Os quatro pontinhos significa a identação. Ela é importante para determiar até aonde vai o código dentro do if.
# Se você sair desta identação o python irá entender que o if terminou.
# 
# O else irá executar somente se a <condição> for falsa. Só pode ter um else em cada if!
# 




#Exemplo 1:

# Faça um programa que peça 1 número e se este for maior que 10 mostre uma mensagem "Numero maior que 10",
# se for menor que 10 apareça a mensagem "Numero menor que 10"

numero = int(input("Digite um número: "))

if numero > 10: # Note que usamos os operadores de comparação para determinar a condição.
    print("Numero maior que 10") # Os quatro espaços da identação
else: # este else só irá execurar se o número for menor.
    print("Numero menor que 10")

print("Não estou identado enão estou fora do if!")





# Exemplo 2:
# Crie um programa que pessa uma senha para o usuário
# A senha deve ser AbrAcAdAbrA
# Se a senha for correta deve aparecer a mensagem: "Seja bem vindo"
# Se a senha for falsa, deve aparecer a mensagem: "Senha incorreta!"

senha_secreta = "AbrAcAdAbrA"

senha = input("Digite a sua senha: ")

if senha_secreta == senha:
    print("Seja bem vindo")
else:
    print("Senha incorreta!")





# Exemplo 3:
# Crie um programa que calcule a função "f = 3/x"
# Peça ao usuário que digite o valor de x
# Se o valor de x for igual a zero, o programa mostrará somente a mensagem final.
# Se x for diferente que zero, o programa fará a conta e mostrará o resultado.

x = int(input("Digite o valor de x: "))

if x != 0:
    f = 3/x
    print("O resultado é: ", f)

    # Note que não possui else. Nem sempre o else é necessário.

print("Fim do programa") # note que neste print não tem identação. Então ele não faz parte do input

