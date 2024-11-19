#regitro producto
class Producto:
    def __init__(self,nombre,precio,cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def actualizar_precio(self,nuevo_precio):
        self.precio = nuevo_precio
        return f"--el precio del producto {self.nombre} se modifico a {nuevo_precio}"

    def ajustar_inventario(self,nueva_cantidad):
        self.cantidad = nueva_cantidad
        return (f"--la cantidad del producto {self.nombre} se modifico a {nueva_cantidad}")

    def mostrar_informacion(self):
        return f"--producto:{self.nombre}, precio:{self.precio}, cantidad:{self.cantidad}"

producto1 = Producto("pera", 10, 21)
print(producto1.actualizar_precio(90))
print(producto1.ajustar_inventario(40))
print(producto1.mostrar_informacion())

producto2 = Producto("fresa", 45, 78)
print(producto2.actualizar_precio(90))
print(producto2.ajustar_inventario(40))
print(producto2.mostrar_informacion())
