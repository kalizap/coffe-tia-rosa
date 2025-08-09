# importando as listas
from servicos import clientes, produtos, pedidos 

# Importando as classes
from client_class import Cliente 
from produto_class import Produto
from pedidos_class import Pedidos

# Colocando dados já prontos de clientes
dados_clientes = [
    {"nome": "Ana Paula", "cpf": "11122233344"},
    {"nome": "Bruno Martins", "cpf": "22233344455"},
    {"nome": "Carla Souza", "cpf": "33344455566"},
    {"nome": "Diego Silva", "cpf": "44455566677"},
    {"nome": "Elisa Ramos", "cpf": "55566677788"},
    {"nome": "Fábio Lima", "cpf": "66677788899"},
    {"nome": "Giovana Costa", "cpf": "77788899900"},
    {"nome": "Hugo Tavares", "cpf": "88899900011"},
    {"nome": "Isabela Rocha", "cpf": "99900011122"},
    {"nome": "João Pedro", "cpf": "00011122233"},
]
# Convertendo os dados do dicionário para a classe Cliente
for dado in dados_clientes:
    cliente = Cliente(dado['nome'], dado['cpf'])
    clientes.append(cliente)

# Colocando dados já prontos de produtos
dados_produtos = [
    {
        "nome": "Café Espresso",
        "ingredientes": ["Café espresso"],
        "preco": 4.00
    },
    {
        "nome": "Café com Leite",
        "ingredientes": ["Café espresso", "Leite vaporizado"],
        "preco": 5.50
    },
    {
        "nome": "Capuccino",
        "ingredientes": ["Café espresso", "Leite vaporizado", "Chocolate", "Canela"],
        "preco": 6.50
    },
    {
        "nome": "Mocha Gelado",
        "ingredientes": ["Café espresso", "Gelo", "Leite", "Calda de chocolate"],
        "preco": 7.00
    },
    {
        "nome": "Chá de Hibisco",
        "ingredientes": ["Flores de hibisco", "Água quente", "Limão", "Mel"],
        "preco": 5.00
    },
    {
        "nome": "Bolo de Cenoura",
        "ingredientes": ["Farinha", "Cenoura", "Ovos", "Cobertura de chocolate"],
        "preco": 6.00
    },
    {
        "nome": "Pão de Queijo",
        "ingredientes": ["Polvilho", "Queijo", "Leite"],
        "preco": 3.50
    },
    {
        "nome": "Croissant",
        "ingredientes": ["Farinha", "Manteiga", "Ovos"],
        "preco": 5.00
    }
]
# Convertendo os dados do dicionário para a classe Produto
for dado in dados_produtos:
    produto = Produto(dado['nome'], dado['ingredientes'], dado['preco'])
    produtos.append(produto)

#Colocando dados já prontos de pedidos
dados_pedidos = [
    {
        "cliente": clientes[0],
        "produtos": [produtos[0], produtos[2]],
        "id_nf": 1
    },
    {
        "cliente": clientes[1],
        "produtos": [produtos[1]],
        "id_nf": 2
    },
    {
        "cliente": clientes[2],
        "produtos": [produtos[3], produtos[4]],
        "id_nf": 3
    },
    {
        "cliente": clientes[3],
        "produtos": [produtos[6], produtos[0]],
        "id_nf": 4
    },
    {
        "cliente": clientes[4],
        "produtos": [produtos[5], produtos[1]],
        "id_nf": 5
    }
]
# Converte os dicionários em objetos Pedidos
for pedido in dados_pedidos:
    novo_pedido = Pedidos(pedido["cliente"], pedido["produtos"], pedido["id_nf"])
    pedidos.append(novo_pedido)


# criação da função de título
def titulo(msg):
    print('\n' + '*-' * 30)
    print(msg.upper().center(60))
    print('*-' * 30 + '\n')


# criação da função de erro
def erro(msg):
    print(f'>>> {msg}', end='')
    

# criação da função sucesso
def sucesso(msg):
    print(f'+++ {msg}', end='')


