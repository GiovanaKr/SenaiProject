#ObjetoPedido
listaP = [] #lista global
listaE = [] #lista de estoque

class Pedido:   #OBJETO
    def __init__(self, name, qtd):
        #self.user = user
        
        self.numero = 0 #numero requisição

        self.nome = name   #nome item
        self.qtd = qtd     #quantidade
        self.dataPed = 0   #data pedido criado

        self.aprovGen = 2  #gerente
        self.modifica = 0  #justificativa modificar produto
        self.dataGen = 0   #data aprovação
        

        self.aprovCom = 2   #compras
        self.dataCom = 0    #data compra feita

        self.log = 2       #logistica
        self.entrega = 0   #entregue
        self.dataLog = 0   #data chegada

        self.justificativa = 0 #caso negado
