from database.dbFunctions import sql_validateInsert
from terminal_text_color import TextColor
from getpass import getpass
import re

tc = TextColor()

def validaNickname():
    while(True):
        nickname = input("Nickname: ")
        if len(nickname) < 6:
            print(tc.italic_red(" ✖ El nombre usuario debe contener al menos 6 caracteres"))
        elif len(nickname) > 12:
            print(tc.italic_red(" ✖ El nombre de usuario no puede contener más de 12 caracteres"))
        elif not nickname.isalnum():
            print(tc.italic_red(" ✖ El nombre de usuario sólo puede contener letras y números"))
        elif sql_validateInsert(nickname) != 0:
            print(tc.italic_red(" ✖ El nombre de usuario ya existe"))
        else:
            break
    return nickname

def validaPassword(msg):
    reg = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*(_|[^\w])).\S+$')
    while(True):
        password = getpass(msg)
        if len(password) < 10 or not reg.search(password):
            print(tc.italic_red(" ✖ Contraseña inválida"))
        else:
            print(tc.italic_green(" ✔ Contraseña válida"))
            break
    return password