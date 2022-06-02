class KeySettingSignal():
    @classmethod
    def setting_signal_init(cls, ui):
        cls.ui = ui
        cls.ui.SelectDo.clicked.connect(lambda : cls.__change_device_key(0))
        cls.ui.SelectRe.clicked.connect(lambda : cls.__change_device_key(1))
        cls.ui.SelectMi.clicked.connect(lambda : cls.__change_device_key(2))
        cls.ui.SelectFa.clicked.connect(lambda : cls.__change_device_key(3))
        cls.ui.SelectSol.clicked.connect(lambda : cls.__change_device_key(4))
        cls.ui.SelectLa.clicked.connect(lambda : cls.__change_device_key(5))
        cls.ui.SelectSi.clicked.connect(lambda : cls.__change_device_key(6))
        cls.ui.SelectHighDo.clicked.connect(lambda : cls.__change_device_key(7))

    @classmethod
    def __change_device_key(cls, index):
        from constants import UNSELECTED_KEY_STYLE, SELECTED_KEY_STYLE

        for i in range(len(cls.ui.key_setting_widgets)):
            cls.ui.key_setting_widgets[i].setStyleSheet(UNSELECTED_KEY_STYLE)

        cls.ui.device_key_status[cls.ui.selected_device_setting]["key"] = index
        cls.ui.key_setting_widgets[index].setStyleSheet(SELECTED_KEY_STYLE)