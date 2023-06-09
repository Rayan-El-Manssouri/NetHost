import socket
HOST = 'localhost'
PORT = 8080
import request.handle_request as handle_request

def run_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    while True:
        client_socket, address = server_socket.accept()
        handle_request.handle_request(client_socket)