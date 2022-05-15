from PyQt5 import QtWidgets

import sys

from ui.piano_stairs_design import Ui_MainWindow
from constants import BLUETOOTH_PAGE_INDEX, INSTRUMENT_PAGE_INDEX

class PianoStairUI(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent=parent)
        self.setupUi(self)
        super().__init__()

    def init_func(self):
        # Page Handle
        self.BlueToothButton.clicked.connect(lambda : self.WorkSpace.setCurrentIndex(BLUETOOTH_PAGE_INDEX))
        self.InstrumentButton.clicked.connect(lambda : self.WorkSpace.setCurrentIndex(INSTRUMENT_PAGE_INDEX))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    piano_stair = PianoStairUI()
    piano_stair.setupUi(MainWindow)
    piano_stair.init_func()

    MainWindow.show()

    sys.exit(app.exec_())