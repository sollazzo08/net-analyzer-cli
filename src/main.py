import argparse
import textwrap
from scapy.all import sniff
from packet_sniffer import packet_callback

def main():
    parser = argparse.ArgumentParser(
        prog="packet_sniffer", 
        description=textwrap.dedent(
            """
            Packet sniffer to capture and display network packets.

            Example usage:
            python main.py --count 10 --proto tcp

            """
        ))
    parser.add_argument("--proto", type=str, default="all", help="Protocol to filter on (e.g., tcp, udp)")
    parser.add_argument("--count", type=int, default=10, help="Number of packets to capture")    
    args = parser.parse_args()

    # Set the filter string based on the protocol argument
    filter_str = args.proto if args.proto != "all" else ""
    
    print("Starting packet capture...")
    sniff(prn=packet_callback, filter=filter_str, count=args.count)  # Capture packets with filter and count

if __name__ == "__main__":
    main()
