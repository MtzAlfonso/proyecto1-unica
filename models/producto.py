class Producto:
    def __init__(self, atributos):
        self.id = atributos[0]
        self.clave = atributos[1]
        self.nombre = atributos[2]
        self.talla = atributos[3]
        self.color = atributos[4]
        self.precio = atributos[5]
        self.stock = atributos[6]
