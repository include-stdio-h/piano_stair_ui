from PyQt5 import QtWidgets

import sys

from ui.piano_stairs_design import Ui_MainWindow
from style.style_handler import StyleHandler
from style.animation.menu import MenuAnimation
from style.animation.theme import ThemeAnimation
from constants import ( 
    BLUETOOTH_PAGE_INDEX, 
    INSTRUMENT_PAGE_INDEX,
    SELECTED_INSTRUMENT_STYLE, 
    UNSELECTED_INSTRUMENT_STYLE,
    INTRUMENTS_THEME
)


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

        self.selected_menu_animation = MenuAnimation(self.SelectedMenu, b"pos")
        self.change_instrumenttheme_animation = ThemeAnimation(self.InstrumentTheme, b"geometry")
        self.change_total_theme_animation = ThemeAnimation(self.TotalTheme, b"geometry")

        self.before_instrument = self.BassGuitarBack
        self.selected_instrument = 1
        self.current_theme = INTRUMENTS_THEME["bass_guitar"]["style"]

    def design_init(self):
        for back in self.instrument_backs:
            back = StyleHandler.add_shadow(back)
        
        for bluetooth_widget in self.bluetooth_widgets:
            bluetooth_widget = StyleHandler.add_shadow(bluetooth_widget)

        self.ToolBar = StyleHandler.add_shadow(self.ToolBar)

    def signal_init(self):
        self.BassGuitarSelect.clicked.connect(lambda : self.change_instrument(self.BassGuitarBack, INTRUMENTS_THEME["bass_guitar"]))
        self.OrganSelect.clicked.connect(lambda : self.change_instrument(self.OrganBack, INTRUMENTS_THEME["organ"]))
        self.AccordionSelect.clicked.connect(lambda : self.change_instrument(self.AccordionBack, INTRUMENTS_THEME["accordion"]))
        self.PianoSelect.clicked.connect(lambda : self.change_instrument(self.PianoBack, INTRUMENTS_THEME["piano"]))
        self.HarpSelect.clicked.connect(lambda : self.change_instrument(self.HarpBack, INTRUMENTS_THEME["harp"]))
        self.VibraPhoneSelect.clicked.connect(lambda : self.change_instrument(self.VibraPhoneBack, INTRUMENTS_THEME["vibra_phone"]))

        self.QuitButton.clicked.connect(sys.exit)

        self.BlueToothButton.clicked.connect(lambda : self.change_page(BLUETOOTH_PAGE_INDEX))
        self.InstrumentButton.clicked.connect(lambda : self.change_page(INSTRUMENT_PAGE_INDEX))

        self.change_instrumenttheme_animation.SelectedMenuAnimation.finished.connect(lambda : self.WorkSpace.setStyleSheet(self.current_theme))
        self.change_total_theme_animation.SelectedMenuAnimation.finished.connect(lambda : self.Background.setStyleSheet(self.current_theme))

    def change_page(self, page_index):
        self.selected_menu_animation.updown_animation(page_index)
        self.WorkSpace.setCurrentIndex(page_index)

    def change_instrument(self, now, widget_theme):
        self.change_instrumenttheme_animation.change_theme(widget_theme, "instrument")
        self.change_total_theme_animation.change_theme(widget_theme, "total")

        self.current_theme = widget_theme["style"]

        self.before_instrument = StyleHandler.change_theme(self.before_instrument, UNSELECTED_INSTRUMENT_STYLE)
        now = StyleHandler.change_theme(now, SELECTED_INSTRUMENT_STYLE)

        self.before_instrument = now
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