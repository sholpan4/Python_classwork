from PyQt6.QtCore import QObject
from data_storage import DataStorage
from gui import Gui
from udp_receiver import UdpReceiver
from udp_sender import UdpSender
from udp_server import UdpServer
from udp_client import UdpClient

class Router(QObject):
    def __init__(self):
        super().__init__()
        self.data_storage = DataStorage()
        self.gui = Gui()
        self.udp_receiver = UdpReceiver()
        self.udp_sender = UdpSender()
        self.udp_server = UdpServer()
        self.udp_client = UdpClient()


    def start(self):
        self.data_storage.start()
        self.gui.start()
        self.udp_receiver.start()
        self.udp_sender.start()
        self.udp_server.start()
        self.udp_client.start()

    def stop(self):
        self.data_storage.stop()
        self.gui.stop()
        self.udp_receiver.stop()
        self.udp_sender.stop()
        self.udp_server.stop()
        self.udp_client.stop()