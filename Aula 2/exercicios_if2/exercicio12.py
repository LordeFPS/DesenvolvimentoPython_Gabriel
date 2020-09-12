# Exercicio 12
# 
# Crie um programa que peça 2 números.
# 
# Depois mostre um menu interativo contendo 5 operações matemáticas do python
# (adição, subtração, multiplicação, divisão e expoente)
# 
# Peça para o usuário escolher uma destas opções e mostre o resultado da operação escolhida.



menu = """
Menu interativo opreações matemáticas:

1) Soma:
2) Subtração:
3) Divisão:
4) Multiplicação:
5) Expoente:
6) sair

digite a opção desejada: """

while True:
    opcao = input(menu)
    
    # if opcao != '6':
    #     num_1 = int(input("Digite um número: "))
    #     num_2 = int(input("Digite outro número: "))

    num_1 = int(input("Digite um número: "))
    num_2 = int(input("Digite outro número: "))
    
    if opcao == '1':
        soma = num_1 + num_2
        print(soma)
    elif opcao == "2":
        subtracao = num_1 - num_2
        print(subtracao)
    elif opcao == "3":
        if num_2 == 0:
            print("Divisão não pode ser feita")
        else:
            divisao = num_1 / num_2
            print(divisao)
    elif opcao == "4":
        multiplicacao = num_1 * num_2
        print(multiplicacao)
    elif opcao == "5":
        expoente = num_1 ** num_2
        print(expoente)
    elif opcao == '6':
        print("Fim do programa")
        break