import sqlite3

# função SQL Select * from
def show_all_produtos():
    connection = sqlite3.connect("loja.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM produtos")
    items = cursor.fetchall()

    connection.commit()
    connection.close()
    return items


# Adiciona uma nova entrada na tabela
def add_one(id, nome, categoria, marca, quantidade, preco):
    connection = sqlite3.connect("loja.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO produtos VALUES (?,?,?,?,?,?)", (id, nome, categoria, marca, quantidade, preco))
    connection.commit()
    connection.close()


def modify(coluna, mod, id):
    connection = sqlite3.connect("loja,db")
    cursor = connection.cursor()
    cursor.execute("UPDATE produtos SET (?) = (?) WHERE id = (?)", (coluna, mod, id))
    connection.commit()
    connection.close()


def delete_one(id):
    connection = sqlite3.connect("loja.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM produtos WHERE id = (?)", id)
    connection.commit()
    connection.close()


def custom_sql(code):
    connection = sqlite3.connect("loja.db")
    cursor = connection.cursor()
    cursor.execute(code)
    items = cursor.fetchall()
    for item in items:
        print(item[0] + "\t\t" + item[1] + "\t\t" + item[2] + "\t\t" + item[3] + "\t\t" + item[4] + "\t\t" + item[5])
    connection.commit()
    connection.close()