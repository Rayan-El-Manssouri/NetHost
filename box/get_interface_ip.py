import socket

def get_interface_ip(interface_index):
    addrs = socket.getaddrinfo(socket.gethostname(), None)
    for addr in addrs:
        if addr[4][0] == socket.AF_INET and addr[0] == socket.SOCK_DGRAM and addr[6] == interface_index:
            return addr[4][0]
    return None