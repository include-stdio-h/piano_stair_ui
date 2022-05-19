from PyQt5 import QtWidgets
from PyQt5.QtCore import QPropertyAnimation, QPoint, QEasingCurve

import sys

from ui.piano_stairs_design import Ui_MainWindow
from handler.style.style_handler import StyleHandler
from constants import BLUETOOTH_PAGE_INDEX, INSTRUMENT_PAGE_INDEX, SELECTED_INSTRUMENT_STYLE, UNSELECTED_INSTRUMENT_STYLE

class PianoStairUI(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent=parent)
        self.setupUi(self)
        super().__init__()

    def variable_init(self):
        self.instruments = {
            self.BaseGuitarSelect : [self.BaseGuitarBack, 1],
            self.OrganSelect : [self.OrganBack, 2],
            self.AccordionSelect : [self.AccordionBack, 3],
            self.PianoSelect : [self.PianoBack, 4],
            self.HarpSelect : [self.HarpBack, 5],
            self.VibraPhoneSelect : [self.VibraPhoneBack, 6]
        }

        self.bluetooth_widgets = [
            self.DeviceStatus,
            self.LoggerBack,
            self.StatusBar
        ]

        # Page Select Animation
        self.SelectedMenuAnimation = QPropertyAnimation(self.SelectedMenu, b"pos")

        # Instrument Handle
        self.before_instrument = self.BaseGuitarBack
        self.selected_instrument = 1

    def design_init(self):
        for _, back in self.instruments.items():
            back[0] = StyleHandler.add_shadow(back[0])
        
        for bluetooth_widget in self.bluetooth_widgets:
            bluetooth_widget = StyleHandler.add_shadow(bluetooth_widget)

        self.ToolBar = StyleHandler.add_shadow(self.ToolBar)

    def signal_init(self):
        for button, back in self.instruments.items():
            button.clicked.connect(lambda : self.change_instrument(back[0], back[1]))

        # Quit App
        self.QuitButton.clicked.connect(self.quit_app)

         # Page Handle
        self.BlueToothButton.clicked.connect(lambda : self.change_page(BLUETOOTH_PAGE_INDEX))
        self.InstrumentButton.clicked.connect(lambda : self.change_page(INSTRUMENT_PAGE_INDEX))

    def change_page(self, page_index):
        self.SelectedMenuAnimation.setEasingCurve(QEasingCurve.InOutCubic)
        self.SelectedMenuAnimation.setEndValue(QPoint(30, 85+(70*page_index))) 
        self.SelectedMenuAnimation.setDuration(650)
        self.SelectedMenuAnimation.start()
        self.WorkSpace.setCurrentIndex(page_index)

    def change_instrument(self, now, instrument_type):
        self.before_instrument.setStyleSheet(UNSELECTED_INSTRUMENT_STYLE)
        self.before_instrument = now
        
        now.setStyleSheet(SELECTED_INSTRUMENT_STYLE)
        self.selected_instrument = instrument_type

    def quit_app(self):
        sys.exit()


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