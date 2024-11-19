#sistema de reservas en un hotel
class Habitacion:
    def __init__(self,numero,tipo,precio,disponible):
        self.numero = numero
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.disponible = disponible

    def reservar(self):
        disponible = False
        return f"--habitacion numero {self.numero}. disponible:{disponible}"

    def liberar(self):
        disponible = True
        return f"--habitacio numero:{self.numero}. disponible:{disponible}"

    def mostrar(self):
        return f"--habitacion:{self.numero}, tipo:{self.tipo}, precio:{self.precio}, disponible:{self.disponible}"

habitacion1 = Habitacion("001","economica", 3000, "True")
print(habitacion1.reservar())
print(habitacion1.liberar())
print(habitacion1.mostrar())
