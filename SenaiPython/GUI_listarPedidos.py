from tkinter import *
from ObjetoPedido import listaP
lista = listaP

#SOCORRO

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