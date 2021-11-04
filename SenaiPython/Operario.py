#Operario
import ObjetoPedido
import os
clear = lambda: os.system('cls')
lista = ObjetoPedido.listaP

#pp = ObjetoPedido.Pedido('caneta','10')
#lista.append(pp)


class Operario:
    def Main():
        clear()
        print("#######PERFIL OPERACIONAL#######")
        Operario.Retirar()
        print("")
        print("1-Solicitar produto")
        print("2-Verificar solicitações")
        print("5-Logout")
        r = int(input(": "))
        if r == 1:
            Operario.CriarPedido()
            Operario.Main()
        elif r == 2:
            Operario.VerLista()
        elif r == 5:
            return
        else:
            Operario.Main()
 
    def Retirar(): #mostra se tem pedidos para serem retirados
        h = 0
        for obj in lista:
            if int(obj.log) == 1:
                h = h+1
        if h > 0:
            print(str(h)+" pedidos para serem retirados")

    def CriarPedido(): #cria pedido novo
        clear()
        print("pressione 's' para sair")
        print("")
        nome = input("Item:") 
        if nome == "s":     #sair
            return
        qtd = input("Quantidade:")
        pdd = ObjetoPedido.Pedido(nome,qtd)
        lista.append(pdd)
        return

    def VerLista(): #lista pedidos
        clear()
        for obj in lista:
            print("Item: "+obj.qtd+" "+obj.nome)
            
            if int(obj.aprovGen) == 0:
                print("[gerencia]Negado")
                print('Motivo: '+obj.justificativa)
            elif int(obj.aprovGen) == 2:
                print("[gerencia]Sendo examinado")
            elif int(obj.aprovGen) == 1:
                print("[gerencia]Aprovado")

                if int(obj.aprovCom) == 0:
                    print("[Compras]Negado")
                    print('Motivo: '+obj.justificativa)
                elif int(obj.aprovCom) == 2:
                    print("[Compras]Sendo examinado")
                elif int(obj.aprovCom) == 1:
                    print("[Compras]Aprovado")

                    if int(obj.log) == 0:
                        print("[Logistica]Negado")
                        print('Motivo: '+obj.justificativa)
                    elif int(obj.log) == 2:
                        print("[Logistica]Sendo examinado")
                    elif int(obj.log) == 1:
                        print("[Logistica]Aprovado")
                        if int(obj.entrega) == 0:
                            print("[Logistica]!Retirar!")
            print("")
        x = input("")
        Operario.Main()     
