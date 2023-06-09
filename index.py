import os
import signal
import threading
from PIL import Image
from pystray import MenuItem as item
import pystray
from setup.config import setup_systray
from loader.run import run_server
from box.list import list_wifi_boxes

def input_thread():
    print('Welcome to nethost 5 !')
    command = input('Nethost 5 >')
    while command != 'exit':
        if command == 'help':
            print('Commands: \nhelp - show this message\nexit - exit the program')
        if command == 'clear':
            os.system('cls')
        if command == 'list':
            list_wifi_boxes()
        else:
            print('Invalid command, type help for a list of commands')
        command = input('Nethost 5 >')

def signal_handler(sig, frame):
    print('Exiting...')
    # Arrêter tous les services ou effectuer d'autres tâches de nettoyage ici
    # ...

    # Terminer le programme
    os._exit(0)

if __name__ == '__main__':
    # Capturer le signal SIGINT (Ctrl+C)
    signal.signal(signal.SIGINT, signal_handler)

    icon_path = './assets/logo.png'  # Specify the path to your custom icon
    icon = setup_systray()
    icon.icon = Image.open(icon_path)
    server_thread = threading.Thread(target=run_server)
    server_thread.start()

    input_thread = threading.Thread(target=input_thread)
    input_thread.start()

    icon.run()
