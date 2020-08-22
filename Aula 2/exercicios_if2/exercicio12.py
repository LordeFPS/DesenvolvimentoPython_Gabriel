# Exercicio 12
# 
# Crie um programa que peça 2 números.
# 
# Depois mostre um menu interativo contendo 5 operações matemáticas do python
# (adição, subtração, multiplicação, divisão e expoente)
# 
# Peça para o usuário escolher uma destas opções e mostre o resultado da operação escolhida.




while True:
    print("Pressione ENTER!")
    input()
    print('''
    ---- Selecione uma opção ----
    ----------- Menu ------------
    ---- (1) - Soma -------------
    ---- (2) - Subtração --------
    ---- (3) - Multiplicação ----
    ---- (4) - Divisão ----------
    ---- (5) - Expoente ---------
    ---- (6) - Sair -------------
    -----------------------------
    -----------------------------
    '''
    )
    menu = input("Escolha uma opção: ")

    if menu != '6':
        numero1 = int(input("Digite o 1º número: "))
        numero2 = int(input("Digite 0 2º número: "))
 
    if menu == '1':
        
        soma = numero1 + numero2

        print(f"Soma: {soma}")
    elif menu == '2':

        subtrai = numero1 - numero2

        print(f"Subtração: {subtrai}")
    elif menu == '3':

        multiplica = numero1 * numero2
        
        print(f"Multiplicação: {multiplica}")
    elif menu == '4':
        if numero2 == 0:
            print("Divisão por zero!")
        else:
            divide = numero1 / numero2
            print(f"Divisão: {divide}")
    elif menu == '5':
        
        expoente = numero1 ** numero2

        print(f"Expoente: {expoente}")
    elif menu == '6':
         
         print("Sair do programa!")
         break


    
    


