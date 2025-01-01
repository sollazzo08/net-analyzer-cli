# Packet Sniffer

This is a simple local CLI tool used for learning purposes to capture and display network packets using Scapy. It supports filtering by protocol, specifying the number of packets to capture, and performing basic OS fingerprinting.

## Requirements

- Python 3.x
- Scapy library

## Installation

1. Install Python 3.x if you haven't already.
2. Install the Scapy library using pip:

    ```sh
    pip install scapy
    ```

## Usage

Run the packet sniffer from the command line with the following options:

- `--proto`: Protocol to filter on (e.g., `tcp`, `udp`). Default is `all` (no filter).
- `--count`: Number of packets to capture. Default is `10`.

### Example Usage

1. Capture 10 packets of any protocol:

    ```sh
    python main.py --count 10
    ```

2. Capture 5 TCP packets:

    ```sh
    python main.py --count 5 --proto tcp
    ```

3. Capture 5 UDP packets:

    ```sh
    python main.py --count 5 --proto udp
    ```

