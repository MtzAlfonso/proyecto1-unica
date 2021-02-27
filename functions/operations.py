import functions.validator as val
from database.dbFunctions import sql_insert, sql_login, sql_select_product
from getpass import getpass
from models.carrito import Carrito
from terminal_text_color import TextColor

tc = TextColor()


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
        archi1 = open("datos.txt", "w")
        archi1=open("datos.txt","w") 
        archi1.write("Bienvenido \t")
        archi1.write(str(nombre))
        print("__")
        archi1.write(str(apellido)) 
        archi1.close()
    except:
        print("Error al guardar los datos")


def login():
    print("\nLogin\n")
    nickname = input("Nickname: ")
    password = getpass("Password: ")
    auth, user = sql_login(nickname, password)
    val.validaLogin(auth, user)


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
                    carrito.total()
            elif opc == 3:
                if len(carrito.productos) == 0:
                    print(tc.italic_yellow("\nEl carrito está vacío"))
                else:
                    if user[8] == input("\nCorreo de PayPal: "):
                        print(tc.italic_green("\nGracias por tu compra"))
                        archi2 = open("compra.txt", "w")
                        archi2=open("compra.txt","w") 
                        archi2.write("***** ¡Gracias por tu compra! ***** \n")
                        archi2.write(str(user[3]))
                        archi2.write("\t")
                        archi2.write(str(user[4]))
                        archi2.write("\n")
                        archi2.write("***** Artículo comprado: \n")
                        archi2.write("Artículo: \t")
                        archi2.write(str(prod[2]))
                        archi2.write("\nTalla: \t")
                        archi2.write(str(prod[3]))
                        archi2.write("\nColor: \t")
                        archi2.write(str(prod[4]))
                        archi2.write("\nPrecio: \t")
                        archi2.write(str(prod[5]))
                        
                        archi2.close()
                        carrito.vaciarCarrito()
                        break
                    else:
                        print(tc.italic_yellow(
                            "\n¡Lamentamos oír eso! Vuelva pronto..."))
            elif opc == 4:
                carrito.vaciarCarrito()
                clear()
                break
            else:
                print("\nOpción inválida")
        except:
            print("\nOpción inválida")
