import os
from windowError import Error
from moviepy import VideoFileClip

class Transform:
    
    def __init__(self, output_path, title, subtype, save):
        self.output_path = output_path
        self.title = title
        self.subtype = subtype
        self.st = save
    
    # Seleccionamos el archivo mp4 y creamos(seleccionamos) el archivo mp3
    def getArchive(self):
        save_as = self.st.save_file(self.title, "mp3")
        if save_as != None: # Si no hay ruta de descarga no se transforma
            self.mp4_file = os.path.join(self.output_path, f'{self.title}.{self.subtype}')
            self.mp3_file = os.path.join(save_as[0], save_as[1])
    
    # Convertimos el archivo a mp3 y borramos el mp4
    def transform(self):
        self.getArchive()
        try:
            audio = VideoFileClip(self.mp4_file)
            audio.audio.write_audiofile(self.mp3_file)
            audio.close()
        except:
            self.error = Error()
            self.error.view("Has cancelado la descarga")
            self.error.show()
        finally:
            os.remove(f"{self.output_path}/{self.title}.{self.subtype}") # Como siempre se va a descargar en la carpeta vid_cache se tiene que borrar aunque pete