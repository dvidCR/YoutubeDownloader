from saveState import saveState
from transform import Transform
from windowError import Error
from pytube import YouTube, Playlist

# TODO Terminar codigo para descargar los videos, !!IMPORTANTE Recuerda que al principio el audio lo tienes que descargar en mp4 pero con get_only_audio
class Download:
    
    def __init__(self, url):
        self.yt = YouTube(url)
        self.playlist = Playlist(url)
        
        self.title = self.removeCharactersTitle()
        self.image = self.yt.thumbnail_url
        
        self.st = saveState()
        
    def removeCharactersTitle(self):
        # Quitamos los caracteres marcados para evitar errores a la hora de transformar el video en mp3
        title = self.yt.title.replace('/', '')
        title = title.replace('*', '')
        title = title.replace("'", '')
        title = title.replace('"', '')
        title = title.replace("|", '')
        title = title.replace(".", '')
        title = title.replace(":", '')
        title = title.replace(",", '')
        
        return title
        
    def audio(self):
        output_path = "./vid_cache" # Para guardar el video mp4 en una carpeta fija
        getAudio = self.yt.streams.filter(file_extension="mp4").first()
        getAudio.download(output_path=output_path)
        Transform(output_path, self.title, getAudio.subtype, self.st).transform()
    
    def video(self, ex, rs):
        try:
            output_path = self.st.save_file(self.title, ex)
            if output_path != None: # Si no hay ruta de descarga no se descarga el archivo
                getVideo = self.yt.streams.filter(file_extension = ex, res = rs).first()
                # El output_path[0] es para marcar la ruta donde se va a guardar, y el otro indica el nombre que le queremos dar
                getVideo.download(output_path=output_path[0], filename=output_path[1])
        except ValueError as e:
            self.error = Error()
            self.error.view(e)
            self.error.show()
    
    def playlists(self, ex, rs):
        # Recorremos la playlist entera para descargar los videos de uno en uno
        for video in self.playlist.videos:
            try:
                output_path = self.st.save_file(video.title, ex)
                if output_path != None:
                    vidPlaylist = video.streams.filter(file_extension = ex, res = rs).first()
                    vidPlaylist.download(output_path=output_path[0], filename=output_path[1])
            except ValueError as e:
                self.error = Error()
                self.error.view(e)
                self.error.show()