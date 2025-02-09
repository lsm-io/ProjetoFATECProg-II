import tkinter as tk
import ttkbootstrap as ttk
from tkinter import *
from dbutils import *
from tkinter import messagebox
import hashlib

# abre e constrói a janela de consulta da tabela
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
    search_entry = ttk.Entry(table_window, width=20, textvariable=search_string)
    search_entry.bind("<Return>", outer_func)
    search_entry.pack(side='top', fill='x', pady=5)

    search_button = ttk.Button(table_window, text='Pesquisar', command = search_table, bootstyle="info")
    search_button.pack(side='top', pady=5)

    table = ttk.Treeview(table_window, columns=('id', # Inicializa o widget da tabela
                                                'nome', 
                                                'categoria', 
                                                'marca', 
                                                'quantidade', 
                                                'preço'), 
                                                show='headings', 
                                                bootstyle = 'info')
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
    for item in items: # Preenche a tablea com os dados
        table.insert(parent='', index='end', values=item)


def outer_func(_):
    search_table()


# busca na tabela 
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


# adiciona os dados fornecidos pelo usuário no banco de dados
def add_outer_func():
    if nome_add_string.get() == '' or categoria_add_string.get() == '' or marca_add_string.get() == '' or quantidade_add_string.get() == '' or preco_add_string.get() == '':
        messagebox.showerror('Erro', 'Preencha todos os campos!')
    else:
        try:
            add_one(nome_add_string.get(), categoria_add_string.get(), marca_add_string.get(), quantidade_add_string.get(), preco_add_string.get())
            messagebox.showinfo('Sucesso', 'Produto adicionado com sucesso!')
        except:
            messagebox.showerror('Erro', 'Erro ao adicionar produto')


# abre e constrói a janela para adicionar produtos
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
    titulo = ttk.Label(add_window, text = 'Adicionar Produto', font = 'montserrat 24')
    titulo.pack()
    nome_add_string = ttk.StringVar()
    nome_label = ttk.Label(add_window, text = 'Nome: ')
    nome_label.pack(side='top', pady=5)
    add_nome = ttk.Entry(add_window, width = 40, textvariable = nome_add_string)
    add_nome.pack(side='top', pady=5)
    categoria_add_string = ttk.StringVar()
    categoria_label = ttk.Label(add_window, text = 'Categoria: ')
    categoria_label.pack(side='top', pady=5)
    add_categoria = ttk.Entry(add_window, width = 40, textvariable = categoria_add_string)
    add_categoria.pack(side='top', pady=5)
    marca_add_string = ttk.StringVar()
    marca_label = ttk.Label(add_window, text = 'Marca: ')
    marca_label.pack(side='top', pady=5)
    add_marca = ttk.Entry(add_window, width = 40, textvariable = marca_add_string)
    add_marca.pack(side='top', pady=5)
    quantidade_add_string = ttk.StringVar()
    quantidade_label = ttk.Label(add_window, text = 'Quantidade: ')
    quantidade_label.pack(side='top', pady=5)
    add_quantidade = ttk.Entry(add_window, width = 40, textvariable = quantidade_add_string)
    add_quantidade.pack(side='top', pady=5)
    preco_add_string = ttk.StringVar()
    preco_label = ttk.Label(add_window, text = 'Preço: ')
    preco_label.pack(side='top', pady=5)
    add_preco = ttk.Entry(add_window, width = 40, textvariable = preco_add_string)
    add_preco.pack(side='top', pady=5)

    add_button = ttk.Button(add_window, text='Adicionar', command = add_outer_func, bootstyle = 'info')
    add_button.pack(side='top', pady=5)


