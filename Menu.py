
def menu():
    print("*********** Bienvenido **********")
    print("Regístrese ")
    usuario()

def usuario():
    nickname=input("Ingrese un nickname: ")
    if len(nickname)<6:
        print("El nombre de usuario debe contener al menos 6 caracteres")
    elif len(nickname)> 12:
        print("El nombre de usuario no puede contener más de 12 caracteres")
    elif nickname.isalnum()==True:
        return (contraseña(nickname))
    else: 
        print("El nombre de usuario solo puede contener letras y números")
        
def contraseña(nick):
    validar=False #que se vayan cumpliendo los requisitos uno a uno.
    contra=input("Ingrese su contraseña: ")
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
        print("La contraseña no puede contener espacios")
    else:
        validar=True #se cumple el primer requisito que no hayan espacios
    if long <10 and validar==True:
        print("Mínimo 10 caracteres")
        validar=False #cambia a False si no se cumple el requisito míinimo de caracteres

    if mayuscula == True and minuscula ==True and numeros == True and y== False and validar ==True:
        validar = True #Cumple el requisito de tener mayuscula, minuscula, numeros y no alfanuméricos
    else:
        correcto=False #uno o mas requisitos de mayuscula, minuscula, numeros y no alfanuméricos no se cumple

    if validar == True and correcto==False:
        print("La contraseña elegida no es segura: debe contener letras minúsculas, mayúsculas, números y al menos 1 carácter no alfanumérico")

    if validar == True and correcto ==True:
        return ingreso(nick,contra)


def ingreso(nickname,contra):
    print(nickname,contra)
    id=input("Ingrese su nickname: ")
    password=input("Ingrese su contraseña: ")
    if (id==nickname and password==contra):
        print("Ok")
    elif (id != nickname):
        print("No")
    else:
        print("Contraseña invalida")

def inventario(contra, nickname):
    print("Tu nombre y contraseña son: ",nickname,contra)


menu()

