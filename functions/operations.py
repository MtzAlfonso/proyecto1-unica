import functions.validator as val
from functions.auxiliar import archivoDatos, archivoRecibo, clear
from database.dbFunctions import sql_insert, sql_login, sql_select_product
from getpass import getpass
from models.carrito import Carrito
from terminal_text_color import TextColor

tc = TextColor()

#Función que registra los datos ingresados por los usuarios y los almacena en la BD
def register():
    print("\nRegistro de usuarios\n")
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
        archivoDatos(entities[2], entities[3])
    except:
        print("Error al guardar los datos")

#Función que para el login, (verifica en la BD)
def login():
    print("\nLogin\n")
    nickname = input("Nickname: ")
    password = getpass("Password: ")
    auth, user = sql_login(nickname, password)
    val.validaLogin(auth, user)

#Función para hacer las operaciones de compras
def comprar(user):
    opc = 0
    carrito = Carrito()
    while(opc != 4):
        # clear()
        print("\n1: Añadir producto")
        print("2: Ver carrito")
        print("3: Comprar")
        print("4: Cancelar compra")

        try:
            opc = int(input(" > "))
            if opc == 1:
                name = input("\nNombre del producto: ")
                prod = sql_select_product(name)
                if prod and prod[6] > 0:
                    carrito.productos.append(prod)
                    print(tc.italic_green("Producto agregado al carrito"))
                elif prod[6] == 0:
                    print(tc.italic_red("No hay productos en stock"))
            elif opc == 2:
                if len(carrito.productos) == 0:
                    print(tc.italic_yellow("\nEl carrito está vacío"))
                else:
                    carrito.mostrarCarrito()
                    print("Total: ${:.2f}".format(carrito.total()))
            elif opc == 3:
                if len(carrito.productos) == 0:
                    print(tc.italic_yellow("\nEl carrito está vacío"))
                else:
                    if user[8] == input("\nCorreo de PayPal: "):
                        print(tc.italic_green("\nGracias por tu compra"))
                        archivoRecibo(user, carrito)
                        carrito.vaciarCarrito()
                        break
                    else:
                        print(tc.italic_yellow(
                            "\n¡Lamentamos oír eso! Vuelva pronto..."))
            elif opc == 4:
                carrito.vaciarCarrito()
                clear()
            else:
                print("\nOpción inválida")
        except:
            print("\nOpción inválida")
