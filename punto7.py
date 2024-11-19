#sistema de facturacion
class Factura:
    def __init__(self,numero,cliente,fecha,monto):
        self.numero = numero
        self.cliente = cliente
        self.fecha = fecha
        self.monto = monto

    def agregar(self,descripcion,cantidad, precio_unitario):

