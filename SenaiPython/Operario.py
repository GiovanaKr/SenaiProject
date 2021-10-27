#Operario
import ObjetoPedido
import os
clear = lambda: os.system('cls')
lista = ObjetoPedido.listaP

class Operario:
    def Main():
        clear()
        print("#######PERFIL OPERACIONAL#######")
        print("1-Solicitar produto")
        print("2-Verificar solicitações")
        print("5-Logout")
        r = input(": ")
        if int(r) == 1:
            Operario.CriarPedido()
        elif int(r) == 2:
            Operario.VerLista()
        elif int(r) == 5:
            return
        else:
            Operario.Main()
 
        
    def CriarPedido(): #cria pedido novo
        clear()
        nome = input("Item:")
        qtd = input("Quantidade:")
        pp = ObjetoPedido.Pedido(nome,qtd)
        lista.append(pp)
        Operario.Main()
 
    def VerLista(): #lista pedidos
        clear()
        for obj in lista:
            print("Item: "+obj.qtd+" "+obj.nome)
            
            if obj.aprovGen == 0:
                print("Pedido Negado[gerencia]")
            elif obj.aprovGen == 2:
                print("Pedido em Exame")
            
            print("")
        x = input("")
        Operario.Main()
