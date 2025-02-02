import os
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
myUI_application = "tutoriel.ui"
# template for UI
class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        ui_path = os.path.join(os.path.dirname(__file__), myUI_application)
        uic.loadUi(ui_path, self)


if __name__ == "__main__":
    app = QApplication([])
    window = MainApp()
    window.show()
    app.exec()
