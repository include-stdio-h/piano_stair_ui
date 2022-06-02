class AnimationSignal():
    @staticmethod
    def animation_signal_init(ui):
        ui.change_instrument_theme_animation.Animation.finished.connect(lambda : ui.WorkSpace.setStyleSheet(ui.current_theme))
        ui.change_total_theme_animation.Animation.finished.connect(lambda : ui.Background.setStyleSheet(ui.current_theme))