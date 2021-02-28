from tabulate import tabulate


class Carrito:
    """Esta clase permite manejar los productos que se van a comprar"""
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
        return total