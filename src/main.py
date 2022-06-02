from PyQt5 import QtWidgets

import sys
import threading

from ui.piano_stairs_design import Ui_MainWindow
from style.style_handler import StyleHandler
from style.animation.menu import MenuAnimation
from style.animation.theme import ThemeAnimation
from network.serial_connect import serial_socket
from signal.signal_handler import SignalHandler
from constants import INSTRUMENTS_THEME


class PianoStairUI(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent=parent)
        self.setupUi(self)
        super().__init__()

    def variable_init(self):
        self.instrument_backs = [
            self.BassGuitarBack,
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

        self.selected_menu_updown = MenuAnimation(self.SelectedMenu, b"pos")
        self.selected_menu_shape = MenuAnimation(self.SelectedMenu, b"size")

        self.key_setting_menu = MenuAnimation(self.KeySettingBar, b"pos")

        self.change_instrumenttheme_animation = ThemeAnimation(self.InstrumentTheme, b"geometry")
        self.change_total_theme_animation = ThemeAnimation(self.TotalTheme, b"geometry")

        self.before_instrument = self.BassGuitarBack
        self.selected_instrument = 1
        self.current_theme = INSTRUMENTS_THEME["bass_guitar"]["style"]

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    piano_stair = PianoStairUI()
    piano_stair.setupUi(MainWindow)

    piano_stair.variable_init()
    StyleHandler.style_init(piano_stair)
    SignalHandler.signal_init(piano_stair)

    # th = threading.Thread(target=serial_socket, args=piano_stair)
    # th.daemon = True
    # th.start()

    # MainWindow.showFullScreen()
    MainWindow.show()

    sys.exit(app.exec_())