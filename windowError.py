from PyQt6.QtWidgets import QMessageBox, QPushButton
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import Qt

class Error(QMessageBox):
    
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Error")
        self.setFixedSize(450, 300)
        icon = QIcon("IMG/icono.ico")
        self.setWindowIcon(icon)
        
    def view(self, message):
        self.setText(f"<h2>{message}</h2>")
        
        img = QPixmap("IMG/error.png").scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio) # Escalamos la imagen
        self.setIconPixmap(img)
        
        button = QPushButton("Ok")
        button.clicked.connect(self.close)
        self.addButton(button, QMessageBox.ButtonRole.AcceptRole) # Añadimos el boton y le damos el rol de aceptar la acción