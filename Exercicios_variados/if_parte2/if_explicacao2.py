# ---
# 
#Laço condicional 2
# 
# ---
# Laço condicional aninhado

# As vezes necesitamos mais condições para o mesmo problema.
# 
# Para isso existe 1 solução o "elif"
# 
# O elif fica aninhado (dentro) do if e é executado somente se a sua condição for verdadeira.
# 
# if <condição1>:
# ....<ação>
# elif <condição2>:
# ....<ação>
# else:
# ....<ação se falso>
# 
# Pode se adicionado quantos elif forem necessário dentro do if. Só lembrando que cada if só pode ter um else!
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
# Se o cliente digitar A deve aparecer a seguinte mendagem: "Primeira classe, caviar liberado!"
# Se o cliente digitar B deve aparecer a seguinte mendagem: "Segunda classe, Café e almoço liberado"
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
# Se ele escolher Prato Feito deve aparecer a seguinte mensage: "1 Prato feito saindo em 15 minutos"
# Se ele escolher Fejoada deve aparecer a seguinte mensage: "1 Fejoada saindo em 30 minutos"
# Se ele escolher Macarronada deve aparecer a seguinte mensage: "1 Macarronada saindo em 10 minutos"

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

