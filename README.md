# Description
Tool fully developed by me. This tool allows you to carry out denial of service attacks with a wide range of methods. There are many methods of spoofing and amplification (like DNS, NTP amplification). It's a tool with a cool interface with colors and easy to use. This tool is developed with the Scapy module. I am therefore in no way responsible for your actions, this tool is for educational purposes and for the safety test on an infrastructure that belongs to you.

# installation
- You need to git clone the repository: `git clone http://`
- then run the requirement.sh file to install the dependencies ([Scapy Module](https://scapy.net/)): `./requirements.sh`
- Then use python3 for the used: `python3 DenialPacketTool.py`

# Methods 
- UDP Flood with spoofed request (We can specify a specific source, or with wordlist, or random source)
- SYN Flood with spoofed request (We can specify a specific source, or with wordlist, or random source)
- ICMP Flood with spoofed request (We can specify a specific source, or with wordlist, or random source)
- Smurf Attack (ICMP spoof to broadcast address) 
- Ping of Death with spoofed request (We can specify a specific source, or with wordlist, or random source)
- DNS Amplification (We can use a specific DNS resolver, or your wordlist, or a commun list in the tool)
- NTP Amplification (We can use a specific NTP server, or your wordlist, or a commun list in the tool)
- SNMP Amplification (Soon ...) 

# Exemple and proof
- UDP flood with spoofed random source request on 192.168.1.11 :
https://cdn.discordapp.com/attachments/351798326129197057/812747148180979742/unknown.png
- SYN flood with spoofed 1.1.1.1 source request on 192.168.1.11 :
https://cdn.discordapp.com/attachments/351798326129197057/812747148180979742/unknown.png
- DNS amplification :
https://cdn.discordapp.com/attachments/744961641246097508/813415935637585930/unknown.png
https://cdn.discordapp.com/attachments/744961641246097508/813416015878291476/unknown.png
