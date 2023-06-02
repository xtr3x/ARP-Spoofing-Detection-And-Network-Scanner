import concurrent
import threading
import time
import re
from concurrent.futures.thread import ThreadPoolExecutor

import requests
from PySide6 import QtWidgets, QtCore
from nmap import nmap
from scapy.arch import get_if_hwaddr
from scapy.config import conf
from scapy.layers.l2 import Ether, ARP
from scapy.sendrecv import srp, send, AsyncSniffer


class NetworkScanner(QtCore.QObject):
    update_table = QtCore.Signal(list)
    finished_signal = QtCore.Signal()

    def __init__(self, parent=None):
        super(NetworkScanner, self).__init__(parent)
        self.thread = None
        self.stop_flag = False
        self.vendor_cache = {}

    def get_mac_address(self, ip):
        try:
            ether = Ether(dst="ff:ff:ff:ff:ff:ff")
            arp = ARP(pdst=ip)
            packet = ether / arp
            mac_addresses = []
            for i in range(4):
                ans, _ = srp(packet, timeout=2, verbose=False)
                for _, received in ans:
                    mac_addresses.append(received[Ether].src.upper())
                time.sleep(0.2)
                if mac_addresses:
                    return ", ".join(mac_addresses)
            return "N/A"
        except:
            return "N/A"

    def scan_network(self, ip):
        if not re.compile(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/\d{1,2}$').match(ip):
            error_message = "Invalid target network format. Please enter in the format 192.168.1.1/24"
            QtWidgets.QMessageBox.warning(None, "Error", error_message)
            return

        scanner = nmap.PortScanner()
        scanner.scan(ip,
                     arguments='-p 22,23,25,53,80,110,143,443,465,587,993,995,1723,3306,3389,5900,5901,8080,8443 -sS')

        results = []
        ips = scanner.all_hosts()

        with ThreadPoolExecutor(max_workers=15) as executor:
            future_to_ip = {executor.submit(self.get_mac_address, ip): ip for ip in ips}
            for future in concurrent.futures.as_completed(future_to_ip):
                ip = future_to_ip[future]
                mac_address = future.result()
                vendor_name = self.get_vendor_name(mac_address)
                host_name = scanner[ip].hostname() if scanner[ip].hostname() else "N/A"
                open_ports = [port for port in scanner[ip]['tcp'].keys() if scanner[ip]['tcp'][port]['state'] == 'open']
                results.append({"IP": ip, "MAC Address": mac_address, "Vendor Name": vendor_name,
                                "Host Name": host_name, "Open Ports": ", ".join(map(str, sorted(open_ports)))})

        self.update_table.emit(results)
        self.finished_signal.emit()
    def get_vendor_name(self, mac_address):
        try:
            if mac_address in self.vendor_cache:
                return self.vendor_cache[mac_address]
            else:
                url = f'https://api.macaddress.io/v1?apiKey=at_yEQ66NTxUcs5Y86lReo22faBDR6YN&output=json&search={mac_address}'
                response = requests.get(url)
                time.sleep(1)
                vendor_name = response.json()['vendorDetails']['companyName']
                self.vendor_cache[mac_address] = vendor_name
                return vendor_name
        except KeyError:
            return ""
        except:
            print("Error: Access restricted. Check the credits balance.")
            return ""

    def start_scan(self, target_network):
        self.stop_flag = False
        self.thread = threading.Thread(target=self._scan, args=(target_network,))
        self.thread.daemon = True
        self.thread.start()

    def stop_scan(self):
        self.stop_flag = True

    def _scan(self, target_network):
        if not re.compile(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/\d{1,2}$').match(target_network):
            error_message = "Invalid target network format. Please enter in the format 192.168.1.1/24"
            QtWidgets.QMessageBox.warning(None, "Error", error_message)
            return

        try:
            self.scan_network(target_network)
        except Exception as e:
            error_message = f"An error occurred while sending the packet: {e}"
            QtWidgets.QMessageBox.warning(None, "Error", error_message)
