from scapy.all import sniff, ARP

ip_mac_map = {}

def process_packet(packet):
    if not packet.haslayer(ARP):
        return

    src_ip = packet[ARP].psrc
    src_mac = packet[ARP].hwsrc

    if src_ip in ip_mac_map:
        if ip_mac_map[src_ip] != src_mac:
            old_mac = ip_mac_map[src_ip]

            print(
                f"\n[!] Possible ARP attack detected\n"
                f"IP Address: {src_ip}\n"
                f"Previous MAC: {old_mac}\n"
                f"Current MAC: {src_mac}\n"
            )

    else:
        ip_mac_map[src_ip] = src_mac

print("Starting ARP Detector...")
sniff(filter = "arp", store = False, prn = process_packet)
