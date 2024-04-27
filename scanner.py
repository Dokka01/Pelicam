from scapy.all import *
import psutil
import socket
import ipaddress
import re

def get_network_to_scan():
    interfaces = psutil.net_if_addrs()
    subnets = set() # on utilise un ensemble au lieu d'une liste pour s'assurer que tous nos sous réseaux trouvés soient différents
    regex = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}/\d{1,2}\b')

    for interface, addrs in interfaces.items():
        for addr in addrs:
            if addr.family == socket.AF_INET:
                if not addr.address.startswith("127."):
                    subnet = ipaddress.ip_interface((addr.address, addr.netmask)).network
                    subnet_str = str(subnet)  # On convertit en str pour pouvoir utiliser la regex
                    subnet_re = regex.search(subnet_str)
                    if subnet_re:
                        subnets.add(subnet_re.group())

    subnets = list(subnets)
    if not subnets:
        manual_subnets = CDIR_check(subnets)
        if manual_subnets:
            subnets.append(manual_subnets)
        else:
            print("No subnet entered. Exiting.")
            exit()
    return subnets

def CDIR_check(subnets):
    cidr_regex = re.compile(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/\d{1,2}$')
    # print(subnets)
    if not subnets:
        user_cdir = input("No subnet has been detected. Please enter your CIDR (xxx.xxx.xxx.xxx/xx) : ")
        check = bool(cidr_regex.match(user_cdir))
        if check:
            return user_cdir
        else:
            CDIR_check(subnets)
            
def scan_arp(subnet_to_scan):
    if len(subnet_to_scan) == 1:
        subnet = subnet_to_scan[0]
        print(f"Scanning subnet : {subnet}")
    else:
        print("\n\033[1mHere are all the subnets found : \033[0m")
        for num, cdir in enumerate(subnet_to_scan, 1):
            print(f"{num}. {cdir}")

        while True:
            try:
                choice = int(input("\033[1mChoose one of them : \033[0m"))
                if 1 <= choice <= len(subnet_to_scan):
                    selected_subnet = subnet_to_scan[choice - 1]
                    print(f"\n\033[1mScanning subnet: {selected_subnet}\033[0m")
                    break
                else:
                    print("Numéro invalide. Veuillez sélectionner un numéro valide.")
            except ValueError:
                print("Veuillez entrer un numéro valide.")
            
    ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=selected_subnet), timeout=3)
    addresses_dict = {} 

    for sent, received in ans:
        mac_address = received[Ether].src.upper()
        ip_address = received[ARP].psrc
        addresses_dict[ip_address] = mac_address

    return addresses_dict

def mac_verif(found_addresses):
    objet_num = 1  
    for ip, mac_og in found_addresses.items():
        mac = mac_og[:8].upper()

        with open("data/manuf.txt", "r", encoding="utf-8") as f: 
            for line in f:
                mac_manuf = line[:8].upper()
                constructor = line[9:18].strip()
                if mac[:8] == mac_manuf:
                    print(f"Manufacturer is {constructor} for {ip}, {mac_og}")
                    objet_num += 1
                    return constructor
            else:
                print(f"No manufacturer found for : {ip}, {mac_og}")
                objet_num += 1

def test_ports(ip, port):
    response = sr1(IP(dst=ip)/TCP(dport=port), timeout=1, verbose=0)
    if response and response.haslayer(TCP) and response[TCP].flags == 18:
        return True
    else:
        return False
    
def check_camera(ip):
    for port in [8554] or [554] or [6688] or [80, 8554]:
        if not test_ports(ip, port):
            return False
    return True

def ports_resume(found_addresses):
    camera_list = []
    # print("si ces ports la sont ouverts")
    ports_list = {554 : "RTSP 1" , 
                  8554 : "RTSP 2", 
                  23 : "TELNET", 
                  80 : "HTTP/ONVIF", 
                  6688 : "ONVIF"}
    for ip, mac in found_addresses.items():
        print(f"\n\033[1mTesting ports for IP address : {ip}\033[0m\n")

        for port, port_name in ports_list.items():
            if test_ports(ip, port):
                print(f"\033[92m({port_name})\033[0m port {port} is \033[92mopen\033[0m on {ip}")
            else:
                print(f"\033[91m({port_name})\033[0m port {port} is \033[91mclosed\033[0m on {ip}")
    
        if check_camera(ip):
            print("=================")
            print("It's an IP Camera")
            print("=================")
            camera_list.append(ip)
        else:
            print("xxxxxxxxxxxxxxxxxxxxx")
            print("It's not an IP Camera")
            print("xxxxxxxxxxxxxxxxxxxxx")

    return camera_list

def choice_target(ip_list_camera):
    if len(ip_list_camera) == 1:
        select_cam = ip_list_camera[0]
        print(f"\n\033[1mTarget : {select_cam}\033[0m\n")
        return select_cam
    else:
        print("\n\033[1mHere are all the cameras found : \033[0m")
        for num, ip in enumerate(ip_list_camera, 1):
            print(f"{num}. {ip}")

        while True:
            try:
                choice = int(input("\033[1mChoose one of them to scan : \033[0m"))
                if 1 <= choice <= len(ip_list_camera):
                    select_cam = ip_list_camera[choice - 1]
                    print(f"Attack camera : {select_cam}")
                    return select_cam
                
                else:
                    print("Numéro invalide. Veuillez sélectionner un numéro valide.")
            except ValueError:
                print("Veuillez entrer un numéro valide.")