from database.dbFunctions import sql_insert
from getpass import getpass
import lib.validator as val


def register():
    print("\nRegistro de usuarios")
    nickname = val.validaNickname()
    password = val.validaPassword("Password: ")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    edad = int(input("Edad: "))
    correo = input("Correo Personal: ")
    numTarjeta = input("Num. Tarjeta: ")
    correoPaypal = input("Correo Paypal: ")
    passPaypal = val.validaPassword("Password Paypal: ")

    entities = (nickname, password, nombre, apellido, edad,
                correo, numTarjeta, correoPaypal, passPaypal)
    try:
        sql_insert(entities)
    except:
        print("Error al guardar los datos")
