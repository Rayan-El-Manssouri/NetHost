import os
import signal
import threading
from PIL import Image
from pystray import MenuItem as item
import pystray
import argparse
from setup.config import setup_systray
from loader.run import run_server
from box.list import list_wifi_boxes


class ConsoleInterface:
    def __init__(self):
        self.icon_path = './assets/logo.png'
        self.icon = setup_systray()
        self.icon.icon = Image.open(self.icon_path)
        self.server_thread = threading.Thread(target=run_server)
        self.input_thread = threading.Thread(target=self.input_loop)

    def input_loop(self):
        print('Welcome to nethost 5 !')
        while True:
            command = input('Nethost 5 > ')
            self.process_command(command)

    def process_command(self, command):
        if command == 'exit':
            self.exit_program()
        elif command == 'help':
            self.show_help()
        elif command == 'clear':
            self.clear_screen()
        elif command == 'list':
            self.list_wifi_boxes()
        elif command == 'driver':
            self.show_driver_info()
        else:
            self.show_invalid_command()

    def exit_program(self):
        print('Exiting...')
        # Arrêter tous les services ou effectuer d'autres tâches de nettoyage ici
        # ...

        # Terminer le programme
        os._exit(0)

    def show_help(self):
        print('Commands:')
        print('help - show this message')
        print('exit - exit the program')

    def clear_screen(self):
        os.system('cls')

    def list_wifi_boxes(self):
        list_wifi_boxes()

    def show_driver_info(self):
        print('Driver Information:')
        print('-' * 20)
        print('Driver Commands:')
        print(' - nethost 5 driver install    : Install the driver')
        print(' - nethost 5 driver uninstall  : Uninstall the driver')
        print()
        print('Your PC is compatible to be used as a Wi-Fi box')
        print('Version: 1.0.0')


    def show_invalid_command(self):
        print('Invalid command, type help for a list of commands')

    def signal_handler(self, sig, frame):
        self.exit_program()

    def start(self):
        # Capturer le signal SIGINT (Ctrl+C)
        signal.signal(signal.SIGINT, self.signal_handler)

        self.server_thread.start()
        self.input_thread.start()

        self.icon.run()


def main():
    parser = argparse.ArgumentParser(description='Nethost 5')

    args = parser.parse_args()

    console_interface = ConsoleInterface()
    console_interface.start()


if __name__ == '__main__':
    main()
