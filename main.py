from cores import cores
from servico_clientes import main
from servico_produtos.cadastro_produtos import cadastro_cardapio, ver_cardapio

print(f'            Seja-bem vindo ao\n{cores["rosa"]}~~*~~*~~*|COFFEE SHOPS TIA ROSA|*~~*~~*~~{cores["n"]}\n')
print


while True:
    print(f'{cores["ops"]}> 1 - Cadastro de clientes{cores["n"]}') 
    print(f'{cores["ops"]}> 2 - Cadastro de produtos{cores["n"]}')
    print(f'{cores["ops"]}> 3 - Realizar pedidos{cores["n"]}')
    print(f'{cores["ops"]}> 4 - Ver cardápio{cores["n"]}')
    print(f'{cores["sair"]}> 9 - Fechar programa{cores["n"]}')
    op = int(input(f'{cores["ops"]}\n>>>>>>>>>>>Escolha uma opção:{cores["n"]}'))
    
    if op == 9:
        print('FIM DO PROGRAMA')
        break
    elif op == 1:
        cadastro()
    elif op == 2:
        cadastro_cardapio()
    elif op == 3:
        print('cu')
    elif op == 4:
        ver_cardapio()
    else: 
        print('DIGITE UM VALOR VÁLIDO!')

        

