from PyQt5.QtCore import QPoint, QEasingCurve

from . import AnimationHandler
from constants import SELECTED_MENU_SIGN_DEFAULT_X_LOCATION, SELECTED_MENU_SIGN_DEFAULT_Y_LOCATION, VERTICAL_DISTANCE_BETWEEN_MENUS, \
                        ANIMATION_SPEED

class MenuAnimation(AnimationHandler):
    def __init__(self, target, type) -> None:
        super().__init__(target, type)

    def updown_animation(self, page_index):
        self.SelectedMenuAnimation.setEasingCurve(QEasingCurve.InOutCubic)
        self.SelectedMenuAnimation.setEndValue(QPoint(SELECTED_MENU_SIGN_DEFAULT_X_LOCATION, 
                                                        SELECTED_MENU_SIGN_DEFAULT_Y_LOCATION + (VERTICAL_DISTANCE_BETWEEN_MENUS * page_index)))
        self.SelectedMenuAnimation.setDuration(ANIMATION_SPEED)
        self.SelectedMenuAnimation.start()