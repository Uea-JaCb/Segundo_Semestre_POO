# Clase Producto: Representa un producto individual en el inventario.
# Incluye atributos para ID, nombre, cantidad y precio.
class Producto:
    def __init__(self, id, descripcion, stock, costo):
        self._id = id  # ID único del producto
        self._descripcion = descripcion     # Nombre o descripción del producto
        self._stock = stock                 # Cantidad disponible
        self._costo = costo                 # Precio unitario

    # Getter para el identificador
    def get_id(self):
        return self._id

    # Setter para el identificador (no cambia)
    def set_id(self, nuevo_id):
        self._id = nuevo_id

    # Getter para la descripción
    def get_descripcion(self):
        return self._descripcion

    # Setter para la descripción
    def set_descripcion(self, nueva_descripcion):
        self._descripcion = nueva_descripcion

    # Getter para el stock
    def get_stock(self):
        return self._stock

    # Setter para el stock
    def set_stock(self, nuevo_stock):
        self._stock = nuevo_stock

    # Getter para el costo
    def get_costo(self):
        return self._costo

    # Setter para el costo
    def set_costo(self, nuevo_costo):
        self._costo = nuevo_costo

    # Metodo para representar el producto como cadena, útil para impresión
    def __str__(self):
        return f"ID: {self._id} | Descripción: {self._descripcion} | Stock: {self._stock} | Costo: ${self._costo:.2f}"

    # Metodo para convertir producto a formato de archivo
    def to_file_format(self):
        return f"{self._id},{self._descripcion},{self._stock},{self._costo}\n"

# Clase Inventario: Gestiona una colección de productos utilizando una lista simple.
# Ahora incluye manejo de archivos para persistencia.
class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.lista_productos = []  # Lista para almacenar objetos Producto
        self.archivo = archivo     # Nombre del archivo para almacenamiento
        self.cargar_inventario()   # Cargar inventario al iniciar

    # Metodo para cargar productos desde el archivo
    def cargar_inventario(self):
        try:
            with open(self.archivo, 'r') as file:
                for linea in file:
                    id_prod, desc, stock, costo = linea.strip().split(',')
                    producto = Producto(id_prod, desc, int(stock), float(costo))
                    self.lista_productos.append(producto)
                print(f"Inventario cargado exitosamente desde {self.archivo}.")
        except FileNotFoundError:
            print(f"Archivo {self.archivo} no encontrado. Se creará uno nuevo.")
            self.guardar_inventario()  # Crear archivo vacío
        except PermissionError:
            print(f"Error: No hay permisos para leer {self.archivo}.")
        except Exception as e:
            print(f"Error al cargar el inventario: {str(e)}")

    # Metodo para guardar productos en el archivo
    def guardar_inventario(self):
        try:
            with open(self.archivo, 'w') as file:
                for prod in self.lista_productos:
                    file.write(prod.to_file_format())
            print(f"Inventario guardado exitosamente en {self.archivo}.")
        except PermissionError:
            print(f"Error: No hay permisos para escribir en {self.archivo}.")
        except Exception as e:
            print(f"Error al guardar el inventario: {str(e)}")

    # Metodo para añadir un nuevo producto, verificando que el ID sea único
    def insertar_producto(self, nuevo_producto):
        for prod in self.lista_productos:
            if prod.get_id() == nuevo_producto.get_id():
                print("Error: El ID del producto ya existe en el inventario.")
                return
        self.lista_productos.append(nuevo_producto)
        self.guardar_inventario()
        print("Producto añadido exitosamente.")

    # Metodo para eliminar un producto por ID
    def remover_producto(self, id_a_remover):
        for i, prod in enumerate(self.lista_productos):
            if prod.get_id() == id_a_remover:
                del self.lista_productos[i]
                self.guardar_inventario()
                print("Producto eliminado exitosamente.")
                return
        print("Error: No se encontró un producto con ese ID.")

    # Metodo para actualizar stock o costo de un producto por ID
    def modificar_producto(self, id_a_modificar, nuevo_stock=None, nuevo_costo=None):
        for prod in self.lista_productos:
            if prod.get_id() == id_a_modificar:
                if nuevo_stock is not None:
                    prod.set_stock(nuevo_stock)
                if nuevo_costo is not None:
                    prod.set_costo(nuevo_costo)
                self.guardar_inventario()
                print("Producto actualizado exitosamente.")
                return
        print("Error: No se encontró un producto con ese ID.")

    # Metodo para buscar productos por descripción (coincidencia parcial, insensible a mayúsculas)
    def localizar_productos(self, termino_busqueda):
        coincidencias = []
        for prod in self.lista_productos:
            if termino_busqueda.lower() in prod.get_descripcion().lower():
                coincidencias.append(prod)
        return coincidencias

    # Metodo para mostrar todos los productos en el inventario
    def listar_todo(self):
        if not self.lista_productos:
            print("El inventario está vacío.")
        else:
            for prod in self.lista_productos:
                print(prod)

