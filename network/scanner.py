import socket, threading, os, time

from scapy.layers.inet import IP, TCP
from scapy.layers.l2 import ARP
from scapy.sendrecv import sr1
from scapy.all import *

# 配置日志记录的级别为 ERROR
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

# 对目标IP进行端口扫描，尝试连接目标IP和端口，如果连接成功，说明端口开放，否则未开放。

def socket_port(ip):
    for port in range(1,65536):
        try:
            s = socket.socket()
            s.settimeout(0.5)       # 设置无法连接情况下超时时间，提升扫描效率
            s.connect((ip, port))
            print(f"端口：{port} 可用.")
            s.close()
        except ConnectionRefusedError:
            # print(f"端口：{port} 不可用.")
            pass
        except socket.timeout:
            pass

# 基于多线程进行端口扫描
def socket_port_thread(ip, start):
    for port in range(start, start+50):
        try:
            s = socket.socket()
            s.settimeout(0.5)       # 设置无法连接情况下超时时间，提升扫描效率
            s.connect((ip, port))
            print(f"端口：{port} 可用.")
            s.close()
        except:
            pass

# 优化思路：将常用端口进行优先扫描，量少后，可以让每一次端口扫描完成后，停止3秒钟（可以防止IDS/IPS进行阈值检测）
# 另外，如果是真实环境，建议在扫描之前，先用别的公网 IP 进行验证，确认是否存在入侵防御。
def socket_port_normal(ip):
    list = [7, 21, 22, 23, 25, 43, 53, 67, 68, 69, 79, 80, 81, 88, 109, 110, 113, 119, 123, 135, 135,
            137, 138, 139, 143, 161, 162, 179, 194, 220, 389, 443, 445, 465, 513, 520, 520, 546, 547,
            554, 563, 631, 636, 991, 993, 995, 1080, 1194, 1433, 1434, 1494, 1521, 1701, 1723, 1755,
            1812, 1813, 1863, 3269, 3306, 3307, 3389, 3544, 4369, 5060, 5061, 5355, 5432, 5671, 5672, 6379,
            7001, 8080, 8081, 8088, 8443, 8883, 8888, 9443, 9988, 9988, 15672, 50389, 50636, 61613, 61614]
    for port in list:
        try:
            s = socket.socket()
            s.settimeout(0.5)       # 设置无法连接情况下超时时间，提升扫描效率
            s.connect((ip, port))
            print(f"端口：{port} 可用.")
            s.close()
        except:
            pass
        time.sleep(3)

# 在公网上，不会进行IP扫描，通常是明确目标IP而进行端口扫描
# 如果要进行内网渗透，则必须要知道有哪些IP地址是存活的，可访问的，进而再进行端口扫描
# IP地址工作在IP层，ICMP，还有ARP协议也存在IP信息
# 先使用 ping 命令进行IP探测，但是此扫描方式存在Bug，一旦防火墙禁止ICMP，那么扫描结果失效
def ping_ip():
    for i in range(128,255):
        ip = f'192.168.112.{i}'
        # output = os.popen(f'ping -n 1 -w 100 {ip}').read()
        # if 'TTL=' in output:
        #     print(f"{ip} online")
        output = os.popen(f'ping -n 1 -w 100 {ip} | findstr TTL=').read()
        if len(output) > 0:
            print(f"{ip} online")

# 如何使用别的方式，让防火墙不存在封锁的行为？了解一下ARP协议，pip install scapy
def scapy_ip(start):
    for i in range(start, start+20):
        ip = f'192.168.112.{i}'
        try:
            pkg = ARP(psrc='192.168.112.1', pdst=ip)
            reply = sr1(pkg, timeout=3, verbose=False)
            print(reply[ARP].hwsrc)
            print(f"{ip} 在线")
        except :
            pass

# 基于半连接 S / SA / RA 等标志位来对端口进行判断
# 如果目标端口开放，则S->SA，如果目标端口未开放，则S->RA
def scapy_port(ip):
    # 通过指定源IP地址，可以实现IP欺骗，进而导致半连接，此类操作也可以用于Flags参数定义上
    # pkg = IP(src='192.168.115.123', dst=ip)/TCP(dport=80, flags='SA')

    for port in range(20, 100):
        try:
            pkg = IP(src='192.168.112.123', dst=ip)/TCP(dport=port, flags='S')
            reply = sr1(pkg, timeout=1, verbose=False)
            # print(reply[TCP].flags)
            if reply[TCP].flags == 0x12:
            # if int(reply[TCP].flags) == 18:
                print(f'端口 {port} 开放')
        except:
            pass


# 基于Ping命令的子域名扫描
def ping_domain():
    with open('../dict/subdomain-top160k.txt') as file:
        domain_list = file.readlines()

    for domain in domain_list:
        result = os.popen(f"ping -n 1 -w 1000 {domain.strip()}.woniuxy.com").read()
        # print(result)
        # if '请求超时' in result or 'TTL=' in result:
        #     print(f"{domain.strip()}.woniuxy.com")

        if '找不到主机' not in result:
            print(f"{domain.strip()}.woniuxy.com")

# 基于socket库的DNS解析功能实现扫描
def socket_domain():
    with open('../dict/subdomain-top160k.txt') as file:
        domain_list = file.readlines()

    for domain in domain_list:
        try:
            ip = socket.gethostbyname(f'{domain.strip()}.woniuxy.com')
            print(f'{domain.strip()}.woniuxy.com, {ip}')
        except socket.gaierror:
            pass

# 查询域名的whois信息
def whois_info():
    from whois import whois
    import json
    result = whois('woniuxy.com')
    # print(result)
    dict = json.loads(str(result))
    print(dict)
    print(dict['registrar'])


if __name__ == '__main__':
    # socket_port('192.168.112.188')

    # for i in range(1, 5000, 50):
    #     threading.Thread(target=socket_port_thread, args=('117.78.44.231', i)).start()

    # socket_port_normal('192.168.112.188')

    # ping_ip()
    # scapy_ip()

    # for i in range(1, 255, 20):
    #     threading.Thread(target=scapy_ip, args=(i,)).start()

    # scapy_port('192.168.112.188')

    # ping_domain()
    # socket_domain()
    whois_info()