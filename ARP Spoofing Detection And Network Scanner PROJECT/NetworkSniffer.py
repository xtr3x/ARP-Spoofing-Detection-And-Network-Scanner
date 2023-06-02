import threading
from datetime import datetime

from PySide6 import QtCore
from scapy.layers.l2 import Ether
from scapy.sendrecv import sniff


class Sniffer(QtCore.QObject):
    update_time = QtCore.Signal(str)
    update_source = QtCore.Signal(str)
    update_destination = QtCore.Signal(str)
    update_protocol = QtCore.Signal(str)
    update_length = QtCore.Signal(int)
    update_info = QtCore.Signal(str)

    def __init__(self, filter="", parent=None):
        super(Sniffer, self).__init__(parent)
        self.filter = filter
        self.stop_flag = False
        self.protocol_names = {
            0x0800: "IPv4",
            0x0806: "ARP",
            0x8100: "VLAN Tagging",
            0x86dd: "IPv6",
            0x880b: "PPP",
            0x8847: "MPLS",
            0x8863: "PPPoE Discovery",
            0x8864: "PPPoE Session",
            0x886f: "802.1X",
            0x88a8: "802.1Q",
            0x88f7: "PTP",
            0x8902: "CFM",
            0x8906: "FCoE Initialization Protocol",
            0x8914: "FCoE",
            0x8915: "RDMA over Converged Ethernet",
            0x892f: "High-availability Seamless Redundancy",
            0x9000: "Ethernet Padding",
            0x9100: "VLAN Tagging",
            0x9200: "VLAN Double Tagging",
            0x9400: "Cisco FabricPath",
            0x0805: "STP",
            0x8035: "RARP",
            0x809b: "AppleTalk",
            0x80f3: "AARP",
            0x8137: "IPX",
            0x8181: "802.1ad",
            0x86db: "AppleTalk",
            0x872d: "TRILL",
            0x8809: "Link Layer Discovery Protocol",
            0x8819: "CobraNet",
            0x8822: "Token Ring",
            0x8848: "MPLS Multi-Protocol Label Switching",
            0x884a: "MPLS Pseudo Wire",
            0x886d: "HyperSCSI",
            0x8870: "Jumbo Frames",
            0x887b: "HomePlug",
            0x888e: "Provider Bridging",
            0x88a2: "ATA over Ethernet",
            0x88a4: "EtherCAT",
            0x88a7: "802.1ah",
            0x88b5: "IEEE 802.1 Local Station Management",
            0x88c7: "802.11e",
            0x88cc: "Link Layer Control",
            0x88cd: "SERCOS III",
            0x88e1: "HomePNA",
            0x88e3: "Media Redundancy Protocol",
            0x88e5: "802.1AE",
            0x88f5: "IEEE 802.1Qat",
            0x890d: "802.11",
            0x891d: "TTEthernet",
            0x894f: "802.1Qbv",
            0x898e: "802.11r",
            0x88f9: "IEEE 802.3br",
            0x88fb: "IEEE 802"
        }

    def start_sniffing(self):
        self.stop_flag = False
        self.thread = threading.Thread(target=self.sniff_packets)
        self.thread.daemon = True
        self.thread.start()

    def stop_sniffing(self):
        self.stop_flag = True

    def sniff_packets(self):

        def capture_packet(packet):
            if Ether in packet:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
                destination = packet[Ether].dst
                source = packet[Ether].src
                ether_protocol = self.protocol_names.get(packet[Ether].type, "Unknown")
                length = len(packet[Ether])
                info = packet.summary()

                app_protocol = "Unknown"
                if packet.haslayer('Raw'):
                    app_protocol = packet.payload.payload.name
                    info += f" {app_protocol}"
                elif packet.haslayer('UDP'):
                    udp = packet.payload
                    if udp.dport == 53 or udp.sport == 53:
                        app_protocol = 'DNS'
                    elif udp.dport == 67 or udp.sport == 67:
                        app_protocol = 'DHCP'
                    elif udp.dport == 68 or udp.sport == 68:
                        app_protocol = 'DHCPv6'
                    info += f" {app_protocol}"

                if self.filter:
                    if self.filter.lower() in destination.lower() or \
                            self.filter.lower() in source.lower() or \
                            self.filter.lower() in ether_protocol.lower() or \
                            self.filter.lower() in app_protocol.lower():
                        self.emit_packet_info(timestamp, source, destination, ether_protocol, length, app_protocol,
                                              info)
                else:
                    self.emit_packet_info(timestamp, source, destination, ether_protocol, length, app_protocol, info)

        while not self.stop_flag:
            sniff(prn=capture_packet, count=1, filter=self.filter, store=0)

    def emit_packet_info(self, timestamp, source, destination, ether_protocol, length, app_protocol, info):
        protocol = app_protocol if app_protocol != "Unknown" else ether_protocol
        self.update_time.emit(timestamp)
        self.update_source.emit(source)
        self.update_destination.emit(destination)
        self.update_protocol.emit(protocol)
        self.update_length.emit(length)
        self.update_info.emit(info)