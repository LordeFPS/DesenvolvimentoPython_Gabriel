# funções para manipular arquivos

def fprg_adiciona(p_arquivo,p_texto): # cria um arquivo txt
    ''' Cria um arqivo .txt'''
    vloc_arquivo = open(f"Aula 4\\Exercicio13\\{p_arquivo}.txt","a")
    vloc_arquivo.write(p_texto)
    vloc_arquivo.close()

#def fprg_esreve():

if __name__ == "__main__": # medida de segurança
    
    vprg_arquivo = 'teste2'
    vprg_texto = '''
    TESTE
    '''
    fprg_adiciona(vprg_arquivo,vprg_texto)

