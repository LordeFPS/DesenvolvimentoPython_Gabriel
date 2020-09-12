# 1) Crie uma função que receba 3 notas por parâmetro e 
# retorne a média.

soma = 0
media = 0

for i in range (3):
    nota = input(f"Digite {i+1}ª nota: ")
    soma = soma + 1
    media = (nota + media) / soma

print(nota)


# for i in range(10):
#     print("Ola mundo")