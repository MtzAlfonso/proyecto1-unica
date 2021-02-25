


def registro():
    nickname=input("Ingrese un nickname para registrarte: ")
    if len(nickname)<6:
        print("El nombre de usuario debe contener al menos 6 caracteres...")
        return registro()
    elif len(nickname)> 12:
        print("El nombre de usuario no puede contener más de 12 caracteres...")
        return registro()
    elif nickname.isalnum()==True:
        
        validar=False #que se vayan cumpliendo los requisitos uno a uno.
        contra=input("Ingrese una contraseña válida: ")
        long=len(contra) #Calcula la longitud de la contraseña
        espacio=False  #variable para identificar espacios
        mayuscula=False #variable para identificar letras mayúsculas
        minuscula=False #variable para contar identificar letras minúsculas
        numeros=False #variable para identificar números
        y=contra.isalnum()#si es alfanumérica retorna True
        correcto=True #verifica que hayan mayuscula, minuscula, numeros y no alfanuméricos
            
        for carac in contra: #ciclo for que recorre caracter por caracter en la contraseña

            if carac.isspace()==True: #Saber si el caracter es un espacio
                espacio=True #si encuentra un espacio se cambia el valor user

            if carac.isupper()== True: #saber si hay mayuscula
                mayuscula=True #acumulador o contador de mayusculas
                    
            if carac.islower()== True: #saber si hay minúsculas
                minuscula=True #acumulador o contador de minúsculas
                    
            if carac.isdigit()== True: #saber si hay números
                numeros=True #acumulador o contador de numeros
                            
        if espacio==True: #hay espacios en blanco
            print("La contraseña no puede contener espacios...")
        else:
            validar=True #se cumple el primer requisito que no hayan espacios
        if long <10 and validar==True:
            print("La contraseña debe tener mínimo 10 caracteres")
            validar=False #cambia a False si no se cumple el requisito míinimo de caracteres

        if mayuscula == True and minuscula ==True and numeros == True and y== False and validar ==True:
            validar = True #Cumple el requisito de tener mayuscula, minuscula, numeros y no alfanuméricos
        else:
            correcto=False #uno o mas requisitos de mayuscula, minuscula, numeros y no alfanuméricos no se cumple

        if validar == True and correcto==False:
            print("La contraseña elegida no es segura: debe contener letras minúsculas, mayúsculas, números y al menos 1 carácter no alfanumérico...")

        if validar == True and correcto ==True:
            print("Contraseña válida :)")
            return datos_personales(nickname,contra)
    else: 
        print("El nombre de usuario solo puede contener letras y números...")
        return registro()
        

def datos_personales(nick,contra):
    nombre=input("Ingresa tu nombre de pila: ")
    apellido=input("Ingresa tu apellido: ")
    edad=input("Ingresa tu edad: ")
    correo=input("Ingresa tu correo electrónico: ")
    tarjeta=input("Ingresa tu tarjeta de crédito: ")
    paypal=input("Ingresa tu cuenta de PayPal: ")
    contra_paypal=input("Ingresa tu contraseña de PayPal: ")
    usuario={

    }
    usuario["Nombre"]=nombre
    usuario["Apellido"]=apellido
    usuario["Edad"]=edad
    usuario["Correo"]=correo
    usuario["Tarjeta"]=tarjeta
    usuario["PayPal"]=paypal
    usuario["PayPal_Contra"]=contra_paypal
    usuario["ID"]=nick
    usuario["Contraseña"]=contra
    print("Tus datos son:",usuario)

    archi1 = open("C:/Users/johnc/OneDrive - UNIVERSIDAD NACIONAL AUTÓNOMA DE MÉXICO/INGENIERIA EN COMPUTACIÓN/BECARIO/PROYECTO/archivo.txt", "w")
    archi1=open("datos.txt","w") 
    archi1.write("Bienvenido \t")
    archi1.write(str(nombre))
    archi1.write(str(apellido)) 
    archi1.close()
    return menu(usuario)


def ingreso(usuario):
    id=input("Ingrese su nickname que registró anteriormente: ")
    if (id!=usuario["ID"]):
        print("Usuario no registrado, registrese por favor")
        return registro()
    password=input("Ingrese su contraseña que registró anteriormente: ")
    if(password != usuario["Contraseña"]):
        print("Contraseña inválida")
        return ingreso(usuario)
    if(id==usuario["ID"] and password==usuario["Contraseña"]):
        print("Ok, bienvenido... :)")
        return inventario(usuario)

def inventario(usuario):
    print("Tus datos son: ",usuario)

def menu(usuario):
    print("*********** Bienvenido **********")
    print("Opción 1: Registrarse")
    print("Opción 2: Ingresar")
    print("Opción 3: Salir")
    opcion=input("...")
    print(usuario)
    print(opcion)
    while opcion !="3":
        if opcion=="1":
            registro()
        elif opcion=="2":
            if(len(usuario)==0):
                print("Registrese primero")
                registro()
            else:
                ingreso(usuario)
        elif opcion=="3":
            print("Hasta luego")
        else:
            print("Opción invalida")


user={

}
menu(user)