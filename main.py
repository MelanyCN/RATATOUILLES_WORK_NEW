from functions import cortar_videos

# Ruta base donde se encuentran los archivos
PATH = "/home/melany/TRABAJO_JASON/codigo_video_new/"

# Especificar las rutas del archivo CSV y carpeta de salida
csv_path = PATH + "tiempos.csv"                 # Ruta del archivo CSV con los datos de los clips
output_folder = PATH + "videos_prueba"          # Carpeta donde se guardarán los clips cortados

# Ejecutar el programa para cortar los clips
cortar_videos(csv_path, output_folder, PATH)
