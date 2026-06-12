class Producto:
    """Representa un producto con nombre, precio y cantidad."""

    def __init__(self, nombre, precio=0.0, cantidad=0):
        if not isinstance(nombre, str):
            raise TypeError("El nombre debe ser una cadena de texto")

        if not isinstance(precio, (int, float)):
            raise TypeError("El precio debe ser un número")
        if precio < 0:
            raise ValueError("El precio no puede ser negativo")

        if not isinstance(cantidad, int):
            raise TypeError("La cantidad debe ser un entero")
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa")

        self.nombre = nombre
        self.precio = float(precio)
        self.cantidad = cantidad

    def __str__(self):
        return f"Producto: {self.nombre} | Precio: ${self.precio:.2f} | Cantidad: {self.cantidad}"

    def __add__(self, otro):
        if not isinstance(otro, Producto):
            raise TypeError("Solo se puede sumar con otro Producto")
        if self.nombre != otro.nombre:
            raise ValueError("Los productos deben tener el mismo nombre para sumarse")
        return Producto(self.nombre, self.precio, self.cantidad + otro.cantidad)

    def __mul__(self, factor):
        if not isinstance(factor, int):
            raise TypeError("El factor debe ser un entero")
        return self.precio * factor

    def __eq__(self, otro):
        if not isinstance(otro, Producto):
            return False
        return self.nombre == otro.nombre and self.precio == otro.precio

    def __del__(self):
        print(f"Eliminando producto: {self.nombre}")