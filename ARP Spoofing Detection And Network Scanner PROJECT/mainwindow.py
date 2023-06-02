# This Python file uses the following encoding: utf-8
import csv
import json
import sys
import threading
import warnings
from concurrent.futures import ThreadPoolExecutor

from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtGui import QMouseEvent
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox

from NetworkScanner import NetworkScanner
from NetworkSniffer import Sniffer
from arp_spoof_detector import ArpSpoofDetector
from ui_form import Ui_MainWindow


# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py


class MainWindow(QMainWindow):
    update_UI_signal = QtCore.Signal(str)

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.Handel_Buttons()
        self.Handel_Window()
        # import
        self.detector = ArpSpoofDetector()
        self.scanner = NetworkScanner()
        self.sniffer = Sniffer()
        self.detection_on = False
        self.detector.attack_detected.connect(self.handle_attack_detected)
        self.detector.attack_stopped.connect(self.handle_attack_stopped)
        self.scanner.finished_signal.connect(self.On_Scan_finished)
        self.scanner.update_table.connect(self.update_table_widget)

        time_window = self.ui.timeWindowSpinBox.value()
        max_mac_changes = self.ui.maxMacChangesSpinBox.value()
        self.detector.set_time_window(time_window)
        self.detector.set_max_mac_changes(max_mac_changes)

        self.Scanner_on = False
        self.Sniffer_on = False

        warnings.filterwarnings("ignore", category=DeprecationWarning)

    def Handel_Window(self):
        self.draggable = True  # Flag to indicate whether the window can be dragged
        self.offset = None  # Offset from the top-left corner of the window to the cursor position
        flags = Qt.WindowFlags(Qt.CustomizeWindowHint | Qt.FramelessWindowHint)
        self.setWindowFlags(flags)
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.tableWidget.setColumnCount(5)
        self.ui.Filter_Edit.hide()
        self.ui.Filter_label.hide()
        self.ui.Target_Network.hide()
        self.ui.Target_label.hide()
        self.ui.Scan_Button.setEnabled(False)
        self.ui.Sniffer_Button.setEnabled(False)
        self.ui.stackedWidget.currentChanged.connect(self.stop_threads)
        ##self.ui.tableWidget.horizontal

    def Handel_Buttons(self):
        self.ui.exit.mousePressEvent = lambda event: self.confirmClose()
        self.ui.minim.mousePressEvent = lambda event: self.showMinimized()
        self.ui.PassiveWin.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.ScanWin.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.export_button.clicked.connect(self.export_results)
        self.ui.Start_Passive.clicked.connect(lambda: self.Handel_LightD())
        self.ui.Scan_Button.clicked.connect(lambda: self.Handel_NetworkScan())
        self.ui.Sniffer_Button.clicked.connect(lambda: self.Handel_NetworkSniffer())
        self.ui.scan_radio.toggled.connect(self.handle_button_click)
        self.ui.sniff_radio.toggled.connect(self.handle_button_click)
        self.ui.timeWindowSpinBox.valueChanged.connect(self.set_time_window)
        self.ui.maxMacChangesSpinBox.valueChanged.connect(self.set_max_mac_changes)

    def handle_button_click(self):
        if self.ui.scan_radio.isChecked():
            # Disable and Hide Sniffer items
            self.ui.Sniffer_Button.hide()
            self.ui.Filter_Edit.hide()
            self.ui.Filter_label.hide()
            self.ui.Sniffer_Button.setEnabled(False)
            # Enabled and Show Scanner items
            self.ui.Target_Network.show()
            self.ui.Target_label.show()
            self.ui.Scan_Button.show()
            self.ui.Scan_Button.setEnabled(True)

        elif self.ui.sniff_radio.isChecked():
            # Disable and Hide Scanner items
            self.ui.Scan_Button.hide()
            self.ui.Scan_Button.setEnabled(False)
            self.ui.Target_Network.hide()
            self.ui.Target_label.hide()
            # Enabled and Show Sniffer items
            self.ui.Filter_label.show()
            self.ui.Filter_Edit.show()
            self.ui.Sniffer_Button.show()
            self.ui.Sniffer_Button.setEnabled(True)

    def stop_threads(self):
        if self.detection_on:
            self.detector.stop_detection()
            self.detection_on = False
            self.ui.Start_Passive.setText("Start")
            self.ui.Start_labelP.setText("Passive Detection Stopped ")
            self.ui.maxMacChangesSpinBox.setValue(4)
            self.ui.timeWindowSpinBox.setValue(60)
        elif self.Scanner_on:
            self.scanner.stop_scan()
            self.ui.scan_radio.setEnabled(True)
            self.ui.sniff_radio.setEnabled(True)
            self.ui.Scan_Button.setText("Start Scan")
            self.Scanner_on = False
        elif self.Sniffer_on:
            self.sniffer.stop_sniffing()
            self.ui.scan_radio.setEnabled(True)
            self.ui.sniff_radio.setEnabled(True)

            def wait_for_thread():
                self.sniffer.thread.join()
                self.ui.Sniffer_Button.setText("Start Sniffer")
                self.Sniffer_on = False

            thread = threading.Thread(target=wait_for_thread)
            thread.daemon = True
            thread.start()

    def confirmClose(self):
        confirm = QMessageBox.question(self, 'Confirm Close', 'Are you sure you want to close the application?',
                                       QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.Yes:
            # Stop all running methods before exiting the application
            QtCore.QCoreApplication.instance().quit()
            sys.exit()

    def handle_attack_detected(self):
        self.ui.OutPut_labelP.setText("[ALERT] Possible ARP spoofing attack detected!")

    def handle_attack_stopped(self):
        self.ui.OutPut_labelP.setText("[INFO] ARP spoofing attack stopped")

    def set_time_window(self, time_window):
        self.detector.set_time_window(time_window)

    def set_max_mac_changes(self, max_mac_changes):
        self.detector.set_max_mac_changes(max_mac_changes)

    # here the method for the ARP Spoofing Passive Detected
    def Handel_LightD(self):
        if not self.detection_on:
            self.detector.start_detection()
            self.detection_on = True
            self.ui.Start_Passive.setText("Stop Passive Detection")
            self.ui.Start_labelP.setText("Passive Detection is running....")
        else:
            self.detector.stop_detection()
            self.detection_on = False
            self.ui.Start_Passive.setText("Start Passive Detection")
            self.ui.Start_labelP.setText("Passive Detection Stopped ")
            self.ui.OutPut_labelP.setText(" ")

    def Handel_ActiveD(self):
        pass

    def update_table_widget(self, results):
        self.ui.tableWidget.setRowCount(len(results))
        for row, result in enumerate(results):
            self.ui.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(result['IP']))
            self.ui.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(result['MAC Address'])))
            self.ui.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(result['Vendor Name']))
            self.ui.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(result['Host Name']))
            self.ui.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(result['Open Ports']))

    def Handel_NetworkScan(self):

        self.ui.tableWidget.setHorizontalHeaderLabels(
            ["IP address", "MAC Address", "Vendor Name", "Host Name", "Open Ports", ])
        if not self.Scanner_on:
            self.ui.scan_radio.setEnabled(False)
            self.ui.sniff_radio.setEnabled(False)
            self.ui.tableWidget.setRowCount(0)
            self.ui.tableWidget.setColumnCount(5)
            self.Scanner_on = True
            self.ui.Scan_Button.setText("Stop Scan")
            target_network = self.ui.Target_Network.text()
            with ThreadPoolExecutor() as executor:
                executor.submit(self.scanner.start_scan, target_network)


        else:
            self.scanner.stop_scan()
            self.Scanner_on = False
            self.ui.Scan_Button.setText("Start Scan")
            self.ui.scan_radio.setEnabled(True)
            self.ui.sniff_radio.setEnabled(True)

    def export_results(self):
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(self.ui.centralwidget, "Export Results", "",
                                                            "CSV Files (*.csv);;JSON Files (*.json)")
        if filename:
            results = []
            for row in range(self.ui.tableWidget.rowCount()):
                result = {}
                for column in range(self.ui.tableWidget.columnCount()):
                    result[self.ui.tableWidget.horizontalHeaderItem(column).text()] = self.ui.tableWidget.item(row,
                                                                                                               column).text()
                results.append(result)
            if filename.endswith(".csv"):
                with open(filename, "w", newline="") as file:
                    writer = csv.DictWriter(file, fieldnames=results[0].keys())
                    writer.writeheader()
                    writer.writerows(results)
            elif filename.endswith(".json"):
                with open(filename, "w") as file:
                    json.dump(results, file, indent=4)

    def On_Scan_finished(self):
        self.Scanner_on = False
        self.ui.Scan_Button.setText("Start Scan")
        self.ui.scan_radio.setEnabled(True)
        self.ui.sniff_radio.setEnabled(True)

    def Handel_NetworkSniffer(self):
        if not self.Sniffer_on:
            self.ui.scan_radio.setEnabled(False)
            self.ui.sniff_radio.setEnabled(False)
            self.ui.Sniffer_Button.setText("Stop Sniffer")
            self.ui.tableWidget.setRowCount(0)
            self.ui.tableWidget.setColumnCount(6)
            self.ui.tableWidget.setHorizontalHeaderLabels(
                ["timestamp", "Source", "Destination", "Protocol", "Length", "Info"])
            self.sniffer.update_time.connect(self.update_time_slot)
            self.sniffer.update_source.connect(self.update_source_slot)
            self.sniffer.update_destination.connect(self.update_destination_slot)
            self.sniffer.update_protocol.connect(self.update_protocol_slot)
            self.sniffer.update_length.connect(self.update_length_slot)
            self.sniffer.update_info.connect(self.update_info_slot)

            filter = self.ui.Filter_Edit.text()
            if filter != "":
                self.sniffer.filter = filter
            self.sniffer.start_sniffing()
            self.Sniffer_on = True
        else:
            self.sniffer.stop_sniffing()
            self.ui.scan_radio.setEnabled(True)
            self.ui.sniff_radio.setEnabled(True)

            def wait_for_thread():
                self.sniffer.thread.join()
                self.ui.Sniffer_Button.setText("Start Sniffer")
                self.Sniffer_on = False

            thread = threading.Thread(target=wait_for_thread)
            thread.daemon = True
            thread.start()

    @QtCore.Slot(str)
    def update_time_slot(self, time):
        row = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(row)
        self.ui.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(time))

    @QtCore.Slot(str)
    def update_source_slot(self, source):
        row = self.ui.tableWidget.rowCount() - 1
        self.ui.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(source))

    @QtCore.Slot(str)
    def update_destination_slot(self, destination):
        row = self.ui.tableWidget.rowCount() - 1
        self.ui.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(destination))

    @QtCore.Slot(str)
    def update_protocol_slot(self, protocol):
        row = self.ui.tableWidget.rowCount() - 1
        self.ui.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(protocol))

    @QtCore.Slot(int)
    def update_length_slot(self, length):
        row = self.ui.tableWidget.rowCount() - 1
        self.ui.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(length)))

    @QtCore.Slot(str)
    def update_info_slot(self, info):
        row = self.ui.tableWidget.rowCount() - 1
        self.ui.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(info))

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton and self.draggable:
            self.offset = event.pos()
            event.accept()

    def mouseMoveEvent(self, event: QMouseEvent):
        if self.offset is not None and self.draggable:
            self.move(self.pos() + event.pos() - self.offset)
            self.offset - event.pos()
            event.accept()

    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton and self.offset is not None:
            self.offset = None
            event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
