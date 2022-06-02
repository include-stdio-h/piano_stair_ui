from constants import UNSELECTED_KEY_STYLE, UNSELECTED_BUTTON_STYLE, SELECTED_KEY_STYLE, SELECTED_BUTTON_STYLE
from .key_setting import KeySettingSignal


class DeviceSelectSignal():
    @classmethod
    def device_select_signal_init(cls, ui):
        cls.ui = ui
        cls.ui.KeySettingButton1.clicked.connect(lambda : cls.__change_device_setting(0))
        cls.ui.KeySettingButton2.clicked.connect(lambda : cls.__change_device_setting(1))
        cls.ui.KeySettingButton3.clicked.connect(lambda : cls.__change_device_setting(2))
        cls.ui.KeySettingButton4.clicked.connect(lambda : cls.__change_device_setting(3))
        cls.ui.KeySettingButton5.clicked.connect(lambda : cls.__change_device_setting(4))
        cls.ui.KeySettingButton6.clicked.connect(lambda : cls.__change_device_setting(5))
        cls.ui.KeySettingButton7.clicked.connect(lambda : cls.__change_device_setting(6))
        cls.ui.KeySettingButton8.clicked.connect(lambda : cls.__change_device_setting(7))

    @classmethod
    def __change_device_setting(cls, index):
        key_setting_widgets = KeySettingSignal.get_key_setting_widgets(cls.ui)
        device_setting_widgets = cls.get_device_setting_widgets(cls.ui)

        for key_setting_widget in key_setting_widgets:
            key_setting_widget.setStyleSheet(UNSELECTED_KEY_STYLE)

        device_setting_widgets[cls.ui.selected_device_setting].setStyleSheet(UNSELECTED_BUTTON_STYLE)
        device_setting_widgets[index].setStyleSheet(SELECTED_BUTTON_STYLE)
        key_setting_widgets[cls.ui.device_key_status[index]["key"]].setStyleSheet(SELECTED_KEY_STYLE)
        
        cls.ui.selected_device_setting = index

    @staticmethod
    def get_device_setting_widgets(ui):
        return [
            ui.KeySettingButton1,
            ui.KeySettingButton2,
            ui.KeySettingButton3,
            ui.KeySettingButton4,
            ui.KeySettingButton5,
            ui.KeySettingButton6,
            ui.KeySettingButton7,
            ui.KeySettingButton8
        ]