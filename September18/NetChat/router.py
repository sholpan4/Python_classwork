from PyQt6.QtCore import QObject
# from logger import Logger
from data_storage import DataStorage
from gui import Gui
from udp_receiver import UdpReceiver
from udp_sender import UdpSender

# log = Logger.Instance

class Router(QObject):
    def __init__(self):
        super().__init__()
        self.data_storage = DataStorage()
        self.gui = Gui()
        self.udp_receiver = UdpReceiver()
        self.udp_sender = UdpSender()

        self.gui.sendMessage.connect(lambda s: print(s))

    def start(self):
        # log.d("Starting router")
        self.data_storage.start()
        self.gui.start()
        self.udp_receiver.start()
        self.udp_sender.start()

    def stop(self):
        self.data_storage.stop()
        self.gui.stop()
        self.udp_receiver.stop()
        self.udp_sender.stop()

    


    # my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # my_addres = ('localhost', 3000)
    # my_socket.bind(my_addres)

    # my_socket.listen()

    # is_running = True
    # while is_running:
    #     client_socket, addr = my_socket.accept()
    #     data = client_socket.recv(1024)

    #     message = data.decode(encoding= "UTF-8")
    #     print(f'получено сообщение от {addr}: {message}')

    #     client_socket.send("HTTP/1.1 200 OK\nContent-Type: text/html\n\n<h1>Hello World</h1>".encode())

    #     if message == "exit":
    #         is_running = False