from scapy.all import *
from scapy.layers.l2 import Ether, ARP
import threading
import time
from PySide6.QtCore import QObject, Signal


class ArpSpoofDetector(QObject):
    attack_detected = Signal()
    attack_stopped = Signal()

    def __init__(self, time_window=50, max_mac_changes=0):
        super().__init__()
        self.cache = {}
        self.time_window = time_window
        self.max_mac_changes = max_mac_changes
        self.attack_ongoing = False
        self.lock = threading.Lock()

    def start_detection(self):
        self.stop_event = threading.Event()
        self.sniff_thread = threading.Thread(target=self._sniff, args=(self.stop_event,))
        self.sniff_thread.daemon = True
        self.sniff_thread.start()

    def stop_detection(self):
        self.stop_event.set()
        self.sniff_thread.join()

    def set_time_window(self, time_window):
        self.time_window = time_window

    def set_max_mac_changes(self, max_mac_changes):
        self.max_mac_changes = max_mac_changes

    def _update_cache(self, arp):
        self.cache[arp.psrc] = (arp.hwsrc, time.time())

    def _check_cache(self):
        now = time.time()
        for ip in self.cache.copy():
            if now - self.cache[ip][1] > self.time_window:
                self.cache.pop(ip)

    def _check_attack(self):
        mac_changes = len(set(self.cache[ip][0] for ip in self.cache))
        if mac_changes > self.max_mac_changes:
            return True
        return False

    def _arp_spoof_detection(self, pkt):
        if self.stop_event.is_set():
            return
        with self.lock:
            try:
                if pkt.haslayer(ARP):
                    arp = pkt.getlayer(ARP)
                    # Check if it's an ARP reply
                    if arp.op == 2:
                        # Update the cache with the new ARP packet
                        self._update_cache(arp)
                        # Check if the sender's IP address is in the cache
                        if arp.psrc in self.cache:
                            # Check if the sender's MAC address has changed within the time window
                            if self._check_attack() and time.time() - self.cache[arp.psrc][1] <= self.time_window:
                                if not self.attack_ongoing:
                                    print("[ALERT] Possible ARP spoofing attack detected!")
                                    self.attack_ongoing = True
                                    self.attack_detected.emit()


                    elif arp.op == 1:
                        # Remove cache entries for gratuitous ARP packets
                        if arp.hwsrc == self.cache.get(arp.psrc, ("", 0))[0]:
                            self.cache.pop(arp.psrc, None)
                else:
                    return
            except Exception as e:
                print(e)
            finally:
                self._check_cache()
                if self.attack_ongoing and not any(
                        time.time() - self.cache[ip][1] <= self.time_window for ip in self.cache):
                    print("[INFO] ARP spoofing attack stopped")
                    self.attack_ongoing = False
                    self.attack_stopped.emit()

    def _sniff(self, stop_event):
        while not stop_event.is_set():
            sniff(prn=self._arp_spoof_detection, filter="arp", store=0, timeout=1)
