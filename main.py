import sys
from ui import MainWindow
from PyQt6.QtWidgets import QApplication

app = QApplication(sys.argv)
execute = MainWindow()

if __name__ == "__main__":
    execute.menu()
    execute.show()
    sys.exit(app.exec())