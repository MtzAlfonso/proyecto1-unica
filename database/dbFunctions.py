# Módulo para conectar con el motor de SQLite
import sqlite3

from sqlite3 import Error


def sql_connection():
    # Funcion que establece la conexión con la base de datos.
    # NOTA: si no existe, la crea
    try:
        con = sqlite3.connect('database/tienda_ropa.db')
        return con
    except Error:
        print(Error)

def sql_validateInsert(query):
    # Se guarda la conexion en una variable
    con = sql_connection()
    # Es necesario instanciar un objeto cursor para poder ejecutar instrucciones SQL
    cursorObj = con.cursor()
    # Esta query aalida que el usuario ingresado no exista en la base de datos y asi evitar inconsistencias.
    cursorObj.execute(
        "SELECT * FROM users WHERE nickname = ?", (query, ))
    rows = cursorObj.fetchall()
    return len(rows)


def sql_insert(entities):
    #
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
