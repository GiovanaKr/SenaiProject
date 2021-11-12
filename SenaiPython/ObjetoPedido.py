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
        self.modifica = '0'  #justificativa modificar produto
        self.dataGen = 0   #data aprovação
        

        self.aprovCom = 2   #compras
        self.dataCom = 0    #data compra feita

        self.log = 2         #logistica
        self.dataLog = 0     #data chegada
        self.emEstoque = 0   #este item esta no estoque
        self.retirada = '0'  #quem retirou

        self.justificativa = '0' #caso negado


def ListaCompleta():
    for obj in listaP:
        print(obj.numero)

        print(obj.nome)
        print(obj.qtd)  
        print(obj.dataPed) 

        print(obj.aprovGen)
        print(obj.modifica)
        print(obj.dataGen)
        
        print(obj.aprovCom) 
        print(obj.dataCom)

        print(obj.log)
        print(obj.dataLog)
        print(obj.emEstoque)
        print(obj.retirada)

        print(obj.justificativa)
