import tkinter as tk
import sqlite3
import tabulate

def show_all_produtos():
    connection = sqlite3.connect("loja.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM produtos")
    items = cursor.fetchall()
    
    print(tabulate.tabulate(items, headers=["ID", "Nome", "Categoria", "Marca", "Quantidade", "Preço"], tablefmt="grid"))

    connection.commit()
    connection.close()


show_all_produtos()
