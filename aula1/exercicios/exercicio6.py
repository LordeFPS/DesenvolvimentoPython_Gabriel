# Crie um programa que solicite ao cliente
# o nome do produto
# o preço do produto
# a quantidade
# e mostre usando o f-string

nomedoproduto = input("Digite o nome do produto: ")
precodoproduto = float(input("Digite o preço do produto: "))
quantidade = int(input("Digite a quantidade: "))

print(f'''
Nome do produto: {nomedoproduto} 
Preço do produto: {precodoproduto}
Quantidade: {quantidade}
Preço total: {precodoproduto*quantidade:.2f}''') 
# :.2f significa 2 casas depois da virgula e o f significa float
