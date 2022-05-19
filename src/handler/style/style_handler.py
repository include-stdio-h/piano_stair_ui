from PyQt5.QtWidgets import QGraphicsDropShadowEffect

class StyleHandler():
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def add_shadow(widget):
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(5)
        shadow.setXOffset(3)
        shadow.setYOffset(3)

        return widget.setGraphicsEffect(shadow)