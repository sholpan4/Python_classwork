from PyQt6.QtCore import QThread, pyqtSignal
from logger import log


class DataStorage(QThread):
    username = None
    ready = pyqtSignal()
    authOk = pyqtSignal(str)
    authBad = pyqtSignal(str)

    def run(self):
        log.i("Дата сторэйдж запущен")
        self.ready.emit()

        

    def auth(self, username):
        self.username = username
        self.authOk.emit(username)