# busca no banco de dados o produto com o ID fornecido
def pesquisar():
    global lookup_string
    result = lookup_one(lookup_string.get()) # retorna uma lista de tuplas
    if result == []: # se a busca retornar uma lista em branco
        mod_id_string.set('')
        mod_nome_string.set('')
        mod_categoria_string.set('')
        mod_marca_string.set('')
        mod_quantidade_string.set('')
        mod_preco_string.set('')
        mod_button['state'] = 'disabled'
        messagebox.showerror('Erro', 'Produto não encontrado') # retorna o erro
    else:
        list = [] # inicializa uma nova lista com os dados 
        for item in result:
            list.append(item[0])
            list.append(item[1])
            list.append(item[2])
            list.append(item[3])
            list.append(item[4])
            list.append(item[5])
        
        # define o campo de entrada dos widgets com os dados recebidos do banco
        mod_id_string.set(list[0])
        mod_nome_string.set(list[1])
        mod_categoria_string.set(list[2])
        mod_marca_string.set(list[3])
        mod_quantidade_string.set(list[4])
        mod_preco_string.set(list[5])
        mod_button['state'] = 'normal'


# modifica o produto de acordo com os dados modificados recebidos
def update():
    try:
        modify(mod_id_string.get(), 
           mod_nome_string.get(), 
           mod_categoria_string.get(), 
           mod_marca_string.get(), 
           mod_quantidade_string.get(), 
           mod_preco_string.get(), 
           lookup_string.get())
        messagebox.showinfo('Sucesso', 'Produto modificado com sucesso')
    except: 
        messagebox.showerror('Erro', 'Erro')


# abre e constrói a janela de modificar
def open_change_window():
    global mod_button
    global lookup_string
    global mod_id_string
    global mod_nome_string
    global mod_categoria_string
    global mod_marca_string
    global mod_quantidade_string
    global mod_preco_string
    change_window = ttk.Toplevel(window)
    change_window.title('Modificar produto')
    change_window.geometry('550x450')
    change_window.grab_set()
    titulo = ttk.Label(change_window, text = 'Modificar Produto', font = 'montserrat 24')
    titulo.pack()

    lookup_string = ttk.StringVar()
    input_frame = ttk.Frame(change_window)
    id_lookup = ttk.Label(input_frame, text = 'Digite o ID do produto: ')
    id_lookup.pack(side = 'left')
    lookup = ttk.Entry(input_frame, width = 5, textvariable = lookup_string)
    lookup.pack(side = 'left', padx = 5)
    lookup_button = ttk.Button(input_frame, text = 'Pesquisar', command = pesquisar, bootstyle = 'info')
    lookup_button.pack(side = 'left', padx = 5)
    input_frame.pack()
    padding = ttk.Label(change_window)
    padding.pack()
    mod_id_string = ttk.StringVar()
    mod_nome_string = ttk.StringVar()
    mod_categoria_string = ttk.StringVar()
    mod_marca_string = ttk.StringVar()
    mod_quantidade_string = ttk.StringVar()
    mod_preco_string = ttk.StringVar()
    mod_frame = ttk.Frame(change_window)
    id_label = ttk.Label(mod_frame, text = 'ID:')
    id_entry = ttk.Entry(mod_frame, width = 40, textvariable = mod_id_string, bootstyle="dark")
    nome_label = ttk.Label(mod_frame, text = 'Nome:')
    nome_entry = ttk.Entry(mod_frame, width = 40, textvariable = mod_nome_string, bootstyle="dark")
    categoria_label = ttk.Label(mod_frame, text = 'Categoria:')
    categoria_entry = ttk.Entry(mod_frame, width = 40, textvariable = mod_categoria_string, bootstyle="dark")
    marca_label = ttk.Label(mod_frame, text = 'Marca:')
    marca_entry = ttk.Entry(mod_frame, width = 40, textvariable = mod_marca_string, bootstyle = 'dark')
    quantidade_label = ttk.Label(mod_frame, text = 'Quantidade:')
    quantidade_entry = ttk.Entry(mod_frame, width = 40, textvariable = mod_quantidade_string, bootstyle = 'dark')
    preco_label = ttk.Label(mod_frame, text = 'Preço:')
    preco_entry = ttk.Entry(mod_frame, width = 40, textvariable = mod_preco_string, bootstyle = 'dark')
    mod_button = ttk.Button(mod_frame, text = 'Modificar', command = update, bootstyle="info")
    id_label.grid(row = 0, column = 1)
    id_entry.grid(row = 1, column = 1)
    nome_label.grid(row = 2, column = 1)
    nome_entry.grid(row = 3, column = 1)
    categoria_label.grid(row = 4, column = 1)
    categoria_entry.grid(row = 5, column = 1)
    marca_label.grid(row = 6, column = 1)
    marca_entry.grid(row = 7, column = 1)
    quantidade_label.grid(row = 8, column = 1)
    quantidade_entry.grid(row = 9, column = 1)
    preco_label.grid(row = 10, column = 1)
    preco_entry.grid(row = 11, column = 1)
    mod_button.grid(row = 12, column = 1, pady = 10)
    mod_frame.pack()

    
