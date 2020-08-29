# calcular a circunferencia e a area de um circulo

import calculo_circulo


# calculo_circulo.fprg_area()

# calculo_circulo.fprg_circunferencia()


print('''
Calculo de um Circulo
'''
)

vprg_raio = int(input('Digite o valor do raio: '))

vprg_circunferencia = calculo_circulo.fprg_circunferencia(vprg_raio)
vprg_area = calculo_circulo.fprg_area(vprg_raio)

# print(f''' 
# Valor da Area: {calculo_circulo.fprg_area(vprg_raio)}m²

# Valor da Circunferencia: {calculo_circulo.fprg_circunferencia(vprg_raio)}m
# '''
# )

# Desse jeito fica melhor esteticamente ↓↓↓↓
print(f''' 
Valor da Area: {vprg_area}m²

Valor da Circunferencia: {vprg_circunferencia}m
'''
)