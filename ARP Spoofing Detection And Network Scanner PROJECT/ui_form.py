# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QDoubleSpinBox,
    QFrame, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QRadioButton, QSizePolicy, QSpinBox, QStackedWidget,
    QTabWidget, QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(900, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(900, 600))
        MainWindow.setMaximumSize(QSize(900, 600))
        palette = QPalette()
        brush = QBrush(QColor(20, 22, 24, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        MainWindow.setPalette(palette)
        MainWindow.setCursor(QCursor(Qt.ArrowCursor))
        MainWindow.setMouseTracking(False)
        MainWindow.setContextMenuPolicy(Qt.NoContextMenu)
        icon = QIcon()
        iconThemeName = u"applications-multimedia"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u"../../../Downloads/ARP.png", QSize(), QIcon.Normal, QIcon.Off)

        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(0.999900000000000)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"\n"
"\n"
"QMainWindow {\n"
"  background-color: #141618;\n"
"\n"
"}")
        MainWindow.setToolButtonStyle(Qt.ToolButtonIconOnly)
        MainWindow.setAnimated(False)
        MainWindow.setTabShape(QTabWidget.Rounded)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget {\n"
"background-color: #141618;\n"
"\n"
"\n"
"}")
        self.Burger = QLabel(self.centralwidget)
        self.Burger.setObjectName(u"Burger")
        self.Burger.setGeometry(QRect(20, 20, 31, 31))
        self.Burger.setStyleSheet(u".QLabel {\n"
"background: rgba(0,0,0,0.0);\n"
"}\n"
".QLabel:hover {\n"
"  background-color: #FC3666;\n"
"}")
        self.Burger.setPixmap(QPixmap(u"Assets/burger.png"))
        self.Burger.setScaledContents(True)
        self.title = QLabel(self.centralwidget)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(230, 10, 501, 41))
        self.title.setStyleSheet(u".QLabel#title{\n"
"font-family:Constantia;\n"
"font-size: 20px;\n"
"background: rgba(0,0,0,0.0);\n"
"text-align: center;\n"
"color:#5A6272;\n"
"}")
        self.exit = QLabel(self.centralwidget)
        self.exit.setObjectName(u"exit")
        self.exit.setGeometry(QRect(870, 10, 16, 16))
        self.exit.setStyleSheet(u".QLabel {\n"
"background: rgba(0,0,0,0.0);\n"
"}\n"
".QLabel:hover {\n"
"  background-color: #FC3666;\n"
"}")
        self.exit.setPixmap(QPixmap(u"Assets/cross.png"))
        self.exit.setScaledContents(True)
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 70, 901, 66))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.ScanWin = QPushButton(self.layoutWidget)
        self.ScanWin.setObjectName(u"ScanWin")
        self.ScanWin.setStyleSheet(u" .QPushButton#ScanWin{\n"
"\n"
"background-color: #141618; \n"
"border-radius: 1px;\n"
"border-bottom: 1px solid #FC3666;\n"
" color: #F5F5F5;\n"
" padding: 20px;\n"
" text-align: center;\n"
" text-decoration: none;\n"
" font-size: 16px;\n"
"\n"
"}\n"
"QPushButton#ScanWin:hover {\n"
" background-color: #FC3666;\n"
"}")

        self.gridLayout.addWidget(self.ScanWin, 0, 1, 1, 1)

        self.PassiveWin = QPushButton(self.layoutWidget)
        self.PassiveWin.setObjectName(u"PassiveWin")
        self.PassiveWin.setEnabled(True)
        font = QFont()
        font.setBold(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.PassiveWin.setFont(font)
        self.PassiveWin.setStyleSheet(u" .QPushButton#PassiveWin{\n"
"background-color: #141618; \n"
"border-radius: 1px;\n"
"border-bottom: 1px solid #FC3666;\n"
" color: #F5F5F5;\n"
" padding: 20px;\n"
" text-align: center;\n"
" text-decoration: none;\n"
" font-size: 16px;\n"
"}\n"
"QPushButton#PassiveWin:hover {\n"
" background-color: #FC3666;\n"
"}")
        self.PassiveWin.setAutoDefault(False)

        self.gridLayout.addWidget(self.PassiveWin, 0, 0, 1, 1)

        self.PassiveWin.raise_()
        self.ScanWin.raise_()
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setGeometry(QRect(10, 140, 881, 461))
        self.PassiveD = QWidget()
        self.PassiveD.setObjectName(u"PassiveD")
        self.Start_Passive = QPushButton(self.PassiveD)
        self.Start_Passive.setObjectName(u"Start_Passive")
        self.Start_Passive.setEnabled(True)
        self.Start_Passive.setGeometry(QRect(330, 190, 221, 80))
        self.Start_Passive.setStyleSheet(u" .QPushButton#Start_Passive{\n"
"\n"
"background-color: #141618; \n"
"border-radius: 1px;\n"
"border-bottom: 2px solid #FC3666;\n"
" color: #F5F5F5;\n"
" padding: 20px;\n"
" text-align: center;\n"
" text-decoration: none;\n"
" font-size: 16px;\n"
"}\n"
"QPushButton#Start_Passive:hover {\n"
" background-color: #FC3666;\n"
"}")
        self.Start_labelP = QLabel(self.PassiveD)
        self.Start_labelP.setObjectName(u"Start_labelP")
        self.Start_labelP.setGeometry(QRect(310, 40, 251, 61))
        self.Start_labelP.setStyleSheet(u"QLabel#Start_labelP{\n"
" color: #F5F5F5;\n"
" padding: 20px;\n"
" text-align: center;\n"
" text-decoration: none;\n"
" font-size: 16px;\n"
"}")
        self.OutPut_labelP = QLabel(self.PassiveD)
        self.OutPut_labelP.setObjectName(u"OutPut_labelP")
        self.OutPut_labelP.setGeometry(QRect(260, 100, 361, 91))
        self.OutPut_labelP.setStyleSheet(u".QLabel#OutPut_labelP{\n"
"border-radius: 1px;\n"
" color: rgb(255, 0, 0);\n"
" padding: 20px;\n"
" font-size: 16px;\n"
"}\n"
"")
        self.maxMacChangesSpinBox = QSpinBox(self.PassiveD)
        self.maxMacChangesSpinBox.setObjectName(u"maxMacChangesSpinBox")
        self.maxMacChangesSpinBox.setGeometry(QRect(410, 360, 51, 25))
        self.maxMacChangesSpinBox.setStyleSheet(u" .QSpinBox#maxMacChangesSpinBox{\n"
"border: 0.5px solid #FC3666;\n"
" color: #F5F5F5;\n"
"}")
        self.maxMacChangesSpinBox.setFrame(True)
        self.maxMacChangesSpinBox.setValue(4)
        self.timeWindowSpinBox = QDoubleSpinBox(self.PassiveD)
        self.timeWindowSpinBox.setObjectName(u"timeWindowSpinBox")
        self.timeWindowSpinBox.setGeometry(QRect(410, 300, 51, 25))
        self.timeWindowSpinBox.setLayoutDirection(Qt.LeftToRight)
        self.timeWindowSpinBox.setAutoFillBackground(False)
        self.timeWindowSpinBox.setStyleSheet(u" .QDoubleSpinBox#timeWindowSpinBox{\n"
"border: 0.5px solid #FC3666;\n"
"color: #F5F5F5;\n"
"}")
        self.timeWindowSpinBox.setWrapping(False)
        self.timeWindowSpinBox.setFrame(True)
        self.timeWindowSpinBox.setReadOnly(False)
        self.timeWindowSpinBox.setAccelerated(False)
        self.timeWindowSpinBox.setValue(60.000000000000000)
        self.MaxMacLabel = QLabel(self.PassiveD)
        self.MaxMacLabel.setObjectName(u"MaxMacLabel")
        self.MaxMacLabel.setGeometry(QRect(370, 340, 111, 16))
        self.MaxMacLabel.setStyleSheet(u".QLabel#MaxMacLabel{\n"
"border-radius: 1px;\n"
" color: #F5F5F5; \n"
"}\n"
"")
        self.TimeWindowLabel = QLabel(self.PassiveD)
        self.TimeWindowLabel.setObjectName(u"TimeWindowLabel")
        self.TimeWindowLabel.setGeometry(QRect(390, 280, 101, 16))
        self.TimeWindowLabel.setStyleSheet(u".QLabel#TimeWindowLabel{\n"
"border-radius: 1px;\n"
" color: #F5F5F5; \n"
"}\n"
"")
        self.stackedWidget.addWidget(self.PassiveD)
        self.Newtwork_Scanner = QWidget()
        self.Newtwork_Scanner.setObjectName(u"Newtwork_Scanner")
        self.Scan_Button = QPushButton(self.Newtwork_Scanner)
        self.Scan_Button.setObjectName(u"Scan_Button")
        self.Scan_Button.setGeometry(QRect(700, 190, 181, 61))
        self.Scan_Button.setStyleSheet(u"  .QPushButton#Scan_Button{\n"
"\n"
"background-color: #141618; \n"
"border-radius: 1px;\n"
"border-bottom: 1px solid #FC3666;\n"
" color: #F5F5F5;\n"
" padding: 20px;\n"
" text-align: center;\n"
" text-decoration: none;\n"
" font-size: 16px;\n"
"}\n"
"QPushButton#Scan_Button:hover {\n"
" background-color: #FC3666;\n"
"}")
        self.tableWidget = QTableWidget(self.Newtwork_Scanner)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        icon1 = QIcon()
        iconThemeName = u"audio-card"
        if QIcon.hasThemeIcon(iconThemeName):
            icon1 = QIcon.fromTheme(iconThemeName)
        else:
            icon1.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setIcon(icon1);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setEnabled(True)
        self.tableWidget.setGeometry(QRect(10, 30, 680, 425))
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QSize(680, 425))
        self.tableWidget.setMaximumSize(QSize(680, 425))
        self.tableWidget.setStyleSheet(u" .QTableWidget{\n"
"\n"
"background-color: #141618; \n"
"border-radius: 1px;\n"
"border-bottom: 1px solid #FC3666;\n"
" color: #F5F5F5;\n"
"\n"
"}\n"
"QTableWidget::item:selected {\n"
"        background-color: #c3daf9;\n"
"    }\n"
"\n"
"    QHeaderView::section {\n"
"     background-color: #141618; \n"
"     border: none;\n"
"     border-right: 1px #FC3666;\n"
"     border-bottom: 1px solid #FC3666;\n"
"     border-radius: 1px;\n"
"	color: #F5F5F5;\n"
" 	padding: 6px;\n"
" 	font-size: 13px;\n"
"    }\n"
"\n"
" \n"
"    QHeaderView::section:last {\n"
"        border-right: none;\n"
"    }\n"
"\n"
"    QHeaderView::section:horizontal {\n"
"        height: 40px;\n"
"    }\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"    QTableWidget::item {\n"
"        padding: 6px;\n"
"		border-bottom: 1px solid #FC3666;\n"
" 		font-size: 6px;\n"
"    }\n"
"\n"
"   ")
        self.tableWidget.setFrameShape(QFrame.Box)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tableWidget.setAutoScrollMargin(10)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setTabKeyNavigation(False)
        self.tableWidget.setProperty("showDropIndicator", False)
        self.tableWidget.setDragDropOverwriteMode(False)
        self.tableWidget.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableWidget.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(135)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(135)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setMinimumSectionSize(30)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.Target_Network = QLineEdit(self.Newtwork_Scanner)
        self.Target_Network.setObjectName(u"Target_Network")
        self.Target_Network.setGeometry(QRect(700, 40, 171, 24))
        self.Target_Network.setStyleSheet(u" .QLineEdit#Target_Network{\n"
"\n"
"\n"
"border-radius: 1px;\n"
"border: 1px solid #FC3666;\n"
" color: #F5F5F5;\n"
"\n"
"\n"
"\n"
" font-size: 12px;\n"
"}\n"
"")
        self.export_button = QPushButton(self.Newtwork_Scanner)
        self.export_button.setObjectName(u"export_button")
        self.export_button.setGeometry(QRect(720, 290, 131, 31))
        self.export_button.setStyleSheet(u"  .QPushButton#export_button{\n"
"\n"
"background-color: #141618; \n"
"border-radius: 1px;\n"
"border-bottom: 1px solid #FC3666;\n"
" color: #F5F5F5;\n"
" text-align: center;\n"
" text-decoration: none;\n"
" font-size: 16px;\n"
"}\n"
"QPushButton#export_button:hover {\n"
" background-color: #FC3666;\n"
"}")
        self.horizontalLayoutWidget = QWidget(self.Newtwork_Scanner)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(690, 140, 191, 41))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.scan_radio = QRadioButton(self.horizontalLayoutWidget)
        self.scan_radio.setObjectName(u"scan_radio")
        self.scan_radio.setEnabled(True)
        self.scan_radio.setStyleSheet(u" .QRadioButton#scan_radio{\n"
"border-radius: 1px;\n"
" color: #F5F5F5;\n"
" font-size: 12px;\n"
"}")
        self.scan_radio.setCheckable(True)
        self.scan_radio.setChecked(False)
        self.scan_radio.setAutoExclusive(True)

        self.horizontalLayout.addWidget(self.scan_radio)

        self.sniff_radio = QRadioButton(self.horizontalLayoutWidget)
        self.sniff_radio.setObjectName(u"sniff_radio")
        self.sniff_radio.setEnabled(True)
        self.sniff_radio.setStyleSheet(u" .QRadioButton#sniff_radio{\n"
"border-radius: 1px;\n"
" color: #F5F5F5;\n"
" font-size: 12px;\n"
"}")
        self.sniff_radio.setCheckable(True)
        self.sniff_radio.setChecked(False)

        self.horizontalLayout.addWidget(self.sniff_radio)

        self.Filter_Edit = QLineEdit(self.Newtwork_Scanner)
        self.Filter_Edit.setObjectName(u"Filter_Edit")
        self.Filter_Edit.setGeometry(QRect(700, 40, 171, 24))
        self.Filter_Edit.setStyleSheet(u" .QLineEdit#Filter_Edit{\n"
"border-radius: 1px;\n"
"border: 1px solid #FC3666;\n"
"color: #F5F5F5;\n"
"font-size: 12px;\n"
"}\n"
"")
        self.Filter_Edit.setFrame(True)
        self.Sniffer_Button = QPushButton(self.Newtwork_Scanner)
        self.Sniffer_Button.setObjectName(u"Sniffer_Button")
        self.Sniffer_Button.setGeometry(QRect(701, 190, 181, 61))
        self.Sniffer_Button.setStyleSheet(u"  .QPushButton#Sniffer_Button{\n"
"\n"
"background-color: #141618; \n"
"border-radius: 1px;\n"
"border-bottom: 1px solid #FC3666;\n"
" color: #F5F5F5;\n"
" padding: 20px;\n"
" text-align: center;\n"
" text-decoration: none;\n"
" font-size: 16px;\n"
"}\n"
"QPushButton#Sniffer_Button:hover {\n"
" background-color: #FC3666;\n"
"}")
        self.Filter_label = QLabel(self.Newtwork_Scanner)
        self.Filter_label.setObjectName(u"Filter_label")
        self.Filter_label.setGeometry(QRect(700, 20, 49, 16))
        self.Filter_label.setStyleSheet(u" .QLabel#Filter_label{\n"
"border-radius: 1px;\n"
" color: #F5F5F5;\n"
" font-size: 12px;\n"
"}\n"
"")
        self.Target_label = QLabel(self.Newtwork_Scanner)
        self.Target_label.setObjectName(u"Target_label")
        self.Target_label.setGeometry(QRect(700, 20, 141, 20))
        self.Target_label.setStyleSheet(u" .QLabel#Target_label{\n"
"border-radius: 1px;\n"
" color: #F5F5F5;\n"
" font-size: 12px;\n"
"}\n"
"")
        self.stackedWidget.addWidget(self.Newtwork_Scanner)
        self.tableWidget.raise_()
        self.Target_Network.raise_()
        self.export_button.raise_()
        self.horizontalLayoutWidget.raise_()
        self.Filter_Edit.raise_()
        self.Sniffer_Button.raise_()
        self.Scan_Button.raise_()
        self.Filter_label.raise_()
        self.Target_label.raise_()
        self.minim = QLabel(self.centralwidget)
        self.minim.setObjectName(u"minim")
        self.minim.setGeometry(QRect(840, 10, 16, 16))
        self.minim.setStyleSheet(u".QLabel {\n"
"background: rgba(0,0,0,0.0);\n"
"}\n"
".QLabel:hover {\n"
"  background-color: #FC3666;\n"
"}")
        self.minim.setPixmap(QPixmap(u"Assets/minimize-sign.png"))
        self.minim.setScaledContents(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.stackedWidget.raise_()
        self.title.raise_()
        self.Burger.raise_()
        self.exit.raise_()
        self.layoutWidget.raise_()
        self.minim.raise_()
        QWidget.setTabOrder(self.ScanWin, self.PassiveWin)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u" ARP Spoofing Detected And Personal Network Scanner", None))
