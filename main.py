from servicos import clientes, produtos, pedidos
from client_class import Cliente
from produto_class import Produto
from pedidos_class import Pedidos


def titulo(msg):
    print('\n' + '*-' * 30)
    print(msg.upper().center(60))
    print('*-' * 30 + '\n')


# ===================== CLIENTES =====================
def ver_clientes():
    titulo('Clientes cadastrados')
    if not clientes:
        print('Nenhum cliente cadastrado.')
    for cliente in clientes:
        print(f'Nome: {cliente.nome}\nCPF: {cliente.cpf}\n')


def cadastro_de_clientes():
    titulo('Cadastro de Clientes')

    while True:
        nome = input('Nome do cliente: ').strip().title()
        if nome:
            break
        print('O nome não pode estar vazio.\n')

    while True:
        cpf = input('CPF (apenas números): ').strip()
        if any(c.cpf == cpf for c in clientes):
            print('CPF já cadastrado.\n')
        elif not cpf.isdigit() or len(cpf) != 11:
            print('CPF inválido! Deve conter 11 dígitos numéricos.\n')
        else:
            novo_cliente = Cliente(nome, cpf)
            clientes.append(novo_cliente)
            print(f'Cliente {nome} cadastrado com sucesso!\n')
            break


def menu_clientes():
    while True:
        titulo('Menu de Clientes')
        print('1 - Ver Clientes')
        print('2 - Cadastrar Cliente')
        print('9 - Voltar ao menu principal')
        opcao = input('Escolha uma opção: ').strip()

        if opcao == '1':
            ver_clientes()
        elif opcao == '2':
            cadastro_de_clientes()
        elif opcao == '9':
            break
        else:
            print('Opção inválida. Tente novamente.\n')


# ===================== PRODUTOS =====================
def ver_cardapio():
    titulo('Cardápio')
    if not produtos:
        print('Nenhum produto cadastrado.')
    for p in produtos:
        print(f'Produto: {p.nome_pro}')
        print(f'Preço: R$ {p.preco:.2f}')
        print(f'Ingredientes: {", ".join(p.ingredientes)}')
        print('-' * 40)


def cadastro_produto():
    titulo('Cadastro de Produto')

    while True:
        nome = input('Nome do produto: ').strip().title()
        if nome:
            break
        print('O nome não pode estar vazio.\n')

    while True:
        ing = input('Ingredientes (separados por vírgula): ').strip()
        if ing:
            ingredientes = [i.strip().title() for i in ing.split(',')]
            break
        print('Informe ao menos um ingrediente.\n')

    while True:
        preco_str = input('Preço (use ponto como separador): ').strip()
        try:
            preco = float(preco_str)
            break
        except ValueError:
            print('Preço inválido. Use apenas números. Ex: 5.00\n')

    novo_produto = Produto(nome, ingredientes, preco)
    produtos.append(novo_produto)
    print(f'Produto {nome} cadastrado com sucesso!\n')


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
            break
        else:
            print('Opção inválida. Tente novamente.\n')


# ===================== MENU PRINCIPAL =====================
def menu_principal():
    while True:
        titulo('Sistema Coffee Shops Tia Rosa')
        print('1 - Menu Clientes')
        print('2 - Menu Produtos')
        print('3 - Sair')
        opcao = input('Escolha uma opção: ').strip()

        if opcao == '1':
            menu_clientes()
        elif opcao == '2':
            menu_produtos()
        elif opcao == '3':
            print('\nSaindo do sistema. Até logo!\n')
            break
        else:
            print('Opção inválida. Tente novamente.\n')


# Executa o sistema
if __name__ == '__main__':
    menu_principal()
