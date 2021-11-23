import sqlite3
from sqlite3 import Error

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

nome=input("digite nome: ")
quantidade=input("digite quantidade: ")
gerente=input("gerente aprovo?1/2")

vsql="INSERT INTO tb_pedidos     (nome, quantidade, gerente)    VALUES('"+nome+"','"+quantidade+"','"+gerente+"')"
def inserir(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print("resistrado")
    except Error as ex:
        print(ex)

inserir(vcon, vsql)
