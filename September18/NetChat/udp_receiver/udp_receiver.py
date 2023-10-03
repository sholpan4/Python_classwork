from PyQt6.QtCore import QThread, pyqtSignal
import socket
from logger import log



class UdpReceiver(QThread):
    message = pyqtSignal(str, str)
    hello = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.addres = ('localhost', 9900)
        self.running = False
        

    def run(self):
        log.i("Ресивер запущен")
        self.socket.bind(self.addres)
        self.running = True
        while self.running:
            data, addr = self.socket.recvfrom(4096)
            message = data.decode(encoding= "utf-8")
            log.d(f'получено сообщение от {addr}: {message}')
            self.message.emit(message, 'public')    

    def stop(self):
        self.running = False
        super().stop()
