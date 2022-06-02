from features.music.player import volume_setting


class VolumeSignal():
    @classmethod
    def volume_signal_init(cls, ui):
        cls.ui = ui
        cls.ui.VolumeController.valueChanged.connect(lambda : cls.__change_volume())

    @classmethod
    def __change_volume(cls):
        volume_level_widgets = [
            cls.ui.VolumeLevel1,
            cls.ui.VolumeLevel2,
            cls.ui.VolumeLevel3,
            cls.ui.VolumeLevel4,
            cls.ui.VolumeLevel5,
            cls.ui.VolumeLevel6,
            cls.ui.VolumeLevel7,
            cls.ui.VolumeLevel8,
            cls.ui.VolumeLevel9,
            cls.ui.VolumeLevel10,
        ]

        for widget in volume_level_widgets:
            widget.setStyleSheet("background-color: rgb(255, 255, 255);")

        cls.ui.device_volume = cls.ui.VolumeController.value()
        volume_setting(cls.ui.device_volume)

        for i in range(cls.ui.device_volume):
            volume_level_widgets[i].setStyleSheet("border-radius: 9px;\nbackground-color: rgb(157, 255, 185);\ncolor: rgb(255, 255, 255);\n")