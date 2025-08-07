def titulo(msg):
    print('*-' * 30)
    print(msg.upper())
    print('*-' * 30)
class Produto:
    def __init__(self, nome_pro, ingredientes, preco):
        self.nome_pro = nome_pro
        self.ingredientes = ingredientes
        self.preco = preco
        pass


produtos = {
    "Café Preto": {
        "ingredientes": ["Café coado", "Água quente"],
        "preco": 3.00
    },
    "Café com Leite": {
        "ingredientes": ["Café coado", "Leite quente"],
        "preco": 4.50
    },
    "Capuccino": {
        "ingredientes": ["Café espresso", "Leite vaporizado", "Chocolate em pó", "Canela"],
        "preco": 6.50
    },
    "Mocha Gelado": {
        "ingredientes": ["Café espresso", "Leite", "Gelo", "Calda de chocolate"],
        "preco": 7.00
    },
    "Chá de Hibisco": {
        "ingredientes": ["Flores de hibisco", "Água quente", "Limão", "Mel"],
        "preco": 5.00
    }
}

cardapio = []

for nome, dados in produtos.items():
    produto = Produto(nome, dados['ingredientes'], dados['preco'])
    cardapio.append(produto)


def ver_cardapio(cardapio):
    titulo('cardápio')
    for c in cardapio:
        print(f'\n{c.nome_pro}')
        print(f'    Preço : {c.preco:.2f}')
        print(f'    ingredientes:{", ".join(c.ingredientes)}\n')
        print('*-' * 30)

    
#ver_cardapio(cardapio)

def cadastro_produtos():
    titulo('cadastro de produtos')
    while True:
        nome = input('Adicione o nome do produto:\n').strip().title()
        if nome == "":
            print('O nome não pode estar vazio!\n').upper
        else:
            break

    while True:
        ingredientes_input = input('Adicione os ingredientes separados por vírgula:\n').strip().title()
        if ingredientes_input == "":
            print('O produto deve conter igredientes!\n')
        else:
            ingredientes = [item.strip().title() for item in ingredientes_input.split(',')]
            break
                        

    while True:
        preco_input = input('Adicione o preço separado com ponto:\n').strip()
        if preco_input.replace('.', '', 1).isdigit():
            preco = float(preco_input)
            break
        else:
            print("Preço inválido! Digite apenas números. Ex: 5.00\n")

    novo_produto = Produto(nome, ingredientes, preco)
    cardapio.append(novo_produto)
    print(f'\nProduto "{nome}" adicionado com sucesso ao cardápio!\n')


#cadastro_produtos()

def menu_cardapio():
    while True:
        print('-='*30)
        print('1 - Ver Cardápio')
        print('2 - Cadastrar Novo Produto')
        print('9 - Voltar ao Menu')
        print('-='*30)
        opcao = input('Escolha uma opção: ').strip()
        

        if opcao == '1':
            ver_cardapio(cardapio)
        elif opcao == '2':
            cadastro_produtos()
        elif opcao == '9':
            print('ainda em construção!')
            break
        else:
            print('Opção inválida, tente novamente.\n')


#menu_cardapio()
