from tkinter import *
import sqlite3
from tkinter import ttk

conn = sqlite3.connect('db.db')
c = conn.cursor()

#sair da def lista()
#input incorreto simples
#loop lista

#Cores
colorbg = "#47CDB5"
bt = "#00A687"
camp = "#B5B3C1"
colorerro = "#ff0000"
colorsucess = "#018415"


def menu_gerente():
    root = Tk()
    root.geometry("200x200")
    root.configure(bg=colorbg)
    root.title("Gerente")
    
    lb = Label(root, text="Perfil Gerencial")
    lb.place(x=20,y=15)
    lb.configure(bg=colorbg, border=0)

    bt = Button(root, text="Verificar/Modificar solicitações", border=0, cursor="hand2",command=Verificar, activebackground=colorbg)                                                                
    bt.place(x= 20, y=40)

    #bt2 = Button(root, text="Logout", command=main, border=0, cursor="hand2", activebackground=colorbg)
    #bt2.place(x= 20, y=90)
    

def Verificar():
    def modificar():

        itemSelection = my_tree.selection()[0]
        valores = my_tree.item(itemSelection, 'values')

        req = valores[0]
        
        nome=bt_codigon.get()
        
        quantidade=bt_codigog.get()

        gerente=bt_codigoa.get()

        c.execute("UPDATE pedidos SET _nome='"+nome+"', _quantidade='"+quantidade+"', _gerente ='"+gerente+"' WHERE _requisicao='"+req+"'")
        conn.commit()

        janela1.withdraw()
        Verificar()  

    def aprovar(): ##aprova direto

        itemSelection = my_tree.selection()[0]
        valores = my_tree.item(itemSelection, 'values')

        req = valores[0]

        c.execute("UPDATE pedidos SET  _gerente ='aprovado' WHERE _requisicao='"+req+"'")
        conn.commit()

        janela1.withdraw()
        Verificar() 

    def negar(): ##nega direto

        itemSelection = my_tree.selection()[0]
        valores = my_tree.item(itemSelection, 'values')

        req = valores[0]

        c.execute("UPDATE pedidos SET  _gerente ='negado' WHERE _requisicao='"+req+"'")
        conn.commit()

        janela1.withdraw()
        Verificar() 


    janela1 = Tk()
    janela1.geometry("450x400")
    janela1.configure(bg=colorbg, border=0)
    janela1.title("Gerente")

    #query the database
    c.execute("SELECT *,oid FROM pedidos")
    data = c.fetchall()
 
    frames1= Frame(janela1,width = 450, height=150, highlightbackground ="#47CDB5", highlightthicknes=3)
    frames1.grid(row=0,column=0)
    
    frames2= Frame(janela1,width = 450, height=150, highlightbackground ="#47CDB5", highlightthicknes=3)
    frames2.grid(row=1,column=0)

    
    bt_alterar=Button(frames1,text='Alterar',command=modificar)
    bt_alterar.place(x=320, y=10)

    bt_ap=Button(frames1,text='Aprovar',command=aprovar)
    bt_ap.place(x=220, y=10)

    bt_ng=Button(frames1,text='Negar',command=negar)
    bt_ng.place(x=120, y=10)

    bt_codigo=Label(frames1,text='Requsição')
    bt_codigo.place(y=2,x=15)
    bt_codigoe=Entry(frames1,width=5)
    bt_codigoe.place(x=20,y=30)

    bt_codigo_nome=Label(frames1,text='Nome')

    bt_codigo_nome.place(y=60,x=15)
    bt_codigon=Entry(frames1,width=15)
    bt_codigon.place(x=20,y=90)

    bt_codigo_qtd=Label(frames1,text='Quantidade')
    bt_codigo_qtd.place(y=60,x=175)
    bt_codigog=Entry(frames1,width=5)
    bt_codigog.place(x=180,y=90)

    bt_codigo_ap=Label(frames1,text='Aprovado')
    bt_codigo_ap.place(y=60,x=300)
    bt_codigoa=Entry(frames1,width=15)
    bt_codigoa.place(x=305,y=90)
    
    my_tree = ttk.Treeview(frames2)
    my_tree['columns'] = ("req","nome", "qtd", "ger")

    my_scrollbar = ttk.Scrollbar(frames2, orient="vertical", command=my_tree.yview)
    my_scrollbar.pack(side='right', fill='y')
    my_tree.configure(yscrollcommand=my_scrollbar.set)

    my_tree.column("#0", width=0)
    my_tree.column("req", anchor=W, width= 60)
    my_tree.column("nome", anchor=CENTER, width=100)
    my_tree.column("qtd", anchor=W, width=120)
    my_tree.column("ger", anchor=W, width=120)

    my_tree.heading("#0", text="Label", anchor=W)
    my_tree.heading("req", text="nº req", anchor=W)
    my_tree.heading("nome", text="Produto", anchor=CENTER)
    my_tree.heading("qtd", text="Qtd", anchor=W)
    my_tree.heading("ger", text="Gerente", anchor=W)

    count = 0
    for record in data:
        my_tree.insert(parent="", index='end', iid=count, text=" ", values=(str(record[0]), str(record[1]), str(record[2]), str(record[3])))
        count +=1
    
    my_tree.pack(side='left', fill='y')
    


# def lista():
#     c.execute("SELECT * FROM pedidos order by _requisicao")
#     db = main.conn #caminho
#     c = db.cursor()
#     c.execute(pdd)
#     db.commit()
#     lista = conn.fetchall()
#     print(lista)


# def atualizarpedido( ):
    
#     up ="UPDATE  pedidos  SET  , _gerente ='"+gerente+"' where _requisicao= '"+req+"' "
#     db = main.conn #caminho
    
#     c = db.cursor()
#     c.execute(up)
#     db.commit()
#     janela.withdraw()
#     Operario.Main()
