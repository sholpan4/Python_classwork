import socket

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

my_address = ('localhost', 3000)
my_socket.bind(my_address)

my_socket.listen()

is_running = True
while is_running:
    client_socket, addr = my_socket.accept()
    data = client_socket.recv(1024)

    message = data.decode(encoding="utf-8")
    print(f'Получено сообщение от {addr}: {message}')

    client_socket.send("HTTP/1.1 200 ok\n Content-type: text/html\n\n<h1>hello</h1>".encode())

    if message == "exit":
        is_running = False
