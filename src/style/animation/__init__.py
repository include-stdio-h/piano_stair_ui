from PyQt5.QtCore import QPropertyAnimation

class AnimationHandler():
    def __init__(self, target, type) -> None:
        self.Animation = QPropertyAnimation(target, type)