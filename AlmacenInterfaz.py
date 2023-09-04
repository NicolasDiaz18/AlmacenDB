import tkinter as tk
from tkinter import ttk
import mysql.connector

db = mysql.connector.connect(host="localhost",
                                   user="root",
                                   password="phpmyadmin",
                                   database="Almacen")

# Crear la ventana principal
root = tk.Tk()
root.title("Visualización de Tablas de Almacen")

# Función para cargar datos de la tabla seleccionada
def cargarTabla(tabla):
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM {tabla}")
    data = cursor.fetchall()
    
    # Limpiar la tabla existente si hay datos
    for i in tabla_tree.get_children():
        tabla_tree.delete(i)
    
    # Insertar nuevos datos en la tabla
    for row in data:
        tabla_tree.insert("", "end", values=row)
    
    cursor.close()

# Crear un cuadro combinado para seleccionar la tabla
tablaCombobox = ttk.Combobox(root, values=["categoria", "marca", "producto"])
tablaCombobox.set("Seleccionar Tabla")
tablaCombobox.pack(pady=10)

# Crear un botón para cargar la tabla seleccionada
cargarButton = tk.Button(root, text="Cargar Tabla", command=lambda: cargarTabla(tablaCombobox.get()))
cargarButton.pack()

# Crear una tabla para mostrar los datos
tabla_tree = ttk.Treeview(root, columns=("id", "Nombre", "Precio", "Stock", "idCategoria", "idMarca"))
tabla_tree.heading("#1", text="id")
tabla_tree.heading("#2", text="Nombre")
tabla_tree.heading("#3", text="Precio")
tabla_tree.heading("#4", text="Stock")
tabla_tree.heading("#5", text="idCategoria")
tabla_tree.heading("#6", text="idMarca")
tabla_tree.pack()

# Iniciar la aplicación
root.mainloop()

# Cerrar la conexión a la base de datos al cerrar la aplicación
db.close()