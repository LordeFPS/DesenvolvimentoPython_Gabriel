# Crie um programa que solicite ao cliente
# o nome do produto
# o preço do produto
# a quantidade
# e mostre usando o f-string

nom_produto = str(input("Nome do produto: ")) 
prc_produto = float(input("Preço do prouto: R$"))
qnt_produto = int(input("Quantidade do produto: "))

print("Status do Produto")
print(f"Nome: {nom_produto}\nPreço: R${prc_produto*qnt_produto}\nQuantidade: {qnt_produto}")