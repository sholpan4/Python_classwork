from logger import log
from PyQt6.QtCore import QObject
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QWidget
from .main_window import MainWindow
from .login_window import LoginWindow


class Gui(QObject):
    sendMessage = pyqtSignal(str)
    loginUser = pyqtSignal(str)
    window : QWidget = None
    
    def __init__(self):
        super().__init__()
        self.running = False
        self.set_window('LoginWindow')

    def start(self):
        self.run()

    def run(self):
        log.i("Интерфэйс запущен")
        self.window.show()
        self.running = True

    def set_window(self, window_name, username=None):
        if self.window is not None:
            self.window.hide()
        match window_name:
            case 'MainWindow':
                self.window = MainWindow(username)
                self.window.sendMessage.connect(self.sendMessage)
            case 'LoginWindow':
                self.window = LoginWindow()
                self.window.loginUser.connect(self.loginUser)
            case _:
                log.e('ERROR', window_name)
        if self.running:
            self.run()
        

