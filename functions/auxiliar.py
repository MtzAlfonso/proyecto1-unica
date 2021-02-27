# Definimos la función estableciendo el nombre que queramos
import os

#Función que limpia pantalla
def clear():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")

#Función que genera el archivo .txt al momento de registarse el usuario en el sistema 
def archivoDatos(nombre, apellido):
    file = open("datos.txt", "w")
    file.write("Bienvenido \t")
    file.write(str(nombre)+" "+str(apellido))
    file.close()

#Función que genera el ticket o recibo al concluir la compra (genera un archivo .txt)
def archivoRecibo(user, carrito):
    file = open("recibo.txt", "w")
    file.write("*** ¡Gracias por tu compra! ***\n")
    file.write("\n----"+str(user[3]))
    file.write(" ")
    file.write(str(user[4])+"----")
    file.write("\n")
    file.write("\n*** Artículo(s) comprado(s) ***\n")
    for producto in carrito.productos:
        file.write("\nArtículo: \t")
        file.write(str(producto[2]))
        file.write("\nTalla: \t\t")
        file.write(str(producto[3]))
        file.write("\nColor: \t\t")
        file.write(str(producto[4]))
        file.write("\nPrecio: \t\t")
        file.write(str(producto[5]))
        file.write("\n-------------")
    file.write(
        "\nTOTAL: ${:.2f}\n".format(carrito.total()))
    file.close()
