
import socket,os,sys
from IPy import IP
import time,threading


def check_ip(ip_address):
    try:
        IP(ip_address)
        return ip_address
    except ValueError:
        return socket.gethostbyname(ip_address)


def tara(host, port):


        hos1 = check_ip(host)
        try:
            sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            sock.connect((hos1, port))
            sock.settimeout(0.5)
            print("[+] " + host + " for Port " + str(port) +" is open: " + sock.recv(1024).decode())
        except:
            pass
#           print("[+] " + host + " for Port " + str(port) + " is Closed")


ipman = []
def basla(targets):
    for ip_add in targets.split('.'):
        ipman.append(ip_add.strip(' '))

    subnet = ""
    for i in range(0, 3):
        subnet = subnet + ipman[i] + "."

    subnet2 = str(subnet) + "0/24"
    print("\nYour Subnet : " + subnet2 + "\n")

    for i in range(1, 254):
        port_list = [21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 443, 445, 902, 993, 995, 1723, 3306, 3389, 5900, 8000, 8080]
        ipler = str(subnet) + str(i)
        print(str(ipler) + " ip address scanning [+]\n")
        for port2 in port_list:
            t = threading.Thread(target=tara, args=(ipler, port2))
            t.start()
            time.sleep(0.5)



if __name__ == "__main__":
    targets = input("Ip adresini giriniz: ")
    basla(targets)
