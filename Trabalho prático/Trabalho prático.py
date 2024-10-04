import re
    
def coletar_dados_e_salvar():
    # Cria uma lista vazia
    lista = []
    # Solicita ao usuário que insira elementos na lista
    while True:
        item = input("Digite um nome para adicionar à lista (ou 'sair' para encerrar): ")
        # Verifica se o usuário quer parar
        if item.lower() == 'sair':
            break
        # Adiciona o item à lista
        lista.append(item)
    # Nome do arquivo onde os dados serão armazenados
    nome_arquivo = 'dados_users.txt'
    # Abre o arquivo em modo de escrita e salva os dados
    with open(nome_arquivo, 'w') as arquivo:
        for item in lista:
            arquivo.write(f'{item}\n')
    print(f'Dados salvos em {nome_arquivo} com sucesso!')

def imprimir_dados_arquivo():
    # Nome do arquivo que será lido
    nome_arquivo = 'dados_users.txt'
    try:
        # Abre o arquivo em modo de leitura
        with open(nome_arquivo, 'r') as arquivo:
            # Lê todas as linhas do arquivo
            conteudo = arquivo.readlines()
        # Verifica se o arquivo está vazio
        if not conteudo:
            print(f'O arquivo {nome_arquivo} está vazio.')
        else:
            print(f'Conteúdo do arquivo {nome_arquivo}:')
            for linha in conteudo:
                print(linha.strip())  # Imprime cada linha removendo espaços em branco extras
    except FileNotFoundError:
        print(f'O arquivo {nome_arquivo} não foi encontrado.')

def excluir_elemento_por_indice():
    # Nome do arquivo
    nome_arquivo = 'dados_users.txt'
    try:
        # Abre o arquivo em modo de leitura para carregar a lista
        with open(nome_arquivo, 'r') as arquivo:
            lista = arquivo.readlines()
        # Remove os espaços extras (quebra de linha) de cada item
        lista = [item.strip() for item in lista]
        # Verifica se a lista está vazia
        if not lista:
            print(f'O arquivo {nome_arquivo} está vazio.')
            return
        # Exibe a lista para o usuário
        print("Lista atual:")
        for i, item in enumerate(lista):
            print(f'{i}: {item}')
        # Solicita o índice do elemento a ser removido
        try:
            indice = int(input("Digite o índice do elemento que deseja excluir: "))
            # Verifica se o índice é válido
            if 0 <= indice < len(lista):
                elemento_removido = lista.pop(indice)
                print(f'Elemento "{elemento_removido}" removido com sucesso!')
                # Reescreve o arquivo sem o elemento removido
                with open(nome_arquivo, 'w') as arquivo:
                    for item in lista:
                        arquivo.write(f'{item}\n')
                print(f'O arquivo {nome_arquivo} foi atualizado.')
            else:
                print(f'Índice inválido. O índice deve estar entre 0 e {len(lista)-1}.')
        except ValueError:
            print('Por favor, insira um número válido para o índice.')
    except FileNotFoundError:
        print(f'O arquivo {nome_arquivo} não foi encontrado.')

def salvar_produtos_servicos_usuario():
    # Cria uma lista vazia para armazenar os produtos/serviços
    produtos_servicos = []
    while True:
        # Solicita ao usuário para adicionar um produto ou serviço
        item = input("Digite o nome do produto ou serviço (ou 'sair' para finalizar): ")
        if item.lower() == 'sair':
            break  # Sai do loop se o usuário digitar 'sair'
        produtos_servicos.append(item)  # Adiciona o item à lista
    # Verifica se a lista não está vazia antes de salvar
    if produtos_servicos:
        # Abre o arquivo em modo de escrita e salva a lista
        with open("produtos_serviços.txt", "w") as arquivo:
            for item in produtos_servicos:
                arquivo.write(item + "\n")

def ler_produtos_servicos():
    try:
        # Abre o arquivo em modo de leitura
        with open("produtos_serviços.txt", "r") as arquivo:
            # Lê todas as linhas do arquivo
            produtos_servicos = arquivo.readlines()
        # Verifica se o arquivo está vazio
        if produtos_servicos:
            print("Produtos e Serviços salvos:")
            for item in produtos_servicos:
                print(item.strip())  # Imprime cada item removendo quebras de linha
        else:
            print("O arquivo está vazio.")
    except FileNotFoundError:
        print("O arquivo 'produtos_serviços.txt' não foi encontrado. Certifique-se de que ele foi criado.")

def excluir_item_por_indice():
    try:
        # Abre o arquivo e lê os itens
        with open("produtos_serviços.txt", "r") as arquivo:
            produtos_servicos = arquivo.readlines()
        # Verifica se o arquivo contém itens
        if not produtos_servicos:
            print("O arquivo está vazio.")
            return
        # Exibe os itens ao usuário com seus índices
        print("Itens disponíveis:")
        for i, item in enumerate(produtos_servicos, 1):
            print(f"{i}. {item.strip()}")
        # Solicita ao usuário qual índice deseja excluir
        try:
            indice_excluir = int(input("Digite o número do item que deseja excluir: ")) - 1
            # Verifica se o índice é válido
            if 0 <= indice_excluir < len(produtos_servicos):
                item_excluido = produtos_servicos.pop(indice_excluir)
                # Reescreve o arquivo sem o item excluído
                with open("produtos_serviços.txt", "w") as arquivo:
                    for item in produtos_servicos:
                        arquivo.write(item)
                print(f"Item '{item_excluido.strip()}' excluído com sucesso.")
            else:
                print(f"Índice inválido. Digite um número entre 1 e {len(produtos_servicos)}.")
        except ValueError:
            print("Por favor, insira um número válido.")
    except FileNotFoundError:
        print("O arquivo 'produtos_serviços.txt' não foi encontrado. Certifique-se de que ele foi criado.")

def permitions(user):
    if user == "gerente":
        print("1-Visualizar serviços e produtos")
        print("2-Criar serviços e produtos")
        print("3-Excluir serviços e produtos")
        print("4-visualizar dados dos usuarios")
        print("5-Criar dados de usuarios")
        print("6-Excluir dados de usuarios")

    elif user == "funcionario":
        print("1-Visualizar serviços e produtos")
        print("2-Criar serviços e produtos")
        print("3-Excluir serviços e produtos")
    elif user == "cliente":
        print("1-Visualizar serviços e produtos")

def navegation(nav):
    if nav==0:
        exit
    elif nav==1:
        return ler_produtos_servicos()
    elif nav==2:
        return salvar_produtos_servicos_usuario()
    elif nav==3:
        return excluir_item_por_indice()
    elif nav==4:
        return imprimir_dados_arquivo()
    elif nav==5:
        coletar_dados_e_salvar()
    elif nav==6:
        excluir_elemento_por_indice()


def security(user, senha):
    user = user.lower()
    if user == "gerente" and senha == "All123**":
        print("acesso liberado")
    elif user == "funcionario" and senha == "half12**":
        print("acesso liberado")
    elif user == "cliente" and senha == "view12**":
        print("acesso liberado")
    else:
        print("Usuario ou senha incorretos")
    exit

dados = "dados.txt"
usuario = input("Digite a sua classe de usuario: ")
senha = input ("Digite sua senha: ")
resp = security(usuario, senha)
print("MENU")
permitions(usuario)
print("Digite 0 se quiser sair")
nav = int(input("digite o número da opção que deseja usar "))
navegation(nav)


