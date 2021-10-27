#Operario
import ObjetoPedido
import os
clear = lambda: os.system('cls')
lista = ObjetoPedido.listaP

#mostrar pedido para retirar

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
            
            if int(obj.aprovGen) == 0:
                print("Negado[gerencia]")
            elif int(obj.aprovGen) == 2:
                print("Sendo examinado")
            elif int(obj.aprovGen) == 1:
                print("Aprovado[gerencia]")
            
            print("")
        x = input("")
        Operario.Main()
