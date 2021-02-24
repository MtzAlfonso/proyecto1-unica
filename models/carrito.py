from tabulate import tabulate


class Carrito:
    productos = []

    def mostrarCarrito(self):
        print()
        print(tabulate(self.productos, headers=['id', 'Código', 'Nombre', 'Talla', 'Color', 'Precio', 'Piezas en Stock'], tablefmt='fancy_grid'))

    def vaciarCarrito(self):
        self.productos.clear()

    def total(self):
        total = 0
        for producto in self.productos:
            total += producto[5]
        print("Total: ${:.2f}".format(total))