# Función para mostrar el menú en formato de tabla simple
def mostrar_menu():
    print("+----+-----------------------------+")
    print("| Opc | Acción a realizar           |")
    print("+----+-----------------------------+")
    print("|  1  | Ingresar nuevo producto     |")
    print("|  2  | Eliminar producto por ID    |")
    print("|  3  | Modificar stock o costo     |")
    print("|  4  | Buscar por descripción      |")
    print("|  5  | Listar todo el inventario   |")
    print("|  6  | Salir del sistema           |")
    print("+----+-----------------------------+")

# Función principal para la interfaz interactiva en consola
def interfaz_principal():
    gestion_inventario = Inventario()
    while True:
        mostrar_menu()
        try:
            seleccion = input("Ingrese el número de opción: ")
            if seleccion == '6':
                print("Saliendo del sistema.")
                break
            elif seleccion == '1':
                id_nuevo = input("Ingrese el ID único del producto: ")
                desc_nueva = input("Ingrese la descripción del producto: ")
                stock_nuevo = int(input("Ingrese el stock inicial: "))
                costo_nuevo = float(input("Ingrese el costo unitario: "))
                prod_nuevo = Producto(id_nuevo, desc_nueva, stock_nuevo, costo_nuevo)
                gestion_inventario.insertar_producto(prod_nuevo)
            elif seleccion == '2':
                id_remover = input("Ingrese el ID del producto a eliminar: ")
                gestion_inventario.remover_producto(id_remover)
            elif seleccion == '3':
                id_modificar = input("Ingrese el ID del producto a modificar: ")
                stock_input = input("Nuevo stock (deje vacío para no modificar): ")
                costo_input = input("Nuevo costo (deje vacío para no modificar): ")
                nuevo_stock = int(stock_input) if stock_input else None
                nuevo_costo = float(costo_input) if costo_input else None
                gestion_inventario.modificar_producto(id_modificar, nuevo_stock, nuevo_costo)
            elif seleccion == '4':
                termino = input("Ingrese el término de búsqueda para la descripción: ")
                resultados = gestion_inventario.localizar_productos(termino)
                if resultados:
                    print("Productos encontrados:")
                    for res in resultados:
                        print(res)
                else:
                    print("No se encontraron productos que coincidan con su búsqueda.")
            elif seleccion == '5':
                print("Inventario actual:")
                gestion_inventario.listar_todo()
            else:
                print("Opción inválida. Por favor, seleccione una opción válida.")
        except ValueError:
            print("Error: Entrada inválida. Asegúrese de ingresar valores numéricos para stock y costo.")
        except Exception as e:
            print(f"Error inesperado: {str(e)}")

# Punto de entrada principal del programa
if __name__ == "__main__":
    interfaz_principal()# Clase Producto: Representa un producto individual en el inventario.
# Incluye atributos para ID, nombre, cantidad y precio.
class Producto:
    def __init__(self, id, descripcion, stock, costo):
        self._id = id  # ID único del producto
        self._descripcion = descripcion     # Nombre o descripción del producto
        self._stock = stock                 # Cantidad disponible
        self._costo = costo                 # Precio unitario

    # Getter para el identificador
    def get_id(self):
        return self._id

    # Setter para el identificador (no cambia)
    def set_id(self, nuevo_id):
        self._id = nuevo_id

    # Getter para la descripción
    def get_descripcion(self):
        return self._descripcion

    # Setter para la descripción
    def set_descripcion(self, nueva_descripcion):
        self._descripcion = nueva_descripcion

    # Getter para el stock
    def get_stock(self):
        return self._stock

    # Setter para el stock
    def set_stock(self, nuevo_stock):
        self._stock = nuevo_stock

    # Getter para el costo
    def get_costo(self):
        return self._costo

    # Setter para el costo
    def set_costo(self, nuevo_costo):
        self._costo = nuevo_costo

    # Metodo para representar el producto como cadena, útil para impresión
    def __str__(self):
        return f"ID: {self._id} | Descripción: {self._descripcion} | Stock: {self._stock} | Costo: ${self._costo:.2f}"

    # Metodo para convertir producto a formato de archivo
    def to_file_format(self):
        return f"{self._id},{self._descripcion},{self._stock},{self._costo}\n"