#if QT_CONFIG(accessibility)
        MainWindow.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        MainWindow.setWindowFilePath("")
        self.Burger.setText("")
        self.title.setText(QCoreApplication.translate("MainWindow", u" ARP Spoofing Detection And  Network Scanner", None))
        self.exit.setText("")
        self.ScanWin.setText(QCoreApplication.translate("MainWindow", u"Network Scanner", None))
        self.PassiveWin.setText(QCoreApplication.translate("MainWindow", u"Passive Detection", None))
        self.Start_Passive.setText(QCoreApplication.translate("MainWindow", u"Start Passive Detection", None))
        self.Start_labelP.setText("")
        self.OutPut_labelP.setText("")
        self.MaxMacLabel.setText(QCoreApplication.translate("MainWindow", u"Max Mac Changes :", None))
        self.TimeWindowLabel.setText(QCoreApplication.translate("MainWindow", u"Time Window :", None))
        self.Scan_Button.setText(QCoreApplication.translate("MainWindow", u"Start Scan", None))
#if QT_CONFIG(tooltip)
        self.Target_Network.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>&quot;Enter the target network in CIDR notation (e.g., 192.168.1.0/24). If left blank, the default value 192.168.1.1/24 will be used.&quot;</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.Target_Network.setText(QCoreApplication.translate("MainWindow", u"192.168.1.1/24", None))
        self.export_button.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.scan_radio.setText(QCoreApplication.translate("MainWindow", u"Scan Network", None))
        self.sniff_radio.setText(QCoreApplication.translate("MainWindow", u"Sniff traffic", None))
        self.Sniffer_Button.setText(QCoreApplication.translate("MainWindow", u"Start Sniffer", None))
        self.Filter_label.setText(QCoreApplication.translate("MainWindow", u"Filter:", None))
        self.Target_label.setText(QCoreApplication.translate("MainWindow", u"Target IP Address Range:", None))
        self.minim.setText("")
    # retranslateUi

