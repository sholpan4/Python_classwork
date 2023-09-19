from PyQt6.QtCore import QThread
from PyQt6.QtWidgets import *
from PyQt6 import uic
from PyQt6.QtCore import pyqtSignal

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/main.ui", self)  #load_ui


    #     self.ButtonSearch = self.findChild(sth)
    #     self.ButtonSearch.button.clicked.connect(self.printButtonPresses)

    # def printButtonPress(self):
    #     on_click()

class Gui(QThread):
    sendMessage = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.window = MainWindow()
        self.window.show()

    def run(self):
        print("Gui is running")
        button = self.window.findChild(QPushButton, "pushButton") #name from main.ui
        button.clicked.connect(self.send_message)
        

    def send_message(self):
        print("Button pressed")
        text = self.window.findChild(QTextEdit, "MessageToSend")
        message = text.toPlainText()
        self.sendMessage.emit(message)
        text.clear()
        
        