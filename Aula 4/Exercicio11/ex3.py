# 3) Crie 4 funções para as operações matemáticas (+, -, /, *)

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

fprg_soma(3,3)
fprg_subtrai(3,3)
fprg_divisao(3,3)
fprg_multiplica(3,3)