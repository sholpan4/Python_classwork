from PyQt6.QtCore import QThread

class UdpClient(QThread):
    def run(self):
        print("Client is running")