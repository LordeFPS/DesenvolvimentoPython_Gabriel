# arquivo = open(r"endereço", "r")
# r = read = leitura
# a = append = adicionar
# w = write = escrever (escreve por cima)


arquivo = open(r"C:\Users\69146\Desktop\Desenvolvimento Agil Python\DesenvolvimentoPython_Gabriel_2020\Aula3\Projeto\sqlite3\Pesquisa.csv","r")


for pessoa in arquivo:
    print(pessoa)