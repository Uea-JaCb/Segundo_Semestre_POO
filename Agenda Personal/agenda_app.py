import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import datetime

class AgendaApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Agenda Personal")
        self.geometry("650x450")  # Aumentar el tamaño para acomodar el nuevo widget

        # Configurar la estructura de la ventana
        self.main_frame = tk.Frame(self)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Crear los frames para organizar la interfaz
        self.input_frame = tk.Frame(self.main_frame)
        self.input_frame.pack(pady=10)

        self.list_frame = tk.Frame(self.main_frame)
        self.list_frame.pack(fill=tk.BOTH, expand=True)

        self.button_frame = tk.Frame(self.main_frame)
        self.button_frame.pack(pady=10)

        # Listado de eventos con TreeView
        self.setup_event_list()

        # Campos de entrada
        self.setup_input_fields()

        # Botones de acción
        self.setup_action_buttons()

        # Datos de ejemplo (opcional)
        self.load_sample_data()

    def setup_event_list(self):
        """Configura y muestra el TreeView para listar los eventos."""
        # Definir las columnas
        columns = ("Fecha", "Hora", "Descripción")
        self.tree = ttk.Treeview(self.list_frame, columns=columns, show="headings")

        # Configurar los encabezados de las columnas
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")

        # Ajustar el ancho de las columnas
        self.tree.column("Fecha", width=100, anchor="center")
        self.tree.column("Hora", width=80, anchor="center")
        self.tree.column("Descripción", width=400, anchor="w")

        # Añadir una barra de desplazamiento
        scrollbar = ttk.Scrollbar(self.list_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def setup_input_fields(self):
        """Configura los campos de entrada para agregar un nuevo evento."""
        # Frame para los campos de entrada
        input_sub_frame = tk.Frame(self.input_frame)
        input_sub_frame.pack(pady=5)

        # Fecha con DateEntry (DatePicker)
        tk.Label(input_sub_frame, text="Fecha:").pack(side=tk.LEFT, padx=5)
        self.date_entry = DateEntry(input_sub_frame, date_pattern='dd/mm/yyyy', width=12, background='darkblue',
                                    foreground='white', borderwidth=2)
        self.date_entry.pack(side=tk.LEFT, padx=5)

        # Hora
        tk.Label(input_sub_frame, text="Hora (hh:mm):").pack(side=tk.LEFT, padx=5)
        self.time_entry = tk.Entry(input_sub_frame, width=10)
        self.time_entry.pack(side=tk.LEFT, padx=5)

        # Descripción con widget Text
        desc_sub_frame = tk.Frame(self.input_frame)
        desc_sub_frame.pack(pady=5)
        tk.Label(desc_sub_frame, text="Descripción:").pack(side=tk.LEFT, padx=5, anchor="n")

        # Frame para el widget Text y su scrollbar
        text_frame = tk.Frame(desc_sub_frame)
        text_frame.pack(side=tk.LEFT, padx=5)

        self.description_text = tk.Text(text_frame, height=4, width=40)
        self.description_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        text_scrollbar = tk.Scrollbar(text_frame, command=self.description_text.yview)
        self.description_text.configure(yscrollcommand=text_scrollbar.set)
        text_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def setup_action_buttons(self):
        """Configura los botones de acción (Agregar, Eliminar, Salir)."""
        # Botón Agregar Evento
        self.add_button = tk.Button(self.button_frame, text="➕ Agregar Evento", command=self.add_event)
        self.add_button.pack(side=tk.LEFT, padx=10)

        # Botón Eliminar Evento
        self.delete_button = tk.Button(self.button_frame, text="🗑️ Eliminar Evento", command=self.delete_event)
        self.delete_button.pack(side=tk.LEFT, padx=10)

        # Botón Salir
        self.exit_button = tk.Button(self.button_frame, text="🚪 Salir", command=self.quit)
        self.exit_button.pack(side=tk.LEFT, padx=10)

    def add_event(self):
        """Agrega un nuevo evento a la lista si los campos no están vacíos."""
        date = self.date_entry.get()
        time = self.time_entry.get()
        # Obtener el texto del widget Text
        description = self.description_text.get("1.0", tk.END).strip()

        if date and time and description:
            # Insertar los datos en el TreeView
            self.tree.insert("", "end", values=(date, time, description))
            # Limpiar los campos de entrada
            self.time_entry.delete(0, tk.END)
            self.description_text.delete("1.0", tk.END)
        else:
            messagebox.showwarning("Campos vacíos", "Por favor, complete todos los campos para agregar un evento.")

    def delete_event(self):
        """Elimina el evento seleccionado del TreeView, previa confirmación."""
        selected_item = self.tree.selection()
        if selected_item:
            # Diálogo de confirmación (Opcional)
            confirm = messagebox.askyesno(
                "Confirmar eliminación",
                "¿Estás seguro de que deseas eliminar el evento seleccionado?"
            )
            if confirm:
                # Eliminar el item seleccionado
                self.tree.delete(selected_item)
        else:
            messagebox.showwarning("Sin selección", "Por favor, seleccione un evento para eliminar.")

    def load_sample_data(self):
        """Carga datos de ejemplo en la lista al iniciar la aplicación."""
        sample_events = [
            ("20/09/2025", "09:40", "Reunión para discutir los objetivos del trabajo práctico."),
            ("21/09/2025", "11:30", "Realizar tarea de POO de la semana 14.")
        ]
        for event in sample_events:
            self.tree.insert("", "end", values=event)

if __name__ == "__main__":
    app = AgendaApp()
    app.mainloop()