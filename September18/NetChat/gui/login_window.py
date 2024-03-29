from logger import log
from PyQt6.QtWidgets import *
from PyQt6 import uic
from PyQt6.QtCore import pyqtSignal


class LoginWindow(QDialog):
    loginUser = pyqtSignal(str, str)

    def __init__(self):
        super().__init__()
        uic.loadUi("gui/login_window.ui", self)
        
    def show(self):
        super().show()
        button = self.findChild(QPushButton, "Login")
        button.clicked.connect(self.login_user)

    def login_user(self):
        name_input = self.findChild(QLineEdit, "Nickname")
        user_name = name_input.text()
        password_input = self.findChild(QLineEdit, "Passowrd")
        user_password = password_input.text()
        if user_name and user_password:
            self.loginUser.emit(user_name, user_password)
            log.i(f"Пользователь '{user_name}' авторизован")