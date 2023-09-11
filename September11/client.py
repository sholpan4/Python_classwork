import socket

my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 9900)

message = 'Hello by UDP!'
my_socket.sendto(message.encode(), server_address)