# Definimos la función estableciendo el nombre que queramos
import os


def clear():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")


def archivoDatos(nombre, apellido):
    file = open("datos.txt", "w")
    file.write("Bienvenido \t")
    file.write(str(nombre)+" "+str(apellido))
    file.close()


def archivoRecibo(user, carrito):
    file = open("recibo.txt", "w")
    file.write("*** ¡Gracias por tu compra! ***n")
    file.write(str(user[3]))
    file.write("\t")
    file.write(str(user[4]))
    file.write("\n")
    file.write("\n*** Artículos comprado ***\n")
    for producto in carrito.productos:
        file.write("\nArtículo: \t")
        file.write(str(producto[2]))
        file.write("\nTalla: \t")
        file.write(str(producto[3]))
        file.write("\nColor: \t")
        file.write(str(producto[4]))
        file.write("\nPrecio: \t")
        file.write(str(producto[5]))
        file.write("\n-------------")
    file.write(
        "\nTOTAL: ${:.2f}\n".format(carrito.total()))
    file.close()
