from PyQt6.QtCore import *
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
        self.running = None
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
        
        # show message() read plus show


class Gui(QObject):
    sendMessage = pyqtSignal(str)
    loginUser = pyqtSignal(str)
    window : QWidget = None

    def __init__(self):
        super().__init__()
        self.set_window('LoginWindow')


    def run(self):
        pass

    def set_window(self, window_name, username=None):
        if self.window is not None:
            self.window.hide()

        if window_name == 'MainWindow':
            self.window = MainWindow()
            self.window.sendMessage.connect(self.sendMessage)
        elif window_name == 'LoginWindow':
            self.window = LoginWindow()
            self.window.loginUser.connect(self.loginUser)
