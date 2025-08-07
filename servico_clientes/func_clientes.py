def titulo(msg):
    print('*-' * 30)
    print(msg.upper())
    print('*-' * 30)
# Criação da classe cliente, onde esse precisa de 2 variáveis:
class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        pass

# criação dos dados que vão ir para a variável clientes
dados_clientes = [
    {
        "nome": "Ana Paula",
        "cpf": "11122233344",
    },
    {
        "nome": "Bruno Martins",
        "cpf": "22233344455",
    },
    {
        "nome": "Carla Souza",
        "cpf": "33344455566",
    }
]

#criação da variável clientes
clientes = []

# Transfirindo os dados do dicionário dados_clientes para a classe Clientes
# 1 cliente tem esse 2 conjunto de dados
# add esse conjunto de dados agora chamado somente de cliente na lista clientes
#clientes = [cliente, cliente, cliente]
for dado in dados_clientes:
    cliente = Cliente(dado['nome'], dado['cpf']) 
    clientes.append(cliente)


#criação da função de visualizar clientes
def ver_clientes(lista):
    titulo('Clientes cadastrados')
    for cliente in lista:
        print(f' {cliente.nome}')
        print(f'   CPF: {cliente.cpf}')


# ver_clientes(clientes)

def cadastro_de_clientes():
    titulo('cadastro de clientes')

    #criação da variável nome sem espaço na frente e atras no formato title
    # se nome vazio a mensagem de erro aparece e retorna ao nome
    while True:
        nome = input('Qual o nome do cliente?\n').strip().title()
        if nome == "":
            print('O nome não pode estar vazio!\n')
        else:
            break
            
    #criação da variavel cpf sem espaço na frente e atras
    # verifica se já tem o mesmo cpf repitido dentro da variavel com um boolean
    # verifica se ta na ordem correta de 11 digitos em numeros
    # se tudo der certo ele cria uma variavel para juntas os dois e atribui na lista de clientes
    while True:
        cpf = input('Qual o CPF? (somente números):\n').strip()
        jatem_cpf = False
        for c in clientes:
            if c.cpf == cpf:
                print('CPF já cadastrado\n')
                jatem_cpf = True
                break
        if jatem_cpf:
            continue
        elif not cpf.isdigit() or len(cpf) != 11:
            print('Formato de CPF inválido!\n')
        else:
            novo_cliente = Cliente(nome, cpf)
            clientes.append(novo_cliente)
            print(f'O cliente {nome} com o CPF {cpf} foi registrado com sucesso!\n')
            break


#cadastro_de_clientes

#menu que aparece logo apos a 
def menuClientes():
    while True:
        print('-'*20)
        print('1 - Ver clientes')
        print('2 - Cadastrar Novo Cliente')
        print('9 - Voltar ao Menu')
        print('-'*20)
        opcao = input('Escolha uma opção: \n''-'*20).strip()

        if opcao == '1':
            ver_clientes(clientes)
        elif opcao == '2':
            cadastro_de_clientes()
        elif opcao == '9':
            print('ainda em construção!')
            break
        else:
            print('Opção inválida, tente novamente.\n')

#menuClientes()
