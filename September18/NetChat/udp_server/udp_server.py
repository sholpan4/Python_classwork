from PyQt6.QtCore import QThread
import socket

class UdpServer(QThread):
    def run(self):
        print("Server is running")

    # pass
    

#my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#my_address = ('192.168.110.119', 9900)
#my_socket.bind(my_address)

#is_running = True
#while is_running:
    #data, addr = my_socket.recvfrom(1024)
    #message = data.decode(encoding="utf-8")
    #print(f'Получено сообщение от {addr}: {message}')
    #if message == "exit":
        #is_running = False