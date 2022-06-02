import sys


class QuitSignal():
    @staticmethod
    def quit_signal_init(ui):
        ui.QuitButton.clicked.connect(sys.exit)