# =-=-=-=-=-=-=-=-=-=-=-=  FUNÇÕES CLIENTES  =-=-=-=-=-=-=-=-=-=-=-=

# Função de ver a lista de clientes
def ver_clientes():
    titulo('Clientes cadastrados')
    if not clientes:
        erro('Nenhum cliente cadastrado.')
        return

    for cliente in clientes:
        print(f'{cliente.nome}')
        print(f'    CPF: {cliente.cpf}')
        print('*~~' * 20)
#ver_clientes()

# Função de cadastro de clientes
def cadastro_de_clientes():
    titulo('Cadastro de Clientes')

    while True:
        # o nome  do cliente é pedido
        # tranformado para title
        # verificado se não está vazio    
        nome = input('Nome do cliente: ').strip().title()
        if nome == "":
            erro('O nome não pode estar vazio!\n')
        else:
            break

    while True:
        # o cpf do cliente é pedido
        # verificado se já existe na lista de clientes
        # se não existir, verificado se é um número
        # se não for um número ou não tiver 11 dígitos, é pedido novamente
        # se passar pela verificação uma variavel cliente é criada
        # e adicionada na lista de clientes
        cpf = input('CPF (somente números): \n').strip()
        jatem_cpf = False
        for c in clientes:
            if c.cpf == cpf:
                erro('CPF já cadastrado!\n')
                jatem_cpf = True
                break
        if jatem_cpf:
            continue
        elif not cpf.isdigit() or len(cpf) != 11:
            erro('Formato de CPF inválido!\n')
        else:
            novo_cliente = Cliente(nome, cpf)
            clientes.append(novo_cliente)
            sucesso(f'O cliente "{nome}" com o CPF "{cpf}" foi registrado com sucesso!\n')
            break
#cadastro_de_clientes()

# Função de menu da parte de clientes
def menu_clientes():
    while True:
        titulo('Menu Clientes')
        print('1 - Clientes Cadastrados')
        print('2 - Cadastrar Novo Cliente')
        print('9 - Voltar ao menu principal')
        opcao = input('Escolha uma opção: ').strip()

        if opcao == '1':
            ver_clientes()
        elif opcao == '2':
            cadastro_de_clientes()
        elif opcao == '9':
            print('Ainda em construção!')
            break
        else:
            erro('Opção inválida. Tente novamente.\n')
#menu_clientes()

#  =-=-=-=-=-=-=-=-=-=-=-=  FUNÇÕES PRODUTOS  =-=-=-=-=-=-=-=-=-=-=-=
# Função de ver o cardápio
def ver_cardapio():
    titulo('Cardápio')
    if not produtos:
        print('Nenhum produto cadastrado.')
    for p in produtos:
        print(f' Produto: {p.nome_pro}')
        print(f'    Preço: R$ {p.preco:.2f}')
        print(f'    Ingredientes: {", ".join(p.ingredientes)}')
        print('*~~' * 20)
#ver_cardapio()

# Função de cadastro de produtos
def cadastro_produto():
    titulo('Cadastro de Produto')

    while True:
        nome = input('Adicione o nome do produto:\n').strip().title()
        if nome == "":
            erro('O nome não pode estar vazio!\n')
        else:
            break

    while True:
        ingred_input = input('\nIngredientes separados por vírgula:\n').strip().title()
        if ingred_input == "":
            erro('O produto deve conter ingredientes!\n')
        else:
            ingredientes = [item.strip().title() for item in ingred_input.split(',')]
            break

    while True:
        preco_input = input('\nAdicione o preço separado com ponto:\n').strip()
        if preco_input.replace('.', '', 1).isdigit():
            preco = float(preco_input)
            break
        else:
            erro("Preço inválido! Digite apenas números. Ex: 5.00\n")

    novo_produto = Produto(nome, ingredientes, preco)
    produtos.append(novo_produto)
    sucesso(f'\nProduto "{nome}" adicionado com sucesso ao cardápio!\n')
#cadastro_produto()

