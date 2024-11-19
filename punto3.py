from datetime import datetime
#sistema de vehiculos
class Vehiculo:
    def __init__(self,marca,modelo,fecha,kilometraje):
        self.marca = marca
        self.modelo = modelo
        self.fecha = fecha
        self.kilometraje = kilometraje

    def conducir(self, nueva_distancia):
        self.kilometraje += nueva_distancia
        return f"--kilometraje total: {self.kilometraje}"

    def mostrar_vehiculo(self):
        return f"--marca:{self.marca}, modelo:{self.modelo}, año:{self.fecha}, kilometraje:{self.kilometraje}"

    def antiguo(self,):
        fecha_actual = datetime.now().year  # Obtener el año actual
        if fecha_actual - self.fecha > 20:
            return f"--antiguo:{True}"
        else:
            return f"--antiguo:{False}"

vehiculo1 = Vehiculo("mercedenz","ju23",1999,3000)
print(vehiculo1.conducir(400))
print(vehiculo1.mostrar_vehiculo())
print(vehiculo1.antiguo())