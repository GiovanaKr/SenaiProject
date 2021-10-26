#Operario
import ObjetoPedido
 
lista = ObjetoPedido.listaP
class Operario:
    def Main():
        print("deseja:")
        r = input("1-fazer pedido   2-checar pedidos")
        if int(r) == 1:
            print("entrou")
            Operario.CriarPedido()
        else:
            Operario.VerLista()
 
        
    def CriarPedido(): #cria pedido novo
        nome = input("nome para o pedido:")
        pp = ObjetoPedido.Pedido(nome)
        lista.append(pp)    #chama lista do main
        Operario.Main()
 
    def VerLista():
        for obj in lista:
            print("Nome pedido:"+obj.name)
            if obj.aprovGen == 2:
                print("Aguardando Aprovação")
        Operario.Main()
 
Operario.Main()