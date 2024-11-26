import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

def extraer_fotos():
    # Obtener las rutas seleccionadas
    ruta_origen = origen_var.get()
    ruta_destino = destino_var.get()

    if not ruta_origen or not ruta_destino:
        messagebox.showerror("Error", "Por favor, selecciona ambas carpetas.")
        return

    # Crear la carpeta destino si no existe
    os.makedirs(ruta_destino, exist_ok=True)

    # Extensiones de imágenes comunes
    extensiones_fotos = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"}
    contador = 0

    for raiz, directorios, archivos in os.walk(ruta_origen):
        for archivo in archivos:
            if os.path.splitext(archivo)[1].lower() in extensiones_fotos:
                ruta_archivo = os.path.join(raiz, archivo)
                try:
                    shutil.copy(ruta_archivo, ruta_destino)
                    contador += 1
                except Exception as e:
                    print(f"Error al copiar {ruta_archivo}: {e}")

    messagebox.showinfo("Completado", f"¡Se copiaron {contador} fotos a la carpeta destino!")

def seleccionar_origen():
    ruta = filedialog.askdirectory(title="Seleccionar carpeta de origen")
    origen_var.set(ruta)

def seleccionar_destino():
    ruta = filedialog.askdirectory(title="Seleccionar carpeta de destino")
    destino_var.set(ruta)

# Crear la ventana principal
root = tk.Tk()
root.title("Extractor de Fotos")

# Variables para las rutas
origen_var = tk.StringVar()
destino_var = tk.StringVar()

# Etiqueta y campo para la carpeta de origen
tk.Label(root, text="Carpeta de origen:").grid(row=0, column=0, padx=10, pady=5)
tk.Entry(root, textvariable=origen_var, width=40).grid(row=0, column=1, padx=10, pady=5)
tk.Button(root, text="Seleccionar", command=seleccionar_origen).grid(row=0, column=2, padx=10, pady=5)

# Etiqueta y campo para la carpeta de destino
tk.Label(root, text="Carpeta de destino:").grid(row=1, column=0, padx=10, pady=5)
tk.Entry(root, textvariable=destino_var, width=40).grid(row=1, column=1, padx=10, pady=5)
tk.Button(root, text="Seleccionar", command=seleccionar_destino).grid(row=1, column=2, padx=10, pady=5)

# Botón para ejecutar el proceso
tk.Button(root, text="Extraer Fotos", command=extraer_fotos, bg="green", fg="white").grid(row=2, column=0, columnspan=3, pady=20)

# Iniciar la aplicación
root.mainloop()
