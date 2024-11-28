import pandas as pd
import os
from moviepy.video.io.VideoFileClip import VideoFileClip

def cortar_videos(video_path, csv_path, output_folder):
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
    # Leer el archivo CSV, saltando las filas irrelevantes iniciales (e.g., encabezados no usados)
    datos = pd.read_csv(csv_path, skiprows=12)  # Saltar las primeras 12 filas para llegar a los datos relevantes

    # Rellenar celdas vacías con el último valor válido
    datos.fillna(method="ffill", inplace=True)

    # Filtrar las columnas relevantes: nombre del archivo, tiempo de inicio y tiempo de fin
    datos = datos[["User", "Category", "Edited Video File", "Start Time (sec)", "End Time (sec)"]].dropna()

    # Iterar sobre cada fila del archivo CSV para procesar los tiempos y nombres de los clips
    for index, row in datos.iterrows():
        usuario = row["User"].strip().lower()           # Usuario que será parte del nombre del archivo
        categoria = row["Category"].strip().lower()     # Categoría del video ("crash" o "no_crash")
        nombre_clip = row["Edited Video File"]          # Nombre con el que se guardará el clip
        tiempo_inicio = row["Start Time (sec)"]         # Tiempo de inicio del clip (en formato hh:mm:ss,ms)
        tiempo_fin = row["End Time (sec)"]              # Tiempo de fin del clip (en formato hh:mm:ss,ms)

        # Convertir los tiempos al formato de segundos que acepta MoviePy
        inicio = convertir_tiempo_a_segundos(tiempo_inicio)
        fin = convertir_tiempo_a_segundos(tiempo_fin)

        # Crear la subcarpeta correspondiente a la categoría
        categoria_folder = os.path.join(output_folder, categoria)
        os.makedirs(categoria_folder, exist_ok=True)

        # Construir el nombre completo del archivo de salida
        output_filename = f"{usuario}_{nombre_clip}.mp4"
        output_path = os.path.join(categoria_folder, output_filename)

        # Abrir el video original para cortar el segmento correspondiente
        with VideoFileClip(video_path) as video:
            # Cortar el video desde 'inicio' hasta 'fin'
            clip = video.subclipped(inicio, fin)
            
            # Guardar el clip cortado en la carpeta de salida con el nombre especificado
            clip.write_videofile(output_path, codec="libx264", audio_codec="aac")  # Guardar con compresión H.264 y audio AAC
            
            # Informar al usuario que el segmento fue guardado correctamente
            print(f"Segmento {index+1} guardado en: {output_path}")

def convertir_tiempo_a_segundos(tiempo):
    """
    Convierte un tiempo en formato hh:mm:ss,ms a segundos.

    Args:
        tiempo (str): Tiempo en formato hh:mm:ss,ms (e.g., "00:01:12,500").

    Returns:
        float: Tiempo convertido a segundos (con milisegundos como decimal).
    """
    # Separar las horas, minutos y el resto del tiempo (segundos,milisegundos)
    horas, minutos, resto = tiempo.split(':')
    segundos, milisegundos = resto.split(',')
    
    # Calcular el total de segundos incluyendo milisegundos
    return int(horas) * 3600 + int(minutos) * 60 + int(segundos) + int(milisegundos) / 1000
