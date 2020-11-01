#!/usr/bin/env python3

import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1)[0]
    client_list = []

    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        client_list.append(client_dict)
    return client_list


def cikti_sonucu(sonuc_list):
    print("IP ADDRESS\t\tMAC ADDRESS\n--------------------------------------------")
    for sonuc in sonuc_list:
        print(sonuc["ip"]+"\t\t"+sonuc["mac"])



ip = input("Taramak istediginiz ip adresi araliginin varsayilan ag gecidini giriniz: ")
ip = ip+"/24"
sonuc = scan(ip)
cikti_sonucu(sonuc)
