from PyQt6.QtCore import QThread, pyqtSignal
import socket
import time
import datetime
from logger import log
import threading
from message import Message


class UdpSender(QThread):
    _queue = []
    sent = pyqtSignal(Message)


    def __init__(self):
        super().__init__()
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        # self.addres = ('localhost', 9900)
        self.running = False
        self.lock = threading.Lock()

    def run(self):
        log.i("Сэндер запущен")
        self.running = True
        msg : Message = None
        while self.running:
            if len(self._queue) > 0:
                self.lock.acquire()
                msg = self._queue.pop()
                self.lock.release()
                msg.time = datetime.datetime.now().strftime('%H:%M:%S')
                string_to_send = msg.toJson()
                if msg.type in ("public", "service_request"):
                    adr = ('255.255.255.255', 9900)
                    self.socket.sendto(string_to_send.encode(), adr)
                elif msg.senderIp:
                    adr = (msg.senderIp, 9900)
                    self.socket.sendto(string_to_send.encode(), adr)
                self.sent.emit(msg)
            else:
                time.sleep(0.025)


    def send(self, msg : Message):
        self.lock.acquire()
        self._queue.append(msg)
        self.lock.release()

    def stop(self):
        self.running = False
        super().stop()
