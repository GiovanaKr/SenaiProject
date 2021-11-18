from tkinter import *
import ObjetoPedido
lista = ObjetoPedido.listaP

def main():
    root = Tk()
    root.title("Estoque")
    root.geometry('490x560')

    x = 0
    for obj in  lista:
        # t = Label(root, text=str(obj.nome)+" "+str(obj.qtd+"\n"))
        # t.grid(row=x, column=0)
        # x += 1

        #[data]banana - 1 penca - req nº x
        t = Label(root, text="["+str(obj.dataPed)+"]"+str(obj.nome)+" - "+str(obj.qtd)+" - nº "+str(obj.numero), anchor="w")
        t.grid(row=x)
        x += 1

        
    root.mainloop()

if __name__ == "__main__":
    main()