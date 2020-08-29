#! /bin/python3
import sqlite3
conexao = sqlite3.connect("email.bd") #Cria o banco de dados
cursor = conexao.cursor() # Cria um cursor

comando_sql = "código sql" # Digite o comando sql desejado

cursor.execute(comando_sql) # Carrega o comando sql
conexao.commit() # Aplica o comando sql
id_inserido = cursor.lastrowid # Recupera o id do ultimo registro cadastrado.

dados = cursor.fetchall() #recupera os dados quando pesquisado no banco de dados.

conexao.close()

##############################
Criar Listar todos -> "SELECT * FROM 01_MDG_ENDERECO"
Listar id          -> f"SELECT * FROM 01_MDG_ENDERECO WHERE ID = {id}"
Salvar             -> f""" INSERT INTO 01_MDG_ENDERECO
        (
            LOGRADOURO,
            NUMERO,
            COMPLEMENTO,
            BAIRRO,
            CIDADE,
            CEP
        )
        VALUES
        (
            '{endereco.logradouro}',
            '{endereco.numero}',
            '{endereco.complemento}',
            '{endereco.bairro}',
            '{endereco.cidade}',
            '{endereco.cep}'
        )"""
Alterar            -> f""" UPDATE 01_MDG_ENDERECO
        SET
            LOGRADOURO = '{endereco.logradouro}',
            NUMERO = '{endereco.numero}',
            COMPLEMENTO = '{endereco.complemento}',
            BAIRRO = '{endereco.bairro}',
            CIDADE = '{endereco.cidade}',
            CEP = '{endereco.cep}'
        WHERE ID = {endereco.id}
        """
deletar            -> f"DELETE FROM 01_MDG_ENDERECO WHERE ID = {id}"
