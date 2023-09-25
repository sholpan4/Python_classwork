from PyQt6.QtCore import QThread

class DataStorage(QThread):
    username = None
    # def run(self):
    pass

    def auth(self, username):
        self.username = username