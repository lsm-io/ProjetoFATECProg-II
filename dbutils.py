import sqlite3

# Validação de login
def validate_login(user, password):
    connection = sqlite3.connect("loja.db")
    cursor = connection.cursor()
    cursor.execute("SELECT count(*) FROM usuarios WHERE user = (?) AND pw = (?)", (user, password))
    item = cursor.fetchone()
    connection.commit()
    connection.close()
    return item

# Criação de um novo usuário
def register_user(username, password):
    connection = sqlite3.connect("loja.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO usuarios (user, pw) VALUES (?,?)", (username, password))
    connection.commit()
    connection.close()


# Seleciona todos os produtos da tabela
def show_all_produtos():
    connection = sqlite3.connect("loja.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM produtos")
    items = cursor.fetchall()
    connection.commit()
    connection.close()
    return items

# Seleciona da tabela o produto com o id correspondente
def lookup_one(id: str):
    connection = sqlite3.connect("loja.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM produtos WHERE id = (?)", (id,))
    item = cursor.fetchall()
    connection.commit()
    connection.close()
    return item

# Adiciona uma nova entrada na tabela
def add_one(nome, categoria, marca, quantidade, preco):
    connection = sqlite3.connect("loja.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO produtos (nome, categoria, marca, quantidade, preco) VALUES (?,?,?,?,?)", (nome, categoria, marca, quantidade, preco))
    connection.commit()
    connection.close()

# Modifica uma entrada da tabela
def modify(mod1, mod2, mod3, mod4, mod5, mod6, id):
    connection = sqlite3.connect("loja.db")
    cursor = connection.cursor()
    cursor.execute("""UPDATE produtos SET id = (?), 
                   nome = (?), 
                   categoria = (?), 
                   marca = (?), 
                   quantidade = (?), 
                   preco = (?) 
                   WHERE id = (?)""", 
                   (mod1, mod2, mod3, mod4, mod5, mod6, id))
    connection.commit()
    connection.close()

# Exclui uma entrada da tabela de acordo com o ID
def delete_one(id):
    connection = sqlite3.connect("loja.db")
    cursor = connection.cursor()
    result = cursor.execute("DELETE FROM produtos WHERE id = (?)", (id,))
    a = result.rowcount
    connection.commit()
    connection.close()
    return a
