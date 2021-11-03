import ObjetoPedido
import os
clear = lambda: os.system('cls')
lista = ObjetoPedido.listaP

#sair da def lista()
#input incorreto simples
#loop lista

gg = ObjetoPedido.Pedido('papel','100')
gg.aprovGen = '1'
lista.append(gg)
pp = ObjetoPedido.Pedido('caneta','10')
pp.aprovGen = '1'
lista.append(pp)

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

    def Lista():
        clear()
        h = 0
        print("pressione 's' para sair")
        print("")
        for x in range(len(lista)): #para cada item na lista
            if int(lista[x].aprovGen) == 1 :
                print(str(x)+" "+"Item: "+lista[x].qtd+" "+lista[x].nome)
                if int(lista[x].aprovCom) == 2:
                    print("Aguardando verificação")
                elif int(lista[x].aprovCom) == 1:
                    print("Aprovado")
                else:
                    print("Negado")
                print("")
                h=h+1

        if h == 0 :
            print("Aguardando requisições") 
        else:
            y = input("Modificar item nº:")
            if y == 's':
                Compras.Main()
            for x in range(len(lista)):
                if int(lista[x].aprovGen) == 1 :
                    if x == int(y):
                        print(lista[x].qtd + " " +lista[x].nome)
                        r = input("Aprovar(1)   Reprovar(0)")
                        if r == 's':
                            Compras.Main() 
                        if  int(r) == 0:
                            lista[x].justificava=input('Motivo:')                      
                        if int(r) == 0 or int(r) == 1:
                            lista[x].aprovCom = r 
                        else:
                            print("input incorreto")
                            x = input("")
                            Compras.Lista()                    
        Compras.Lista()
Compras.Main()

#try:
#    x = int(r)
#except ValueError: #se input não for 's' nem int
#    print("input incorreto")
#    x = input("")

Compras.Lista()
