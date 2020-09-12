# Este programa serve para podermos abrir arquivos
# O comando para abrir é o:
# open("arquivo.txt","r") 
# Usamos uma variável chamada arquivo para receber as
# informações lidas.


# arquivo = open(r"endereço\arquivo.txt","r")

# Dentro do opené passado 2 informações:
# Uma é o nome do arquivo que pode ser acompanahdo do
# seu endereço.

# A segunda é a forma de abertura do arquivo.

# r = read = leitura
# O r só serve para fazer a leitura do arquivo.

# a = appende = adicionar
# O a serve para adicionar novas linhas no final do arquivo

# w = write = escrever (escreve por cima)
# O w ele sobrescreve o arquivo por um novo com 
# as novas informações. Tem que tomar cuidado com ele!


arquivo = open(r"C:\Users\abioluz.behrend\Desktop\Aula Python\Desenvolvimento_Agil_em_Python_2_2020\aula3\sqlite3\pesquisa.csv","r")

#"2020/08/29 7:52:51 PM GMT-3","Abioluz","044333222000","4799999999","aa@aa.com","baia","302","","marmeleuiro","CamboriÃº","Arroz","18","M","1.69"

for pessoa in arquivo: # o for pega linha por linha
    pessoa = pessoa.replace('","','";"') # Primeiro tratamento para
    # trocar as , por ;
    pessoa = pessoa.replace('"','') # Segundo tratamento
    # para trocar as aspas por nada
    pessoa = pessoa.split(";") # Tranforma os dados em listas
    print (pessoa)
