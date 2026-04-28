# Este codigo es para mantenerlo en modo script, no tiene nada que ver con la interfaz grafica que se ejecuta

from yt_dlp import YoutubeDL

import os

FFMPEG_BASE = r'.\ffmpeg-8.1-essentials_build\bin'
DENO_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'deno')

os.environ['PATH'] = DENO_PATH + os.pathsep + os.environ['PATH']

# def quitar_caracteres(title):
#     name = title.replace('/', '')
#     name = name.replace("'", '')
#     name = name.replace('"', '')
#     name = name.replace("|", '')
#     name = name.replace(".", '')
#     name = name.replace(":", '')
#     name = name.replace(",", '')
#     return name
        
def main():
    while(True):
        os.system("cls")
        print("Bienvenido a YoutubeDownloader v1.0")
        op = int(input(("\nQue quieres hacer:\n  1. Descargar audio de Youtube\n  2. Descargar un video de Youtube\n  3. Descarga los videos de una playlist de Youtube\n  : ")))
        
        if op == 3:
            url = input("Introduze la URL de la playlist que te quieras descargar: ")
        else:
            url = input("Introduce la URL del video que quieras descargar: ")

        file = input("En que carpeta lo quieres guardar: ")
        
        project_directory = os.path.dirname(os.path.abspath(__file__))
        output_path = os.path.join(project_directory, file)
        
        print(f"La carpeta del projecto es {project_directory}")
        print(f"La carpeta donde se va a descargar el video es en {output_path}")

        ydl_opts = {
            'ffmpeg_location': os.path.join(FFMPEG_BASE, 'ffmpeg.exe'),
            'ffprobe_location': os.path.join(FFMPEG_BASE, 'ffprobe.exe'),
            'extractor_args': {
                'youtube': {
                    'js_runtimes': [f'{DENO_PATH}\\deno.exe'],
        }
    }
        }
        
        match op:
            case 1:
                descargar_audio(ydl_opts, output_path, url)
            case 2:
                descargar_video(ydl_opts, output_path, url)
            case 3:
                descargar_playlist(ydl_opts, output_path, url)
            case _:
                print("Opción no válida.")
        
        os.system("pause")
            
        exit = input("¿Quieres salir de la aplicacion?(y/n): ")
        
        if exit.lower() == "y":
            return False

def descargar_audio(ydl_opts, output_path, url):
    ydl_opts.update({
        'format': 'm4a/bestaudio/best',
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        # ℹ️ See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
        'postprocessors': [{  # Extract audio using ffmpeg
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'm4a',
        }]
    })

    with YoutubeDL(ydl_opts) as ydl:
           ydl.download([url])

def descargar_video(ydl_opts, output_path, url):
    ydl_opts.update({
        'format': '(bv*[ext=mp4][height<=1080]+ba[ext=m4a])/(bv*[ext=webm][height<=1080]+ba[ext=webm])/best',
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
    })
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def descargar_playlist(ydl_opts, output_path, url):
    ydl_opts.update({
        'format': '(bv*[ext=mp4][height<=1080]+ba[ext=m4a])/(bv*[ext=webm][height<=1080]+ba[ext=webm])/best',
        'outtmpl': os.path.join(output_path, '%(playlist_index)s - %(title)s.%(ext)s'),
        'ignoreerrors': True,
        'yes_playlist': True,
    })
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    main()