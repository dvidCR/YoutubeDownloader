# Este codigo es para mantenerlo en modo script, no tiene nada que ver con la interfaz grafica que se ejecuta

import os
from pytube import YouTube, Playlist
from moviepy import VideoFileClip

def quitar_caracteres(title):
    name = title.replace('/', '')
    name = name.replace("'", '')
    name = name.replace('"', '')
    name = name.replace("|", '')
    name = name.replace(".", '')
    name = name.replace(":", '')
    name = name.replace(",", '')
    return name
    
def descargar_audio(url, output_path):
    os.system("cls")
    try:
        yt = YouTube(url)
        title = quitar_caracteres(yt.title)
        print(f"Descargando el audio {title}...")
        video = yt.streams.filter(file_extension = "mp4").first()
        video.download(output_path = output_path)
        mp4_file = os.path.join(output_path, f'{title}.{video.subtype}')
        mp3_file = os.path.join(output_path, f'{title}.mp3')
        audio = VideoFileClip(mp4_file)
        audio.audio.write_audiofile(mp3_file)
        audio.close()
        os.remove(mp4_file)
        print(f"{yt.title} descargado exitosamente")
    except Exception as e:
        print(f"No se pudo descargar el audio por {e}")

def descargar_video(url, output_path):
    os.system("cls")
    try:
        yt = YouTube(url)
        print(f"Descargando el video {yt.title}...")
        yt.streams.filter(file_extension = "mp4").first().download(output_path = output_path)
        #yt.streams.get_highest_resolution().download(output_path = output_path)
        #prueba = yt.streams.filter(only_audio = True, file_extension="webm", bitrate="50kbps")
        #print(prueba)
        print(f"{yt.title} descargado exitosamente")
    except Exception as e:
        print(f"No se pudo descargar el video por {e}")
        
def descargar_playlist(url, output_path):
    os.system("cls")
    try:
        p = Playlist(url)
        print(f"Descargando los videos de la playlist {p.title}")
        for video in p.videos:
            video.streams.filter(file_extension = "mp4").first().download(output_path = output_path)
        print(f"La playlist {p.title} descargado exitosamente")
    except Exception as e:
        print(f"No se pudo descargar la playlist por {e}")
        
def main():
    while(True):
        os.system("cls")
        print("Bienvenido a YoutubeDownloader v1.0")
        op = int(input(("\nQue quieres hacer:\n  1. Descargar audio de Youtube\n  2. Descarga los videos de una playlist de Youtube\n  3. Descargar un video de Youtube\n  : ")))

        if op == 2:
            url = input("Introduze la URL de la playlist que te quieras descargar: ")
        else:
            url = input("Introduce la URL del video que quieras descargar: ")
            
        file = input("En que carpeta lo quieres guardar: ")
        
        project_directory = os.path.dirname(os.path.abspath(__file__))
        output_path = os.path.join(project_directory, file)
        
        print(f"La carpeta del projecto es {project_directory}")
        print(f"La carpeta donde se va a descargar el video es en {output_path}")
        
        match (op):
            case 1:
                descargar_audio(url, output_path)
            case 2:
                descargar_playlist(url, output_path)
            case 3:
                descargar_video(url, output_path)
        
        os.system("pause")
    
        exit = input("¿Quieres salir de la aplicacion?(y/n): ")
        
        if exit.lower() == "y":
            return False
    
if __name__ == "__main__":
    main()