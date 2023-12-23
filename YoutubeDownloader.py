import subprocess
import sys
import os

def instalar_pytube():
    try:
        # Intenta importar pytube para verificar si ya está instalado
        import pytube
    except ImportError as e:
        print(e)
        install = input("¿Quieres instalar la libreria?(y/n):")
        if install == "y" or "Y":
            subprocess.check_call([sys.executable, "-m", "pip", "install", "pytube"])
            print("pytube instalado correctamente.")
        else:
            print("Para poder descargar algo necesitas descargar la libreria.")    
    return "yes"

if instalar_pytube() == "yes":
    from pytube import YouTube
    from pytube import Playlist
    
def descargar_video(url, output_path):
    try:
        yt = YouTube(url)
        print(f"Descargando el video {yt.title}...")
        yt.streams.get_audio_only().download(output_path = output_path)
        #yt.streams.get_highest_resolution().download(output_path = output_path)
        #prueba = yt.streams.filter(only_audio = True, file_extension="webm", bitrate="50kbps")
        #print(prueba)
        print(f"{yt.title} descargado exitosamente")
    except Exception as e:
        print(f"No se pudo descargar el video por {e}")
        
def descargar_playlist(url, output_path):
    try:
        p = Playlist(url)
        print(f"Descargando los videos de la playlist {p.title}")
        for video in p.videos:
            video.streams.first().download(output_path = output_path)
        print(f"La playlist {p.title} descargado exitosamente")
    except Exception as e:
        print(f"No se pudo descargar la playlist por {e}")
        
def main():
    while(True):
        print("Bienvenido a YoutubeDownloader v1.0")
        op = int(input(("\nQue quieres hacer:\n  1. Descargar Video de Youtube\n  2. Descarga los videos de una playlist de Youtube\n: ")))
        if op == 1:
            url = input("Introduce la URL del video que quieras descargar: ")
        if op == 2:
            url = input("Introduze la URL de la playlist que te quieras descargar: ")
            
        file = input("En que carpeta lo quieres guardar: ")
        
        project_directory = os.path.dirname(os.path.abspath(__file__))
        output_path = os.path.join(project_directory, file)
        
        print(f"La carpeta del projecto es {project_directory}")
        print(f"La carpeta donde se va a descargar el video es en {output_path}")
        
        if op == 1:
            descargar_video(url, output_path)
        if op == 2:
            descargar_playlist(url, output_path)
        
        os.system("pause")
    
        exit = input("¿Quieres salir de la aplicacion?(y/n): ")
        
        if exit == "y" or "Y":
            return False
    
if __name__ == "__main__":
    instalar_pytube()
    main()