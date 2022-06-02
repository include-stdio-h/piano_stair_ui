import sys


class SignalHandler():
    @classmethod
    def signal_init(cls, ui):
        cls.ui = ui

        cls.__instrument_signal_init()
        cls.__page_signal_init()
        cls.__quit_signal_init()
        cls.__animation_signal_init()
        cls.__setting_signal_init()

    @classmethod
    def __setting_signal_init(cls):
        cls.ui.KeySettingButton1.clicked.connect(lambda : cls.__change_device_setting(0))
        cls.ui.KeySettingButton2.clicked.connect(lambda : cls.__change_device_setting(1))
        cls.ui.KeySettingButton3.clicked.connect(lambda : cls.__change_device_setting(2))
        cls.ui.KeySettingButton4.clicked.connect(lambda : cls.__change_device_setting(3))
        cls.ui.KeySettingButton5.clicked.connect(lambda : cls.__change_device_setting(4))
        cls.ui.KeySettingButton6.clicked.connect(lambda : cls.__change_device_setting(5))
        cls.ui.KeySettingButton7.clicked.connect(lambda : cls.__change_device_setting(6))
        cls.ui.KeySettingButton8.clicked.connect(lambda : cls.__change_device_setting(7))

        cls.ui.SelectDo.clicked.connect(lambda : cls.__change_device_key(0))
        cls.ui.SelectRe.clicked.connect(lambda : cls.__change_device_key(1))
        cls.ui.SelectMi.clicked.connect(lambda : cls.__change_device_key(2))
        cls.ui.SelectFa.clicked.connect(lambda : cls.__change_device_key(3))
        cls.ui.SelectSol.clicked.connect(lambda : cls.__change_device_key(4))
        cls.ui.SelectLa.clicked.connect(lambda : cls.__change_device_key(5))
        cls.ui.SelectSi.clicked.connect(lambda : cls.__change_device_key(6))
        cls.ui.SelectHighDo.clicked.connect(lambda : cls.__change_device_key(7))

        cls.ui.VolumeController.valueChanged.connect(lambda : cls.__change_volume())

    @classmethod
    def __animation_signal_init(cls):
        cls.ui.change_instrument_theme_animation.Animation.finished.connect(lambda : cls.ui.WorkSpace.setStyleSheet(cls.ui.current_theme))
        cls.ui.change_total_theme_animation.Animation.finished.connect(lambda : cls.ui.Background.setStyleSheet(cls.ui.current_theme))

    @classmethod
    def __quit_signal_init(cls):
        cls.ui.QuitButton.clicked.connect(sys.exit)

    @classmethod
    def __page_signal_init(cls):
        from constants import BLUETOOTH_PAGE_INDEX, INSTRUMENT_PAGE_INDEX, SETTING_PAGE_INDEX

        cls.ui.BlueToothButton.clicked.connect(lambda : cls.__change_page(BLUETOOTH_PAGE_INDEX))
        cls.ui.InstrumentButton.clicked.connect(lambda : cls.__change_page(INSTRUMENT_PAGE_INDEX))
        cls.ui.SettingButton.clicked.connect(lambda : cls.__change_page(SETTING_PAGE_INDEX))

    @classmethod
    def __instrument_signal_init(cls):
        from constants import INSTRUMENTS_THEME

        cls.ui.BassGuitarSelect.clicked.connect(lambda : cls.__change_instrument(cls.ui.BassGuitarBack, INSTRUMENTS_THEME["bass_guitar"]))
        cls.ui.OrganSelect.clicked.connect(lambda : cls.__change_instrument(cls.ui.OrganBack, INSTRUMENTS_THEME["organ"]))
        cls.ui.AccordionSelect.clicked.connect(lambda : cls.__change_instrument(cls.ui.AccordionBack, INSTRUMENTS_THEME["accordion"]))
        cls.ui.PianoSelect.clicked.connect(lambda : cls.__change_instrument(cls.ui.PianoBack, INSTRUMENTS_THEME["piano"]))
        cls.ui.HarpSelect.clicked.connect(lambda : cls.__change_instrument(cls.ui.HarpBack, INSTRUMENTS_THEME["harp"]))
        cls.ui.VibraPhoneSelect.clicked.connect(lambda : cls.__change_instrument(cls.ui.VibraPhoneBack, INSTRUMENTS_THEME["vibra_phone"]))

    @classmethod
    def __change_page(cls, page_index):
        cls.ui.selected_menu_updown.updown_animation(page_index)
        cls.ui.WorkSpace.setCurrentIndex(page_index)

    @classmethod
    def __change_instrument(cls, now_instrument, widget_theme):
        from constants import SELECTED_INSTRUMENT_STYLE, UNSELECTED_INSTRUMENT_STYLE
        from music.player import select_instrument

        cls.ui.change_instrument_theme_animation.change_theme(widget_theme, "instrument")
        cls.ui.change_total_theme_animation.change_theme(widget_theme, "total")

        cls.ui.current_theme = widget_theme["style"]

        cls.ui.before_instrument.setStyleSheet(UNSELECTED_INSTRUMENT_STYLE)
        now_instrument.setStyleSheet(SELECTED_INSTRUMENT_STYLE)

        cls.ui.before_instrument = now_instrument
        cls.ui.selected_instrument = cls.ui.instrument_backs.index(now_instrument)
        select_instrument(cls.ui.selected_instrument)

    @classmethod
    def __change_device_setting(cls, index):
        from constants import UNSELECTED_KEY_STYLE, UNSELECTED_BUTTON_STYLE, SELECTED_KEY_STYLE, SELECTED_BUTTON_STYLE

        for i in range(len(cls.ui.key_setting_widgets)):
            cls.ui.key_setting_widgets[i].setStyleSheet(UNSELECTED_KEY_STYLE)
            cls.ui.device_setting_widgets[i].setStyleSheet(UNSELECTED_BUTTON_STYLE)

        cls.ui.device_setting_widgets[index].setStyleSheet(SELECTED_BUTTON_STYLE)
        cls.ui.key_setting_widgets[cls.ui.device_key_status[index]["key"]].setStyleSheet(SELECTED_KEY_STYLE)
        
        cls.ui.selected_device_setting = index

    @classmethod
    def __change_device_key(cls, index):
        from constants import UNSELECTED_KEY_STYLE, SELECTED_KEY_STYLE

        for i in range(len(cls.ui.key_setting_widgets)):
            cls.ui.key_setting_widgets[i].setStyleSheet(UNSELECTED_KEY_STYLE)

        cls.ui.device_key_status[cls.ui.selected_device_setting]["key"] = index
        cls.ui.key_setting_widgets[index].setStyleSheet(SELECTED_KEY_STYLE)

    @classmethod
    def __change_volume(cls):
        from music.player import volume_setting

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
        print(cls.ui.device_volume)
        volume_setting(cls.ui.device_volume)

        for i in range(cls.ui.device_volume):
            volume_level_widgets[i].setStyleSheet("border-radius: 9px;\nbackground-color: rgb(157, 255, 185);\ncolor: rgb(255, 255, 255);\n")