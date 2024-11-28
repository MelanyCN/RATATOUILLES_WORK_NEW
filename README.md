
---

# Video Cutter Script

Este proyecto contiene un script en Python que corta un video en múltiples clips basándose en los tiempos especificados en un archivo CSV. Los clips resultantes se guardan con nombres personalizados.

## Requisitos

### Librerías necesarias
Instala las siguientes bibliotecas antes de ejecutar el script:

```bash
pip install pandas moviepy
```

### Versión de Python
Este script ha sido probado con **Python 3.8 o superior**.

## Formato del CSV

El archivo CSV debe tener el siguiente formato:
- **Inicio desde la fila 13**: Las primeras 12 filas se omiten automáticamente.
- **Columnas relevantes**:
  - `Edited Video File`: Nombre con el que se guardará el clip.
  - `Start Time (sec)`: Tiempo de inicio del clip en formato `hh:mm:ss,ms`.
  - `End Time (sec)`: Tiempo de fin del clip en formato `hh:mm:ss,ms`.

Ejemplo de datos en el archivo CSV:

| Edited Video File | Start Time (sec) | End Time (sec) | Notes                                           |
|-------------------|------------------|----------------|------------------------------------------------|
| dash_cam_part22_1 | 00:00:11,10      | 00:00:17,15    | Al menos chocaron 3 de 5 carros                |
| dash_cam_part22_2 | 00:00:20,00      | 00:00:25,50    | Daños mínimos, nadie necesitó ambulancia       |
| dash_cam_part26_1 | 00:01:00,10      | 00:01:05,00    | SUV pasó en rojo, chocó contra un camión       |

### Formato del Tiempo
Los tiempos de inicio y fin deben estar en el formato `hh:mm:ss,ms`:
- `hh` = horas
- `mm` = minutos
- `ss` = segundos
- `ms` = milisegundos (separados por una coma)

## Configuración

El script utiliza la variable `path` para definir las rutas a los archivos. Asegúrate de configurar las rutas correctamente antes de ejecutarlo:

```python
path = "/ruta/a/tu/directorio/"

video_path = path + "video_carros.mp4"  # Ruta al video principal
csv_path = path + "tiempos.csv"         # Ruta al archivo CSV
output_folder = path + "videos_prueba"  # Carpeta donde se guardarán los clips
```

## Ejecución

### En Linux
1. Asegúrate de que el archivo `main.py` esté en el directorio del proyecto.
2. Ejecuta el script con el siguiente comando:
   ```bash
   python3 main.py
   ```

### En Windows
1. Abre un terminal o `cmd` en el directorio del proyecto.
2. Ejecuta el script con el siguiente comando:
   ```bash
   python main.py
   ```

## Resultado esperado

Por cada fila en el archivo CSV:
- Se corta un clip del video principal basado en los tiempos de inicio y fin.
- Los clips se guardan en la carpeta especificada en `output_folder`.
- Los nombres de los clips serán los especificados en la columna `Edited Video File` del archivo CSV.

Ejemplo:
- Entrada:
  - `Start Time (sec)` = `00:00:11,10`
  - `End Time (sec)` = `00:00:17,15`
  - `Edited Video File` = `dash_cam_part22_1`
- Salida:
  - Se genera un archivo `dash_cam_part22_1.mp4` en la carpeta `videos_prueba`.

---
