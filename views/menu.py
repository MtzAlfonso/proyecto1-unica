from functions.operations import register, login
from functions.auxiliar import clear

def start():
    op = 0
    while(op != 3):
        print("\n** Menú Principal **")
        print("\nSeleccione una opción:")
        print(" 1: Registrar")
        print(" 2: Ingresar")
        print(" 3: Salir")
        try:
            op = int(input("\n> "))
            if op == 1:
                clear()
                register()
            elif op == 2:
                clear()
                login()
            elif op == 3:
                print("\nHasta luego, esperamos que vuelva pronto.")
            else:
                print("\nOpción inválida")
        except:
            print("\nOpción inválida")
