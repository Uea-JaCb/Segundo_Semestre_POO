# Programa que modela una biblioteca con clases Libro y Biblioteca.
# Los libros tienen atributos como título, autor, ISBN y estado (disponible o no).
# La biblioteca gestiona una lista de libros y permite agregar libros, prestarlos, devolverlos y mostrar su información.

class Libro:
    # Constructor que inicializa los atributos del libro
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo  # Atributo: título del libro
        self.autor = autor    # Atributo: autor del libro
        self.isbn = isbn      # Atributo: ISBN del libro
        self.disponible = True  # Atributo: estado del libro (disponible o no)

    # Metodo para prestar el libro
    def prestar(self):
        if self.disponible:
            self.disponible = False
            return f"El libro '{self.titulo}' ha sido prestado."
        else:
            return f"El libro '{self.titulo}' no está disponible."

    # Metodo para devolver el libro
    def devolver(self):
        if not self.disponible:
            self.disponible = True
            return f"El libro '{self.titulo}' ha sido devuelto."
        else:
            return f"El libro '{self.titulo}' ya está disponible."

    # Metodo para mostrar información del libro
    def mostrar_info(self):
        estado = "Disponible" if self.disponible else "No disponible"
        return f"Título: {self.titulo}, Autor: {self.autor}, ISBN: {self.isbn}, Estado: {estado}"

class Biblioteca:
    # Constructor que inicializa la lista de libros
    def __init__(self):
        self.libros = []  # Atributo: lista de libros en la biblioteca

    # Metodo para agregar un libro a la biblioteca
    def agregar_libro(self, libro):
        self.libros.append(libro)
        return f"Libro '{libro.titulo}' agregado a la biblioteca."

    # Metodo para mostrar todos los libros
    def mostrar_libros(self):
        if not self.libros:
            return "La biblioteca está vacía."
        return "\n".join([libro.mostrar_info() for libro in self.libros])

# Ejemplo de uso
if __name__ == "__main__":
    # Crear una biblioteca
    biblioteca = Biblioteca()

    # Crear algunos libros
    libro1 = Libro("El Principito", "Antoine de Saint-Exupéry", "978-3-16-148410-0")
    libro2 = Libro("Cien Años de Soledad", "Gabriel García Márquez", "978-0-14-243719-3")

    # Agregar libros a la biblioteca
    print(biblioteca.agregar_libro(libro1))
    print(biblioteca.agregar_libro(libro2))

    # Mostrar todos los libros
    print("\nLibros en la biblioteca:")
    print(biblioteca.mostrar_libros())

    # Prestar un libro
    print("\n" + libro1.prestar())

    # Mostrar estado actualizado
    print("\nLibros en la biblioteca después de prestar:")
    print(biblioteca.mostrar_libros())

    # Devolver un libro
    print("\n" + libro1.devolver())

    # Mostrar estado final
    print("\nLibros en la biblioteca después de devolver:")
    print(biblioteca.mostrar_libros())
