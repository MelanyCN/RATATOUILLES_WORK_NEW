import pandas as pd
import os
from moviepy.video.io.VideoFileClip import VideoFileClip

def cortar_videos(csv_path, output_folder):
    """
    Corta un video en múltiples clips basados en los tiempos de inicio y fin
    especificados en un archivo CSV, organizados en subcarpetas según la categoría (Category)
    y con el prefijo del usuario (User) en el nombre del archivo.

    Args:
        video_path (str): Ruta del video principal que se va a cortar.
        csv_path (str): Ruta del archivo CSV que contiene los tiempos y nombres de los clips.
        output_folder (str): Carpeta donde se guardarán los clips cortados.

    Returns:
        None
    """
    # Leer el archivo CSV, saltando las filas iniciales irrelevantes
    datos = pd.read_csv(csv_path, skiprows=12)

    # Rellenar celdas vacías con el último valor válido
    datos = datos.ffill()

    # Filtrar columnas relevantes
    datos = datos[["User", "Nombre Guardado", "Edited Video File", "Category", "Start Time", "End Time"]].dropna()

    # Iterar sobre cada fila
    for index, row in datos.iterrows():
        usuario = row["User"].strip().lower()           # Usuario en minúsculas
        video_name = row["Nombre Guardado"].strip()     # Nombre del video a cortar
        nombre_clip = row["Edited Video File"]          # Nombre base del clip
        categoria = row["Category"].strip().lower()     # Categoría en minúsculas
        tiempo_inicio = row["Start Time"]         # Tiempo de inicio (hh:mm:ss,ms)
        tiempo_fin = row["End Time"]              # Tiempo de fin (hh:mm:ss,ms)

        # Convertir tiempos al formato de segundos
        inicio = convertir_tiempo_a_segundos(tiempo_inicio)
        fin = convertir_tiempo_a_segundos(tiempo_fin)

        # Crear carpetas para categoría, audio y video
        categoria_folder = os.path.join(output_folder, categoria)
        os.makedirs(categoria_folder, exist_ok=True)

        audio_folder = os.path.join(categoria_folder, "audio")
        os.makedirs(audio_folder, exist_ok=True)

        video_folder = os.path.join(categoria_folder, "video")
        os.makedirs(video_folder, exist_ok=True)

        # Construir rutas de salida
        output_video_path = os.path.join(video_folder, f"{usuario}_{nombre_clip}.mp4")
        output_audio_path = os.path.join(audio_folder, f"{usuario}_{nombre_clip}.mp3")

        # Construir la ruta del video principal
        video_path = f"{video_name}.mp4"

        with VideoFileClip(video_path) as video:
            # Cortar el video
            clip = video.subclipped(inicio, fin)

            # Guardar el audio
            clip.audio.write_audiofile(output_audio_path)
            print(f"Audio guardado en: {output_audio_path}")

            # Guardar el video
            clip.write_videofile(output_video_path, codec="libx264", audio_codec="aac")
            print(f"Video guardado en: {output_video_path}")

def convertir_tiempo_a_segundos(tiempo):
    """
    Convierte un tiempo en formato hh:mm:ss,ms a segundos.

    Args:
        tiempo (str): Tiempo en formato hh:mm:ss,ms (e.g., "00:01:12,500").

    Returns:
        float: Tiempo convertido a segundos (con milisegundos como decimal).
    """
    horas, minutos, resto = tiempo.split(':')
    segundos, milisegundos = resto.split(',')
    return int(horas) * 3600 + int(minutos) * 60 + int(segundos) + int(milisegundos) / 1000
