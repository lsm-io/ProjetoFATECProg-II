import tkinter as tk
import ttkbootstrap as ttk
from dbutils import *

# janela de consulta da tabela
def open_table_window():
    items = show_all_produtos()
    table_window = ttk.Toplevel(window)
    table_window.title('Tabela de produtos')
    table_window.geometry('900x500')
    table = ttk.Treeview(table_window, columns=('id', 'nome', 'categoria', 'marca', 'quantidade', 'preço'), show='headings')
    table.heading('id', text='ID')
    table.heading('nome', text='Nome')
    table.heading('categoria', text='Categoria')
    table.heading('marca', text='Marca')
    table.heading('quantidade', text='Quantidade')
    table.heading('preço', text='Preço')
    table.column('id', width=1)
    table.column('nome', width=250)
    table.column('categoria', width=50)
    table.column('marca', width=50)
    table.column('quantidade', width=5)
    table.column('preço', width=5)
    table.pack(fill = 'both', expand = True)
    for item in items:
        table.insert(parent='', index='end', values=item)

def open_add_window():
    c = 2


def open_change_window():
    a = 2


def open_delete_window():
    b = 1


def open_custom_window():
    d = 1


# main window
window = ttk.Window(themename = 'flatly')
window.title('Menu Principal')
window.geometry('450x400')

# labels
bem_vindo = tk.Label(master = window, text = 'Bem vindo', font = 'calibri 24 bold')
bem_vindo.place(relx=0.5, rely=0.1, anchor='center')

# botões
consultar_tabela_botao = ttk.Button(master = window, text = 'Consultar tabela', command = open_table_window, width = 50)
consultar_tabela_botao.place(relx=0.5, rely=0.3, anchor='center')
adicionar_produto_botao = ttk.Button(master = window, text = 'Adicionar produto', command = open_add_window, width = 50)
adicionar_produto_botao.place(relx=0.5, rely=0.4, anchor='center')
modificar_produto_botao = ttk.Button(master = window, text = 'Modificar produto', command = open_change_window, width = 50)
modificar_produto_botao.place(relx=0.5, rely=0.5, anchor='center')
excluir_produto_botao = ttk.Button(master = window, text = 'Excluir produto', command = open_delete_window, width = 50)
excluir_produto_botao.place(relx=0.5, rely=0.6, anchor='center')
consulta_custom_botao = ttk.Button(master = window, text = 'Consulta personalizada', command = open_custom_window, width = 50)
consulta_custom_botao.place(relx=0.5, rely=0.7, anchor='center')

# run
window.mainloop()