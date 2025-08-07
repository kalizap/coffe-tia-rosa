def titulo(msg):
    print('*-' * 30)
    print(msg.upper())
    print('*-' * 30)

class Pedidos:
    def __init__(self, clientes, produtos,id_nf):
        self.clientes = clientes
        self.produtos = produtos
        self.id_nf = id_nf
        pass


