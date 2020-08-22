# Exercicio 13

# Crie um programa que peça o nome do cliente, idade, endereço, email e telefone.

# Depois crie um menu interativo com as seguintes opções: Dados, Endereço, Contato.

# Se o usuário selecionar "Dados" deve aparecer o nome do cliente e a idade

# Se o usuário selecionar "Endereço" deve aparecer o nome do cliente e o endereço

# Se o usuário selecionar "Contato" deve aparecer o nome do cliente, email e o telefone

nome_cliente = input("Nome: ")
idade_cliente = input("Idade: ")
endereco_cliente = input("Endereço: ")
email_cliente = input("Email: ")
telefode_cliente = input("Telefone: ")

saida_sim = 'S'
saida_nao = 'N'

while True:
    saida = input("Desenha continuar(S/N): ").upper
    if saida == saida_sim:
    # print("Press ENTER!")
    # input()
    
        print('''
        ------- STATUS -------
        -- (1) - Dados      --
        -- (2) - Endereço   --
        -- (3) - Contato    --
        -- (4) - Sair       --
        ----------------------
        '''
        )

        opcao = input("Digite uma opção: ")

        if opcao == '1':
            print(f"""
            Nome: {nome_cliente}
            Idade: {idade_cliente}
            """    
            )
        elif opcao == '2':
            print(f"""
            Nome: {nome_cliente}
            Endereço: {endereco_cliente}
            """    
            )
        elif opcao == '3':
            print(f"""
            Nome: {nome_cliente}
            Email: {email_cliente}
            Telefode: {telefode_cliente}
            """    
            )
        elif opcao == '4':
            print("Saiu do programa!")
            break
    elif saida == saida_nao:
        print("Saiu do programa!")
        break

