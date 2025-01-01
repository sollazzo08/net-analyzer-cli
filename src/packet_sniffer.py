from scapy.all import IP

def packet_callback(packet):
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        print(f"Source: {src_ip}, Destination: {dst_ip}")
