
# Formula juros composto 
# dinheiro_a_receber = capita_inicial*(1+(juros/100))**tempo

def juros_composto(capita_inicial, juros, tempo):
    dinheiro_a_receber = capita_inicial*(1+(juros/100))**tempo
    return dinheiro_a_receber

cap_ini = float(input("Digite o valor emprestado: "))
juros_emprestimo = float(input("Digite a porcentagem de juros mensais: "))
tempo_empr = int(input("Digite o tempo"))

print(f"{juros_composto(cap_ini, juros_emprestimo, tempo_empr)}")