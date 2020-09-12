def salvar(texto): 
    # função para salvar o texto
    arquivo = open("Aula 4/nomes.txt","a")
    arquivo.write(texto)
    arquivo.close()

def abrir(): 
    arquivo = open("Aula 4/nomes.txt","r")
    for i in arquivo:
        print(i)

lista_nome = []

for i in range(5):
    nome = input(f"Digite o nome {i+1}: ")
    salvar(f"{nome}\n")

abrir()