from download import Download

class Options(Download):
    
    def __init__(self, url):
        super().__init__(url)
        self.diccionario()

    def removeCharactersStreams(self, streams):
        streams = str(streams) # Convierto la lista en un strig para quitarle los caracteres especiales string
        streams = streams.replace("=", " ")
        streams = streams.replace('"', '')
        streams = streams.replace("[<Stream: ", "")
        streams = streams.replace("<Stream: ", "")
        streams = streams.replace(">,", "")
        streams = streams.replace(">]", "")
        streams = streams.replace(", itag", "itag")
        streams = streams.replace("video/", "")
        streams = streams.replace("audio/", "")
        
        self.addStreams(streams.split(" "))
        
    def addStreams(self, streams):
        cont = 0
        temp = None
        for i in range(0, len(streams), 2):  # Iteramos de dos en dos (clave y valor)
            key, value = streams[i], streams[i+1]

            if key == 'itag':  # Si encontramos un nuevo itag
                temp = cont  # Usamos el contador como clave
                self.dic[temp] = {}  # Crear una nueva entrada para el itag
                cont += 1
            elif key == 'mime_type' or key == 'res': # Añado al diccionario solo los elementos que me interesa                
                if temp is not None:  # Si ya tenemos un valor en temp
                    self.dic[temp][key] = value  # Agregar atributos al itag actual
    
    def diccionario(self):
        self.dic = {
            
        }

    def getTitle(self):
        self.dic.update({"title": self.title}) # Añadimos el titulo del video al diccionario
    
    def getImage(self):
        self.dic.update({"image": self.image}) # Añadimos la url de la imagen del video al diccionario
    
    def getInfo(self):
        # Pedinos que nos muestre los flujos adaptativos que tenga el video en cuestion
        ''' En realidad para que el video no se descarge corrupto tiene que ser el flujo en progresivo,
            pero uso el adaptativo ya que muesra todas las resolciones en la que esta el video en verdad '''
        self.removeCharactersStreams(self.yt.streams.filter(adaptive=True))