from pytube import YouTube
import os

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
        
def main():
    url = input("Introduce la URL del video que quieras descargar: ")
    file = input("En que carpeta lo quieres guardar: ")
    
    project_directory = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(project_directory, file)
    
    print(f"La carpeta del projecto es {project_directory}")
    print(f"La carpeta donde se va a descargar el video es en {output_path}")
    
    descargar_video(url, output_path)
    
if __name__ == "__main__":
    main()