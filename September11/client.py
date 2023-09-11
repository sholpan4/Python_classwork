import socket

my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('192.168.110.119', 9900)  #192.168.110.119

message = 'Hello by UDP!'
my_socket.sendto(message.encode(), server_address)