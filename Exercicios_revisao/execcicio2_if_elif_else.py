###############################################################################

# Operadores de comparação


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
print("numero (10) > valor (10)? ", numero > valor) # Note que 10 não é maior que 
                                                    # 10 por isso será falso.

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
print("numero (10) < valor (10)? ", numero < valor) # Note que 10 não é menor que 
                                                    # 10 por isso será falso.

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

###############################################################################


# Laço condicional 1

# Controle de Fluxo ou Estrutura de Decisão

# O controle de fluxo serve para orientar o programa a executar um código especifico 
# dependendo da condição.
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
# Os quatro pontinhos significa a identação. Ela é importante para determiar até aonde 
# vai o código dentro do if.
# Se você sair desta identação o python irá entender que o if terminou.
# 
# O else irá executar somente se a <condição> for falsa. Só pode ter um else em cada if!
# 


#Exemplo 1:

# Faça um programa que peça 1 número e se este for maior que 10 mostre uma mensagem 
# "Numero maior que 10",
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

print("Fim do programa") # note que neste print não tem identação. Então ele não faz 
                         # parte do input

###############################################################################

# Laço condicional aninhado

# As vezes necesitamos mais condiçõe. Uma forma de se fazer isso é adicionar mais if. 
# Porem adicionar mais if significa mais consumo de processamento, 
# pois cada if será executado de forma independnete. Para isso usamos o elif, 
# poupando o usu de processador pois quando um elif os outros que sobraram não 
# são processados.
#
 
# O elif fica aninhado (dentro) do if e é executado somente se a sua condição for 
# verdadeira.
# 
# if <condição1>:
# ....<ação>
# elif <condição2>:
# ....<ação>
# else:
# ....<ação se falso>
# 
# Pode se adicionado quantos elif forem necessário dentro do if. Só lembrando que cada 
# if só pode ter um else!
# 
# if <condição1>:
# ....<ação>
# elif <condição2>:
# ....<ação>
# elif <condição3>:
# ....<ação>
# elif <condição4>:
# ....<ação>
# else:
# ....<ação se falso>
# 




# Exemplo 1:
# Faça um programa que peça a classe de embarque de uma compania aéria.
# As opções são A, B e C
# Se o cliente digitar A deve aparecer a seguinte mendagem: 
# "Primeira classe, caviar liberado!"
# Se o cliente digitar B deve aparecer a seguinte mendagem: 
# "Segunda classe, Café e almoço liberado"
# Se o cliente digitar C deve aparecer a seguinte mendagem: 
# "Terceira classe, pacotinho de bolacha 10g por pessoa liberado"
# Caso digite qualquer coisa deve aparecer a seguinte mendagem: "Opção inválida"

passagem = input("Digite a classe de embarque A,B ou C?: ")

if passagem == "A":
    print("Primeira classe, caviar liberado!")
elif passagem == "B":
    print("Segunda classe, Café e almoço liberado")
elif passagem == "C":
    print("Terceira classe, pacotinho de bolacha 10g por pessoa liberado")
else:
    print("Opção inválida")
    
# Note que ao ser selecionado uma condição o laço condicional termina.



# Exemplo 2:
# Faça um menu interativo que possua 3 opções: Prato feito, Fejoada, Macarronada
# Peça para o usuário digitar a opção desejada.
# Se ele escolher Prato Feito deve aparecer a seguinte mensage: 
# "1 Prato feito saindo em 15 minutos"
# Se ele escolher Fejoada deve aparecer a seguinte mensage: 
# "1 Fejoada saindo em 30 minutos"
# Se ele escolher Macarronada deve aparecer a seguinte mensage: 
# "1 Macarronada saindo em 10 minutos"

mensagem = '''
Cardapio do dia:]

1) Prato feito
2) Fejoada
3) Macarronada

Digite a opção desejada: '''

opcao = input(mensagem)

if opcao == '1':
    print("1 Prato feito saindo em 15 minutos")
elif opcao == '2':
    print("1 Fejoada saindo em 30 minutos")
elif opcao == '3':
    print("1 Macarronada saindo em 10 minutos")
else:
    print("Opção invalida")

###############################################################################

# Exercícios if, else, operdores de comparação:

# Exercicio 1
# Faça um programa que peça 2 numeros inteiros e mostre o maior deles.


# Exercicio 2
# Faça um programa que peça a idade do cliente.
# Se ele tiver 18 anos ou mais deve aparecer a mensagem "Entrada permitida"
# Caso contrário deve aparecer a mensagem "Entrada Negada!"

# Exercicio 3
# Escreva um programa que peça a nota de um aluno
# Se a nota for 7 ou mais deve aparecer a mensagem: "Aprovado"
# Caso contrário deve aparecer a mensagem: "Reprovado"

###############################################################################

# Exercícios if, elif, else, operdores de comparação:


# Exercicio 4
# Faça um programa que peça o sexo do cliente. 
# Se o cliente digitar 'F' deve aparecer a mensagem "Como você está bonita hoje!"
# Se o cliente digitar 'M' deve aparecer a mensagem "Como você está forte? andou malhando?"
# Se o cliente digitar qualquer outra coisa, deve aparecer a mensagem: "opção invalida!"
# 

# Exercicio 5
# 
# Crie um programa que peça 2 números.
# Depois mostre um menu interativo contendo 5 operações matemáticas do python
# (adição, subtração, multiplicação, divisão e expoente)
# Peça para o usuário escolher uma destas opções e mostre o resultado da operação
# escolhida.



# Exercicio 6
# Crie um programa que peça ao usuário digitar um número de 1 a 7 e 
# mostre o dia da semana correspondente sendo que segunda feira é o 
# numero 1 e domingo é 7.