from PyQt6.QtCore import QThread, pyqtSignal
from logger import log


class DataStorage(QThread):
    username = None
    password = None
    ready = pyqtSignal()
    authOk = pyqtSignal(str)
    authBad = pyqtSignal(str)

    def run(self):
        log.i("Дата сторэйдж запущен")
        self.ready.emit()

        

    def auth(self, username, password):
        with open("data_storage/user.db", encoding="utf-8") as user_fl:
            user_data = user_fl.read().split()
        #create hash
        
        if username == user_data[0] and password == user_data[1]:
            self.username = username
            self.authOk.emit(username)
        else:
            self.authBad.emit("Not corrected username or password!")
