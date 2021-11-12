import ObjetoPedido
import os
from datetime import datetime
clear = lambda: os.system('cls')
lista = ObjetoPedido.listaP
estoque = ObjetoPedido.listaE


#resolver modificações no estoque
#retirar do estoque = retirada de produto
#receber produto = coloca no estoque

class Logistica:
    def Main():
        clear()
        print("#######PERFIL Logistica#######")
        print("1-Pedidos Abertos")
        print("2-Retirada de produto")
        print("5-Logout")
        r = input(": ")
        if int(r) == 1:
            Logistica.Lista()
        elif int(r) == 2:
            Logistica.Retirada()
        elif int(r) == 5:
            return
        Logistica.Main()

    #recebe pedido e coloca no estoque
    def Lista():
        clear()
        h = 0
        print("pressione '0' para sair")
        print("")
        for x in range(len(lista)): #lista de pedidos abertos
            if int(lista[x].aprovCom) == 1 and int(lista[x].log) == 2 :
                print("Requisição nº"+str(lista[x].numero))
                print(lista[x].qtd+" "+lista[x].nome)
                print("Aguardando verificação")
                print("")
                h=h+1

        if h == 0 :     #lista vazia/sem pedidos abertos
            print("Aguardando pedidos")
            f = input("")
            return
        else:
            y = input("nº da requisição:")
            if int(y) == 0:
                return
            for x in range(len(lista)):
                if int(lista[x].aprovCom) == 1 :
                    if x == int(y)-1:
                        print(lista[x].qtd + " " +lista[x].nome)
                        r = input("Recebido(1)   Recusado(0)")

                        if  int(r) == 0:    #se recusado
                            lista[x].justificativa=input('Motivo:')
                            lista[x].log = r
                            data = datetime.now()       #pega data
                            lista[x].dataLog = data.strftime('%d/%m/%Y %H:%M') #salva data atual
                            
                        elif int(r) == 1:   #se aceito
                            lista[x].log = r 
                            data = datetime.now()       #pega data
                            lista[x].dataLog = data.strftime('%d/%m/%Y %H:%M') #salva data atual
                            lista[x].emEstoque = 1    #adiciona ao estoque

                        else:
                            print("input incorreto")
                            x = input("")
                            Logistica.Lista()

        Logistica.Lista()

    #entrega pedido para operario e tira item do estoque
    def Retirada():
        clear()
        print("pressione '0' para sair")
        print("")
        h=0
        for obj in lista:     #lista produtos recebidos em estoque
            if int(obj.emEstoque)==1 :
                print("Requisição nº"+str(obj.numero))
                print(obj.qtd+" "+obj.nome)
                print('')
                h=h+1

        if h==0:         #lista vazia   
            print("Aguardando produtos")        
        else:
            y = input("Retirar requisição nº:")
            r = input("tirar total(0)   tirar qtd(1)")
            if y == 0:
                return
            for obj in lista:     #retira item pedido
                if int(obj.numero) == int(y) : #and int(r) == 0:      #pedido inteiro
                    obj.emEstoque = 0
                    obj.retirada = input("Quem esta retirando:")
                #elif int(obj.numero) == int(y) and int(r) == 1:    #qtd especifica
                #    print(obj.nome)
                #    obj.qtd = input('quantidade restante:')
        x = input("")
        return
        
#Logistica.Main()
