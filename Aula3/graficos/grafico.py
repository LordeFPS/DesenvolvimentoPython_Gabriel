import matplotlib.pyplot as plt


x = [i for i in range(1,7)]
y = [i for i in range(11,17)]

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 
         'Maio', 'Junho']
valores = [105235, 107697, 110256, 109236, 108859, 109986]

# plt.plot(meses, valores)
# plt.show()


plt.plot(meses, valores, color='green')
plt.bar(meses, valores, color='blue',)
plt.scatter(meses, valores, color='red') # Adiciona pontos vermelhos
# Mudar base de valores do eixo y
plt.ylim(100000, 120000)
# Titulo do gráfico
plt.title('Faturamento no primeiro semestre de 2017')
plt.xlabel('Meses')
plt.ylabel('Faturamento em R$')
plt.show()











# plt.plot(meses, valores, color='green')
# plt.bar(meses, valores, color='yellow',)
# plt.scatter(meses, valores, color='red') # Adiciona pontos vermelhos
# # Mudar base de valores do eixo y
# plt.ylim(100000, 120000)
# # Titulo do gráfico
# plt.title('Faturamento no primeiro semestre de 2017')
# plt.xlabel('Meses')
# plt.ylabel('Faturamento em R$')
# plt.show()


# plt.barh(meses, valores, color='yellow',)
# plt.show()

# plt.savefig('nome_da_imagem.png')
