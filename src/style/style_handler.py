from PyQt5.QtWidgets import QGraphicsDropShadowEffect

class StyleHandler():
    @classmethod
    def style_init(cls, ui):
        for back in ui.instrument_backs:
            back = cls.add_shadow(back)
        
        for bluetooth_widget in ui.bluetooth_widgets:
            bluetooth_widget = cls.add_shadow(bluetooth_widget)

        ui.ToolBar = cls.add_shadow(ui.ToolBar)
    
    @classmethod
    def add_shadow(cls, widget):
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(5)
        shadow.setXOffset(3)
        shadow.setYOffset(3)

        return widget.setGraphicsEffect(shadow)