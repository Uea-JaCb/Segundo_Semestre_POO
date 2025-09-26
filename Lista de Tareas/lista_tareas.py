"""
Aplicación GUI de Lista de Tareas
Autor: Johao Caicedo Bautista
Descripción:
Esta aplicación permite gestionar una lista de tareas utilizando Tkinter.
El usuario puede añadir nuevas tareas, marcarlas como completadas y eliminarlas.
Se implementan eventos de clic y teclado para una experiencia más fluida.
"""
import tkinter as tk
from tkinter import messagebox

# --- Clase Principal ---
class ListaTareasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas 📝")
        self.root.geometry("410x450")
        self.root.resizable(False, False)
        self.root.configure(bg="#f5f5f5")

        # --- Lista para almacenar tareas ---
        self.tareas = []

        # --- Etiqueta principal ---
        self.label_titulo = tk.Label(
            root, text="Gestor de Tareas", font=("Arial", 16, "bold"), bg="#f5f5f5"
        )
        self.label_titulo.pack(pady=10)

        # --- Campo de entrada ---
        self.entry_tarea = tk.Entry(root, width=35, font=("Arial", 12))
        self.entry_tarea.pack(pady=10)
        self.entry_tarea.focus()

        # Evento: presionar Enter para agregar tarea
        self.entry_tarea.bind("<Return>", self.agregar_tarea_evento)

        # --- Botones ---
        frame_botones = tk.Frame(root, bg="#f5f5f5")
        frame_botones.pack(pady=5)

        self.btn_agregar = tk.Button(
            frame_botones,
            text="Añadir Tarea",
            width=15,
            command=self.agregar_tarea,
            bg="#4CAF50",
            fg="white",
        )
        self.btn_agregar.grid(row=0, column=0, padx=5)

        self.btn_completar = tk.Button(
            frame_botones,
            text="Marcar como Completada",
            width=20,
            command=self.marcar_completada,
            bg="#2196F3",
            fg="white",
        )
        self.btn_completar.grid(row=0, column=1, padx=5)

        self.btn_eliminar = tk.Button(
            frame_botones,
            text="Eliminar Tarea",
            width=15,
            command=self.eliminar_tarea,
            bg="#f44336",
            fg="white",
        )
        self.btn_eliminar.grid(row=0, column=2, padx=5)

        # --- Listbox para mostrar tareas ---
        self.listbox_tareas = tk.Listbox(
            root,
            width=50,
            height=15,
            selectmode=tk.SINGLE,
            font=("Arial", 11),
            activestyle="none",
        )
        self.listbox_tareas.pack(pady=15)

        # Evento opcional: doble clic para marcar completada
        self.listbox_tareas.bind("<Double-Button-1>", self.marcar_completada_evento)

    # --- Función para añadir tarea ---
    def agregar_tarea(self):
        tarea = self.entry_tarea.get().strip()
        if tarea == "":
            messagebox.showwarning("Campo vacío", "Por favor, ingresa una tarea.")
        else:
            # Añadir tarea a la lista interna y al listbox
            self.tareas.append({"texto": tarea, "completada": False})
            self.listbox_tareas.insert(tk.END, tarea)
            self.entry_tarea.delete(0, tk.END)

    # --- Evento Enter para añadir tarea ---
    def agregar_tarea_evento(self, event):
        self.agregar_tarea()

    # --- Función para marcar como completada ---
    def marcar_completada(self):
        seleccion = self.listbox_tareas.curselection()
        if not seleccion:
            messagebox.showinfo("Sin selección", "Selecciona una tarea para marcarla.")
            return

        index = seleccion[0]
        tarea = self.tareas[index]

        # Cambiar estado
        tarea["completada"] = not tarea["completada"]

        # Actualizar visualmente
        self.listbox_tareas.delete(index)
        texto = f"✔️ {tarea['texto']}" if tarea["completada"] else tarea["texto"]
        self.listbox_tareas.insert(index, texto)

        # Mantener la selección
        self.listbox_tareas.selection_set(index)

    # --- Evento doble clic ---
    def marcar_completada_evento(self, event):
        self.marcar_completada()

    # --- Función para eliminar tarea ---
    def eliminar_tarea(self):
        seleccion = self.listbox_tareas.curselection()
        if not seleccion:
            messagebox.showinfo("Sin selección", "Selecciona una tarea para eliminarla.")
            return

        index = seleccion[0]
        confirm = messagebox.askyesno(
            "Eliminar Tarea", f"¿Seguro que deseas eliminar '{self.tareas[index]['texto']}'?"
        )
        if confirm:
            self.listbox_tareas.delete(index)
            self.tareas.pop(index)

# --- Ejecución Principal ---
if __name__ == "__main__":
    root = tk.Tk()
    app = ListaTareasApp(root)
    root.mainloop()
