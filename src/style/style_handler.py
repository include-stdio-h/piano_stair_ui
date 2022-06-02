from PyQt5.QtWidgets import QGraphicsDropShadowEffect

from signal.instrument import InstrumentSignal


class StyleHandler():
    @classmethod
    def style_init(cls, ui):
        for back in InstrumentSignal.get_instrument_backs(ui):
            back = cls.add_shadow(back)
        
        for bluetooth_widget in cls.get_shadow_widgets(ui):
            bluetooth_widget = cls.add_shadow(bluetooth_widget)

        ui.ToolBar = cls.add_shadow(ui.ToolBar)
    
    @classmethod
    def add_shadow(cls, widget):
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(5)
        shadow.setXOffset(3)
        shadow.setYOffset(3)

        return widget.setGraphicsEffect(shadow)

    @staticmethod
    def get_shadow_widgets(ui):
        return [
            ui.DeviceStatus,
            ui.LoggerBack,
            ui.StatusBar
        ]