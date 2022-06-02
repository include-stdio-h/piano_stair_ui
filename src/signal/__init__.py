from signal.page import PageSignal
from signal.instrument import InstrumentSignal
from signal.quit import QuitSignal
from signal.animation import AnimationSignal
from signal.setting_signal import SettingSignalHandler


class SignalHandler():
    @classmethod
    def signal_init(cls, ui):
        InstrumentSignal.instrument_signal_init(ui)
        PageSignal.page_signal_init(ui)
        QuitSignal.quit_signal_init(ui)
        AnimationSignal.animation_signal_init(ui)
        SettingSignalHandler.setting_signal_init(ui)