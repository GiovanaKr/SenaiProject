import ObjetoPedido
import os
from datetime import datetime
clear = lambda: os.system('cls')
lista = ObjetoPedido.listaP
estoque = ObjetoPedido.listaE

gg = ObjetoPedido.Pedido('papel','100')
gg.aprovLog = 1
gg.entrega = 0
gg.numero = 1
lista.append(gg)

#resolver modificações no estoque
#retirar do estoque = retirada de produto
#receber produto = coloca no estoque

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
        elif int(r) == 2:
            Logistica.Retirada()
        elif int(r) == 3:
            Logistica.VerEstoque()
        elif int(r) == 5:
            return
        Logistica.Main()

    #recebe pedido e coloca no estoque
    def Lista():
        clear()
        h = 0
        print("pressione '0' para sair")
        print("")
        for x in range(len(lista)): #para cada item na lista
            if int(lista[x].aprovCom) == 1 :
                print("Requisição nº"+str(lista[x].numero))
                print(lista[x].qtd+" "+lista[x].nome)
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

                        else:
                            print("input incorreto")
                            x = input("")
                            Logistica.Lista()

        x = input("")
        Logistica.Lista()

    #entrega pedido para operario e tira item do estoque
    def Retirada():
        clear()
        print("pressione '0' para sair")
        print("")
        h=0
        for x in range(len(lista)):     #lista produtos recebidos
            if (int(lista[x].log)==1):
                if (int(lista[x].entrega)==0):
                    print("Requisição nº"+str(lista[x].numero))
                    print(lista[x].qtd+" "+lista[x].nome)
                    h=h+1

        if h==0: 
            print("Aguardando Requisições")         #lista vazia   
        else:
            y = input("Modificar item nº:")
            if y == 0:
                return
            for x in range(len(lista)):     #resolver essa parte!!!!!!!!!!
                    if x == int(y)-1:
                        r = input("Sim(1)   Não(0)")
                        lista[x].entrega = r
                        pp = ObjetoPedido.Pedido(lista[x].nome, lista[x].qtd)
                        estoque.append(pp)
        x = input("")
        return

    #modificar quantidade de um item especifico
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
                            print('achei item:'+t)
                            input('')
            elif y == 2:
                for x in range(len(lista)):
                        if x == int(y)-1:
                            r = input("Sim(1)   Não(0)")
                            lista[x].entrega = r
        x = input("")
        Logistica.Main()
        
