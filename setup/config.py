import pystray
from PIL import Image
from pystray import MenuItem as item
import threading
import webbrowser
from loader.run import run_server
HOST = 'localhost'
PORT = 8080


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