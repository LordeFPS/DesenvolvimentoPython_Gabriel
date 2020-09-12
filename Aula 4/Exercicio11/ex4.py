# 4) Crie um programa que peça 2 números. 
# Depois crie um menu interativo que peça qual 
# operação matemática deseja realizar (+, -, /, *). 
# Utilize as funções criadas no exercício anterior e
# mostre o resultado da operação escolhida. 

import os     # importa uma opção para limpar a tela

import time   # importa opções de timer 

def fprg_soma(p_valor1 , p_valor2):
    vloc_soma = p_valor1 + p_valor2

    return print(f"Soma entre {p_valor1} e {p_valor2} é: {vloc_soma}")

def fprg_subtrai(p_valor1 , p_valor2):
    vloc_subtrai = p_valor1 - p_valor2

    return print(f"Sbtração entre {p_valor1} e {p_valor2} é: {vloc_subtrai}")

def fprg_divisao(p_valor1 , p_valor2):
    if p_valor2 == 0:
        print("Divisão inválida")
    else:
        vloc_divisao = p_valor1 / p_valor2
    
    return print(f"Divisão entre {p_valor1} e {p_valor2} é: {vloc_divisao}")

def fprg_multiplica(p_valor1 , p_valor2):
    vloc_multiplica = p_valor1 * p_valor2

    return print(f"Multiplicação entre {p_valor1} e {p_valor2} é: {vloc_multiplica}")

def pprg_menu():
    print('''
    *********** MENU *********** 
    *** [1] - SOMA           ***
    *** [2] - SUBTRAÇÃO      ***
    *** [3] - MULTIPLICAÇÃO  ***
    *** [4] - DIVISÃO        ***
    *** [5] - SAIR           ***
    ****************************
    '''
    )


def pprg_tlimpa(): # cria um  um procedimento que executa o código abaixo 
    
    time.sleep(2) # conseguimos fazer um temporizador de tela
    
    os.system('cls' if os.name == 'nt' else 'clear') # com esse código conseguimos limpar a tela

while True:
    
    pprg_menu()
    vprg_menu = input("Escolha uma opção: ")

    if vprg_menu >= '1' and vprg_menu <= '4' :
        vprg_valor1 = int(input("Digite 1º valor: "))
        vprg_valor2 = int(input("Digite 2º valor: "))
    # elif vprg_menu <= '4':
    #     vprg_valor1 = input("Digite 1º valor: ")
    #     vprg_valor2 = input("Digite 2º valor: ")

    if vprg_menu == '1':
        fprg_soma(vprg_valor1,vprg_valor2)
    elif vprg_menu == '2':
        fprg_subtrai(vprg_valor1,vprg_valor2)
    elif vprg_menu == '3':
        fprg_multiplica(vprg_valor1,vprg_valor2)
    elif vprg_menu == '4':
        fprg_divisao(vprg_valor1,vprg_valor2)
    elif vprg_menu == '5':
        print("Você saiu do programa!")
        break
    else:
        print("Opção inválida!")
    
    pprg_tlimpa()