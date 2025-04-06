class Producto:
    def __init__(self, id_producto, nombre, precio, cantidad):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Precio: {self.precio}, Cantidad: {self.cantidad}"
