import tkinter as tk
import ttkbootstrap as ttk
from tkinter import *
from dbutils import *
from tkinter import messagebox

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

    search_button = ttk.Button(table_window, text='Pesquisar', command = search_table, bootstyle="info")
    search_button.pack(side='top', pady=5)

    table = ttk.Treeview(table_window, columns=('id', 
                                                'nome', 
                                                'categoria', 
                                                'marca', 
                                                'quantidade', 
                                                'preço'), 
                                                show='headings', bootstyle = 'info')
    table.heading('id', text='ID')
    table.heading('nome', text='Nome')
    table.heading('categoria', text='Categoria')
    table.heading('marca', text='Marca')
    table.heading('quantidade', text='Quantidade')
    table.heading('preço', text='Preço')
    table.column('id', width=1, anchor=tk.CENTER)
    table.column('nome', width=250, anchor=tk.CENTER)
    table.column('categoria', width=50, anchor=tk.CENTER)
    table.column('marca', width=50, anchor=tk.CENTER)
    table.column('quantidade', width=5, anchor=tk.CENTER)
    table.column('preço', width=5, anchor=tk.CENTER)
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
    change_window.geometry('550x380')
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
    padding = ttk.Label(change_window)
    padding.pack()
    id_frame = ttk.Frame(change_window)
    id_change_string = ttk.StringVar()
    id_label = ttk.Label(id_frame, text = 'ID: ')
    id_label.pack(side='left', fill='x', pady=5, padx = 26)
    change_id = ttk.Entry(id_frame, width = 45, textvariable = id_change_string)
    change_id.pack(side='left', pady=5)
    id_button = ttk.Button(id_frame, width = 10, text = 'Modificar')
    id_button.pack(side='left', padx = 10)
    id_frame.pack()
    nome_frame = ttk.Frame(change_window)
    nome_add_string = ttk.StringVar()
    nome_label = ttk.Label(nome_frame, text = 'Nome: ')
    nome_label.pack(side='left', fill='x', pady=5, padx = 15)
    add_nome = ttk.Entry(nome_frame, width = 45, textvariable = nome_add_string)
    add_nome.pack(side='left', pady=5)
    nome_button = ttk.Button(nome_frame, width = 10, text = 'Modificar')
    nome_button.pack(side='left', padx = 10)
    nome_frame.pack()
    categoria_frame = ttk.Frame(change_window)
    categoria_add_string = ttk.StringVar()
    categoria_label = ttk.Label(categoria_frame, text = 'Categoria: ')
    categoria_label.pack(side='left', fill='x', pady=5, padx = 6)
    add_categoria = ttk.Entry(categoria_frame, width = 45, textvariable = categoria_add_string)
    add_categoria.pack(side='left', pady=5)
    categoria_button = ttk.Button(categoria_frame, width = 10, text = 'Modificar')
    categoria_button.pack(side='left', padx = 10)
    categoria_frame.pack()
    marca_frame = ttk.Frame(change_window)
    marca_add_string = ttk.StringVar()
    marca_label = ttk.Label(marca_frame, text = 'Marca: ')
    marca_label.pack(side='left', fill='x', pady=5, padx = 15)
    add_marca = ttk.Entry(marca_frame, width = 45, textvariable = marca_add_string)
    add_marca.pack(side='left', pady=5)
    marca_button = ttk.Button(marca_frame, width = 10, text = 'Modificar')
    marca_button.pack(side='left', padx = 10)
    marca_frame.pack()
    quantidade_frame = ttk.Frame(change_window)
    quantidade_add_string = ttk.StringVar()
    quantidade_label = ttk.Label(quantidade_frame, text = 'Quantidade: ')
    quantidade_label.pack(side='left', fill='x', pady=5)
    add_quantidade = ttk.Entry(quantidade_frame, width = 45, textvariable = quantidade_add_string)
    add_quantidade.pack(side='left', pady=5)
    quantidade_button = ttk.Button(quantidade_frame, width = 10, text = 'Modificar')
    quantidade_button.pack(side = 'left', padx = 10)
    quantidade_frame.pack()
    preco_frame = ttk.Frame(change_window)
    preco_add_string = ttk.StringVar()
    preco_label = ttk.Label(preco_frame, text = 'Preço: ')
    preco_label.pack(side='left', fill='x', pady=5, padx = 17)
    add_preco = ttk.Entry(preco_frame, width = 45, textvariable = preco_add_string)
    add_preco.pack(side='left', pady=5)
    preco_button = ttk.Button(preco_frame, width = 10, text = 'Modificar')
    preco_button.pack(side = 'left', padx = 10)
    preco_frame.pack()
    


