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
  - `User`: Usuario que será parte del nombre del archivo.
  - `Nombre Guardado`: Nombre del archivo de video original.
  - `Edited Video File`: Nombre con el que se guardará el clip.
  - `Category`: Categoría del video (`crash` o `no_crash`).
  - `Start Time`: Tiempo de inicio del clip en formato `hh:mm:ss,ms`.
  - `End Time`: Tiempo de fin del clip en formato `hh:mm:ss,ms`.

Ejemplo de datos en el archivo CSV:

| User   | Nombre Guardado   | Edited Video File | Category  | Start Time   | End Time     |
|--------|-------------------|-------------------|-----------|--------------|--------------|
| Nena   | video1            | dash_cam_part22_1 | crash     | 00:00:09,10  | 00:00:16,10  |
| Nena   | video1            | dash_cam_part22_2 | no_crash  | 00:00:00,00  | 00:00:09,45  |
| Sebas  | video2            | dash_cam_part26_1 | crash     | 00:00:05,10  | 00:00:08,10  |
| Sebas  | video2            | dash_cam_part26_3 | no_crash  | 00:00:19,10  | 00:00:22,10  |

---
### Formato del Tiempo
Los tiempos de inicio y fin deben estar en el formato `hh:mm:ss,ms`:
- `hh` = horas
- `mm` = minutos
- `ss` = segundos
- `ms` = milisegundos (separados por una coma)

## Configuración

El script utiliza las rutas relativas al directorio actual. Asegúrate de que los archivos se encuentren en el mismo directorio o especifica rutas correctas.

```python
csv_path = "tiempos.csv"                # Ruta al archivo CSV
output_folder = "VIDEOS"               # Carpeta donde se guardarán los clips cortados
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
- **Nombre Guardado**: `video1`
- **Category**: `crash`
- **Start Time**: `00:00:11,10`
- **End Time**: `00:00:17,15`
- **Edited Video File**: `dash_cam_part22_1`

#### Salida:
- Los archivos se guardarán de la siguiente manera:
  - **Audio**: `VIDEOS/crash/audio/nena_dash_cam_part22_1.mp3`
  - **Video**: `VIDEOS/crash/video/nena_dash_cam_part22_1.mp4`

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
