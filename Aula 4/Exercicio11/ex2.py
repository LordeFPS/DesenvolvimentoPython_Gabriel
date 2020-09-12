# 2) Crie uma função que receba uma lista de qualquer 
# tamanho e retorne a média

def fprg_lista(p_lista):
    vloc_lista = []
    for i in range(p_lista):
        vloc_valor = int(input(f"Digite o {i + 1}º valor: "))
        vloc_lista.append(vloc_valor)
    
    vloc_soma = sum(vloc_lista)
    vloc_tamanho = len(vloc_lista)

    vloc_media = vloc_soma / vloc_tamanho

    return print(f"Media da lista é: {vloc_media}")

vprg_tamanho = int(input("Escolha o tamanho da lista: "))

fprg_lista(vprg_tamanho)

