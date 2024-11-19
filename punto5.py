#gestion de libros
class Libro:
    def __init__(self,titulo,autor,genero,precio):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.precio = precio

    def descuento(self,descuento):
        self.precio = self.precio - (self.precio*(descuento/100))
        return f"--el precio con descuento del libro {self.titulo} es {self.precio}"

    def mostrar(self):
        return f"--libro: {self.titulo}, autor:{self.autor}, genero:{self.genero}, precio:{self.precio}"

    def mas_caro(self,otro_libro):
        if self.precio > otro_libro.precio:
            return f"--el libro '{self.titulo}' es mas caro que el libro '{otro_libro.titulo}'"
        elif self.precio < otro_libro.precio:
            return f"--el libro '{otro_libro.titulo}' es mas caro que el libro '{self.titulo}'"
        else:
            return "--los dos libros cuestan los mismo"

libro1 = Libro("cien años de soledad", "gabrile garcia marquez","raalismo",50000)
libro2 = Libro("el principito", "juan lopez", "fantasia y aventura", 35000)
print(libro2.descuento(20))
print(libro1.mostrar())
print(libro2.mas_caro(libro1))

