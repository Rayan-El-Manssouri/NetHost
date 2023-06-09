import pywifi

wifi_scanner = pywifi.PyWiFi()
interface = wifi_scanner.interfaces()[0]
interface.scan()

networks = interface.scan_results()

for network in networks:
    print("SSID:", network.ssid)
    print("Signal Strength:", network.signal)
    print("MAC Address:", network.bssid)
    print("---------------------")
