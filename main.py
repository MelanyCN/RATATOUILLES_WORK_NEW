from functions import cortar_videos

# Ruta base donde se encuentran los archivos
path = "/home/melany/TRABAJO_JASON/codigo_video_new/"

# Especificar las rutas del video principal, archivo CSV y carpeta de salida
video_path = path + "video_carros.mp4"          # Ruta del video principal
csv_path = path + "tiempos.csv"                 # Ruta del archivo CSV con los datos de los clips
output_folder = path + "videos_prueba"          # Carpeta donde se guardarán los clips cortados

# Ejecutar el programa para cortar los clips
cortar_videos(video_path, csv_path, output_folder)
