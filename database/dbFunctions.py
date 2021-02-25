# Módulo para conectar con el motor de SQLite
import sqlite3
from sqlite3 import Error


def sql_connection():
    """
    Funcion que establece la conexión con la base de datos.
    NOTA: si no existe, la crea
    """
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
    # Esta query trae los nombres de usuario para verificar no exista en la base de datos y asi evitar inconsistencias.
    cursorObj.execute(
        "SELECT * FROM users WHERE nickname = ?", (query, ))
    # Guarda los resultados en la variable rows
    rows = cursorObj.fetchall()
    # Retorna la cantidad de usuarios con ese nombre
    return len(rows)


def sql_insert(entities):
    # Se guarda la conexion en una variable
    con = sql_connection()
    # Es necesario instanciar un objeto cursor para poder ejecutar instrucciones SQL
    cursorObj = con.cursor()
    cursorObj.execute(
        "INSERT INTO users (nickname, password, nombre, apellido, edad, correo, numTarjeta, correoPaypal, passPaypal) VALUES (?,?,?,?,?,?,?,?,?)", entities)
    con.commit()


def sql_login(nickname, password):
    # Se guarda la conexion en una variable
    con = sql_connection()
    # Es necesario instanciar un objeto cursor para poder ejecutar instrucciones SQL
    cursorObj = con.cursor()
    # Esta query busca el usuario con el nickname y password que recibe como paramatros
    cursorObj.execute(
        "SELECT * FROM users WHERE nickname = ? AND password = ?", (
            nickname, password, )
    )
    # Guardamos el usuario en una variable
    user = cursorObj.fetchone()
    # Comprobamos que el usuario exista, si es asi, se retorna el valor True asi como dicho usuario, de lo contrario retornamos False
    if user:
        return True, user
    else:
        return False, None


def sql_select_products():
    # Se guarda la conexion en una variable
    con = sql_connection()
    # Es necesario instanciar un objeto cursor para poder ejecutar instrucciones SQL
    cursorObj = con.cursor()
    # Con esta query traemos todos los productos de la base de datos
    cursorObj.execute(
        "SELECT * FROM products"
    )
    # Los guardamos en una variable y posteriormente los retornamos
    products = cursorObj.fetchall()
    return products


def sql_select_product(name):
    # Se guarda la conexion en una variable
    con = sql_connection()
    # Es necesario instanciar un objeto cursor para poder ejecutar instrucciones SQL
    cursorObj = con.cursor()
    cursorObj.execute(
        "SELECT * FROM products WHERE nombre = ?", (name, )
    )
    product = cursorObj.fetchone()
    return product
