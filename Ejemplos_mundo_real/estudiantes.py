# Programa que Modela un sistema de gestión de estudiantes con clases Estudiante y Curso.
# Los estudiantes pueden inscribirse en cursos, y los cursos mantienen una lista de estudiantes inscritos.
# Cada clase tiene métodos para mostrar información.

class Estudiante:
    # Constructor que inicializa los atributos del estudiante
    def __init__(self, nombre, id_estudiante):
        self.nombre = nombre  # Atributo: nombre del estudiante
        self.id_estudiante = id_estudiante  # Atributo: ID del estudiante
        self.cursos = []  # Atributo: lista de cursos inscritos

    # Metodo para inscribir al estudiante en un curso
    def inscribir_curso(self, curso):
        self.cursos.append(curso)
        return f"{self.nombre} se ha inscrito en {curso.nombre}."

    # Metodo para mostrar los cursos del estudiante
    def mostrar_cursos(self):
        if not self.cursos:
            return f"{self.nombre} no está inscrito en ningún curso."
        return f"Cursos de {self.nombre}: " + ", ".join([curso.nombre for curso in self.cursos])


class Curso:
    # Constructor que inicializa los atributos del curso
    def __init__(self, nombre, codigo):
        self.nombre = nombre  # Atributo: nombre del curso
        self.codigo = codigo  # Atributo: código del curso
        self.estudiantes = []  # Atributo: lista de estudiantes inscritos

    # Metodo para agregar un estudiante al curso
    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)
        estudiante.inscribir_curso(self)
        return f"{estudiante.nombre} agregado al curso {self.nombre}."

    # Metodo para mostrar los estudiantes del curso
    def mostrar_estudiantes(self):
        if not self.estudiantes:
            return f"No hay estudiantes en {self.nombre}."
        return f"Estudiantes en {self.nombre}: " + ", ".join([estudiante.nombre for estudiante in self.estudiantes])


# Ejemplo de uso
if __name__ == "__main__":
    # Crear algunos estudiantes
    estudiante1 = Estudiante("Johanna Gamboa", "UEA001")
    estudiante2 = Estudiante("Cristhian Chacha", "UEA002")
    estudiante3 = Estudiante("Cinthia Carrión", "UEA003")

    # Crear algunos cursos
    curso1 = Curso("Sistemas Operativos", "SO101")
    curso2 = Curso("Programación Orientada a Objetos", "POO101")

    # Inscribir estudiantes en cursos
    print(curso1.agregar_estudiante(estudiante1))
    print(curso1.agregar_estudiante(estudiante2))
    print(curso2.agregar_estudiante(estudiante1))
    print(curso2.agregar_estudiante(estudiante3))

    # Mostrar los cursos de cada estudiante
    print("\n" + estudiante1.mostrar_cursos())
    print(estudiante2.mostrar_cursos())

    # Mostrar los estudiantes de cada curso
    print("\n" + curso1.mostrar_estudiantes())
    print(curso2.mostrar_estudiantes())