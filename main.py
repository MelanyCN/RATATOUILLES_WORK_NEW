from functions import cortar_videos

# Especificar las rutas del archivo CSV y carpeta de salida
csv_path = "tiempos.csv"                 # Ruta del archivo CSV con los datos de los clips
output_folder = "VIDEOS"          # Carpeta donde se guardarán los clips cortados

# Ejecutar el programa para cortar los clips
cortar_videos(csv_path, output_folder)
