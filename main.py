import subprocess
import sys
from PyQt5.QtWidgets import QApplication
from GUI import Window
import scanner
import attack_rtsp
import attack_onvif

LIBRARIES = ["opencv-python", "psutil", "ipaddress", "datetime", "scapy", "onvif_zeep"]
missing_libraries = [lib for lib in LIBRARIES if lib not in subprocess.check_output(["pip", "freeze"]).decode()]
if missing_libraries:
    subprocess.call(["pip", "install"] + missing_libraries)

def handle_onvif_selected():
    subnet_scan_and_attack(attack_onvif.onvif_live_video)

def handle_rtsp_selected():
    subnet_scan_and_attack(attack_rtsp.RTSP_attack)

def handle_scan_selected():
    subnet_scan_and_attack(None)

def subnet_scan_and_attack(attack_function):
    subnet_to_scan = scanner.get_network_to_scan()

    if not subnet_to_scan:
        print("No subnets were found. The program is stopped.")
        sys.exit()

    found_addresses = scanner.scan_arp(subnet_to_scan)
    factory = scanner.mac_verif(found_addresses)
    ip_list_camera = scanner.ports_resume(found_addresses)

    if not ip_list_camera:
        print("No cameras were found. The program is stopped.")
        sys.exit()

    target = scanner.choice_target(ip_list_camera)

    if attack_function:
        attack_function(target, factory)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.onvif_selected.connect(handle_onvif_selected)
    window.rtsp_selected.connect(handle_rtsp_selected)
    window.scan_selected.connect(handle_scan_selected)

    window.show()
    sys.exit(app.exec_())
