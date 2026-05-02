import os
import zipfile
import tkinter as tk
from tkinter import filedialog, messagebox
import sys

# ========================
# FUNCIONES BASE
# ========================

def comprimir(ruta, salida=None, nombre=None):
    if not os.path.exists(ruta):
        raise Exception("La ruta no existe")

    base_dir = os.path.dirname(ruta)
    if not salida:
        salida = base_dir

    if not nombre:
        nombre = os.path.basename(ruta)

    archivo_salida = os.path.join(salida, nombre + ".sgs-compressed-file")

    with zipfile.ZipFile(archivo_salida, 'w', zipfile.ZIP_DEFLATED) as zipf:
        if os.path.isfile(ruta):
            zipf.write(ruta, os.path.basename(ruta))
        else:
            for root, dirs, files in os.walk(ruta):
                for file in files:
                    ruta_completa = os.path.join(root, file)
                    ruta_relativa = os.path.relpath(ruta_completa, ruta)
                    zipf.write(ruta_completa, ruta_relativa)

    return archivo_salida


def descomprimir(archivo, destino=None, nombre_carpeta=None):
    if not os.path.exists(archivo):
        raise Exception("El archivo no existe")

    base_dir = os.path.dirname(archivo)

    if not destino:
        destino = base_dir

    if nombre_carpeta:
        destino = os.path.join(destino, nombre_carpeta)

    os.makedirs(destino, exist_ok=True)

    with zipfile.ZipFile(archivo, 'r') as zipf:
        zipf.extractall(destino)

    return destino

# ========================
# CLI (modo terminal)
# ========================

def modo_terminal():
    args = sys.argv

    if len(args) < 3:
        print("Uso:")
        print("  c <ruta> [salida] [nombre]         -> Comprimir")
        print("  x <archivo> [destino] [nombre]     -> Descomprimir")
        sys.exit()

    comando = args[1]

    try:
        if comando == "c":
            ruta = args[2]
            salida = args[3] if len(args) > 3 else None
            nombre = args[4] if len(args) > 4 else None

            resultado = comprimir(ruta, salida, nombre)
            print(f"Comprimido en: {resultado}")

        elif comando == "x":
            archivo = args[2]
            destino = args[3] if len(args) > 3 else None
            nombre = args[4] if len(args) > 4 else None

            resultado = descomprimir(archivo, destino, nombre)
            print(f"Descomprimido en: {resultado}")

        else:
            print("Comando no válido")

    except Exception as e:
        print("Error:", str(e))

# ========================
# GUI
# ========================

def iniciar_gui():
    root = tk.Tk()
    root.title("SGS Compressor")
    root.geometry("520x450")

    # -------- COMPRESIÓN --------

    tk.Label(root, text="Comprimir archivo o carpeta").pack(pady=5)

    entry_ruta = tk.Entry(root, width=60)
    entry_ruta.pack()

    def seleccionar_archivo():
        archivo = filedialog.askopenfilename()
        entry_ruta.delete(0, tk.END)
        entry_ruta.insert(0, archivo)

    def seleccionar_carpeta():
        carpeta = filedialog.askdirectory()
        entry_ruta.delete(0, tk.END)
        entry_ruta.insert(0, carpeta)

    tk.Button(root, text="Seleccionar archivo", command=seleccionar_archivo).pack(pady=2)
    tk.Button(root, text="Seleccionar carpeta", command=seleccionar_carpeta).pack(pady=2)

    entry_salida = tk.Entry(root, width=60)
    entry_salida.pack()
    entry_salida.insert(0, "Salida (opcional)")

    def seleccionar_salida():
        carpeta = filedialog.askdirectory()
        entry_salida.delete(0, tk.END)
        entry_salida.insert(0, carpeta)

    tk.Button(root, text="Seleccionar salida", command=seleccionar_salida).pack(pady=2)

    entry_nombre = tk.Entry(root, width=60)
    entry_nombre.pack()
    entry_nombre.insert(0, "Nombre archivo (opcional)")

    def ejecutar_comprimir():
        try:
            ruta = entry_ruta.get()
            salida = entry_salida.get() if "Salida" not in entry_salida.get() else None
            nombre = entry_nombre.get() if "Nombre" not in entry_nombre.get() else None

            resultado = comprimir(ruta, salida, nombre)
            messagebox.showinfo("Éxito", f"Comprimido en:\n{resultado}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(root, text="Comprimir", bg="green", fg="white", command=ejecutar_comprimir).pack(pady=10)

    # -------- DESCOMPRESIÓN --------

    tk.Label(root, text="Descomprimir archivo").pack(pady=5)

    entry_archivo = tk.Entry(root, width=60)
    entry_archivo.pack()

    def seleccionar_archivo_zip():
        archivo = filedialog.askopenfilename(filetypes=[("SGS Files", "*.sgs-compressed-file")])
        entry_archivo.delete(0, tk.END)
        entry_archivo.insert(0, archivo)

    tk.Button(root, text="Seleccionar archivo", command=seleccionar_archivo_zip).pack(pady=2)

    entry_destino = tk.Entry(root, width=60)
    entry_destino.pack()
    entry_destino.insert(0, "Destino (opcional)")

    def seleccionar_destino():
        carpeta = filedialog.askdirectory()
        entry_destino.delete(0, tk.END)
        entry_destino.insert(0, carpeta)

    tk.Button(root, text="Seleccionar destino", command=seleccionar_destino).pack(pady=2)

    entry_nombre_out = tk.Entry(root, width=60)
    entry_nombre_out.pack()
    entry_nombre_out.insert(0, "Nombre carpeta (opcional)")

    def ejecutar_descomprimir():
        try:
            archivo = entry_archivo.get()
            destino = entry_destino.get() if "Destino" not in entry_destino.get() else None
            nombre = entry_nombre_out.get() if "Nombre" not in entry_nombre_out.get() else None

            resultado = descomprimir(archivo, destino, nombre)
            messagebox.showinfo("Éxito", f"Descomprimido en:\n{resultado}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(root, text="Descomprimir", bg="blue", fg="white", command=ejecutar_descomprimir).pack(pady=10)

    root.mainloop()

# ========================
# MAIN
# ========================

if __name__ == "__main__":
    if len(sys.argv) > 1:
        modo_terminal()
    else:
        iniciar_gui()