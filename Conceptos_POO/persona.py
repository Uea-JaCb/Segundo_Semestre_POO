# Definimos la clase base llamada Persona
class Persona:
    # El metodo __init__ es el constructor. Se ejecuta automáticamente al crear un objeto.
    def __init__(self, nombre, edad, cedula):
        self.nombre = nombre      # Atributo público
        self.edad = edad          # Atributo público
        self.__cedula = cedula    # Atributo privado (encapsulado), con doble guión bajo

    # Metodo para saludar (comportamiento de la clase Persona)
    def saludar(self):
        print(f"Hola, me llamo {self.nombre}.")

    # Metodo para mostrar la información de la persona
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        # Accedemos al atributo privado desde dentro de la clase
        print(f"CEDULA: {self.__cedula}")

    # Metodo público para acceder al atributo privado desde fuera
    def obtener_cedula(self):
        return self.__cedula
    # Metodo público para modificar el DNI (setter controlado)
    def cambiar_cedula(self, nueva_cedula):
        self.__cedula = nueva_cedula

# Definimos una clase derivada llamada Estudiante que hereda de Persona
class Estudiante(Persona):
    # Constructor de la clase Estudiante
    def __init__(self, nombre, edad, cedula, universidad):
        # Llamamos al constructor de la clase base (Persona) con super()
        super().__init__(nombre, edad, cedula)
        self.universidad = universidad  # Atributo propio de la clase Estudiante

    # Polimorfismo: redefinimos el metodo mostrar_informacion
    def mostrar_informacion(self):
        # Llamamos primero al metodo original de la clase base
        super().mostrar_informacion()
        # Agregamos más información específica del estudiante
        print(f"Universidad: {self.universidad}")

# Creamos un objeto de tipo Persona
persona_1 = Persona("Johao", 30, "0951519784")

# Usamos los métodos de Persona
persona_1.saludar()
persona_1.mostrar_informacion()

print("****************************************************")

# Creamos un objeto de tipo Estudiante (hereda de Persona)
estudiante_1 = Estudiante("Astrid", 29, "0952345678", "Universidad Estatal Amazónica")

# Usamos los métodos del Estudiante
estudiante_1.saludar()  # Heredado de Persona
estudiante_1.mostrar_informacion()  # Redefinido (polimorfismo)

print("****************************************************")

# Accedemos al atributo privado mediante métodos públicos
print(f"La cedula de la estudiante es: {estudiante_1.obtener_cedula()}")
estudiante_1.cambiar_cedula("0932378946")  # Encapsulación: cambio controlado
print(f"Nueva cedula de la estudiante: {estudiante_1.obtener_cedula()}")
