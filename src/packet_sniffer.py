from scapy.all import IP, TCP

def packet_callback(packet):
    if packet.haslayer(IP) and packet.haslayer(TCP):
        ip_layer = packet.getlayer(IP)
        tcp_layer = packet.getlayer(TCP)
        print(f"New Packet: {ip_layer.src} -> {ip_layer.dst}")
        print(f"TTL: {ip_layer.ttl}")
        print(f"Window Size: {tcp_layer.window}")
        print(f"Flags: {tcp_layer.flags}")
        print(f"Options: {tcp_layer.options}")
        print("-" * 50)
