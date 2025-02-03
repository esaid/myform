import os
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

myUI_application = "tutoriel.ui"


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(myUI_application, self)  # Charge le fichier UI
        # Connecte le bouton à la boîte de message
        self.pushButton.clicked.connect(self.show_message)

    def show_message(self):
        msg = QMessageBox()
        msg.setWindowTitle("Information")
        msg.setText("Ceci est un message d'alerte !")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.exec_()


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
