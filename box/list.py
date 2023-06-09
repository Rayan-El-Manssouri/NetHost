import pywifi

def list_wifi_boxes():
    wifi = pywifi.PyWiFi()

    ifaces = wifi.interfaces()
    if len(ifaces) == 0:
        print("Aucune interface WiFi disponible.")
        return

    iface = ifaces[0]  # Sélectionne la première interface WiFi
    iface.scan()  # Effectue une analyse des réseaux WiFi

    networks = iface.scan_results()
    if len(networks) == 0:
        print("Aucun réseau WiFi trouvé.")
        return

    print("Liste des box WiFi disponibles :")
    for network in networks:
        print(f"SSID : {network.ssid}, Signal : {network.signal}")
