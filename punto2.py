#registro estudiantes
class Estudiante:
    def __init__(self,nombre,edad,grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        self.materias = []

    def inscribir_materias(self,nueva_materia):
        self.materias.append(nueva_materia)
        return f"--se agrego la nueva materia {nueva_materia}"

    def mostrar_materias(self):
        for i in self.materias:
            return f"--las materias del estudiante {self.nombre} son {i}"

    def actualizar_grado(self,nuevo_grado):
        self.grado = nuevo_grado
        return f"--se cambio el grado del estudiate {self.nombre} a {nuevo_grado}"

estudiante1 = Estudiante("julian","19","11")
print(estudiante1.inscribir_materias("matematicas"))
print(estudiante1.mostrar_materias())
print(estudiante1.actualizar_grado(8))