# Função de menu da parte de produtos
def menu_produtos():
    while True:
        titulo('Menu de Produtos')
        print('1 - Ver Cardápio')
        print('2 - Cadastrar Produto')
        print('9 - Voltar ao menu principal')
        opcao = input('Escolha uma opção: ').strip()

        if opcao == '1':
            ver_cardapio()
        elif opcao == '2':
            cadastro_produto()
        elif opcao == '9':
            print('Ainda em construção!')
            break
        else:
            erro('Opção inválida. Tente novamente.\n')
#menu_produtos()

#  =-=-=-=-=-=-=-=-=-=-=-=  FUNÇÕES PEDIDOS  =-=-=-=-=-=-=-=-=-=-=-=
def fazer_pedido():
    titulo('Fazer Pedido')
    # Buscar cliente
    while True:
        cliente_input = input('Digite o nome do cliente: ').strip().title()
        if cliente_input == "":
            erro('O nome do cliente não pode estar vazio!\n')
            continue

        cliente_encontrado = False
        cliente_obj = None

        for c in clientes:
            if c.nome == cliente_input:
                cliente_encontrado = True
                cliente_obj = c
                break

        if not cliente_encontrado:
            erro(f'Cliente "{cliente_input}" não encontrado!\n')
            continue
        else:
            sucesso(f'Cliente "{cliente_obj.nome}" encontrado!\n')
            break

    while True:
        produtos_input = input('Digite os produtos separados por vírgula: ').strip()
        if produtos_input == "":
            erro('Você precisa digitar pelo menos um produto!\n')
            continue  

        nomes_produtos = [p.strip().title() for p in produtos_input.split(',')]
        produtos_selecionados = []
        produtos_nao_encontrados = []

        for nome_prod in nomes_produtos:
            encontrado = False
            for p in produtos:
                if p.nome_pro == nome_prod:
                    produtos_selecionados.append(p)
                    encontrado = True
                    break
            if not encontrado:
                produtos_nao_encontrados.append(nome_prod)

        if produtos_nao_encontrados:
            erro(f'Produtos não encontrados: {", ".join(produtos_nao_encontrados)}\n')
            continue
        else:
            sucesso(f'Produtos selecionados: {", ".join([p.nome_pro for p in produtos_selecionados])}\n')
            print('-' * 20)
            print('NOTA FISCAL')
            print('-' * 20)
            print(f'Cliente: {cliente_obj.nome}')
            print(f'CPF: {cliente_obj.cpf}')
            print('Produtos:')
            for p in produtos_selecionados:
                print(f' - {p.nome_pro} - R$ {p.preco:.2f}')
            print('-' * 10)
            total = sum(p.preco for p in produtos_selecionados)
            print(f'Total: R$ {total:.2f}')
            print('-' * 20)
            print('Obrigado pela preferência!')
            print('-' * 20)                      
            break

    if pedidos:
        id_nf = pedidos[-1].id_nf + 1
    else:
        id_nf = 1

    novo_pedido = Pedidos(cliente_obj, produtos_selecionados, id_nf)
    pedidos.append(novo_pedido)
    sucesso(f'Pedido #{id_nf} criado com sucesso!\n')

fazer_pedido()


                


# ===================== MENU PRINCIPAL =====================

# Função do menu principal
def menu_principal():
    while True:
        titulo('coffee tia rosa')
        print('1 - Novo Cliente'.title())
        print('2 - Ver clientes'.title())
        print('3 - Novo Produto'.title())
        print('4 - ver Cardápio'.title())
        print('5 - Fazer pedido'.title())
        print('9 - Sair')
        opcao = input('Escolha uma opção: ').strip()

        if opcao == '1':
            cadastro_de_clientes()
        elif opcao == '2':
            ver_clientes()
        elif opcao == '3':
            cadastro_produto()
        elif opcao == '4':
            ver_cardapio()
        elif opcao == '5':
            print('Ainda em construção!')
        elif opcao == '9':
            sucesso('\nAté mais!!!\n')
            break
        else:
            print('Opção inválida. Tente novamente.\n')
#menu_principal()


# Executa o sistema
#if __name__ == '__main__':
#    menu_principal()
