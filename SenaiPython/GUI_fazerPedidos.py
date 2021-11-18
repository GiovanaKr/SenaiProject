from tkinter import *
from datetime import datetime
import ObjetoPedido
lista = ObjetoPedido.listaP



def criarPedido(nome, qtd, root):                 #cria pedido ao clicas no botão
    pdd = ObjetoPedido.Pedido(nome,qtd)
    pdd.numero = (len(lista)+1)
    data = datetime.now()                         #pega data
    pdd.dataPed = data.strftime('%d/%m/%Y %H:%M') #salva data atual
    lista.append(pdd)
    root.destroy()                                #fecha


def main():                                       #tela
    root = Tk()
    root.title("Lista Pedidos")
    root.geometry('490x360')

    n = Label(root, text="Item", border=20)
    n.grid(row=1, column=0)
    nome = Entry(root, width=50)
    nome.grid(row=1, column=1)

    q = Label(root, text="quantidade", border=20)
    q.grid(row=2, column=0)
    qtd = Entry(root, width=50)
    qtd.grid(row=2, column=1)

    button_verificacao = Button(root, text="criar requisição", command= lambda: criarPedido(nome.get(), qtd.get(), root))
    button_verificacao.grid(row=3, column=1)

    root.mainloop()


if __name__ == "__main__":
    main()