#sistema de animales
class Animal:
    def __init__(self,nombre, especie,edad, habitat):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.habitat = habitat

    def cumplir(self):
        self.edad += 1
        return f"--la edad de {self.nombre} es {self.edad}"

    def  cambiar_habitat(self,nuevo_habitat):
        self.habitat = nuevo_habitat
        return (f"--el nuevo habitat de {self.nombre} es: {self.habitat}")

    def mostrar(self):
        return f"--nombre:{self.nombre}, especie:{self.especie}, edad:{self.edad}, habitat:{self.habitat}"

animal1 = Animal("coco", "gorila", 12, "bosque")
print(animal1.mostrar())
print(animal1.cambiar_habitat("selva"))
print(animal1.cumplir())