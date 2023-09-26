from PyQt6.QtCore import QObject, pyqtSignal
from logger import log

# тут будет контроллер
class Controller(QObject):
    switchWindow = pyqtSignal(str, str)
    def login(self, username):
        if username:
            self.switchWindow.emit('MainWindow', username)  

    def message_received(self, message_text, message_type):
        log.d(f'mess poluchen: {message_text} tip: {message_type}')