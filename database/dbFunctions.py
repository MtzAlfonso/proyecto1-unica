import sqlite3

from sqlite3 import Error


def sql_connection():
    try:
        con = sqlite3.connect('database/tienda_ropa.db')
        return con
    except Error:
        print(Error)


def sql_validateInsert(query):
    con = sql_connection()
    cursorObj = con.cursor()
    cursorObj.execute(
        "SELECT * FROM users WHERE nickname = ?", (query, ))
    rows = cursorObj.fetchall()
    return len(rows)


def sql_insert(entities):
    con = sql_connection()
    cursorObj = con.cursor()
    cursorObj.execute(
        "INSERT INTO users (nickname, password, nombre, apellido, edad, correo, numTarjeta, correoPaypal, passPaypal) VALUES (?,?,?,?,?,?,?,?,?)", entities)
    con.commit()


def sql_login(nickname, password):
    con = sql_connection()
    cursorObj = con.cursor()
    cursorObj.execute(
        "SELECT * FROM users WHERE nickname = ? AND password = ?", (
            nickname, password, )
    )
    user = cursorObj.fetchone()
    if user:
        return True, user
    else:
        return False, None


def sql_select_products():
    con = sql_connection()
    cursorObj = con.cursor()
    cursorObj.execute(
        "SELECT * FROM products"
    )
    products = cursorObj.fetchall()
    return products


def sql_select_product(name):
    con = sql_connection()
    cursorObj = con.cursor()
    cursorObj.execute(
        "SELECT * FROM products WHERE nombre = ?", (name, )
    )
    product = cursorObj.fetchone()
    return product