def delete_outer_func():
    global query_result
    table.delete(*table.get_children())
    query_result = lookup_one(id_string.get())
    for item in query_result:
        table.insert(parent='', index='end', values=item)


def delete_prod():
    #messagebox.askokcancel('Tem certeza de que deseja deletar o produto com o ID: {id_string.get()} ?')
    answer = messagebox.askyesno('Confirm', f'Tem certeza que deseja excluir o produto com id {id_string.get()}')
    if answer:
        try:
            rowcount = delete_one(id_string.get())
            if rowcount > 0:
                messagebox.showinfo('Sucesso', 'Produto excluído com sucesso')
            else:
                messagebox.showerror('Erro', 'Produto não encontrado')
        except:
            messagebox.showerror('Erro', 'Erro')
    

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
    table = ttk.Treeview(delete_window, columns=('id', 
                                                 'nome', 
                                                 'categoria', 
                                                 'marca', 
                                                 'quantidade', 
                                                 'preço'), 
                                                 show='headings', 
                                                 height = 2)
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
           
     
def open_main_window():
    # janela principal
    global window
    window = ttk.Toplevel(login_window)
    window.title('Menu Principal')
    window.geometry('400x300')
    window_frame = ttk.Frame(window)

    # mensagem
    bem_vindo = tk.Label(master = window_frame, text = 'Bem vindo', font = 'FiraCode 24 bold')
    bem_vindo.grid(row = 0, column = 1)

    # botões
    consultar_tabela_botao = ttk.Button(master = window_frame, text = 'Consultar tabela', command = open_table_window, width = 50, bootstyle="info")
    consultar_tabela_botao.grid(row = 1, column = 1, pady = 10)
    adicionar_produto_botao = ttk.Button(master = window_frame, text = 'Adicionar produto', command = open_add_window, width = 50, bootstyle="info")
    adicionar_produto_botao.grid(row = 2, column = 1, pady = 10)
    modificar_produto_botao = ttk.Button(master = window_frame, text = 'Modificar produto', command = open_change_window, width = 50, bootstyle="info")
    modificar_produto_botao.grid(row = 3, column = 1, pady = 10)
    excluir_produto_botao = ttk.Button(master = window_frame, text = 'Excluir produto', command = open_delete_window, width = 50, bootstyle="info")
    excluir_produto_botao.grid(row = 4, column = 1, pady = 10)
    window_frame.pack()
    login_window.withdraw()
    window.protocol("WM_DELETE_WINDOW", on_closing)


def on_closing():
    login_window.destroy()


def outer_login(_):
    login()


def login():
    global counter
    item = validate_login(login_str.get(), senha_str.get())
    if counter == 0:
            messagebox.showerror('Erro', 'Número de tentativas esgoatadas')
            quit()
    if item[0] > 0:
        messagebox.showinfo('Sucesso', 'Login efetuado com sucesso')
        open_main_window()
        login_window.withdraw()
    else:
        messagebox.showerror('Erro', f'Usuário ou senha incorretos, {counter} tentativas restantes')
        counter -= 1


# janela de login
login_window = ttk.Window(themename = 'darkly')
login_window.title('Login')
login_window.geometry('300x200')
login_window.grab_set()
login_frame = ttk.Frame(login_window)

counter = 2
login_str = ttk.StringVar()
senha_str = ttk.StringVar()
login_label = ttk.Label(login_frame, text = 'Login: ')
login_entry = ttk.Entry(login_frame, width = 20, textvariable = login_str, bootstyle="dark")
senha_label = ttk.Label(login_frame, text = 'Senha: ')
senha_entry = ttk.Entry(login_frame, width = 20, show = '*', textvariable = senha_str, bootstyle="dark")
senha_entry.bind("<Return>", outer_login)
login_button = ttk.Button(login_frame, text = 'Entrar', command = login, bootstyle="info")
login_label.grid(row = 0, column = 1)
login_entry.grid(row = 1, column = 1)
login_entry.focus_set()
senha_label.grid(row = 2, column = 1)
senha_entry.grid(row = 3, column = 1,)
login_button.grid(row = 5, column = 1, pady = 10)
login_frame.pack()
login_window.mainloop()