# preenche a tabela com os dados recebidos do banco de dados
def delete_search():
    global query_result
    table.delete(*table.get_children())
    query_result = lookup_one(id_string.get())
    for item in query_result:
        table.insert(parent='', index='end', values=item)


# exclui o produto de acordo com o id digitado
def delete_prod():
    answer = messagebox.askyesno('Confirm', f'Tem certeza que deseja excluir o produto com id {id_string.get()}')
    if answer:
        try:
            rowcount = delete_one(id_string.get()) # recebe o número de fileiras modificadas pelo banco de dados
            if rowcount > 0: # se o número for maior que 0, significa que a exclusão ocorreu de fato
                messagebox.showinfo('Sucesso', 'Produto excluído com sucesso')
            else: # senão o produto correspondente ao id não existe 
                messagebox.showerror('Erro', 'Produto não encontrado')
        except:
            messagebox.showerror('Erro', 'Erro')
    

# abre e constrói a janela de excluir
def open_delete_window():
    global id_string
    global query_result
    global table
    global delete_window
    global lookup
    delete_window = ttk.Toplevel(window)
    delete_window.title('Excluir produto')
    delete_window.geometry('1000x200')
    delete_window.grab_set()
    titulo = ttk.Label(delete_window, text = 'Excluir Produto', font = 'montserrat 24')
    titulo.pack()
    input_frame = ttk.Frame(delete_window)
    id_lookup = ttk.Label(input_frame, text = 'Digite o ID do produto: ')
    id_lookup.pack(side = 'left')
    id_string = ttk.StringVar()
    lookup = ttk.Entry(input_frame, width = 5, textvariable = id_string)
    lookup.pack(side = 'left', padx = 5)
    lookup_button = ttk.Button(input_frame, text = 'Pesquisar', command = delete_search, bootstyle = 'info')
    lookup_button.pack(side = 'left', padx = 5)
    input_frame.pack()
    table = ttk.Treeview(delete_window, columns=('id', 
                                                 'nome', 
                                                 'categoria', 
                                                 'marca', 
                                                 'quantidade', 
                                                 'preço'), 
                                                 show='headings', 
                                                 height = 2, bootstyle = 'info')
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
    table.column('quantidade', width=1, anchor=tk.CENTER)
    table.column('preço', width=1, anchor=tk.CENTER)
    table.pack(fill = 'x', pady=5)

    delete_button = ttk.Button(delete_window, text='Excluir', command = delete_prod, bootstyle = 'danger')
    delete_button.pack(side='top', pady=5)
           
    
# abre e constrói a janela de menu principal
def open_main_window():
    global window
    window = ttk.Toplevel(login_window)
    window.title('Menu Principal')
    window.geometry('400x300')
    window_frame = ttk.Frame(window)

    bem_vindo = tk.Label(master = window_frame, text = 'Bem vindo', font = 'montserrat 24')
    bem_vindo.grid(row = 0, column = 1)

    consultar_tabela_botao = ttk.Button(master = window_frame, 
                                        text = 'Consultar tabela', 
                                        command = open_table_window, 
                                        width = 50, 
                                        bootstyle="info")
    consultar_tabela_botao.grid(row = 1, column = 1, pady = 10)
    adicionar_produto_botao = ttk.Button(master = window_frame, 
                                         text = 'Adicionar produto', 
                                         command = open_add_window, 
                                         width = 50, 
                                         bootstyle="info")
    adicionar_produto_botao.grid(row = 2, column = 1, pady = 10)
    modificar_produto_botao = ttk.Button(master = window_frame, 
                                         text = 'Modificar produto', 
                                         command = open_change_window, 
                                         width = 50, 
                                         bootstyle="info")
    modificar_produto_botao.grid(row = 3, column = 1, pady = 10)
    excluir_produto_botao = ttk.Button(master = window_frame, 
                                       text = 'Excluir produto', 
                                       command = open_delete_window, 
                                       width = 50, 
                                       bootstyle="info")
    excluir_produto_botao.grid(row = 4, column = 1, pady = 10)
    window_frame.pack()
    login_window.withdraw()
    window.protocol("WM_DELETE_WINDOW", on_closing)


