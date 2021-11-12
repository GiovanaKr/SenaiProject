import ObjetoPedido
import os
from datetime import datetime
clear = lambda: os.system('cls')
lista = ObjetoPedido.listaP
estoque = ObjetoPedido.listaE

#pp = ObjetoPedido.Pedido('caneta','100')
#pp.numero = 2
#lista.append(pp)

class Gerente:
    def Main():
        clear()
        print("#######PERFIL GERENCIAL#######")
        print("1-Verificar/Modificar solicitações")
        print("5-Logout")
        r = input(": ")
        if int(r) == 1:
            Gerente.Lista()
            Gerente.Main()
        elif int(r) == 5:
            return
        else:
            Gerente.Main()

    def Lista():
        clear()
        h = 0
        print("presione '0' para sair")
        print('')
        for x in range(len(lista)): #para cada item na lista
            if int(lista[x].aprovGen) == 2:
                print("requisição nº"+str(lista[x].numero))
                print(lista[x].qtd+" "+lista[x].nome)
                if int(lista[x].aprovGen) == 2:
                    print("Aguardando verificação")
                elif int(lista[x].aprovGen) == 1:
                    print("Aprovado")
                else:
                    print("Negado")
                print("")
                h = h+1

        if h == 0 :     #caso não tenha itens
            print("Aguardando requisições") 
            f = input('')
            return
        else:
            y = input("Modificar item nº:")
            if int(y) == 0:
                return
            else:
                for x in range(len(lista)):
                    if x == int(y)-1:
                        print(lista[x].qtd + " " +lista[x].nome)
                        r = input("Aprovar(1)   Reprovar(0)     modificar(3)") #e modificar
                        if  r == '0':       #pedido negado
                            lista[x].justificativa=input('Motivo:')             
                            lista[x].aprovGen = r
                            data = datetime.now()       #pega data
                            lista[x].dataGen = data.strftime('%d/%m/%Y %H:%M') #salva data atual

                        elif r == '1':      #pedido aprovado
                            lista[x].aprovGen = r 
                            data = datetime.now()       #pega data
                            lista[x].dataGen = data.strftime('%d/%m/%Y %H:%M') #salva data atual

                        elif r == '3':      #modificar pedido
                            lista[x].modifica = ('modificado['+lista[x].qtd+' '+lista[x].nome+' '+']')
                            print('modificação')
                            lista[x].nome = input('nome:')
                            lista[x].qtd = input('quantidade:')
                            t = input('motivo: ')
                            lista[x].modifica = (lista[x].modifica + t)
                            lista[x].aprovGen = '1'     #aprova pedido
                            data = datetime.now()       #pega data
                            lista[x].dataGen = data.strftime('%d/%m/%Y %H:%M') #salva data atual

                        else:
                            print("input incorreto")
                            x = input("")
                            return
        Gerente.Lista()
