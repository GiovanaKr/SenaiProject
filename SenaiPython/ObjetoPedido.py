#ObjetoPedido
listaP = [] #lista global
listaE = [] #lista de estoque
 


class Pedido:   #OBJETO
    def __init__(self, name, qtd):
        #self.user = user
        
        self.numero = 0 #numero requisição

        self.nome = name   #nome item
        self.qtd = qtd     #quantidade
        self.aprovGen = 2  #gerente
        self.aprovCom = 2   #compras
        self.log = 2       #logistica
        self.entrega = 0   #entregue

        self.justificativa = 0 #caso negado
        self.modifica = 0 #justificativa modificar produto

gg = Pedido('papel','10 pacotes')
listaE.append(gg)

pp = Pedido('caneta','1 caixa')
listaE.append(pp)

ee = Pedido('canetão','1 caixa')
listaE.append(ee)
