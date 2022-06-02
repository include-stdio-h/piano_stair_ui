from PyQt5.QtCore import QPoint, QEasingCurve, QSize, QAbstractAnimation, QRect, QSequentialAnimationGroup, QPropertyAnimation

from . import AnimationHandler
from constants import TOTAL_THEME_LOCATION_DIFF

class ThemeAnimation(AnimationHandler):
    def __init__(self, target, type) -> None:
        super().__init__(target, type)

        self.target_widget = target
        self.TotalThemeAnimation = QPropertyAnimation(target, type)


    def change_theme(self, widget_theme, type):
        if type == "total":
            animate_location = QPoint(widget_theme["location"][0] + TOTAL_THEME_LOCATION_DIFF[0], 
                                        widget_theme["location"][1] + TOTAL_THEME_LOCATION_DIFF[1])
        elif type == "instrument":
            animate_location = QPoint(widget_theme["location"][0], widget_theme["location"][1])

        self.target_widget.setStyleSheet(widget_theme["style"])
        start_value = QRect(animate_location, QSize(40,40))
        end_value = QRect(animate_location, QSize(1500,1100))
        end_value.moveCenter(start_value.center())

        self.Animation.setEasingCurve(QEasingCurve.OutCubic)
        self.Animation.setStartValue(start_value)
        self.Animation.setEndValue(end_value)
        self.Animation.setDuration(1200)
        self.Animation.setDirection(QAbstractAnimation.Forward)
        self.Animation.start()