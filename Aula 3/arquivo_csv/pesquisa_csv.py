import matplotlib.pyplot as plt

# O metodo novo para este exercico é o .replace('{velho}','{novo}') - O velho
# é um caracter que queira substituir e o novo é o caracter que deseja incluir.

def abrir(endereco):
    arquivo = open(endereco,'r')
    lista_cadastro = []
    cont=0
    for pessoa in arquivo:
        if cont == 0:
            cont += 1
            continue
        pessoa = pessoa.replace('","',";")
        pessoa = pessoa.replace('"',"")    
        pessoa = pessoa.strip()
        pessoa = pessoa.split(';')
        lista_cadastro.append(pessoa)
    arquivo.close()
    return lista_cadastro


# clientes = abrir("aula4/exercicios/Pesquisa de Gostos.csv")

clientes = abrir("Pesquisa de Gostos.csv")
for i in clientes:
    print(i)

