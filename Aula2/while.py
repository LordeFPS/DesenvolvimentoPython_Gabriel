# while <condição>: # só vai executar se a condição for True
#     continue # Vai voltar para o inici do loop
#     break # Termina o loop

# exemplo: 
# printe na tela números de 0 a 10

# # Forma 1: A mais correta
# numero = 0
# while numero <= 11:
#     print(numero)
#     numero = numero + 1


# #Forma 2 - A mais usada
# numero = 0
# while True:
#     print(numero)
#     numero = numero + 1
#     if numero == 11:
#         break

# Este é para lembrar que o while só funciona quando verdadeiro
# O loop infinito do While True
numero = 0
while True:
    print(numero)
    numero = numero + 1
