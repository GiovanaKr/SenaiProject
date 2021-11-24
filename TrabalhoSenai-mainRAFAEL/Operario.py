import os
import main
from tkinter import *
import sqlite3

clear = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
lista = ObjetoPedido.listaP

#Cores
colorbg = "#47CDB5"
bt = "#00A687"
camp = "#B5B3C1"
colorerro = "#ff0000"
colorsucess = "#018415"
class Operario:
    def CriarPedido(): #cria pedido novo
        global root
        global janela
        root.withdraw()
        janela = Tk()
        janela.geometry("200x200")
        janela.configure(bg=colorbg)
        janela.title("Criar Pedido")
        lb = Label(janela, text="Item:")
        lb.place(x=10 ,y=35)
        lb.configure(bg=colorbg)
        it = Entry(janela, border=0) #nome
        it.place(x=10 ,y=55)
        it.configure(bg=camp)
        lb2 = Label(janela, text="Quantidade:")
        lb2.place(x=10 ,y=75)
        lb2.configure(bg=colorbg)
        it2 = Entry(janela, border=0) #quantidade
        it2.place(x=10 ,y=95)
        it2.configure(bg=camp)
        bt = Button(janela, text="Confirmar", command=lambda: Operario.salvaPedido(it.get(),it2.get())) #salva pedidos
        bt.place(x=10, y=125)
        #bt.configure(bg=bt, border=0)  

    def salvaPedido(nome, qtd):
        if nome:
            pdd = "INSERT INTO pedidos (_nome, _quantidade, _gerente, _compras, _logistica, _entrega) VALUES('"+nome+"','"+qtd+"','espera','espera','espera','não')"
            db = main.conn #caminho
            c = db.cursor()
            c.execute(pdd)
            db.commit()
            janela.withdraw()
            Operario.main()
 
    def VerLista(): #lista pedidos
        janela3 = Tk()
        janela3.geometry("250x300")
        janela3.configure(bg=colorbg)
        janela3.title("Lista Operario")
        #integrar com o tkinter e database
        
        listbox = Listbox(janela3)
        listbox.pack(side = LEFT, fill = BOTH)

        scrollbar = Scrollbar(janela3)
        scrollbar.pack(side = RIGHT, fill = BOTH)

        for values in range(100):
            listbox.insert(END, values)

        listbox.config(yscrollcommand = scrollbar.set)
        scrollbar.config(command = listbox.yview)
        
    
    def logout():
        root.quit()

    def main():
        #Janela Tkinter
        global root
        main.janela2.withdraw()
        root = Tk()
        root.geometry("200x200")
        root.configure(bg=colorbg)
        root.title("Operario")
        
        lb = Label(root, text="Perfil Operacional")
        lb.place(x=20,y=15)
        lb.configure(bg=colorbg, border=0)

        bt = Button(root, text="Solicitar produto", command=Operario.CriarPedido, border=0, cursor="hand2", activebackground=colorbg)
        bt.place(x= 20, y=40)

        bt2 = Button(root, text="Verificar solicitações", command=Operario.VerLista, border=0, cursor="hand2", activebackground=colorbg)
        bt2.place(x= 20, y=65)

        bt3 = Button(root, text="Logout", command=Operario.logout, border=0, cursor="hand2", activebackground=colorbg)
        bt3.place(x= 20, y=90)
        
