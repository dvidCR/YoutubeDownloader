import requests
from option import Options
from PyQt6.QtWidgets import QWidget, QLabel, QHBoxLayout, QVBoxLayout, QPushButton, QComboBox
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import pyqtSignal, Qt, QRect

class WindowOption(QWidget):
    
    optionsSelected = pyqtSignal(str, str)
    
    def __init__(self, url):
        super().__init__()
        
        self.opt = Options(url)
        self.opt.getTitle()
        self.opt.getImage()
        self.opt.getInfo()
        
        self.setWindowTitle("YoutubeDownloader")
        icon = QIcon("IMG/icono.ico")
        self.setWindowIcon(icon)
        
        self.label = QLabel()
        self.layoutH = QHBoxLayout()
        self.layoutV = QVBoxLayout()
        
    def opWindow(self, message = ""):
        label = QLabel(f'<h1><b>{self.opt.dic["title"]}</b></h1>')
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layoutV.addWidget(label)
        
        img_label  = QLabel(self)
        pixmap = QPixmap()
        request = requests.get(self.opt.dic["image"])
        pixmap.loadFromData(request.content)
        img_label.setPixmap(pixmap)
        img_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layoutV.addWidget(img_label)
        
        # Este mensaje solo aparecera cuando descarguemos una playlist
        adv = QLabel(f"<h3>{message}</h3>")
        adv.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layoutV.addWidget(adv)

        self.opResolution = QComboBox()
        self.opExtension = QComboBox()
        
        self.addResolution()
        self.opExtension.currentIndexChanged.connect(self.changeExtension)
        
        self.layoutH.addWidget(self.opExtension)
        self.layoutH.addWidget(self.opResolution)
        
        self.layoutV.addLayout(self.layoutH)
        
        button = QPushButton("Descargar")
        button.clicked.connect(self.sendOptions)
        
        self.layoutV.addWidget(button)
        
        self.setLayout(self.layoutV)
    
    def addResolution(self):
        for i in range(0, len(self.opt.dic) - 2):
            extension = self.opt.dic[i].get("mime_type")
            if self.opExtension.findText(extension) == -1:
                self.opExtension.addItem(extension)
                
        self.changeExtension()
       
    def changeExtension(self):
        self.opResolution.clear()
        
        for i in range(0, len(self.opt.dic) - 2):
            extension = self.opt.dic[i].get("mime_type")
            resolution = self.opt.dic[i].get("res")
            
            if self.opExtension.currentText() == extension and resolution != None and self.opResolution.findText(resolution) == -1:
                self.opResolution.addItem(resolution)
        
    def sendOptions(self):
        extension = self.opExtension.currentText()
        resolution = self.opResolution.currentText()
        self.optionsSelected.emit(extension, resolution)
        self.close()