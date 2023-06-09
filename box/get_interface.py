import wmi
import box.get_interface_ip as get_interface_ip

def get_wifi_boxes():
    wifi_boxes = []
    wmi_service = wmi.WMI()
    interfaces = wmi_service.Win32_NetworkAdapter(NetConnectionID="Wi-Fi")

    for interface in interfaces:
        ip = get_interface_ip.get_interface_ip(interface.Index)
        
        wifi_box = {
            "ssid": interface.NetConnectionID,
            "mac": interface.MACAddress,
            "ip": ip,
            "state": interface.NetConnectionStatus
        }

        wifi_boxes.append(wifi_box)

    return wifi_boxes