import sys

from style.style_handler import StyleHandler

from constants import ( 
    BLUETOOTH_PAGE_INDEX, 
    INSTRUMENT_PAGE_INDEX,
    SETTING_PAGE_INDEX,
    SELECTED_INSTRUMENT_STYLE, 
    UNSELECTED_INSTRUMENT_STYLE,
    INSTRUMENTS_THEME
)

class SignalHandler():
    @classmethod
    def signal_init(cls, ui):
        cls.ui = ui

        cls.__instrument_signal_init()
        cls.__page_signal_init()
        cls.__quit_signal_init()
        cls.__animation_signal_init()

        # cls.ui.KeySettingButton1.clicked.connect()
        # cls.ui.KeySettingButton2.clicked.connect()
        # cls.ui.KeySettingButton3.clicked.connect()
        # cls.ui.KeySettingButton4.clicked.connect()
        # cls.ui.KeySettingButton5.clicked.connect()
        # cls.ui.KeySettingButton6.clicked.connect()
        # cls.ui.KeySettingButton7.clicked.connect()
        # cls.ui.KeySettingButton8.clicked.connect()

    @classmethod
    def __animation_signal_init(cls):
        cls.ui.change_instrumenttheme_animation.Animation.finished.connect(lambda : cls.ui.WorkSpace.setStyleSheet(cls.ui.current_theme))
        cls.ui.change_total_theme_animation.Animation.finished.connect(lambda : cls.ui.Background.setStyleSheet(cls.ui.current_theme))

    @classmethod
    def __quit_signal_init(cls):
        cls.ui.QuitButton.clicked.connect(sys.exit)

    @classmethod
    def __page_signal_init(cls):
        cls.ui.BlueToothButton.clicked.connect(lambda : cls.__change_page(BLUETOOTH_PAGE_INDEX))
        cls.ui.InstrumentButton.clicked.connect(lambda : cls.__change_page(INSTRUMENT_PAGE_INDEX))
        cls.ui.SettingButton.clicked.connect(lambda : cls.__change_page(SETTING_PAGE_INDEX))

    @classmethod
    def __instrument_signal_init(cls):
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
        cls.ui.change_instrumenttheme_animation.change_theme(widget_theme, "instrument")
        cls.ui.change_total_theme_animation.change_theme(widget_theme, "total")

        cls.ui.current_theme = widget_theme["style"]

        cls.ui.before_instrument = StyleHandler.change_style(cls.ui.before_instrument, UNSELECTED_INSTRUMENT_STYLE)
        now_instrument = StyleHandler.change_style(now_instrument, SELECTED_INSTRUMENT_STYLE)

        cls.ui.before_instrument = now_instrument
        cls.ui.selected_instrument = cls.ui.instrument_backs.index(now_instrument) + 1