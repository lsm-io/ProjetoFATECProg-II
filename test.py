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

def validate_login(user, password):
    connection = sqlite3.connect("loja.db")
    cursor = connection.cursor()
    cursor.execute("SELECT count(*) FROM usuarios WHERE user = (?) AND pw = (?)", (user, password))
    item = cursor.fetchone()
    connection.commit()
    connection.close()
    return item

user = input('Enter username: ')
password = input('Enter password: ')

item = validate_login(user, password)
if item[0] > 0:
    print(item[0])