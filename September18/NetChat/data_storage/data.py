from PyQt6.QtCore import QThread
from logger import log


class DataStorage(QThread):
    username = None

    def run(self):
        log.i("Дата сторэйдж запущен")

    def auth(self, username):
        self.username = username