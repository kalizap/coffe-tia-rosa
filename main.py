# importando a biblioteca de tempo
from time import sleep

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

# criação da função de título
def titulo(msg):
    sleep(2.0)
    print('\n' + '*-' * 30)
    print(msg.upper().center(60))
    print('*-' * 30 + '\n')


# criação da função de erro
def erro(msg):
    print(f'>>> {msg}', end='')
    

# criação da função sucesso
def sucesso(msg):
    print(f'+++ {msg}', end='')

# =-=-=-=-=-=-=-=-=-=-=-=  MENU PRINCIAPAL  =-=-=-=-=-=-=-=-=-=-=-=
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
            fazer_pedido()
        elif opcao == '9':
            sucesso('\nAté mais!!!\n')
            break
        else:
            print('Opção inválida. Tente novamente.\n')

# =-=-=-=-=-=-=-=-=-=-=-=  FUNÇÕES CLIENTES  =-=-=-=-=-=-=-=-=-=-=-=
# Função de ver a lista de clientes
def ver_clientes():
    titulo('Clientes cadastrados')
    for cliente in clientes:
        print(f'{cliente.nome}')
        print(f'    CPF: {cliente.cpf}\n')
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
            sucesso(f'\nO cliente "{nome}" com o CPF "{cpf}" foi registrado com sucesso!\n')
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
            menu_principal()
            break
        else:
            erro('Opção inválida. Tente novamente.\n')
#menu_clientes()

#  =-=-=-=-=-=-=-=-=-=-=-=  FUNÇÕES PRODUTOS  =-=-=-=-=-=-=-=-=-=-=-=
# Função de ver o cardápio
def ver_cardapio():
    titulo('Cardápio')
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
            continue
        else:
            sucesso('Ingredientes adicionados com sucesso!\n')
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
    menu_produtos()
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
            menu_principal()
            break
        else:
            erro('Opção inválida. Tente novamente.\n')
#menu_produtos()

#  =-=-=-=-=-=-=-=-=-=-=-=  FUNÇÕES PEDIDOS  =-=-=-=-=-=-=-=-=-=-=-=
# Função nota fiscal
def NF(cliente, produtos, id_nf):
    titulo(f'Nota Fiscal #{id_nf}')
    print(f'Cliente: {cliente.nome}')
    print(f'CPF: {cliente.cpf}')
    print('Produtos:')
    for p in produtos:
        print(f' - {p.nome_pro} - R$ {p.preco:.2f}')
    print('-' * 30)
    total = sum(p.preco for p in produtos)
    print(f'Total: R$ {total:.2f}')
    print('-' * 30)
    print('Obrigado pela preferência!')
    print('-' * 30)
#fazer_pedido()

# Função para fazer um pedido
def fazer_pedido():
    titulo('Fazer Pedido')
    while True:
        #valida se o nome do cliente existe nos dados já criados
        cliente_input = input('Digite o nome do cliente:\n').strip()
        if cliente_input == "":
            erro('O nome do cliente não pode estar vazio!\n')
        else:
            cliente_obj = next((c for c in clientes if c.nome.lower() == cliente_input.lower()), None)
            if not cliente_obj:
                erro(f'Cliente "{cliente_input}" não encontrado!\n')
                continue
            else:
                sucesso(f'Cliente "{cliente_obj.nome}" encontrado!\n')
                break

    while True:
        # validação do CPF do cliente + verificar se corresponde ao cliente informado
        cpf_input = input('Digite o CPF do cliente (somente números): ').strip()
        if cpf_input == "":
            erro('O CPF não pode estar vazio!\n')
            continue
        elif not cpf_input.isdigit() or len(cpf_input) != 11:
            erro('Formato de CPF inválido!\n')
            continue
        elif cliente_obj.cpf != cpf_input:
            erro('O CPF não corresponde ao cliente informado.\n')
            continue
        else:
            sucesso(f'CPF "{cpf_input}" confirmado!\n')
            break
    
    while True:
        
        titulo("Cardápio")
        for i, p in enumerate(produtos, start=1):
            print(f'{i} - {p.nome_pro} - R$ {p.preco:.2f}')
            print(f'    Ingredientes: {", ".join(p.ingredientes)}\n')

        produtos_input = input('Digite os id dos produtos separados por vírgula: ').strip()
        if produtos_input == "":
            erro('Digite um número informado\n')
            continue 

        ids_produtos = set()
        valido = True
        for p_id in produtos_input.split(','):
            p_id = p_id.strip()
            if not p_id.isdigit():
                erro(f'ID inválido: {p_id}\n')
                valido = False
                break
            ids_produtos.add(int(p_id))

        if not valido:
            continue

        prod_nao_enc = []
        prod_selecionados = []
        for id_prod in ids_produtos:
            if 1 <= id_prod <= len(produtos):
                prod_selecionados.append(produtos[id_prod - 1])
            else:
                prod_nao_enc.append(str(id_prod))

        if prod_nao_enc:
            erro(f'Ids não encontrados: {", ".join(prod_nao_enc)}\n')
            continue
        else:
            sucesso('Produtos selecionados com sucesso!\n')
            titulo('Resumo do Pedido')
            for p in prod_selecionados: 
                print(f' - {p.nome_pro} - R$ {p.preco:.2f}')
            print('-' * 30)
            total = sum(p.preco for p in prod_selecionados)
            print(f'Total: R$ {total:.2f}')
            print('-' * 30)
            break

    # Confirmar pedido
    while True:
        confirmar = input('Deseja prosseguir [S/N]? ').strip().lower()
        if confirmar == 's':
            sucesso('Pedido confirmado!\n')
            # identificação da nota fiscal
            id_nf = pedidos[-1].id_nf + 1 if pedidos else 1

            # cria o pedido e salva na lista de pedidos
            novo_pedido = Pedidos(cliente_obj, prod_selecionados, id_nf)
            pedidos.append(novo_pedido)

            # mostrar a nota fiscal
            titulo('imprimindo nota fiscal')
            NF(cliente_obj, prod_selecionados, id_nf)
            sucesso(f'Pedido #{id_nf} criado com sucesso!\n')
            break
        elif confirmar == 'n':
            sleep(1.0)
            erro('Pedido cancelado!\n')
            menu_principal()
        else:
            erro('Opção inválida. Digite S ou N.\n')
#fazer_pedido()



# Executa o sistema
if __name__ == '__main__':
    menu_principal()
