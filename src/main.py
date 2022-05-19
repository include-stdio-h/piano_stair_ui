from PyQt5 import QtWidgets
from PyQt5.QtCore import QPropertyAnimation, QPoint, QEasingCurve

import sys

from ui.piano_stairs_design import Ui_MainWindow
from style.style_handler import StyleHandler
from constants import BLUETOOTH_PAGE_INDEX, INSTRUMENT_PAGE_INDEX, SELECTED_INSTRUMENT_STYLE, UNSELECTED_INSTRUMENT_STYLE

class PianoStairUI(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent=parent)
        self.setupUi(self)
        super().__init__()

    def variable_init(self):
        self.instrument_backs = [
            self.BaseGuitarBack,
            self.OrganBack,
            self.AccordionBack,
            self.PianoBack,
            self.HarpBack,
            self.VibraPhoneBack
        ]

        self.bluetooth_widgets = [
            self.DeviceStatus,
            self.LoggerBack,
            self.StatusBar
        ]

        self.SelectedMenuAnimation = QPropertyAnimation(self.SelectedMenu, b"pos")

        self.before_instrument = self.BaseGuitarBack
        self.selected_instrument = 1

    def design_init(self):
        for back in self.instrument_backs:
            back = StyleHandler.add_shadow(back)
        
        for bluetooth_widget in self.bluetooth_widgets:
            bluetooth_widget = StyleHandler.add_shadow(bluetooth_widget)

        self.ToolBar = StyleHandler.add_shadow(self.ToolBar)

    def signal_init(self):
        self.BaseGuitarSelect.clicked.connect(lambda : self.change_instrument(self.BaseGuitarBack))
        self.OrganSelect.clicked.connect(lambda : self.change_instrument(self.OrganBack))
        self.AccordionSelect.clicked.connect(lambda : self.change_instrument(self.AccordionBack))
        self.PianoSelect.clicked.connect(lambda : self.change_instrument(self.PianoBack))
        self.HarpSelect.clicked.connect(lambda : self.change_instrument(self.HarpBack))
        self.VibraPhoneSelect.clicked.connect(lambda : self.change_instrument(self.VibraPhoneBack))        

        self.QuitButton.clicked.connect(sys.exit)

        self.BlueToothButton.clicked.connect(lambda : self.change_page(BLUETOOTH_PAGE_INDEX))
        self.InstrumentButton.clicked.connect(lambda : self.change_page(INSTRUMENT_PAGE_INDEX))

    def change_page(self, page_index):
        self.SelectedMenuAnimation.setEasingCurve(QEasingCurve.InOutCubic)
        self.SelectedMenuAnimation.setEndValue(QPoint(30, 85+(70*page_index))) 
        self.SelectedMenuAnimation.setDuration(650)
        self.SelectedMenuAnimation.start()
        self.WorkSpace.setCurrentIndex(page_index)

    def change_instrument(self, now):
        self.before_instrument.setStyleSheet(UNSELECTED_INSTRUMENT_STYLE)
        self.before_instrument = now
        
        now.setStyleSheet(SELECTED_INSTRUMENT_STYLE)
        self.selected_instrument = self.instrument_backs.index(now) + 1


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    piano_stair = PianoStairUI()
    piano_stair.setupUi(MainWindow)

    piano_stair.variable_init()
    piano_stair.design_init()
    piano_stair.signal_init()

    MainWindow.show()

    sys.exit(app.exec_())