# 🧩 SGS Compressor

**SGS Compressor** es una herramienta simple pero potente para comprimir y descomprimir archivos y carpetas usando un formato personalizado:
`.sgs-compressed-file`

Incluye:

* Interfaz gráfica (GUI)
* Uso desde terminal (CLI estilo 7zr)
* Soporte para archivos y carpetas
* Opciones personalizables

---

# 🚀 Características

## 📦 Compresión

* ✅ Comprimir **carpetas o archivos**
* ✅ Elegir ubicación de salida (opcional)
* ✅ Elegir nombre del archivo (opcional)
* ✅ Si no se especifica:

  * Se guarda en la misma ubicación del archivo/carpeta
  * Usa el mismo nombre automáticamente

---

## 📂 Descompresión

* ✅ Seleccionar archivo `.sgs-compressed-file`
* ✅ Elegir ubicación de destino (opcional)
* ✅ Elegir nombre de la carpeta de salida (opcional)
* ✅ Si no se especifica:

  * Se extrae en la misma ubicación del archivo
  * Usa el nombre original

---

## 🖥️ Interfaz gráfica

* Selección fácil de archivos/carpetas
* Botones para comprimir y descomprimir
* Mensajes de éxito/error

---

## ⚙️ Modo terminal (CLI)

Funciona similar a herramientas como 7-Zip.

### 📦 Comprimir

```bash
sgs_compressor.exe c <ruta> [salida] [nombre]
```

Ejemplo:

```bash
sgs_compressor.exe c "C:\proyecto"
sgs_compressor.exe c "C:\proyecto" "D:\backups"
sgs_compressor.exe c "C:\proyecto" "D:\backups" "backup1"
```

---

### 📂 Descomprimir

```bash
sgs_compressor.exe x <archivo> [destino] [nombre_carpeta]
```

Ejemplo:

```bash
sgs_compressor.exe x archivo.sgs-compressed-file
sgs_compressor.exe x archivo.sgs-compressed-file "C:\extraido"
sgs_compressor.exe x archivo.sgs-compressed-file "C:\extraido" "mi_carpeta"
```

---

# 🧠 Cómo funciona

Aunque usa la extensión `.sgs-compressed-file`, internamente:

* Utiliza compresión tipo ZIP
* Permite compatibilidad futura
* Es rápido y fiable

---

# 📦 Compilación

## Instalar PyInstaller:

```bash
pip install pyinstaller
```

## Crear ejecutable:

```bash
pyinstaller --onefile --noconsole sgs_compressor.py
```

El ejecutable se generará en:

```
/dist/sgs_compressor.exe
```

---

# 📁 Estructura por defecto

Si no se especifican rutas:

* Compresión:

```
mis_archivos/
archivo.sgs-compressed-file
```

* Descompresión:

```
archivo.sgs-compressed-file
archivo/
```

---

# 🔥 Posibles mejoras futuras

* 🔐 Soporte para contraseña
* 📊 Barra de progreso
* ⚡ Compresión multinúcleo
* 📄 Listar contenido sin extraer
* 🧪 Verificar integridad del archivo
* 🎨 Interfaz moderna (tipo WinRAR/7-Zip)
* 🧩 Drag & Drop

---

# 💡 Notas

* La extensión `.sgs-compressed-file` es personalizada
* Solo este programa puede abrir estos archivos (por ahora)
* Se puede expandir fácilmente a un formato completamente propio

---

# 👨‍💻 Autor

StormGamesStudios
Proyecto personal orientado a herramientas y sistemas personalizados

---

# ⚡ Licencia

Uso libre para proyectos personales y educativos.
