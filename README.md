# Python Wi-Fi Box App

<div align="center">
  <img src="./assets/logo.png" alt="Logo" height="200">
</div>

This code is a Python application that turns your computer into a Wi-Fi box. It creates a local web server on port 8080, allowing you to access static files and manage Wi-Fi boxes from a web browser.

## Prerequisites
- Python 3.x
- The following packages need to be installed:
  - `socket`
  - `os`
  - `threading`
  - `webbrowser`
  - `json`
  - `wmi`
  - `win10toast`
  - `PIL`
  - `pystray`

## Configuration
Before running the application, make sure to configure the following:

### Directory for Static Files
The `www` directory contains the static files (HTML, CSS, JavaScript) that you want to make accessible through the local web server. Place your files in this directory.

### Path to the Logo Image
Specify the path to your own logo image by replacing the path `./assets/logo.png` with the path to your image.

## Usage
1. Run the Python script using the command `python script.py`.
2. The application will start and display the logo in the system tray.
3. Right-click on the icon to show the menu.
4. Select "Open Web Server" to start the server.
5. The server is now running and accessible at `http://localhost:8080`.
6. The static files present in the `www` directory can be viewed from the browser.
7. The `index.html` file is specially handled, and whenever it is loaded, the list of available Wi-Fi boxes is updated and saved to the `wifi_boxes.json` file.
8. To stop the server, select "Quit" from the menu.

## Note
- Make sure appropriate permissions and firewalls are configured to allow access to the server on port 8080.
- The application uses the `wmi` library to retrieve Wi-Fi box information. Ensure that you have sufficient privileges to access this information.
