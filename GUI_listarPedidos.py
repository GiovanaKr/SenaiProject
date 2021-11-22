import sqlite3
from sqlite3 import Error

from tkinter import *
from ObjetoPedido import listaP
lista = listaP

#SOCORRO
###############cria conexão
def ConexaoBanco():
    caminho = 'C:\\Users\\SENAI\\Downloads\\TrabalhoSenai-main\\databaseeeee.db'
    con = None
    try:
        con=sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con

vcon=ConexaoBanco()

############criar tabela
vsql="""CREATE TABLE tb_pedidos(
        numero_requisição INTEGER PRIMARY KEY AUTOINCREMENT,
        nome STRING,
        quantidade STRING,
        gerente INTEGER,
        compras INTEGER,
        logistica INTEGER,
        entrega INTEGER
        );"""

def criarTabela(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        print("Table criada")
    except Error as ex:
        print(ex)


criarTabela(vcon,vsql)
vcon.close()
#####################





def main():
    root = Tk()
    root.title("Lista Pedidos")
    root.geometry('490x560')

    x = 0
    for obj in  lista:
        t = Label(root, text=str(obj.numero)+"\n")
        t.grid(row=x, column=0)
        x += 1

        t = Label(root, text=str(obj.nome)+" "+str(obj.qtd)+str(obj.dataPed)+"\n")
        t.grid(row=x, column=0)
        x += 1

        t = Label(root, text=str(obj.aprovGen)+"["+str(obj.dataGen)+"]"+"\n")
        t.grid(row=x, column=0)
        x += 1

        t = Label(root, text=str(obj.aprovCom)+str(obj.dataCom)+"\n")
        t.grid(row=x, column=0)
        x += 1

        t = Label(root, text=str(obj.log)+str(obj.dataLog)+"\n")
        t.grid(row=x, column=0)
        x += 1

        t = Label(root, text="  ")
        t.grid(row=x, column=0)
        x += 1
        t = Label(root, text="  ")
        t.grid(row=x, column=0)

    root.mainloop()


if __name__ == "__main__":
    main()