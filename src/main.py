from scapy.all import sniff
from packet_sniffer import packet_callback

def main():
    print("Starting packet capture...")
    sniff(prn=packet_callback, count=10)  # Capture 10 packets

if __name__ == "__main__":
    main()
