class Archivo:
    def __init__(self, nombre_archivo):
        """
        Constructor de la clase.
        Se ejecuta al crear un objeto de tipo Archivo.
        Inicializa el atributo nombre_archivo y simula abrir el archivo.
        """
        self.nombre_archivo = nombre_archivo
        print(f"El archivo fue abierto: {self.nombre_archivo}")

    def leer(self):
        """
        Metodo de ejemplo que simula la lectura de un archivo.
        """
        print(f"Se esta leyendo el archivo: {self.nombre_archivo}")

    def __del__(self):
        """
        Destructor de la clase.
        Se ejecuta automáticamente cuando el objeto se destruye,
        por ejemplo al finalizar el programa o cuando ya no se usa.
        """
        print(f"El archivo ha sido cerrado: {self.nombre_archivo}")


# Programa principal
if __name__ == "__main__":
    primer_archivo = Archivo("Prueba_POO.txt")  # Se llama automáticamente al constructor __init__
    primer_archivo.leer()                  # Usamos el metodo leer

    print("El programa está por finalizar...")
    # Al terminar el programa, Python llama automáticamente a __del__ del objeto primer_archivo
