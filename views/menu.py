from lib.operations import register

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
                register()
            elif op == 2:
                print("Login")
            elif op == 3:
                print("Hasta luego, esperamos que vuelva pronto.")
            else:
                print("Opción inválida")
        except:
            print("No ingresaste ninguna opción")
