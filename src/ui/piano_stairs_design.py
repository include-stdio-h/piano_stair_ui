# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui\piano_stairs_design.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ToolBar = QtWidgets.QLabel(self.centralwidget)
        self.ToolBar.setGeometry(QtCore.QRect(20, 40, 171, 391))
        self.ToolBar.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"")
        self.ToolBar.setText("")
        self.ToolBar.setObjectName("ToolBar")
        self.BlueToothButton = QtWidgets.QPushButton(self.centralwidget)
        self.BlueToothButton.setEnabled(True)
        self.BlueToothButton.setGeometry(QtCore.QRect(80, 90, 90, 30))
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        font.setPointSize(11)
        self.BlueToothButton.setFont(font)
        self.BlueToothButton.setToolTipDuration(-15)
        self.BlueToothButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.BlueToothButton.setAutoFillBackground(False)
        self.BlueToothButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style: outset;")
        self.BlueToothButton.setInputMethodHints(QtCore.Qt.ImhNone)
        self.BlueToothButton.setShortcut("")
        self.BlueToothButton.setCheckable(False)
        self.BlueToothButton.setAutoExclusive(False)
        self.BlueToothButton.setAutoRepeatInterval(100)
        self.BlueToothButton.setAutoDefault(False)
        self.BlueToothButton.setDefault(False)
        self.BlueToothButton.setFlat(True)
        self.BlueToothButton.setObjectName("BlueToothButton")
        self.InstrumentButton = QtWidgets.QPushButton(self.centralwidget)
        self.InstrumentButton.setGeometry(QtCore.QRect(80, 160, 90, 30))
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        font.setPointSize(11)
        self.InstrumentButton.setFont(font)
        self.InstrumentButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style: outset;")
        self.InstrumentButton.setShortcut("")
        self.InstrumentButton.setFlat(True)
        self.InstrumentButton.setObjectName("InstrumentButton")
        self.BlueToothIcon = QtWidgets.QLabel(self.centralwidget)
        self.BlueToothIcon.setGeometry(QtCore.QRect(40, 94, 21, 21))
        self.BlueToothIcon.setStyleSheet("")
        self.BlueToothIcon.setText("")
        self.BlueToothIcon.setPixmap(QtGui.QPixmap("style/icons/bluetooth.png"))
        self.BlueToothIcon.setScaledContents(True)
        self.BlueToothIcon.setObjectName("BlueToothIcon")
        self.InstrumentIcon = QtWidgets.QLabel(self.centralwidget)
        self.InstrumentIcon.setGeometry(QtCore.QRect(36, 160, 28, 28))
        self.InstrumentIcon.setText("")
        self.InstrumentIcon.setPixmap(QtGui.QPixmap("style/icons/live-music.png"))
        self.InstrumentIcon.setScaledContents(True)
        self.InstrumentIcon.setObjectName("InstrumentIcon")
        self.QuitButton = QtWidgets.QPushButton(self.centralwidget)
        self.QuitButton.setGeometry(QtCore.QRect(80, 370, 41, 41))
        self.QuitButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("style/icons/power-on.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.QuitButton.setIcon(icon)
        self.QuitButton.setIconSize(QtCore.QSize(32, 32))
        self.QuitButton.setShortcut("")
        self.QuitButton.setCheckable(False)
        self.QuitButton.setFlat(True)
        self.QuitButton.setObjectName("QuitButton")
        self.WorkSpace = QtWidgets.QStackedWidget(self.centralwidget)
        self.WorkSpace.setGeometry(QtCore.QRect(210, 10, 631, 531))
        self.WorkSpace.setObjectName("WorkSpace")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.DeviceStatus = QtWidgets.QLabel(self.page)
        self.DeviceStatus.setGeometry(QtCore.QRect(10, 30, 331, 141))
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        font.setPointSize(22)
        self.DeviceStatus.setFont(font)
        self.DeviceStatus.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"background-color: rgb(255, 100,100);")
        self.DeviceStatus.setText("")
        self.DeviceStatus.setAlignment(QtCore.Qt.AlignCenter)
        self.DeviceStatus.setObjectName("DeviceStatus")
        self.LoggerBack = QtWidgets.QLabel(self.page)
        self.LoggerBack.setGeometry(QtCore.QRect(10, 200, 331, 221))
        self.LoggerBack.setAutoFillBackground(False)
        self.LoggerBack.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"")
        self.LoggerBack.setText("")
        self.LoggerBack.setObjectName("LoggerBack")
        self.DeviceStatusIcon = QtWidgets.QLabel(self.page)
        self.DeviceStatusIcon.setGeometry(QtCore.QRect(160, 110, 41, 41))
        self.DeviceStatusIcon.setStyleSheet("background-color: rgb(255, 100,100);")
        self.DeviceStatusIcon.setText("")
        self.DeviceStatusIcon.setPixmap(QtGui.QPixmap("style/icons/disable.png"))
        self.DeviceStatusIcon.setScaledContents(True)
        self.DeviceStatusIcon.setObjectName("DeviceStatusIcon")
        self.DeviceStatusLabel = QtWidgets.QLabel(self.page)
        self.DeviceStatusLabel.setGeometry(QtCore.QRect(100, 40, 161, 61))
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        font.setPointSize(26)
        self.DeviceStatusLabel.setFont(font)
        self.DeviceStatusLabel.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 100,100);")
        self.DeviceStatusLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.DeviceStatusLabel.setObjectName("DeviceStatusLabel")
        self.StatusBar = QtWidgets.QLabel(self.page)
        self.StatusBar.setGeometry(QtCore.QRect(360, 30, 201, 391))
        self.StatusBar.setMinimumSize(QtCore.QSize(0, 45))
        self.StatusBar.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"")
        self.StatusBar.setText("")
        self.StatusBar.setObjectName("StatusBar")
        self.Status2 = QtWidgets.QLabel(self.page)
        self.Status2.setGeometry(QtCore.QRect(470, 70, 61, 61))
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        font.setPointSize(20)
        self.Status2.setFont(font)
        self.Status2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Status2.setStyleSheet("border-radius: 20px;\n"
"background-color: rgb(234, 234, 234);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.Status2.setAlignment(QtCore.Qt.AlignCenter)
        self.Status2.setObjectName("Status2")
        self.Status1 = QtWidgets.QLabel(self.page)
        self.Status1.setGeometry(QtCore.QRect(390, 70, 61, 61))
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        font.setPointSize(20)
        self.Status1.setFont(font)
        self.Status1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Status1.setStyleSheet("border-radius: 20px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(234, 234, 234);")
        self.Status1.setAlignment(QtCore.Qt.AlignCenter)
        self.Status1.setObjectName("Status1")
        self.Status3 = QtWidgets.QLabel(self.page)
        self.Status3.setGeometry(QtCore.QRect(390, 150, 61, 61))
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        font.setPointSize(20)
        self.Status3.setFont(font)
        self.Status3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Status3.setStyleSheet("border-radius: 20px;\n"
"background-color: rgb(234, 234, 234);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.Status3.setAlignment(QtCore.Qt.AlignCenter)
        self.Status3.setObjectName("Status3")
        self.Status4 = QtWidgets.QLabel(self.page)
        self.Status4.setGeometry(QtCore.QRect(470, 150, 61, 61))
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        font.setPointSize(20)
        self.Status4.setFont(font)
        self.Status4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Status4.setStyleSheet("border-radius: 20px;\n"
"background-color: rgb(234, 234, 234);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.Status4.setAlignment(QtCore.Qt.AlignCenter)
        self.Status4.setObjectName("Status4")
        self.Status5 = QtWidgets.QLabel(self.page)
        self.Status5.setGeometry(QtCore.QRect(390, 230, 61, 61))
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        font.setPointSize(20)
        self.Status5.setFont(font)
        self.Status5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Status5.setStyleSheet("border-radius: 20px;\n"
"background-color: rgb(234, 234, 234);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.Status5.setAlignment(QtCore.Qt.AlignCenter)
        self.Status5.setObjectName("Status5")
        self.Status6 = QtWidgets.QLabel(self.page)
        self.Status6.setGeometry(QtCore.QRect(470, 230, 61, 61))
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        font.setPointSize(20)
        self.Status6.setFont(font)
        self.Status6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Status6.setStyleSheet("border-radius: 20px;\n"
"background-color: rgb(234, 234, 234);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.Status6.setAlignment(QtCore.Qt.AlignCenter)
        self.Status6.setObjectName("Status6")
        self.Status7 = QtWidgets.QLabel(self.page)
        self.Status7.setGeometry(QtCore.QRect(390, 310, 61, 61))
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        font.setPointSize(20)
        self.Status7.setFont(font)
        self.Status7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Status7.setStyleSheet("border-radius: 20px;\n"
"background-color: rgb(234, 234, 234);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.Status7.setAlignment(QtCore.Qt.AlignCenter)
        self.Status7.setObjectName("Status7")
        self.Status8 = QtWidgets.QLabel(self.page)
        self.Status8.setGeometry(QtCore.QRect(470, 310, 61, 61))
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        font.setPointSize(20)
        self.Status8.setFont(font)
        self.Status8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Status8.setStyleSheet("border-radius: 20px;\n"
"background-color: rgb(234, 234, 234);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.Status8.setAlignment(QtCore.Qt.AlignCenter)
        self.Status8.setObjectName("Status8")
        self.Logger = QtWidgets.QLabel(self.page)
        self.Logger.setGeometry(QtCore.QRect(30, 220, 291, 181))
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        font.setPointSize(12)
        self.Logger.setFont(font)
        self.Logger.setStyleSheet("border-radius : 15px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(174, 255, 242);\n"
"")
        self.Logger.setAlignment(QtCore.Qt.AlignCenter)
        self.Logger.setObjectName("Logger")
        self.WorkSpace.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.OrganBack = QtWidgets.QLabel(self.page_2)
        self.OrganBack.setGeometry(QtCore.QRect(210, 30, 171, 161))
        self.OrganBack.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"")
        self.OrganBack.setText("")
        self.OrganBack.setObjectName("OrganBack")
        self.AccordionBack = QtWidgets.QLabel(self.page_2)
        self.AccordionBack.setGeometry(QtCore.QRect(400, 30, 171, 161))
        self.AccordionBack.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"")
        self.AccordionBack.setText("")
        self.AccordionBack.setObjectName("AccordionBack")
        self.HarpBack = QtWidgets.QLabel(self.page_2)
        self.HarpBack.setGeometry(QtCore.QRect(210, 230, 171, 161))
        self.HarpBack.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"")
        self.HarpBack.setText("")
        self.HarpBack.setObjectName("HarpBack")
        self.VibraPhoneBack = QtWidgets.QLabel(self.page_2)
        self.VibraPhoneBack.setGeometry(QtCore.QRect(400, 230, 171, 161))
        self.VibraPhoneBack.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"")
        self.VibraPhoneBack.setText("")
        self.VibraPhoneBack.setObjectName("VibraPhoneBack")
        self.PianoBack = QtWidgets.QLabel(self.page_2)
        self.PianoBack.setGeometry(QtCore.QRect(20, 230, 171, 161))
        self.PianoBack.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"")
        self.PianoBack.setText("")
        self.PianoBack.setObjectName("PianoBack")
        self.BassGuitarSelect = QtWidgets.QPushButton(self.page_2)
        self.BassGuitarSelect.setGeometry(QtCore.QRect(25, 35, 160, 151))
        self.BassGuitarSelect.setAutoFillBackground(False)
        self.BassGuitarSelect.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"")
        self.BassGuitarSelect.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("style/icons/guitar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BassGuitarSelect.setIcon(icon1)
        self.BassGuitarSelect.setIconSize(QtCore.QSize(100, 100))
        self.BassGuitarSelect.setFlat(True)
        self.BassGuitarSelect.setObjectName("BassGuitarSelect")
        self.BassGuitarBack = QtWidgets.QLabel(self.page_2)
        self.BassGuitarBack.setGeometry(QtCore.QRect(20, 30, 171, 161))
        self.BassGuitarBack.setStyleSheet("border-radius: 20px;\n"
"background-color: rgb(182, 182, 182);\n"
"")
        self.BassGuitarBack.setText("")
        self.BassGuitarBack.setObjectName("BassGuitarBack")
        self.OrganSelect = QtWidgets.QPushButton(self.page_2)
        self.OrganSelect.setGeometry(QtCore.QRect(215, 35, 160, 151))
        self.OrganSelect.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"")
        self.OrganSelect.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("style/icons/organ.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.OrganSelect.setIcon(icon2)
        self.OrganSelect.setIconSize(QtCore.QSize(100, 100))
        self.OrganSelect.setFlat(True)
        self.OrganSelect.setObjectName("OrganSelect")
        self.AccordionSelect = QtWidgets.QPushButton(self.page_2)
        self.AccordionSelect.setGeometry(QtCore.QRect(405, 35, 160, 151))
        self.AccordionSelect.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"")
        self.AccordionSelect.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("style/icons/accordion.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AccordionSelect.setIcon(icon3)
        self.AccordionSelect.setIconSize(QtCore.QSize(100, 100))
        self.AccordionSelect.setFlat(True)
        self.AccordionSelect.setObjectName("AccordionSelect")
        self.PianoSelect = QtWidgets.QPushButton(self.page_2)
        self.PianoSelect.setGeometry(QtCore.QRect(25, 235, 160, 151))
        self.PianoSelect.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"")
        self.PianoSelect.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("style/icons/piano.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PianoSelect.setIcon(icon4)
        self.PianoSelect.setIconSize(QtCore.QSize(100, 100))
        self.PianoSelect.setFlat(True)
        self.PianoSelect.setObjectName("PianoSelect")
        self.HarpSelect = QtWidgets.QPushButton(self.page_2)
        self.HarpSelect.setGeometry(QtCore.QRect(215, 235, 160, 151))
        self.HarpSelect.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"")
        self.HarpSelect.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("style/icons/harp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.HarpSelect.setIcon(icon5)
        self.HarpSelect.setIconSize(QtCore.QSize(100, 100))
        self.HarpSelect.setFlat(True)
        self.HarpSelect.setObjectName("HarpSelect")
        self.VibraPhoneSelect = QtWidgets.QPushButton(self.page_2)
        self.VibraPhoneSelect.setGeometry(QtCore.QRect(405, 235, 160, 151))
        self.VibraPhoneSelect.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"")
        self.VibraPhoneSelect.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("style/icons/vibraphone.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.VibraPhoneSelect.setIcon(icon6)
        self.VibraPhoneSelect.setIconSize(QtCore.QSize(100, 100))
        self.VibraPhoneSelect.setFlat(True)
        self.VibraPhoneSelect.setObjectName("VibraPhoneSelect")
        self.InstrumentTheme = QtWidgets.QLabel(self.page_2)
        self.InstrumentTheme.setGeometry(QtCore.QRect(80, 90, 41, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.InstrumentTheme.sizePolicy().hasHeightForWidth())
        self.InstrumentTheme.setSizePolicy(sizePolicy)
        self.InstrumentTheme.setStyleSheet("border-radius: 20px;\n"
"background-color: rgb(255, 195, 56);")
        self.InstrumentTheme.setText("")
        self.InstrumentTheme.setObjectName("InstrumentTheme")
        self.InstrumentTheme.raise_()
        self.OrganBack.raise_()
        self.AccordionBack.raise_()
        self.HarpBack.raise_()
        self.VibraPhoneBack.raise_()
        self.PianoBack.raise_()
        self.BassGuitarBack.raise_()
        self.BassGuitarSelect.raise_()
        self.OrganSelect.raise_()
        self.AccordionSelect.raise_()
        self.PianoSelect.raise_()
        self.HarpSelect.raise_()
        self.VibraPhoneSelect.raise_()
        self.WorkSpace.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.KeySettingBar = QtWidgets.QLabel(self.page_3)
        self.KeySettingBar.setGeometry(QtCore.QRect(300, 30, 431, 391))
        self.KeySettingBar.setStyleSheet("border-radius: 20px;\n"
"background-color: rgb(255, 255, 255);")
        self.KeySettingBar.setText("")
        self.KeySettingBar.setObjectName("KeySettingBar")
        self.StatusBar_2 = QtWidgets.QLabel(self.page_3)
        self.StatusBar_2.setGeometry(QtCore.QRect(20, 30, 201, 391))
        self.StatusBar_2.setMinimumSize(QtCore.QSize(0, 45))
        self.StatusBar_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"")
        self.StatusBar_2.setText("")
        self.StatusBar_2.setObjectName("StatusBar_2")
        self.KeySettingButton1 = QtWidgets.QPushButton(self.page_3)
        self.KeySettingButton1.setGeometry(QtCore.QRect(50, 80, 61, 61))
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        font.setPointSize(20)
        self.KeySettingButton1.setFont(font)
        self.KeySettingButton1.setStyleSheet("border-radius: 20px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(234, 234, 234);")
        self.KeySettingButton1.setFlat(True)
        self.KeySettingButton1.setObjectName("KeySettingButton1")
        self.KeySettingButton3 = QtWidgets.QPushButton(self.page_3)
        self.KeySettingButton3.setGeometry(QtCore.QRect(50, 160, 61, 61))
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        font.setPointSize(20)
        self.KeySettingButton3.setFont(font)
        self.KeySettingButton3.setStyleSheet("border-radius: 20px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(234, 234, 234);")
        self.KeySettingButton3.setFlat(True)
        self.KeySettingButton3.setObjectName("KeySettingButton3")
        self.KeySettingButton5 = QtWidgets.QPushButton(self.page_3)
        self.KeySettingButton5.setGeometry(QtCore.QRect(50, 240, 61, 61))
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        font.setPointSize(20)
        self.KeySettingButton5.setFont(font)
        self.KeySettingButton5.setStyleSheet("border-radius: 20px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(234, 234, 234);")
        self.KeySettingButton5.setFlat(True)
        self.KeySettingButton5.setObjectName("KeySettingButton5")
        self.KeySettingButton7 = QtWidgets.QPushButton(self.page_3)
        self.KeySettingButton7.setGeometry(QtCore.QRect(50, 320, 61, 61))
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        font.setPointSize(20)
        self.KeySettingButton7.setFont(font)
        self.KeySettingButton7.setStyleSheet("border-radius: 20px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(234, 234, 234);")
        self.KeySettingButton7.setFlat(True)
        self.KeySettingButton7.setObjectName("KeySettingButton7")
        self.KeySettingButton8 = QtWidgets.QPushButton(self.page_3)
        self.KeySettingButton8.setGeometry(QtCore.QRect(130, 320, 61, 61))
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        font.setPointSize(20)
        self.KeySettingButton8.setFont(font)
        self.KeySettingButton8.setStyleSheet("border-radius: 20px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(234, 234, 234);")
        self.KeySettingButton8.setFlat(True)
        self.KeySettingButton8.setObjectName("KeySettingButton8")
        self.KeySettingButton4 = QtWidgets.QPushButton(self.page_3)
        self.KeySettingButton4.setGeometry(QtCore.QRect(130, 160, 61, 61))
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        font.setPointSize(20)
        self.KeySettingButton4.setFont(font)
        self.KeySettingButton4.setStyleSheet("border-radius: 20px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(234, 234, 234);")
        self.KeySettingButton4.setFlat(True)
        self.KeySettingButton4.setObjectName("KeySettingButton4")
        self.KeySettingButton2 = QtWidgets.QPushButton(self.page_3)
        self.KeySettingButton2.setGeometry(QtCore.QRect(130, 80, 61, 61))
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        font.setPointSize(20)
        self.KeySettingButton2.setFont(font)
        self.KeySettingButton2.setStyleSheet("border-radius: 20px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(234, 234, 234);")
        self.KeySettingButton2.setFlat(True)
        self.KeySettingButton2.setObjectName("KeySettingButton2")
        self.KeySettingButton6 = QtWidgets.QPushButton(self.page_3)
        self.KeySettingButton6.setGeometry(QtCore.QRect(130, 240, 61, 61))
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        font.setPointSize(20)
        self.KeySettingButton6.setFont(font)
        self.KeySettingButton6.setStyleSheet("border-radius: 20px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(234, 234, 234);")
        self.KeySettingButton6.setFlat(True)
        self.KeySettingButton6.setObjectName("KeySettingButton6")
        self.SelectDo = QtWidgets.QPushButton(self.page_3)
        self.SelectDo.setGeometry(QtCore.QRect(330, 80, 60, 60))
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        font.setPointSize(13)
        self.SelectDo.setFont(font)
        self.SelectDo.setStyleSheet("border-radius: 30px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(234, 234, 234);")
        self.SelectDo.setFlat(True)
        self.SelectDo.setObjectName("SelectDo")
        self.SelectRe = QtWidgets.QPushButton(self.page_3)
        self.SelectRe.setGeometry(QtCore.QRect(410, 80, 60, 60))
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        font.setPointSize(13)
        self.SelectRe.setFont(font)
        self.SelectRe.setStyleSheet("border-radius: 30px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(234, 234, 234);")
        self.SelectRe.setFlat(True)
        self.SelectRe.setObjectName("SelectRe")
        self.SelectFa = QtWidgets.QPushButton(self.page_3)
        self.SelectFa.setGeometry(QtCore.QRect(410, 160, 60, 60))
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        font.setPointSize(13)
        self.SelectFa.setFont(font)
        self.SelectFa.setStyleSheet("border-radius: 30px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(234, 234, 234);")
        self.SelectFa.setFlat(True)
        self.SelectFa.setObjectName("SelectFa")
        self.SelectMi = QtWidgets.QPushButton(self.page_3)
        self.SelectMi.setGeometry(QtCore.QRect(330, 160, 60, 60))
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        font.setPointSize(13)
        self.SelectMi.setFont(font)
        self.SelectMi.setStyleSheet("border-radius: 30px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(234, 234, 234);")
        self.SelectMi.setFlat(True)
        self.SelectMi.setObjectName("SelectMi")
        self.SelectSol = QtWidgets.QPushButton(self.page_3)
        self.SelectSol.setGeometry(QtCore.QRect(330, 240, 60, 60))
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        font.setPointSize(13)
        self.SelectSol.setFont(font)
        self.SelectSol.setStyleSheet("border-radius: 30px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(234, 234, 234);")
        self.SelectSol.setFlat(True)
        self.SelectSol.setObjectName("SelectSol")
        self.SelectLa = QtWidgets.QPushButton(self.page_3)
        self.SelectLa.setGeometry(QtCore.QRect(410, 240, 60, 60))
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        font.setPointSize(13)
        self.SelectLa.setFont(font)
        self.SelectLa.setStyleSheet("border-radius: 30px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(234, 234, 234);")
        self.SelectLa.setFlat(True)
        self.SelectLa.setObjectName("SelectLa")
        self.SelectSi = QtWidgets.QPushButton(self.page_3)
        self.SelectSi.setGeometry(QtCore.QRect(330, 320, 60, 60))
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        font.setPointSize(13)
        self.SelectSi.setFont(font)
        self.SelectSi.setStyleSheet("border-radius: 30px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(234, 234, 234);")
        self.SelectSi.setFlat(True)
        self.SelectSi.setObjectName("SelectSi")
        self.SelectHighDo = QtWidgets.QPushButton(self.page_3)
        self.SelectHighDo.setGeometry(QtCore.QRect(410, 320, 60, 60))
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        font.setPointSize(13)
        self.SelectHighDo.setFont(font)
        self.SelectHighDo.setStyleSheet("border-radius: 30px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(234, 234, 234);")
        self.SelectHighDo.setFlat(True)
        self.SelectHighDo.setObjectName("SelectHighDo")
        self.label = QtWidgets.QLabel(self.page_3)
        self.label.setGeometry(QtCore.QRect(80, 45, 81, 21))
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.page_3)
        self.label_2.setGeometry(QtCore.QRect(360, 40, 81, 21))
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.StatusBar_2.raise_()
        self.KeySettingBar.raise_()
        self.KeySettingButton1.raise_()
        self.KeySettingButton3.raise_()
        self.KeySettingButton5.raise_()
        self.KeySettingButton7.raise_()
        self.KeySettingButton8.raise_()
        self.KeySettingButton4.raise_()
        self.KeySettingButton2.raise_()
        self.KeySettingButton6.raise_()
        self.SelectDo.raise_()
        self.SelectRe.raise_()
        self.SelectFa.raise_()
        self.SelectMi.raise_()
        self.SelectSol.raise_()
        self.SelectLa.raise_()
        self.SelectSi.raise_()
        self.SelectHighDo.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.WorkSpace.addWidget(self.page_3)
        self.SelectedMenu = QtWidgets.QLabel(self.centralwidget)
        self.SelectedMenu.setGeometry(QtCore.QRect(30, 85, 41, 41))
        self.SelectedMenu.setStyleSheet("border-radius: 20px;\n"
"background-color: rgb(41, 255, 194);\n"
"")
        self.SelectedMenu.setText("")
        self.SelectedMenu.setObjectName("SelectedMenu")
        self.TotalTheme = QtWidgets.QLabel(self.centralwidget)
        self.TotalTheme.setGeometry(QtCore.QRect(290, 100, 41, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TotalTheme.sizePolicy().hasHeightForWidth())
        self.TotalTheme.setSizePolicy(sizePolicy)
        self.TotalTheme.setStyleSheet("border-radius: 20px;\n"
"background-color: rgb(255, 195, 56);")
        self.TotalTheme.setText("")
        self.TotalTheme.setObjectName("TotalTheme")
        self.Background = QtWidgets.QLabel(self.centralwidget)
        self.Background.setGeometry(QtCore.QRect(-170, -60, 1091, 701))
        self.Background.setText("")
        self.Background.setObjectName("Background")
        self.SettingButton = QtWidgets.QPushButton(self.centralwidget)
        self.SettingButton.setGeometry(QtCore.QRect(75, 230, 71, 30))
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        font.setPointSize(11)
        self.SettingButton.setFont(font)
        self.SettingButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style: outset;")
        self.SettingButton.setShortcut("")
        self.SettingButton.setFlat(True)
        self.SettingButton.setObjectName("SettingButton")
        self.Settingicon = QtWidgets.QLabel(self.centralwidget)
        self.Settingicon.setGeometry(QtCore.QRect(40, 235, 21, 21))
        self.Settingicon.setText("")
        self.Settingicon.setPixmap(QtGui.QPixmap("style/icons/settings.png"))
        self.Settingicon.setScaledContents(True)
        self.Settingicon.setObjectName("Settingicon")
        self.Background.raise_()
        self.TotalTheme.raise_()
        self.WorkSpace.raise_()
        self.ToolBar.raise_()
        self.QuitButton.raise_()
        self.SelectedMenu.raise_()
        self.BlueToothIcon.raise_()
        self.BlueToothButton.raise_()
        self.InstrumentIcon.raise_()
        self.InstrumentButton.raise_()
        self.SettingButton.raise_()
        self.Settingicon.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.WorkSpace.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.BlueToothButton.setText(_translate("MainWindow", "BlueTooth"))
        self.InstrumentButton.setText(_translate("MainWindow", "Instrument"))
        self.DeviceStatusLabel.setText(_translate("MainWindow", "Disable"))
        self.Status2.setText(_translate("MainWindow", "2"))
        self.Status1.setText(_translate("MainWindow", "1"))
        self.Status3.setText(_translate("MainWindow", "3"))
        self.Status4.setText(_translate("MainWindow", "4"))
        self.Status5.setText(_translate("MainWindow", "5"))
        self.Status6.setText(_translate("MainWindow", "6"))
        self.Status7.setText(_translate("MainWindow", "7"))
        self.Status8.setText(_translate("MainWindow", "8"))
        self.Logger.setText(_translate("MainWindow", "Log"))
        self.KeySettingButton1.setText(_translate("MainWindow", "1"))
        self.KeySettingButton3.setText(_translate("MainWindow", "3"))
        self.KeySettingButton5.setText(_translate("MainWindow", "5"))
        self.KeySettingButton7.setText(_translate("MainWindow", "7"))
        self.KeySettingButton8.setText(_translate("MainWindow", "8"))
        self.KeySettingButton4.setText(_translate("MainWindow", "4"))
        self.KeySettingButton2.setText(_translate("MainWindow", "2"))
        self.KeySettingButton6.setText(_translate("MainWindow", "6"))
        self.SelectDo.setText(_translate("MainWindow", "DO"))
        self.SelectRe.setText(_translate("MainWindow", "RE"))
        self.SelectFa.setText(_translate("MainWindow", "FA"))
        self.SelectMi.setText(_translate("MainWindow", "MI"))
        self.SelectSol.setText(_translate("MainWindow", "SOL"))
        self.SelectLa.setText(_translate("MainWindow", "LA"))
        self.SelectSi.setText(_translate("MainWindow", "SI"))
        self.SelectHighDo.setText(_translate("MainWindow", "HDO"))
        self.label.setText(_translate("MainWindow", "Module"))
        self.label_2.setText(_translate("MainWindow", "Key"))
        self.SettingButton.setText(_translate("MainWindow", "Setting"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
