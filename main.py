import subprocess

# auto-install library if you dont have them
libraries = ["opencv-python", "psutil", "ipaddress", "datetime", "scapy", "onvif_zeep"]
missing_libraries = [lib for lib in libraries if lib not in subprocess.check_output(["pip", "freeze"]).decode()]
if missing_libraries:
    subprocess.call(["pip", "install"] + missing_libraries)

import scanner
import attack_rtsp
import attack_onvif

logo= r"""
⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⢀⠔⠉⢝⡕⢢⠤⠤⠤⠤⠄⠀⣀⣀⣀⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠙⠕⠈⠒⠒⠒⠀⠠⠤⠤⠤⠀⢈⡑⢄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⡾⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⠁⠉
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢦⡀⠈⠪⡢⣂⠀⠀⠀⠀⠀⣀⠶⠋⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢄⠀⠘⢆⠉⠁⠒⠉⠉⠀⠀⠀⠀⠀⠀               
⠀⠀⠀⠀⠀⠀⢀⡠⠒⠊⠉⠉⠁⠒⠠⣀⡃⠀⠀⢣⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                  ___     _ _               
⠀⠀⠀⠀⢀⠔⠁⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀                 | _ \___| (_)__ __ _ _ __  
⠀⠀⢀⠔⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀                 |  _/ -_) | / _/ _` | '  \ 
⠀⢀⠞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⣶⠀⠀⠀⠀⢰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                 |_| \___|_|_\__\__,_|_|_|_|
⠀⡎⡄⡄⡄⡄⡄⣀⣰⣰⣸⣼⣷⡿⠁⠀⠀⠀⠀⡌⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀              
⢸⣷⣷⣷⣿⣿⣿⡿⠿⠟⠛⢻⠁⠀⠀⠀⠀⠀⡐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀              
⡟⠛⠉⠉⠉⠀⠀⠀⠀⠀⢠⠃⠀⠀⠀⢀⠠⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⡇⠀⠀⠀⠀⠀⢀⣀⣀⢴⠧⢤⠄⠒⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠉⠉⠉⠉⠉⠉⢢⢰⠁⠈⢡⢨⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⢸⢀⣀⢼⢸⠀⢀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠸⠬⠤⠭⠽⣘⣛⣂⣀⡣⠀⠀⠀⠀
"""

def main():
    print(logo)
    nb = 0
    while True:
        
        print("\033[4mPelicam options (enter the number to choose):\033[0m")
        print("\033[1m1. \033[0mScan network (ARP)")
        print("\033[1m2. \033[0mAttack target (RTSP)")
        print("\033[1m3. \033[0mAttack and control target (RTSP/ONVIF)")
        print("\033[1mq. \033[0mQuit")
        choice = input("Enter the number of the option that you want to use : ")
        match choice:
            case "1":
                nb = 1
                subnet_to_scan = scanner.get_network_to_scan()

                if not subnet_to_scan:
                    print("No subnets were found. The programme is stopped.")
                    exit()

                found_addresses = scanner.scan_arp(subnet_to_scan)
                factory = scanner.mac_verif(found_addresses)
                ip_list_camera = scanner.ports_resume(found_addresses)

                if not ip_list_camera:
                    print("No cam was found. The programme is stopped.")
                    exit()

                target = scanner.choice_target(ip_list_camera)

            case "2":
                if nb == 1:
                    attack_rtsp.RTSP_attack(target, factory)
                    
                else:
                    subnet_to_scan = scanner.get_network_to_scan()

                    if not subnet_to_scan:
                        print("No subnets were found. The programme is stopped.")
                        exit()

                    found_addresses = scanner.scan_arp(subnet_to_scan)
                    factory = scanner.mac_verif(found_addresses)
                    ip_list_camera = scanner.ports_resume(found_addresses)

                    if not ip_list_camera:
                        print("No cam was found. The programme is stopped.")
                        exit()

                    target = scanner.choice_target(ip_list_camera)
                    attack_rtsp.RTSP_attack(target, factory)
                exit()
                
            case "3":
                if nb == 1:
                    attack_onvif.onvif_live_video(target)

                else:
                    subnet_to_scan = scanner.get_network_to_scan()

                    if not subnet_to_scan:
                        print("No subnets were found. The programme is stopped.")
                        exit()

                    found_addresses = scanner.scan_arp(subnet_to_scan)
                    factory = scanner.mac_verif(found_addresses)
                    ip_list_camera = scanner.ports_resume(found_addresses)

                    if not ip_list_camera:
                        print("No cam was found. The programme is stopped.")
                        exit()

                    target = scanner.choice_target(ip_list_camera)
                    attack_onvif.onvif_live_video(target)
                exit()

            case "q":
                print("Thank you for using Pelicam. See you soon, stay safe and secure !")
                break
            case _:
                print("Invalid choice. Please enter a valid option.\n")

main()