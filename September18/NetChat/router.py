from PyQt6.QtCore import QObject
from data_storage import DataStorage
from gui import Gui
from udp_receiver import UdpReceiver
from udp_sender import UdpSender

class Router(QObject):
    def __init__(self):
        super().__init__()
        self.data_storage = DataStorage()
        self.gui = Gui()
        self.udp_receiver = UdpReceiver()
        self.udp_sender = UdpSender()


    def start(self):
        self.data_storage.start()
        self.gui.start()
        self.udp_receiver.start()
        self.udp_sender.start()

    def stop(self):
        self.data_storage.stop()
        self.gui.stop()
        self.udp_receiver.stop()
        self.udp_sender.stop()