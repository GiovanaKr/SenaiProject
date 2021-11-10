#Operario
import ObjetoPedido
import os
from datetime import datetime
clear = lambda: os.system('cls')
lista = ObjetoPedido.listaP
estoque = ObjetoPedido.listaE

#pp = ObjetoPedido.Pedido('caneta','10')
#lista.append(pp)

#comparar pedido com o que tem no estoque

class Operario:
    def Main():
        clear()
        print("#######PERFIL OPERACIONAL#######")
        Operario.Retirar()
        print("")
        print("1-Solicitar produto")
        print("2-Verificar solicitações")
        print("3-Ver estoque")
        print("5-Logout")
        r = int(input(": "))
        if r == 1:
            Operario.CriarPedido()
        elif r == 2:
            Operario.VerLista()
        elif r == 3:
            Operario.VerEstoque()
        elif r == 5:
            return
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
        print("pressione '0' para sair")
        print("")
        nome = input("Item:") 
        if nome == '0':     #sair
            return
        qtd = input("Quantidade:")
        pdd = ObjetoPedido.Pedido(nome,qtd)
        pdd.numero = (len(lista)+1)
        data = datetime.now()       #pega data
        pdd.dataPed = data.strftime('%d/%m/%Y %H:%M') #salva data atual
        lista.append(pdd)
        return

    def VerLista(): #lista pedidos
        clear()
        for obj in lista:
            print('['+obj.dataPed+']'+" Requisição nº"+str(obj.numero))
            print(obj.qtd+" "+obj.nome)
            
            if obj.aprovGen == '0':
                print('['+obj.dataGen+']'+"[gerencia]Negado")
                print('Motivo: '+str(obj.justificativa))
            elif obj.aprovGen == '2':
                print("[gerencia]Sendo examinado")
            elif obj.aprovGen == '1':
                if not obj.modifica == 0: #mostra modificação
                    print(obj.modifica)
                print('['+obj.dataGen+']'+"[gerencia]Aprovado")

                if int(obj.aprovCom) == 0:
                    print('['+obj.dataCom+']'+"[Compras]Negado")
                    print('Motivo: '+str(obj.justificativa))
                elif int(obj.aprovCom) == 2:
                    print("[Compras]Sendo examinado")
                elif int(obj.aprovCom) == 1:
                    print('['+obj.dataCom+']'+"[Compras]Aprovado")

                    if int(obj.log) == 0:
                        print('['+obj.dataLog+']'+"[Logistica]Negado")
                        print('Motivo: '+str(obj.justificativa))
                    elif int(obj.log) == 2:
                        print("[Logistica]Sendo examinado")
                    elif int(obj.log) == 1:
                        print('['+obj.dataLog+']'+"[Logistica]Aprovado")
                        if int(obj.entrega) == 0:
                            print("[Logistica]!Retirar!")
            print("")
        x = input("")
        return

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
        x = input("")
        return

#from datetime import datetime

#data_e_hora_atuais = datetime.now()
#data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')

#print(data_e_hora_em_texto)
