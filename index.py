import socket
import os
import threading
import webbrowser
import json
import wmi
from win10toast import ToastNotifier
from PIL import Image
from pystray import MenuItem as item
import pystray

HOST = 'localhost'
PORT = 8080
DIRECTORY = 'www'
WIFI_BOXES_JSON = './www/wifi_boxes.json'

def get_wifi_boxes():
    wifi_boxes = []
    wmi_service = wmi.WMI()
    interfaces = wmi_service.Win32_NetworkAdapter(NetConnectionID="Wi-Fi")

    for interface in interfaces:
        ip = get_interface_ip(interface.Index)
        
        wifi_box = {
            "ssid": interface.NetConnectionID,
            "mac": interface.MACAddress,
            "ip": ip,
            "state": interface.NetConnectionStatus
        }

        wifi_boxes.append(wifi_box)

    return wifi_boxes

def get_interface_ip(interface_index):
    addrs = socket.getaddrinfo(socket.gethostname(), None)
    for addr in addrs:
        if addr[4][0] == socket.AF_INET and addr[0] == socket.SOCK_DGRAM and addr[6] == interface_index:
            return addr[4][0]
    return None

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

def run_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)

    while True:
        client_socket, address = server_socket.accept()
        handle_request(client_socket)

def save_wifi_boxes_json():
    wifi_boxes = get_wifi_boxes()
    with open(WIFI_BOXES_JSON, 'w') as file:
        json.dump(wifi_boxes, file)

def setup_systray():
    # Load the image using PIL
    image_path = './assets/logo.png'  # Specify the path to your logo
    image = Image.open(image_path)

    # Convert the image to an icon
    menu_icon = pystray.Icon("name")
    menu_icon.icon = image

    def quit_action(icon, item):
        print("Serveur arrêté")
        icon.stop()

    def open_server_action(icon, item):
        print("Serveur ouvert")
        server_thread = threading.Thread(target=run_server)
        server_thread.start()
        webbrowser.open(f'http://{HOST}:{PORT}')

    quit_item = item('Quitter', quit_action)
    open_server_item = item('Ouvrir le serveur web', open_server_action)

    menu = (open_server_item, quit_item)

    icon = pystray.Icon("name", menu_icon, "Title", menu)
    return icon

if __name__ == '__main__':
    icon_path = './assets/logo.png'  # Specify the path to your custom icon
    icon = setup_systray()
    icon.icon = Image.open(icon_path)
    server_thread = threading.Thread(target=run_server)
    server_thread.start()
    icon.run()
