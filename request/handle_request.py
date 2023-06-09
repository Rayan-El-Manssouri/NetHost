import os
from box.save import save_wifi_boxes_json
DIRECTORY = 'www'


def handle_request(client_socket):
    request_data = client_socket.recv(1024).decode('utf-8')
    request_lines = request_data.split('\r\n')

    if len(request_lines) < 1:
        client_socket.close()
        return

    request_method = request_lines[0].split(' ')[0]

    if len(request_lines[0].split(' ')) < 2:
        client_socket.close()
        return

    request_path = request_lines[0].split(' ')[1]

    if request_method == 'GET':
        if request_path == '/':
            file_path = os.path.join(DIRECTORY, 'index.html')
        else:
            file_path = os.path.join(DIRECTORY, request_path[1:])

        if os.path.isfile(file_path):
            with open(file_path, 'rb') as file:
                file_data = file.read()

            content_type = 'application/octet-stream'

            if file_path.endswith('.html'):
                content_type = 'text/html'
            elif file_path.endswith('.css'):
                content_type = 'text/css'
            elif file_path.endswith('.js'):
                content_type = 'application/javascript'

            response_headers = [
                'HTTP/1.0 200 OK',
                f'Content-Type: {content_type}',
                f'Content-Length: {len(file_data)}',
                '\r\n'
            ]
            response = '\r\n'.join(response_headers).encode('utf-8') + file_data

            if file_path == os.path.join(DIRECTORY, 'index.html'):
                save_wifi_boxes_json()

        else:
            response = 'HTTP/1.0 404 Not Found\r\n\r\nFile Not Found'.encode('utf-8')

        client_socket.sendall(response)

    client_socket.close()
