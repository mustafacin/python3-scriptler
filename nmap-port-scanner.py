#!/usr/bin/python3

import nmap
scanner = nmap.PortScanner()
print("nmap tool'una hosgeldiniz.")
print("--------------------------------")

ip_adres= input("ip adresinizi giriniz:")
print("Girmis oldugunuz ip adresi : ")

cevap = input("""\nLutfen yapmak istediginiz secenegi seciniz.
                    1)Hizli tarama
                    2)Tum portlar taramasi
                    3)UDP taramasi\n""")

print("\n sectiginiz secenek :",cevap)

if cevap == '1':
    scanner.scan(ip_adres,'1-1024','-v')
    print("host aktifligi : ",scanner[ip_adres].state())
    print(scanner[ip_adres].all_protocols())
    print("acik portlar : ", scanner[ip_adres]['tcp'].keys())

elif cevap == '2':
    scanner.scan(ip_adres,'1-65535','-v -sS')
    print("host aktifligi : ",scanner[ip_adres].state())
    print(scanner[ip_adres].all_protocols())
    print("acik portlar : ", scanner[ip_adres]['tcp'].keys())

elif cevap == '3':
    scanner.scan(ip_adres,'1-1024','-sU ')
    print("host aktifligi : ",scanner[ip_adres].state())
    print(scanner[ip_adres].all_protocols())
    print("acik portlar : ", scanner[ip_adres]['udp'].keys())
else:
    print("Yanlis deger girdiniz.")