# Clase Inventario: Gestiona una colección de productos utilizando una lista simple.
# Ahora incluye manejo de archivos para persistencia.
class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.lista_productos = []  # Lista para almacenar objetos Producto
        self.archivo = archivo     # Nombre del archivo para almacenamiento
        self.cargar_inventario()   # Cargar inventario al iniciar

    # Metodo para cargar productos desde el archivo
    def cargar_inventario(self):
        try:
            with open(self.archivo, 'r') as file:
                for linea in file:
                    id_prod, desc, stock, costo = linea.strip().split(',')
                    producto = Producto(id_prod, desc, int(stock), float(costo))
                    self.lista_productos.append(producto)
                print(f"Inventario cargado exitosamente desde {self.archivo}.")
        except FileNotFoundError:
            print(f"Archivo {self.archivo} no encontrado. Se creará uno nuevo.")
            self.guardar_inventario()  # Crear archivo vacío
        except PermissionError:
            print(f"Error: No hay permisos para leer {self.archivo}.")
        except Exception as e:
            print(f"Error al cargar el inventario: {str(e)}")

    # Metodo para guardar productos en el archivo
    def guardar_inventario(self):
        try:
            with open(self.archivo, 'w') as file:
                for prod in self.lista_productos:
                    file.write(prod.to_file_format())
            print(f"Inventario guardado exitosamente en {self.archivo}.")
        except PermissionError:
            print(f"Error: No hay permisos para escribir en {self.archivo}.")
        except Exception as e:
            print(f"Error al guardar el inventario: {str(e)}")

    # Metodo para añadir un nuevo producto, verificando que el ID sea único
    def insertar_producto(self, nuevo_producto):
        for prod in self.lista_productos:
            if prod.get_id() == nuevo_producto.get_id():
                print("Error: El ID del producto ya existe en el inventario.")
                return
        self.lista_productos.append(nuevo_producto)
        self.guardar_inventario()
        print("Producto añadido exitosamente.")

    # Metodo para eliminar un producto por ID
    def remover_producto(self, id_a_remover):
        for i, prod in enumerate(self.lista_productos):
            if prod.get_id() == id_a_remover:
                del self.lista_productos[i]
                self.guardar_inventario()
                print("Producto eliminado exitosamente.")
                return
        print("Error: No se encontró un producto con ese ID.")

    # Metodo para actualizar stock o costo de un producto por ID
    def modificar_producto(self, id_a_modificar, nuevo_stock=None, nuevo_costo=None):
        for prod in self.lista_productos:
            if prod.get_id() == id_a_modificar:
                if nuevo_stock is not None:
                    prod.set_stock(nuevo_stock)
                if nuevo_costo is not None:
                    prod.set_costo(nuevo_costo)
                self.guardar_inventario()
                print("Producto actualizado exitosamente.")
                return
        print("Error: No se encontró un producto con ese ID.")

    # Metodo para buscar productos por descripción (coincidencia parcial, insensible a mayúsculas)
    def localizar_productos(self, termino_busqueda):
        coincidencias = []
        for prod in self.lista_productos:
            if termino_busqueda.lower() in prod.get_descripcion().lower():
                coincidencias.append(prod)
        return coincidencias

    # Metodo para mostrar todos los productos en el inventario
    def listar_todo(self):
        if not self.lista_productos:
            print("El inventario está vacío.")
        else:
            for prod in self.lista_productos:
                print(prod)

# Función para mostrar el menú en formato de tabla simple
def mostrar_menu():
    print("+----+-----------------------------+")
    print("| Opc | Acción a realizar           |")
    print("+----+-----------------------------+")
    print("|  1  | Ingresar nuevo producto     |")
    print("|  2  | Eliminar producto por ID    |")
    print("|  3  | Modificar stock o costo     |")
    print("|  4  | Buscar por descripción      |")
    print("|  5  | Listar todo el inventario   |")
    print("|  6  | Salir del sistema           |")
    print("+----+-----------------------------+")

# Función principal para la interfaz interactiva en consola
def interfaz_principal():
    gestion_inventario = Inventario()
    while True:
        mostrar_menu()
        try:
            seleccion = input("Ingrese el número de opción: ")
            if seleccion == '6':
                print("Saliendo del sistema.")
                break
            elif seleccion == '1':
                id_nuevo = input("Ingrese el ID único del producto: ")
                desc_nueva = input("Ingrese la descripción del producto: ")
                stock_nuevo = int(input("Ingrese el stock inicial: "))
                costo_nuevo = float(input("Ingrese el costo unitario: "))
                prod_nuevo = Producto(id_nuevo, desc_nueva, stock_nuevo, costo_nuevo)
                gestion_inventario.insertar_producto(prod_nuevo)
            elif seleccion == '2':
                id_remover = input("Ingrese el ID del producto a eliminar: ")
                gestion_inventario.remover_producto(id_remover)
            elif seleccion == '3':
                id_modificar = input("Ingrese el ID del producto a modificar: ")
                stock_input = input("Nuevo stock (deje vacío para no modificar): ")
                costo_input = input("Nuevo costo (deje vacío para no modificar): ")
                nuevo_stock = int(stock_input) if stock_input else None
                nuevo_costo = float(costo_input) if costo_input else None
                gestion_inventario.modificar_producto(id_modificar, nuevo_stock, nuevo_costo)
            elif seleccion == '4':
                termino = input("Ingrese el término de búsqueda para la descripción: ")
                resultados = gestion_inventario.localizar_productos(termino)
                if resultados:
                    print("Productos encontrados:")
                    for res in resultados:
                        print(res)
                else:
                    print("No se encontraron productos que coincidan con su búsqueda.")
            elif seleccion == '5':
                print("Inventario actual:")
                gestion_inventario.listar_todo()
            else:
                print("Opción inválida. Por favor, seleccione una opción válida.")
        except ValueError:
            print("Error: Entrada inválida. Asegúrese de ingresar valores numéricos para stock y costo.")
        except Exception as e:
            print(f"Error inesperado: {str(e)}")

# Punto de entrada principal del programa
if __name__ == "__main__":
    interfaz_principal()