import os
import threading
from PIL import Image
from pystray import MenuItem as item
import pystray
from setup.config import setup_systray
from loader.run import run_server


if __name__ == '__main__':
    icon_path = './assets/logo.png'  # Specify the path to your custom icon
    icon = setup_systray()
    icon.icon = Image.open(icon_path)
    server_thread = threading.Thread(target=run_server)
    server_thread.start()
    icon.run()
