# Abrir arquivo ".txt" e recuperar dados salvos

vprg_arquivo = open(r"Aula 4\Manipulando_Aqruivos\arquivo_teste.txt","r")

for linha in vprg_arquivo:
    print(linha)
vprg_arquivo.close()