import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 9998

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))
    server.listen(5)
    print(f'[*] Nasłuchiwanie na {IP}:{PORT}')

    while True:
        client, addresss = server.accept()
        print(f'[*] Przyjęto połączenie od {address[0]} :{address{1}}')
        client_handler = threading.Threading(target=handle_client, args=(client,))
        client_handler.start()

def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recv(1024)
        print(f'[*] Odebrano: {request.decode("utf-8)}')
        sock.send(b'ACKKK')

if __name__ == '__main__':
    main()