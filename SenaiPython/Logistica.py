import ObjetoPedido
import os
clear = lambda: os.system('cls')
lista = ObjetoPedido.listaP
estoque = ObjetoPedido.listaE

#gg = ObjetoPedido.Pedido('papel','100')
#lista.append(gg)

#ver estoque
#tirar do estoque
#modificar estoque
#colocar produtos recebidos no estoque

class Logistica:
    def Main():
        clear()
        print("#######PERFIL Logistica#######")
        print("1-Verificar/Modificar solicitações")
        print("2-Retirada de produto")
        print("3-Verificar/Modificar Estoque")
        print("5-Logout")
        r = input(": ")
        if int(r) == 1:
            Logistica.Lista()
            Logistica.Main()
        elif int(r) == 2:
            Logistica.Retirada()
            Logistica.Main()
        elif int(r) == 3:
            Logistica.VerEstoque()
            Logistica.Main()
        elif int(r) == 5:
            return
        else:
            Logistica.Main()

    def Lista():
        clear()
        h = 0
        print("pressione '0' para sair")
        print("")
        for x in range(len(lista)): #para cada item na lista
            if int(lista[x].aprovCom) == 1 :
                print(str(x+1)+" "+"Item: "+lista[x].qtd+" "+lista[x].nome)
                if int(lista[x].log) == 2:
                    print("Aguardando verificação")
                elif int(lista[x].log) == 1:
                    print("Aprovado")
                else:
                    print("Negado")
                print("")
                h=h+1

        if h == 0 :
            print("Aguardando requisições")
            f = input("")
            return
        else:
            y = input("Modificar item nº:")
            d = int(y)-1
            if int(y) == 0:
                return
            for x in range(len(lista)):
                if int(lista[x].aprovCom) == 1 :
                    if x == d:
                        print(lista[x].qtd + " " +lista[x].nome)
                        r = input("Recebido(1)   Recusado(0)")
                        if  int(r) == 0:
                            lista[x].justificava=input('Motivo:')

                        if r == 0:
                            Logistica.Main()
                        if int(r) == 0 or int(r) == 1:
                            lista[x].log = r 
                        else:
                            print("input incorreto")
                            x = input("")
                            Logistica.Lista()

                        if int(lista[x].log) == 1:
                            s = input("Foi entregue(1)  Em espera(0) ")
                            lista[x].entrega = s

        x = input("")
        Logistica.Main()

    def Retirada():
        clear()
        print("pressione '0' para sair")
        print("")
        h=0
        for x in range(len(lista)):
            if (int(lista[x].log)==1):
                if (int(lista[x].entrega)==0):
                    print(str(x)+" "+"Item: "+lista[x].qtd+" "+lista[x].nome)
                    h=h+1

        if h==0: 
            print("Aguardando Requisições")            
        else:
            y = input("Modificar item nº:")
            if y == 0:
                return
            for x in range(len(lista)):
                    if x == int(y):
                        r = input("Sim(1)   Não(0)")
                        lista[x].entrega = r
                        pp = ObjetoPedido.Pedido(lista[x].nome, lista[x].qtd)
                        estoque.append(pp)
        x = input("")
        Logistica.Main()

    def VerEstoque(): #mostra items do estoque
        clear()
        h = 0
        for obj in estoque:
            print(obj.qtd+" "+obj.nome)
            h=h+1
        if h == 0:
            print('estoque vazio')
            x = input("")
            return
        else:       #modificar itens (necessario?????)
            y = input("Retirar(1)   Modificar(2)")
            if y == 0:
                return
            elif y == 1:
                t = input('nome registrado:')
                for obj in lista:
                        if obj.nome == t:


            elif y == 2:
                for x in range(len(lista)):
                        if x == int(y)-1:
                            r = input("Sim(1)   Não(0)")
                            lista[x].entrega = r
        x = input("")
        Logistica.Main()
        
