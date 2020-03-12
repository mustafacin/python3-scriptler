#!/usr/bin/python3


import socket
ip_adres = input("Hedef ip adresini giriniz.")
port_listesi = [21,22,23,80,88,139,445,443,3306,8080]
#isterseniz bu port listesini degistirerek daha genis bir tarama yapabilirsiniz.


for port in port_listesi:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cikti = s.connect_ex((ip_adres,port))

    if cikti == 0:
        print("Port ", port ," aciktir.")

