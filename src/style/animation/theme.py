from PyQt5.QtCore import QPoint, QEasingCurve, QSize, QAbstractAnimation, QRect

from . import AnimationHandler
from constants import TOTAL_THEME_LOCATION_DIFF

class ThemeAnimation(AnimationHandler):
    def __init__(self, target, type) -> None:
        self.target_widget = target
        super().__init__(target, type)

    def change_theme(self, widget_theme, type):
        if type == "total":
            animate_location = QPoint(widget_theme["location"][0] + TOTAL_THEME_LOCATION_DIFF[0], 
                                        widget_theme["location"][1] + TOTAL_THEME_LOCATION_DIFF[1])
        elif type == "instrument":
            animate_location = QPoint(widget_theme["location"][0], widget_theme["location"][1])

        self.target_widget.setStyleSheet(widget_theme["style"])
        start_value = QRect(animate_location, QSize(40,40))
        end_value = QRect(animate_location, QSize(1750,1250))
        end_value.moveCenter(start_value.center())

        self.SelectedMenuAnimation.setEasingCurve(QEasingCurve.OutCubic)
        self.SelectedMenuAnimation.setStartValue(start_value)
        self.SelectedMenuAnimation.setEndValue(end_value)
        self.SelectedMenuAnimation.setDuration(1200)
        self.SelectedMenuAnimation.setDirection(QAbstractAnimation.Forward)
        self.SelectedMenuAnimation.start()