# ao fechar a janela principal, encerra o processo de fundo de plano
def on_closing():
    login_window.destroy()


def outer_login(_):
    login()


# valida o login e senha digitados
def login():
    global counter
    encrypted_password = hashlib.sha256(senha_str.get().encode()).hexdigest()
    item = validate_login(login_str.get(), encrypted_password)
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


def cadastro():
    if cadastro_login_string.get() == '' or cadastro_senha_string.get() == '' or cadastro_senha_confirm_string.get() == '':
        messagebox.showerror('Erro', 'Preencha todos os campos')
    else:
        if cadastro_senha_string.get() == cadastro_senha_confirm_string.get():
            try:
                encrypted_password = hashlib.sha256(cadastro_senha_string.get().encode()).hexdigest()
                register_user(cadastro_login_string.get(), encrypted_password)
                messagebox.showinfo('Sucesso', 'Usuário cadastrado com sucesso')
            except:
                messagebox.showerror('Erro', 'Nome de usuário indisponível')
        else:
            messagebox.showerror('Erro', 'As senhas digitadas são diferentes')


def cadastro_window():
    global cadastro_login_string
    global cadastro_senha_string
    global cadastro_senha_confirm_string
    cadastro_window = ttk.Toplevel(login_window)
    cadastro_window.title('Cadastrar novo usuário')
    cadastro_window.geometry('300x250')
    cadastro_window.grab_set()
    titulo = ttk.Label(cadastro_window, text = 'Cadastro', font = 'montserrat 24')
    titulo.pack()
    input_frame = ttk.Frame(cadastro_window)
    cadastro_login_string = ttk.StringVar()
    cadastro_senha_string = ttk.StringVar()
    cadastro_senha_confirm_string = ttk.StringVar()
    login_label = ttk.Label(input_frame, text = 'Login:')
    login_entry = ttk.Entry(input_frame, width = 20, bootstyle="dark", textvariable = cadastro_login_string)
    login_label.grid(row = 0, column = 1)
    login_entry.grid(row = 1, column = 1)
    senha_label = ttk.Label(input_frame, text = 'Senha:')
    senha_entry = ttk.Entry(input_frame, width = 20, show = '*', bootstyle="dark", textvariable = cadastro_senha_string)
    senha_label.grid(row = 2, column = 1)
    senha_entry.grid(row = 3, column = 1)
    senha_confirm = ttk.Label(input_frame, text = 'Repita a Senha:')
    senha_confirm_entry = ttk.Entry(input_frame, width = 20, show = '*', bootstyle="dark", textvariable = cadastro_senha_confirm_string)
    senha_confirm.grid(row = 4, column = 1)
    senha_confirm_entry.grid(row = 5, column = 1)
    cadastro_button = ttk.Button(input_frame, text = 'Cadastrar', command = cadastro, bootstyle = 'info')
    cadastro_button.grid(row = 6, column = 1, pady = 10)
    input_frame.pack()
    

# inicializa o programa pela janela de login
login_window = ttk.Window(themename = 'flatly')
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
cadastro_button = ttk.Button(login_frame, text = 'Cadastrar Novo Usuário', command = cadastro_window, bootstyle="success")
cadastro_button.grid(row = 6, column = 1, pady = 10)
login_frame.pack()
login_window.mainloop()
