import os
from tkinter import *
import sqlite3

#Cores
colorbg = "#47CDB5"
bt = "#00A687"
camp = "#B5B3C1"
colorerro = "#ff0000"
colorsucess = "#018415"


def menu_compras():
    root = Tk()
    root.geometry("200x200")
    root.configure(bg=colorbg)
    root.title("Compras")
    
    lb = Label(root, text="Perfil Compras")
    lb.place(x=20,y=15)
    lb.configure(bg=colorbg, border=0)

    bt = Button(root, text="Verificar/Modificar solicitações", command=Lista, border=0, cursor="hand2", activebackground=colorbg)
    bt.place(x= 20, y=40)

    #bt2 = Button(root, text="Logout", command=main, border=0, cursor="hand2", activebackground=colorbg)
    #bt2.place(x= 20, y=90)

def Lista(): 
    janela = Tk()
    janela.geometry("350x300")
    janela.configure(bg=colorbg)
    janela.title("Lista Compras")

    def done(): ##passa adiante
        conn = sqlite3.connect('db.db')
        c = conn.cursor()
        c.execute("SELECT *,oid FROM pedidos")
        data = c.fetchall()

        for key in l:
            if l.get(key)[1].get() == 1:
                print("key: "+str(key))
                c.execute("UPDATE pedidos SET _compras = 'aprovado' WHERE _requisicao = '"+key+"' ")
                conn.commit()
                conn.close()
    
    def miss(): ##cancela
        conn = sqlite3.connect('db.db')
        c = conn.cursor()
        c.execute("SELECT *,oid FROM pedidos")
        data = c.fetchall()

        for key in l:
            if l.get(key)[1].get() == 1:
                print("key: "+str(key))
                c.execute("UPDATE pedidos SET _compras = 'negado' WHERE _requisicao = '"+key+"' ")
                conn.commit()
                conn.close()

    def clean(): ##limpa selecionados
        for key in l:
            l.get(key)[0].deselect()
            

    frames1= Frame(janela,width = 250, height=300, highlightbackground ="#47CDB5", highlightthicknes=3)
    frames1.grid(row=0,column=0)
    frames2= Frame(janela,width = 200, height=300, highlightbackground ="#47CDB5", highlightthicknes=3)
    frames2.grid(row=0,column=1)

    bt_done = Button(frames2, text="compra feita", command=done)
    bt_done.place(x=30 ,y=40)

    bt_done = Button(frames2, text="item em falta", command=miss)
    bt_done.place(x=30 ,y=80)

    bt_done = Button(frames2, text="limpar", command=clean)
    bt_done.place(x=30 ,y=120)

    conn = sqlite3.connect('db.db')
    c = conn.cursor()
    c.execute("SELECT *,oid FROM pedidos")
    data = c.fetchall()

    l = {}
    x=0
    for obj in data:
        var = IntVar()
        b = Checkbutton(frames1, text="req nº" + str(obj[0]) +" "+ str(obj[1]) +" "+ str(obj[2]), variable=var)
        l[obj[0]]=[b, var]
        l.get(obj[0])[0].pack(anchor=W)
        x+=1
    
