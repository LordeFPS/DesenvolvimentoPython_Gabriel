# 1) Crie uma função que receba 3 notas por parâmetro e 
# retorne a média.

def fprg_media(p_media):
    vloc_soma = 0
    vloc_media = 0

    for i in range(p_media):
        vloc_nota = int(input(f"Digite {i + 1}ª nota: "))
        vloc_soma = vloc_soma + 1
        vloc_media = (vloc_media + vloc_nota)
    
    return print(f"Média: {vloc_media / vloc_soma}")


vprg_qtd_nota = int(input("Digite quantas notas quer inserir: "))

fprg_media(vprg_qtd_nota)
