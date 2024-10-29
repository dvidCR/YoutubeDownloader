import os
from PyQt6.QtWidgets import QFileDialog, QDialog
from PyQt6.QtGui import QIcon

class saveState(QDialog):
    
    def __init__(self):
        super().__init__()
        
        icon = QIcon("IMG/icono.ico")
        self.setWindowIcon(icon)
        
    # Función para abrir la ventana "Guardar como"
    def save_file(self, fileName, extension):
        programDir = os.getcwd() # Guardar la ruta del programa
        
        # Cambiamos a la carpeta descargas para que se abra como punto de guardado por defecto
        os.chdir(os.path.join(os.path.expanduser("~"), "Downloads"))
        
        # Mostrar la ventana de "Guardar como" y obtener la ruta seleccionada
        file_name, _ = QFileDialog.getSaveFileName(
            self,
            "Guardar archivo como",  # Título de la ventana
            fileName,  # Nombre por defecto
            f"Archivos (*.{extension});; Todos los archivos (*.*)",  # Tipos de archivo que aparecen
        )
        
        os.chdir(programDir) # Vovlemos a la carpeta del programa para evitar errores
        
        if not file_name: # Si le das a cancelar devuelve nada
            return None
        
        # Devuelve la ruta en la que se ha guardado el archivo y el nombre del archivo
        return os.path.dirname(file_name), os.path.basename(file_name)