from database.dbFunctions import sql_select_products
from tabulate import tabulate
from functions.auxiliar import clear
import functions.operations as fo

#Función que muestra la tabla con los artículos disponibles en la BD
def show(msg, user):
    opc = 0
    while(opc != 2):
        # clear()
        print(msg + "\n")
        print(tabulate(sql_select_products(), headers=['id', 'Código', 'Nombre', 'Talla', 'Color', 'Precio', 'Piezas en Stock']))
        print("\n1: Realizar una compra")
        print("2: Cerrar sesión")

        try:
            opc = int(input(" > "))
            if opc == 1:
                fo.comprar(user)
            elif opc == 2:
                clear()
                break
            else:
                print("\nOpción inválida")
        except:
            print("\nOpción inválida")
