import random
import time

import scapy
from scapy.layers.inet import IP, TCP
from scapy.layers.l2 import ARP
from scapy.sendrecv import sr1
from scapy.all import *

# try:
#     pkg = ARP(psrc='192.168.112.1', pdst='192.168.112.189')
#     reply = sr1(pkg, timeout=3, verbose=False)
#     print(reply[ARP].hwsrc)
#     print(f"IP在线")
# except :
#     pass


# 利用scapy完成三次握手：五元组：源IP，源端口，协议，目标IP，目标端口， S,SA,A, seq, ack
seq = random.randint(10000, 20000)
sport = random.randint(12000, 30000)
pkg_1 = IP(dst='192.168.112.130')/TCP(sport=sport, dport=6666, flags='S', seq=seq)
reply = sr1(pkg_1, timeout=5, verbose=False)
seq = reply[TCP].ack
ack = reply[TCP].seq + 1
pkg_2 = IP(dst='192.168.112.130')/TCP(sport=sport, dport=6666, flags='A', seq=seq, ack=ack)
sr1(pkg_2, timeout=3, verbose=False)

# 三次握手完成后，发送聊天消息
reply = sr1(IP(dst='192.168.112.130')/TCP(sport=sport, dport=6666, flags='PA', seq=seq, ack=ack)/"你好吗？", verbose=False)
time.sleep(1)
print(reply[Raw].load.decode())

