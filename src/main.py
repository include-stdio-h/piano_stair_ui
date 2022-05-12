from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication

from ui.piano_stairs_design import Ui_MainWindow

import sys

class PianoStairUI(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent=parent)
        self.setupUi(self)
        super().__init__()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    piano_stair = PianoStairUI()
    piano_stair.setupUi(MainWindow)

    MainWindow.show()

    sys.exit(app.exec_())