from windowOption import WindowOption
from windowError import Error
from download import Download
from PyQt6.QtWidgets import QMainWindow, QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton, QRadioButton, QButtonGroup
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("YoutubeDownloader")
        self.setFixedSize(450, 300)
        icon = QIcon("IMG/icono.ico")
        self.setWindowIcon(icon)
        
        self.widget = QWidget()
        self.label = QLabel()
        self.layoutV = QVBoxLayout()
        
    def menu(self):
        # Imagen
        img = QPixmap("./IMG/yotubedownloader.png")  # Cargar la imagen
        label_img = QLabel()  # Crear un QLabel
        label_img.setPixmap(img)  # Asignar el QPixmap al QLabel
        label_img.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layoutV.addWidget(label_img)
        
        # Los botones para seleccionar que quieres descargar
        self.group = QButtonGroup()
        r1 = QRadioButton("Descargar Audio")
        r2 = QRadioButton("Descargar Video")
        r3 = QRadioButton("Descargar Playlist")
        
        # Agrego todos los botones a un mismo grupo
        self.group.addButton(r1)
        self.group.addButton(r2)
        self.group.addButton(r3)

        # Establezco ids opcionales para cada botón en el grupo (opcional)
        self.group.setId(r1, 1)
        self.group.setId(r2, 2)
        self.group.setId(r3, 3)
        
        self.layoutV.addWidget(r1)
        self.layoutV.addWidget(r2)
        self.layoutV.addWidget(r3)
        
        # El cuadro de texto en el que pones la url del video
        self.url = QLineEdit()
        self.url.setPlaceholderText("Pon la url del viedo que quieres descargar")
        self.url.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.layoutV.addWidget(self.url)
        
        # El boton para descargar el video con la opcion seleccionada
        buscar = QPushButton("Descargar")
        buscar.clicked.connect(self.selectedOption)
        
        self.layoutV.addWidget(buscar)
        
        self.widget.setLayout(self.layoutV) # Añadimos todos los elementos al layout principal
        self.setCentralWidget(self.widget) # Centramos todo el layout
    
    # Para diferenciar que opcion ha escogido el usuario    
    def selectedOption(self):
        buttonId = self.group.checkedId()  # Obtiene el ID del botón seleccionado

        if buttonId != -1:
            url = self.url.text()
            self.url.clear()
            try:
                self.download = Download(url)
                self.wp = WindowOption(url)
                
                match buttonId:
                    case 1:
                        self.download.audio()
                    case 2:
                        self.windowOp(buttonId)
                    case 3:
                        msg = "!!! IMPORTANTE, Escoge bien las opciones del video ya que todos se van a descargar con la misma y puede que no todos los videos tengan esas opciones"
                        self.windowOp(buttonId, msg)
            except:
                self.error = Error()
                self.error.view("La url que has puesto es incorrecta o ya no existe")
                self.error.show()
        else:
            self.error = Error()
            self.error.view("Tienes que escoger una de las opciones para continuar")
            self.error.show()

    def windowOp(self, buttonId, message = ""):
        # Captura la señal de la ventana(como un return) para evitar que el programa siga sin esperar
        self.wp.optionsSelected.connect(lambda extension, resolution: self.otherDownload(buttonId, extension, resolution))
        self.wp.opWindow(message)
        self.wp.show()

    def otherDownload(self, buttonId, extension, resolution):
        if buttonId == 2:
            self.download.video(extension, resolution)
        elif buttonId == 3:
            self.download.playlists(extension, resolution)
