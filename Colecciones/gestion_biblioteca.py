# Sistema de Gestión de Biblioteca Digital

# Clase Libro
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # Usamos tupla para título y autor (inmutables)
        self.info = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.info[0]} por {self.info[1]} | Categoría: {self.categoria} | ISBN: {self.isbn}"

# Clase Usuario
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista para libros prestados

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.id_usuario})"

# Clase Biblioteca
class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario ISBN: Libro
        self.usuarios = {}  # Diccionario ID: Usuario
        self.ids_usuarios = set()  # Conjunto de IDs únicos

    # Métodos para libros
    def agregar_libro(self, libro):
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            print("Libro añadido exitosamente.")
        else:
            print("El libro ya esta registrado.")

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print("Libro eliminado exitosamente.")
        else:
            print("No se ha encontró el libro.")

    # Métodos para usuarios
    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.ids_usuarios:
            self.usuarios[usuario.id_usuario] = usuario
            self.ids_usuarios.add(usuario.id_usuario)
            print("Usuario registrado exitosamente.")
        else:
            print("El ID ya se encuentra registrado.")

    def dar_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]
            self.ids_usuarios.remove(id_usuario)
            print("Usuario dado de baja del sistema.")
        else:
            print("Usuario no encontrado.")

    # Métodos de préstamos
    def prestar_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios and isbn in self.libros:
            usuario = self.usuarios[id_usuario]
            libro = self.libros.pop(isbn)
            usuario.libros_prestados.append(libro)
            print(f"Libro '{libro.info[0]}' prestado a {usuario.nombre}.")
        else:
            print("Usuario o libro no encontrado.")

    def devolver_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    usuario.libros_prestados.remove(libro)
                    self.libros[isbn] = libro
                    print("Libro devuelto exitosamente.")
                    return
        print("No se pudo devolver el libro.")

    # Métodos de búsqueda
    def buscar_libro(self, criterio, valor):
        resultados = []
        for libro in self.libros.values():
            if criterio == 'titulo' and valor.lower() in libro.info[0].lower():
                resultados.append(libro)
            elif criterio == 'autor' and valor.lower() in libro.info[1].lower():
                resultados.append(libro)
            elif criterio == 'categoria' and valor.lower() in libro.categoria.lower():
                resultados.append(libro)
        return resultados

    def listar_prestados(self, id_usuario):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            if usuario.libros_prestados:
                for libro in usuario.libros_prestados:
                    print(libro)
            else:
                print("No tiene libros prestados.")
        else:
            print("Usuario no encontrado en el sistema.")

# Menú interactivo con tabla

def mostrar_menu():
    print("\n+---------------------------------+")
    print("|        SISTEMA BIBLIOTECA       |")
    print("+-----+---------------------------+")
    print("|  1  | Agregar libro al sistema  |")
    print("|  2  | Quitar libro del sistema  |")
    print("|  3  | Registrar nuevo usuario   |")
    print("|  4  | Dar de baja un usuario    |")
    print("|  5  | Prestar un libro          |")
    print("|  6  | Devolver un libro         |")
    print("|  7  | Buscar un libro           |")
    print("|  8  | Listar libros prestados   |")
    print("|  9  | Salir                     |")
    print("+----+----------------------------+")

# Programa principal
if __name__ == "__main__":
    biblioteca = Biblioteca()
    while True:
        mostrar_menu()
        opcion = input("Digite una opción: ")

        if opcion == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            categoria = input("Categoría: ")
            isbn = input("ISBN: ")
            libro = Libro(titulo, autor, categoria, isbn)
            biblioteca.agregar_libro(libro)

        elif opcion == "2":
            isbn = input("ISBN del libro a quitar: ")
            biblioteca.quitar_libro(isbn)

        elif opcion == "3":
            nombre = input("Nombre del usuario: ")
            id_usuario = input("ID único: ")
            usuario = Usuario(nombre, id_usuario)
            biblioteca.registrar_usuario(usuario)

        elif opcion == "4":
            id_usuario = input("ID del usuario: ")
            biblioteca.dar_baja_usuario(id_usuario)

        elif opcion == "5":
            id_usuario = input("ID del usuario: ")
            isbn = input("ISBN del libro: ")
            biblioteca.prestar_libro(id_usuario, isbn)

        elif opcion == "6":
            id_usuario = input("ID del usuario: ")
            isbn = input("ISBN del libro: ")
            biblioteca.devolver_libro(id_usuario, isbn)

        elif opcion == "7":
            criterio = input("Buscar por (titulo/autor/categoria): ")
            valor = input("Valor a buscar: ")
            resultados = biblioteca.buscar_libro(criterio, valor)
            if resultados:
                for libro in resultados:
                    print(libro)
            else:
                print("No se encontraron libros.")

        elif opcion == "8":
            id_usuario = input("ID del usuario: ")
            biblioteca.listar_prestados(id_usuario)

        elif opcion == "9":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")
