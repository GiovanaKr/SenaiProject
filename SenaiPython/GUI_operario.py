from tkinter import *
import GUI_estoque
import GUI_fazerPedidos
import GUI_listar

root = Tk()
root.title("Perfil Operario")
root.geometry('490x560')

def fazerPedido():
    GUI_fazerPedidos.main()

def verificarPedidos():
    GUI_listar.main()

def estoque():
    GUI_estoque.main()

def destroi():
    root.destroy()

def main():
    
    l = Label(root, text="Bom dia funcionario")
    l.grid(row=0, column=0)

    button_pedido = Button(root, text="Criar pedido", padx=30, pady=5, command=fazerPedido)
    button_pedido.grid(row=1, column=0)

    button_verificacao = Button(root, text="Verificar pedidos", padx=18, pady=5, command=verificarPedidos)
    button_verificacao.grid(row=2, column=0)

    button_estoque = Button(root, text="Abrir estoque", padx=27, pady=5, command=estoque)
    button_estoque.grid(row=3, column=0)

    button_sair = Button(root, text="logout", padx=30, pady=5, command=destroi)
    button_sair.grid(row=4, column=0)

    root.mainloop()

if __name__ == "__main__":
    main()