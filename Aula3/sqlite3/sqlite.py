
import sqlite3
conexao = sqlite3.connect(r"C:\Users\abioluz.behrend\Desktop\Aula Python\Desenvolvimento_Agil_em_Python_2_2020\aula3\sqlite3\pesquisa2.db") #Cria o banco de dados
cursor = conexao.cursor() # Cria um cursor

cliente = """CREATE TABLE Clientes (
	id INTEGER NOT NULL,
	nome TEXT,
	cpf TEXT,
	telefone TEXT,
	email TEXT,
	id_endereco INTEGER,
	CONSTRAINT Clientes_PK PRIMARY KEY (id),
	CONSTRAINT Clientes_FK FOREIGN KEY (id_endereco) REFERENCES Endereco(id)
);
"""

endereco = '''CREATE TABLE Endereco (
	id INTEGER NOT NULL,
	rua TEXT,
	complemento TEXT,
	numero INTEGER,
	bairro TEXT,
	cidade INTEGER,
	CONSTRAINT Endereco_PK PRIMARY KEY (id)
);
'''
respostas = '''
CREATE TABLE Respostas (
	id INTEGER NOT NULL,
	pergunta1 TEXT,
	pergunta2 TEXT,
	pergunta4 TEXT,
	pergunta TEXT,
	id_cliente INTEGER NOT NULL,
	CONSTRAINT Respostas_PK PRIMARY KEY (id),
	CONSTRAINT Respostas_FK FOREIGN KEY (id_cliente) REFERENCES Clientes(id)
);'''


cursor.execute(endereco) # Carrega o comando sql
conexao.commit() # Aplica o comando sql
cursor.execute(cliente)
conexao.commit()
cursor.execute(respostas)
conexao.commit()

conexao.close()








# comando_sql = "create table" # Digite o comando sql desejado

# cursor.execute(comando_sql) # Carrega o comando sql
# conexao.commit() # Aplica o comando sql
# id_inserido = cursor.lastrowid # Recupera o id do ultimo registro cadastrado.

# dados = cursor.fetchall() #recupera os dados quando pesquisado no banco de dados.

# conexao.close()

# ##############################
# Criar Listar todos -> "SELECT * FROM 01_MDG_ENDERECO"
# Listar id          -> f"SELECT * FROM 01_MDG_ENDERECO WHERE ID = {id}"
# Salvar             -> f""" INSERT INTO 01_MDG_ENDERECO
#         (
#             LOGRADOURO,
#             NUMERO,
#             COMPLEMENTO,
#             BAIRRO,
#             CIDADE,
#             CEP
#         )
#         VALUES
#         (
#             '{endereco.logradouro}',
#             '{endereco.numero}',
#             '{endereco.complemento}',
#             '{endereco.bairro}',
#             '{endereco.cidade}',
#             '{endereco.cep}'
#         )"""
# Alterar            -> f""" UPDATE 01_MDG_ENDERECO
#         SET
#             LOGRADOURO = '{endereco.logradouro}',
#             NUMERO = '{endereco.numero}',
#             COMPLEMENTO = '{endereco.complemento}',
#             BAIRRO = '{endereco.bairro}',
#             CIDADE = '{endereco.cidade}',
#             CEP = '{endereco.cep}'
#         WHERE ID = {endereco.id}
#         """
# deletar            -> f"DELETE FROM 01_MDG_ENDERECO WHERE ID = {id}"
