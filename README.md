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

| User   | Edited Video File | Start Time (sec) | End Time (sec) | Category  | Notes                                           |
|--------|-------------------|------------------|----------------|-----------|------------------------------------------------|
| Nena   | dash_cam_part22_1 | 00:00:09,10      | 00:00:16,10    | crash     | Al menos chocaron 3 de 5 carros                |
| Nena   | dash_cam_part22_2 | 00:00:00,00      | 00:00:09,45    | no_crash  | Daños mínimos, nadie necesitó ambulancia       |
| Sebas  | dash_cam_part26_1 | 00:00:05,10      | 00:00:08,10    | crash     | Por lo menos 2 vehículos fueron afectados      |
| Sebas  | dash_cam_part26_3 | 00:00:19,10      | 00:00:22,10    | no_crash  | SUV pasó en rojo, chocó contra un camión       |

---
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
- Los clips de video y sus audios se guardan en la carpeta especificada en `output_folder`.
- Los clips se organizan en subcarpetas según su categoría (`crash` o `no_crash`).
- Dentro de cada categoría, se crean subcarpetas adicionales:
  - **`audio/`**: Contiene los archivos de audio extraídos del clip.
  - **`video/`**: Contiene los clips de video cortados.
- Los nombres de los archivos se generan con el formato: `<User>_<Edited Video File>.<extensión>`.

### Ejemplo:
#### Entrada (CSV):
- **User**: `Nena`
- **Category**: `crash`
- **Start Time (sec)**: `00:00:11,10`
- **End Time (sec)**: `00:00:17,15`
- **Edited Video File**: `dash_cam_part22_1`

#### Salida:
- Los archivos se guardarán de la siguiente manera:
  - **Audio**: `videos_prueba/crash/audio/nena_dash_cam_part22_1.mp3`
  - **Video**: `videos_prueba/crash/video/nena_dash_cam_part22_1.mp4`

### Organización de carpetas:
Si hay múltiples categorías y usuarios, la estructura será la siguiente:
```
output_folder/
├── crash/
│   ├── audio/
│   │   ├── nena_dash_cam_part22_1.mp3
│   │   └── otro_audio.mp3
│   ├── video/
│   │   ├── nena_dash_cam_part22_1.mp4
│   │   └── otro_video.mp4
├── no_crash/
│   ├── audio/
│   │   ├── sebas_dash_cam_part26_1.mp3
│   │   └── otro_audio.mp3
│   ├── video/
│   │   ├── sebas_dash_cam_part26_1.mp4
│   │   └── otro_video.mp4
```

