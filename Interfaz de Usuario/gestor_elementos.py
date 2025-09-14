import tkinter as tk
from tkinter import messagebox

class DerNote:
    def __init__(self, ventana):
        """
        Inicializa la aplicación con una interfaz simple para gestionar elementos.

        Args:
            ventana: La ventana principal de Tkinter
        """
        self.ventana = ventana
        self.ventana.title("DerNote")
        self.ventana.geometry("500x400")

        # Crear y colocar los elementos en la ventana
        self.crear_widgets()

    def crear_widgets(self):
        """Crea y coloca todos los elementos de la interfaz gráfica."""
        # Título de la aplicación
        self.titulo = tk.Label(
            self.ventana,
            text="Gestor de Elementos - DerNote",
            font=("Arial", 16, "bold")
        )
        self.titulo.pack(pady=10)

        # Marco para el campo de entrada y botones
        marco_entrada = tk.Frame(self.ventana)
        marco_entrada.pack(pady=10, padx=20, fill=tk.X)

        # Etiqueta para el campo de texto
        self.etiqueta = tk.Label(
            marco_entrada,
            text="Ingrese nuevo elemento:"
        )
        self.etiqueta.grid(row=0, column=0, sticky=tk.W, pady=5)

        # Campo de texto para ingresar elementos
        self.campo_texto = tk.Entry(
            marco_entrada,
            width=30
        )
        self.campo_texto.grid(row=1, column=0, padx=(0, 10), sticky=tk.W + tk.E)
        self.campo_texto.bind("<Return>", self.agregar_elemento)

        # Botón para agregar elementos
        self.boton_agregar = tk.Button(
            marco_entrada,
            text="Agregar elemento",
            command=self.agregar_elemento
        )
        self.boton_agregar.grid(row=1, column=1, padx=(10, 0))

        # Configurar la expansión de la columna del campo de texto
        marco_entrada.columnconfigure(0, weight=1)

        # Marco para la lista de elementos
        marco_lista = tk.Frame(self.ventana)
        marco_lista.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

        # Etiqueta para la lista
        self.etiqueta_lista = tk.Label(
            marco_lista,
            text="Elementos agregados:"
        )
        self.etiqueta_lista.pack(anchor=tk.W)

        # Lista para mostrar los elementos (usaremos un Listbox)
        self.lista_elementos = tk.Listbox(
            marco_lista,
            height=10
        )
        self.lista_elementos.pack(fill=tk.BOTH, expand=True, pady=(5, 10))

        # Marco para los botones inferiores
        marco_botones = tk.Frame(self.ventana)
        marco_botones.pack(pady=10)

        # Botón para limpiar la lista
        self.boton_limpiar = tk.Button(
            marco_botones,
            text="Vaciar Lista",
            command=self.limpiar_lista
        )
        self.boton_limpiar.pack(side=tk.LEFT, padx=5)

        # Botón para eliminar elemento seleccionado
        self.boton_eliminar = tk.Button(
            marco_botones,
            text="Eliminar Seleccionado",
            command=self.eliminar_elemento
        )
        self.boton_eliminar.pack(side=tk.LEFT, padx=5)

        # Botón para salir de la aplicación
        self.boton_salir = tk.Button(
            marco_botones,
            text="Salir",
            command=self.ventana.quit
        )
        self.boton_salir.pack(side=tk.LEFT, padx=5)

    def agregar_elemento(self, event=None):
        """
        Agrega un elemento a la lista a partir del texto en el campo de entrada.

        Args:
            event: Evento opcional (para manejar la tecla Enter)
        """
        # Obtener el texto del campo de entrada
        texto = self.campo_texto.get().strip()

        # Verificar que el texto no esté vacío
        if texto:
            # Agregar el elemento a la lista
            self.lista_elementos.insert(tk.END, texto)
            # Limpiar el campo de texto
            self.campo_texto.delete(0, tk.END)
        else:
            # Mostrar advertencia si el campo está vacío
            messagebox.showwarning("Campo vacío", "Por favor, ingresa un elemento.")

    def eliminar_elemento(self):
        """Elimina el elemento seleccionado de la lista."""
        # Obtener el índice del elemento seleccionado
        seleccion = self.lista_elementos.curselection()

        # Verificar si hay una selección
        if seleccion:
            # Eliminar el elemento seleccionado
            self.lista_elementos.delete(seleccion[0])
        else:
            # Mostrar advertencia si no hay selección
            messagebox.showwarning("Sin selección", "Por favor, selecciona un elemento para eliminar.")

    def limpiar_lista(self):
        """Elimina toda la lista de elementos."""
        # Verificar si la lista tiene elementos
        if self.lista_elementos.size() > 0:
            # Preguntar confirmación al usuario
            respuesta = messagebox.askyesno(
                "Confirmar eliminación",
                "¿Estás seguro de que quieres eliminar todos los elementos de la lista?"
            )
            if respuesta:
                # Eliminar la lista
                self.lista_elementos.delete(0, tk.END)
        else:
            # Mostrar mensaje si la lista está vacía
            messagebox.showinfo("Lista vacía", "La lista ya está vacía.")

def main():
    """Función principal que inicia la aplicación."""
    # Crear la ventana principal
    ventana = tk.Tk()

    # Crear la aplicación
    app = DerNote(ventana)

    # Iniciar el bucle principal de la aplicación
    ventana.mainloop()

if __name__ == "__main__":
    main()