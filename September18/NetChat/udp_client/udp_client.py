from PyQt6.QtCore import QThread
import socket

class UdpClient(QThread):
    def run(self):
        print("Client is running")
        
    #my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    #server_address = ('localhost', 9900)  #192.168.110.119  127.0.0.1

    #message = 'Sholpan'
    #my_socket.sendto(message.encode(), server_address)