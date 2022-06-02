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
        from constants import UNSELECTED_KEY_STYLE, UNSELECTED_BUTTON_STYLE, SELECTED_KEY_STYLE, SELECTED_BUTTON_STYLE

        for i in range(len(cls.ui.key_setting_widgets)):
            cls.ui.key_setting_widgets[i].setStyleSheet(UNSELECTED_KEY_STYLE)
            cls.ui.device_setting_widgets[i].setStyleSheet(UNSELECTED_BUTTON_STYLE)

        cls.ui.device_setting_widgets[index].setStyleSheet(SELECTED_BUTTON_STYLE)
        cls.ui.key_setting_widgets[cls.ui.device_key_status[index]["key"]].setStyleSheet(SELECTED_KEY_STYLE)
        
        cls.ui.selected_device_setting = index