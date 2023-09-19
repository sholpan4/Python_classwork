from PyQt6.QtCore import QThread

class UdpServer(QThread):
    def run(self):
        print("Server is running")

    # pass