# calcular a circunferencia e a area de um circulo

def fprg_area(Raio):
    Pi = 3.14
    A = Pi * (Raio**2)
    return A

def fprg_circunferencia(Raio):
    Pi = 3.14
    C = 2 * Pi * Raio
    return C

print('''
Calculo de um Circulo
'''
)

vprg_raio = int(input('Digite o valor do raio: '))

print(f''' 
Valor da Area: {fprg_area(vprg_raio)}m²

Valor da Circunferencia: {fprg_circunferencia(vprg_raio)}m
'''
)