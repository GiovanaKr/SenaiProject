import ObjetoPedido
import os
from datetime import datetime
clear = lambda: os.system('cls')
lista = ObjetoPedido.listaP

#gg = ObjetoPedido.Pedido('papel','100')
#gg.aprovGen = 1
#gg.numero = 1
#lista.append(gg)

#pp = ObjetoPedido.Pedido('papel','100')
#pp.aprovGen = 1
#pp.numero = 2
#lista.append(pp)

#qual marca foi comprada

class Compras:
    def Main():
        clear()
        print("#######PERFIL Compras#######")
        print("1-Verificar/Modificar solicitações")
        print("5-Logout")
        r = input(": ")
        if int(r) == 1:
            Compras.Lista()
        elif int(r) == 5:
            return
        else:
            Compras.Main()
        Compras.Main()

    def Lista():
        clear()
        h = 0
        print("pressione '0' para sair")
        print("")
        for x in range(len(lista)): #para cada item na lista
            if int(lista[x].aprovGen) == 1 :
                print("Requisição nº"+str(lista[x].numero))
                print(lista[x].qtd+" "+lista[x].nome)
                if int(lista[x].aprovCom) == 2:
                    print("Aguardando verificação")
                elif int(lista[x].aprovCom) == 1:
                    print("Aprovado")
                else:
                    print("Negado")
                print("")
                h=h+1

        if h == 0 :     #caso lista vazia
            print("Aguardando requisições") 
            f = input('')
            return
        else:
            y = input("Modificar item nº:")
            if int(y) == 0:
                return
            for x in range(len(lista)):
                if int(lista[x].aprovGen) == 1 :
                    if x == int(y)-1:
                        print(lista[x].qtd + " " +lista[x].nome)
                        r = input("Aprovar(1)   Reprovar(0)")
                        if  int(r) == 0:
                            lista[x].justificativa=input('Motivo:')  
                            lista[x].aprovCom = r
                            data = datetime.now()       #pega data
                            lista[x].dataCom = data.strftime('%d/%m/%Y %H:%M') #salva data atual                    

                        if int(r) == 0 or int(r) == 1:
                            lista[x].aprovCom = r 
                            data = datetime.now()       #pega data
                            lista[x].dataCom = data.strftime('%d/%m/%Y %H:%M') #salva data atual 

                        else:
                            print("input incorreto")
                            x = input("")
                            Compras.Lista()                    
        Compras.Lista()
