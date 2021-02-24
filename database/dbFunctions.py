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
