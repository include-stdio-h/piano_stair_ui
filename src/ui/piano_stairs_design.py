# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\piano_stairs_design.ui'
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
        self.BlueToothButton.setStyleSheet("background-color: rgb(255, 255, 255);")
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
        self.InstrumentButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.InstrumentButton.setShortcut("")
        self.InstrumentButton.setFlat(True)
        self.InstrumentButton.setObjectName("InstrumentButton")
        self.BlueToothIcon = QtWidgets.QLabel(self.centralwidget)
        self.BlueToothIcon.setGeometry(QtCore.QRect(40, 94, 21, 21))
        self.BlueToothIcon.setStyleSheet("")
        self.BlueToothIcon.setText("")
        self.BlueToothIcon.setPixmap(QtGui.QPixmap("C:/Users/2203kdh/Downloads/bluetooth.png"))
        self.BlueToothIcon.setScaledContents(True)
        self.BlueToothIcon.setObjectName("BlueToothIcon")
        self.InstrumentIcon = QtWidgets.QLabel(self.centralwidget)
        self.InstrumentIcon.setGeometry(QtCore.QRect(35, 157, 31, 31))
        self.InstrumentIcon.setText("")
        self.InstrumentIcon.setPixmap(QtGui.QPixmap("C:/Users/2203kdh/Downloads/live-music.png"))
        self.InstrumentIcon.setScaledContents(True)
        self.InstrumentIcon.setObjectName("InstrumentIcon")
        self.QuitButton = QtWidgets.QPushButton(self.centralwidget)
        self.QuitButton.setGeometry(QtCore.QRect(80, 370, 41, 41))
        self.QuitButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/2203kdh/Downloads/power-on.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.QuitButton.setIcon(icon)
        self.QuitButton.setIconSize(QtCore.QSize(32, 32))
        self.QuitButton.setShortcut("")
        self.QuitButton.setCheckable(False)
        self.QuitButton.setFlat(True)
        self.QuitButton.setObjectName("QuitButton")
        self.WorkSpace = QtWidgets.QStackedWidget(self.centralwidget)
        self.WorkSpace.setGeometry(QtCore.QRect(220, 10, 631, 531))
        self.WorkSpace.setObjectName("WorkSpace")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.DeviceStatus = QtWidgets.QLabel(self.page)
        self.DeviceStatus.setGeometry(QtCore.QRect(10, 30, 331, 141))
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        font.setPointSize(22)
        self.DeviceStatus.setFont(font)
        self.DeviceStatus.setStyleSheet("border-radius: 20px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(114, 240, 145);")
        self.DeviceStatus.setText("")
        self.DeviceStatus.setAlignment(QtCore.Qt.AlignCenter)
        self.DeviceStatus.setObjectName("DeviceStatus")
        self.ToolBar_3 = QtWidgets.QLabel(self.page)
        self.ToolBar_3.setGeometry(QtCore.QRect(10, 200, 331, 221))
        self.ToolBar_3.setAutoFillBackground(False)
        self.ToolBar_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"")
        self.ToolBar_3.setText("")
        self.ToolBar_3.setObjectName("ToolBar_3")
        self.DeviceStatusIcon = QtWidgets.QLabel(self.page)
        self.DeviceStatusIcon.setGeometry(QtCore.QRect(150, 100, 51, 51))
        self.DeviceStatusIcon.setText("")
        self.DeviceStatusIcon.setPixmap(QtGui.QPixmap("C:/Users/2203kdh/Downloads/check.png"))
        self.DeviceStatusIcon.setScaledContents(True)
        self.DeviceStatusIcon.setObjectName("DeviceStatusIcon")
        self.DeviceStatusLabel = QtWidgets.QLabel(self.page)
        self.DeviceStatusLabel.setGeometry(QtCore.QRect(100, 40, 161, 61))
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        font.setPointSize(26)
        self.DeviceStatusLabel.setFont(font)
        self.DeviceStatusLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.DeviceStatusLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.DeviceStatusLabel.setObjectName("DeviceStatusLabel")
        self.ToolBar_4 = QtWidgets.QLabel(self.page)
        self.ToolBar_4.setGeometry(QtCore.QRect(360, 30, 201, 391))
        self.ToolBar_4.setMinimumSize(QtCore.QSize(0, 45))
        self.ToolBar_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"")
        self.ToolBar_4.setText("")
        self.ToolBar_4.setObjectName("ToolBar_4")
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
        self.Statua5 = QtWidgets.QLabel(self.page)
        self.Statua5.setGeometry(QtCore.QRect(390, 230, 61, 61))
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        font.setPointSize(20)
        self.Statua5.setFont(font)
        self.Statua5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Statua5.setStyleSheet("border-radius: 20px;\n"
"background-color: rgb(234, 234, 234);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.Statua5.setAlignment(QtCore.Qt.AlignCenter)
        self.Statua5.setObjectName("Statua5")
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
        self.ElectGuitarBack = QtWidgets.QLabel(self.page_2)
        self.ElectGuitarBack.setGeometry(QtCore.QRect(210, 30, 171, 161))
        self.ElectGuitarBack.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"")
        self.ElectGuitarBack.setText("")
        self.ElectGuitarBack.setObjectName("ElectGuitarBack")
        self.ChelloBack = QtWidgets.QLabel(self.page_2)
        self.ChelloBack.setGeometry(QtCore.QRect(400, 30, 171, 161))
        self.ChelloBack.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"")
        self.ChelloBack.setText("")
        self.ChelloBack.setObjectName("ChelloBack")
        self.DrumBack = QtWidgets.QLabel(self.page_2)
        self.DrumBack.setGeometry(QtCore.QRect(210, 230, 171, 161))
        self.DrumBack.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"")
        self.DrumBack.setText("")
        self.DrumBack.setObjectName("DrumBack")
        self.VoiceBack = QtWidgets.QLabel(self.page_2)
        self.VoiceBack.setGeometry(QtCore.QRect(400, 230, 171, 161))
        self.VoiceBack.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"")
        self.VoiceBack.setText("")
        self.VoiceBack.setObjectName("VoiceBack")
        self.PianoBack = QtWidgets.QLabel(self.page_2)
        self.PianoBack.setGeometry(QtCore.QRect(20, 230, 171, 161))
        self.PianoBack.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"")
        self.PianoBack.setText("")
        self.PianoBack.setObjectName("PianoBack")
        self.BaseGuitarSelect = QtWidgets.QPushButton(self.page_2)
        self.BaseGuitarSelect.setGeometry(QtCore.QRect(25, 35, 160, 151))
        self.BaseGuitarSelect.setAutoFillBackground(False)
        self.BaseGuitarSelect.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"")
        self.BaseGuitarSelect.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/2203kdh/Downloads/guitar (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BaseGuitarSelect.setIcon(icon1)
        self.BaseGuitarSelect.setIconSize(QtCore.QSize(100, 100))
        self.BaseGuitarSelect.setFlat(True)
        self.BaseGuitarSelect.setObjectName("BaseGuitarSelect")
        self.BaseGuiterBack = QtWidgets.QLabel(self.page_2)
        self.BaseGuiterBack.setGeometry(QtCore.QRect(20, 30, 171, 161))
        self.BaseGuiterBack.setStyleSheet("border-radius: 20px;\n"
"background-color: rgb(182, 182, 182);\n"
"")
        self.BaseGuiterBack.setText("")
        self.BaseGuiterBack.setObjectName("BaseGuiterBack")
        self.ElecGuitarSelect = QtWidgets.QPushButton(self.page_2)
        self.ElecGuitarSelect.setGeometry(QtCore.QRect(220, 40, 151, 141))
        self.ElecGuitarSelect.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"")
        self.ElecGuitarSelect.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:/Users/2203kdh/Downloads/guitar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ElecGuitarSelect.setIcon(icon2)
        self.ElecGuitarSelect.setIconSize(QtCore.QSize(100, 100))
        self.ElecGuitarSelect.setFlat(True)
        self.ElecGuitarSelect.setObjectName("ElecGuitarSelect")
        self.ChelloSelect = QtWidgets.QPushButton(self.page_2)
        self.ChelloSelect.setGeometry(QtCore.QRect(410, 40, 151, 141))
        self.ChelloSelect.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"")
        self.ChelloSelect.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("C:/Users/2203kdh/Downloads/cello.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ChelloSelect.setIcon(icon3)
        self.ChelloSelect.setIconSize(QtCore.QSize(100, 100))
        self.ChelloSelect.setFlat(True)
        self.ChelloSelect.setObjectName("ChelloSelect")
        self.PianoSelect = QtWidgets.QPushButton(self.page_2)
        self.PianoSelect.setGeometry(QtCore.QRect(30, 240, 151, 141))
        self.PianoSelect.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"")
        self.PianoSelect.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("C:/Users/2203kdh/Downloads/piano (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PianoSelect.setIcon(icon4)
        self.PianoSelect.setIconSize(QtCore.QSize(100, 100))
        self.PianoSelect.setFlat(True)
        self.PianoSelect.setObjectName("PianoSelect")
        self.DrumSelect = QtWidgets.QPushButton(self.page_2)
        self.DrumSelect.setGeometry(QtCore.QRect(220, 240, 151, 141))
        self.DrumSelect.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"")
        self.DrumSelect.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("C:/Users/2203kdh/Downloads/drums.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.DrumSelect.setIcon(icon5)
        self.DrumSelect.setIconSize(QtCore.QSize(100, 100))
        self.DrumSelect.setFlat(True)
        self.DrumSelect.setObjectName("DrumSelect")
        self.VoiceSelect = QtWidgets.QPushButton(self.page_2)
        self.VoiceSelect.setGeometry(QtCore.QRect(410, 240, 151, 141))
        self.VoiceSelect.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"")
        self.VoiceSelect.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("C:/Users/2203kdh/Downloads/microphone.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.VoiceSelect.setIcon(icon6)
        self.VoiceSelect.setIconSize(QtCore.QSize(100, 100))
        self.VoiceSelect.setFlat(True)
        self.VoiceSelect.setObjectName("VoiceSelect")
        self.ElectGuitarBack.raise_()
        self.ChelloBack.raise_()
        self.DrumBack.raise_()
        self.VoiceBack.raise_()
        self.PianoBack.raise_()
        self.BaseGuiterBack.raise_()
        self.BaseGuitarSelect.raise_()
        self.ElecGuitarSelect.raise_()
        self.ChelloSelect.raise_()
        self.PianoSelect.raise_()
        self.DrumSelect.raise_()
        self.VoiceSelect.raise_()
        self.WorkSpace.addWidget(self.page_2)
        self.SelectedMenu = QtWidgets.QLabel(self.centralwidget)
        self.SelectedMenu.setGeometry(QtCore.QRect(30, 85, 171, 41))
        self.SelectedMenu.setStyleSheet("border-radius: 20px;\n"
"background-color: rgb(41, 255, 194);\n"
"")
        self.SelectedMenu.setText("")
        self.SelectedMenu.setObjectName("SelectedMenu")
        self.ToolBar.raise_()
        self.QuitButton.raise_()
        self.WorkSpace.raise_()
        self.SelectedMenu.raise_()
        self.BlueToothIcon.raise_()
        self.BlueToothButton.raise_()
        self.InstrumentIcon.raise_()
        self.InstrumentButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.WorkSpace.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.BlueToothButton.setText(_translate("MainWindow", "BlueTooth"))
        self.InstrumentButton.setText(_translate("MainWindow", "Instrument"))
        self.DeviceStatusLabel.setText(_translate("MainWindow", "Ready"))
        self.Status2.setText(_translate("MainWindow", "2"))
        self.Status1.setText(_translate("MainWindow", "1"))
        self.Status3.setText(_translate("MainWindow", "3"))
        self.Status4.setText(_translate("MainWindow", "4"))
        self.Statua5.setText(_translate("MainWindow", "5"))
        self.Status6.setText(_translate("MainWindow", "6"))
        self.Status7.setText(_translate("MainWindow", "7"))
        self.Status8.setText(_translate("MainWindow", "8"))
        self.Logger.setText(_translate("MainWindow", "Log"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
