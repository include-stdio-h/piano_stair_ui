from PyQt5 import QtWidgets
from PyQt5.QtCore import QPropertyAnimation, QPoint, QEasingCurve

import sys

from ui.piano_stairs_design import Ui_MainWindow
from constants import BLUETOOTH_PAGE_INDEX, INSTRUMENT_PAGE_INDEX, SELECTED_INSTRUMENT_STYLE, UNSELECTED_INSTRUMENT_STYLE

class PianoStairUI(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent=parent)
        self.setupUi(self)
        super().__init__()

    def init_func(self):
        # Page Handle
        self.BlueToothButton.clicked.connect(lambda : self.change_page(BLUETOOTH_PAGE_INDEX))
        self.InstrumentButton.clicked.connect(lambda : self.change_page(INSTRUMENT_PAGE_INDEX))

        # Page Select Animation
        self.SelectedMenuAnimation = QPropertyAnimation(self.SelectedMenu, b"pos")

        # Instrument Handle
        self.before_instrument = self.BaseGuitarBack
        self.selected_instrument = 1

        self.BaseGuitarSelect.clicked.connect(lambda : self.change_instrument(self.BaseGuitarBack, 1))
        self.ElecGuitarSelect.clicked.connect(lambda : self.change_instrument(self.ElecGuitarBack, 2))
        self.ChelloSelect.clicked.connect(lambda : self.change_instrument(self.ChelloBack, 3))
        self.PianoSelect.clicked.connect(lambda : self.change_instrument(self.PianoBack, 4))
        self.DrumSelect.clicked.connect(lambda : self.change_instrument(self.DrumBack, 5))
        self.VoiceSelect.clicked.connect(lambda : self.change_instrument(self.VoiceBack, 6))

        # Quit App
        self.QuitButton.clicked.connect(lambda : self.quit_app())

    def change_page(self, page_index):
        self.SelectedMenuAnimation.setEasingCurve(QEasingCurve.InOutCubic)
        self.SelectedMenuAnimation.setEndValue(QPoint(30, 85+(70*page_index))) 
        self.SelectedMenuAnimation.setDuration(400)
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
    piano_stair.init_func()

    MainWindow.show()

    sys.exit(app.exec_())