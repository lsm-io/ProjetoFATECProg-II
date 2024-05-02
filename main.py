import tkinter as tk
import ttkbootstrap as ttk
from tkinter import messagebox
from dbutils import *

# função que abre a janela de consulta da tabela
def open_table_window():
    global search_string
    global table
    global items
    items = show_all_produtos()
    table_window = ttk.Toplevel(window)
    table_window.title('Tabela de produtos')
    table_window.geometry('900x500')
    table_window.grab_set()

    search_string = tk.StringVar()
    search_entry = tk.Entry(table_window, width=20, textvariable=search_string)
    search_entry.bind("<Return>", outer_func)
    search_entry.pack(side='top', fill='x', pady=5)

    search_button = ttk.Button(table_window, text='Pesquisar', command = search_table)
    search_button.pack(side='top', pady=5)

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
    table.pack(fill='both', expand=True)
    for item in items:
        table.insert(parent='', index='end', values=item)

def outer_func(_):
    search_table()

def search_table():
    search_text = search_string.get().upper()
    filtered_items = []
    for item in items:
        item_string = str(item)
        if search_text in item_string.upper():
            filtered_items.append(item)
    table.delete(*table.get_children()) 
    for item in filtered_items:
        table.insert(parent='', index='end', values=item)


def add_outer_func():
    id_str = id_add_string.get()
    nome_str = nome_add_string.get()
    categoria_str = categoria_add_string.get()
    marca_str = marca_add_string.get()
    quantidade_str = quantidade_add_string.get()
    preco_str = preco_add_string.get()
    add_one(id_str, nome_str, categoria_str, marca_str, quantidade_str, preco_str)


def open_add_window():
    global id_add_string
    global nome_add_string
    global categoria_add_string
    global marca_add_string
    global quantidade_add_string
    global preco_add_string
    add_window = ttk.Toplevel(window)
    add_window.title('Adicionar produto')
    add_window.geometry('550x500')
    add_window.grab_set()
    titulo = ttk.Label(add_window, text = 'Adicionar Produto', font = 'FiraCode 24 bold')
    titulo.pack()
    id_add_string = ttk.StringVar()
    id_label = ttk.Label(add_window, text = 'ID: ')
    id_label.pack(side='top', fill='x', pady=5)
    add_id = ttk.Entry(add_window, width = 20, textvariable = id_add_string)
    add_id.pack(side='top', fill='x', pady=5)
    nome_add_string = ttk.StringVar()
    nome_label = ttk.Label(add_window, text = 'Nome: ')
    nome_label.pack(side='top', fill='x', pady=5)
    add_nome = ttk.Entry(add_window, width = 20, textvariable = nome_add_string)
    add_nome.pack(side='top', fill='x', pady=5)
    categoria_add_string = ttk.StringVar()
    categoria_label = ttk.Label(add_window, text = 'Categoria: ')
    categoria_label.pack(side='top', fill='x', pady=5)
    add_categoria = ttk.Entry(add_window, width = 20, textvariable = categoria_add_string)
    add_categoria.pack(side='top', fill='x', pady=5)
    marca_add_string = ttk.StringVar()
    marca_label = ttk.Label(add_window, text = 'Marca: ')
    marca_label.pack(side='top', fill='x', pady=5)
    add_marca = ttk.Entry(add_window, width = 20, textvariable = marca_add_string)
    add_marca.pack(side='top', fill='x', pady=5)
    quantidade_add_string = ttk.StringVar()
    quantidade_label = ttk.Label(add_window, text = 'Quantidade: ')
    quantidade_label.pack(side='top', fill='x', pady=5)
    add_quantidade = ttk.Entry(add_window, width = 20, textvariable = quantidade_add_string)
    add_quantidade.pack(side='top', fill='x', pady=5)
    preco_add_string = ttk.StringVar()
    preco_label = ttk.Label(add_window, text = 'Preço: ')
    preco_label.pack(side='top', fill='x', pady=5)
    add_preco = ttk.Entry(add_window, width = 20, textvariable = preco_add_string)
    add_preco.pack(side='top', fill='x', pady=5)

    add_button = ttk.Button(add_window, text='Adicionar', command = add_outer_func)
    add_button.pack(side='top', fill='x', pady=5)


def open_change_window():
    change_window = ttk.Toplevel(window)
    change_window.title('Modificar produto')
    change_window.geometry('550x500')
    change_window.grab_set()
    titulo = ttk.Label(change_window, text = 'Modificar Produto', font = 'FiraCode 24 bold')
    titulo.pack()

    input_frame = ttk.Frame(change_window)
    id_lookup = ttk.Label(input_frame, text = 'Digite o ID do produto: ')
    id_lookup.pack(side = 'left')
    lookup = ttk.Entry(input_frame, width = 5)
    lookup.pack(side = 'left', padx = 5)
    lookup_button = ttk.Button(input_frame, text = 'Pesquisar')
    lookup_button.pack(side = 'left', padx = 5)
    input_frame.pack()


def delete_outer_func():
    global query_result
    table.delete(*table.get_children())
    query_result = lookup_one(id_string.get())
    for item in query_result:
        table.insert(parent='', index='end', values=item)


def delete_prod():
    #messagebox.askokcancel('Tem certeza de que deseja deletar o produto com o ID: {id_string.get()} ?')
    try:
        delete_one(id_string.get())
        messagebox.showinfo('Sucesso', 'Produto excluído com sucesso')
    except:
        messagebox.showerror('Erro', 'Produto não encontrado')
    


def open_delete_window():
    global id_string
    global query_result
    global table
    global delete_window
    global lookup
    delete_window = ttk.Toplevel(window)
    delete_window.title('Excluir produto')
    delete_window.geometry('800x300')
    delete_window.grab_set()
    titulo = ttk.Label(delete_window, text = 'Excluir Produto', font = 'FiraCode 24 bold')
    titulo.pack()
    input_frame = ttk.Frame(delete_window)
    id_lookup = ttk.Label(input_frame, text = 'Digite o ID do produto: ')
    id_lookup.pack(side = 'left')
    id_string = ttk.StringVar()
    lookup = ttk.Entry(input_frame, width = 5, textvariable = id_string)
    lookup.pack(side = 'left', padx = 5)
    lookup_button = ttk.Button(input_frame, text = 'Pesquisar', command = delete_outer_func)
    lookup_button.pack(side = 'left', padx = 5)
    input_frame.pack()
    table = ttk.Treeview(delete_window, columns=('id', 'nome', 'categoria', 'marca', 'quantidade', 'preço'), show='headings', height = 2)
    table.heading('id', text='ID')
    table.heading('nome', text='Nome')
    table.heading('categoria', text='Categoria')
    table.heading('marca', text='Marca')
    table.heading('quantidade', text='Quantidade')
    table.heading('preço', text='Preço')
    table.column('id', width=1)
    table.column('nome', width=100)
    table.column('categoria', width=50)
    table.column('marca', width=50)
    table.column('quantidade', width=1)
    table.column('preço', width=1)
    table.pack(fill = 'x', pady=5)

    delete_button = ttk.Button(delete_window, text='Excluir', command = delete_prod)
    delete_button.pack(side='top', pady=5)
    delete_window.mainloop()


def open_custom_window():
    d = 1


# janela principal
window = ttk.Window(themename = 'flatly')
window.title('Menu Principal')
window.geometry('450x400')

# mensagem
bem_vindo = tk.Label(master = window, text = 'Bem vindo', font = 'FiraCode 24 bold')
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