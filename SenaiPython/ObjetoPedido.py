#ObjetoPedido
listaP = [] #lista global
 
class Pedido:   #OBJETO
    def __init__(self, name):
        self.name = name
        self.aprovGen = 2
        self.arovCom = 2
        self.logis = 2
        self.entrega = 0