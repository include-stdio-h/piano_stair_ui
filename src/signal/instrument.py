from constants import INSTRUMENTS_THEME, SELECTED_INSTRUMENT_STYLE, UNSELECTED_INSTRUMENT_STYLE
from music.player import select_instrument


class InstrumentSignal():
    @classmethod
    def instrument_signal_init(cls, ui):
        cls.ui = ui

        cls.ui.BassGuitarSelect.clicked.connect(lambda : cls.__change_instrument(cls.ui.BassGuitarBack, INSTRUMENTS_THEME["bass_guitar"]))
        cls.ui.OrganSelect.clicked.connect(lambda : cls.__change_instrument(cls.ui.OrganBack, INSTRUMENTS_THEME["organ"]))
        cls.ui.AccordionSelect.clicked.connect(lambda : cls.__change_instrument(cls.ui.AccordionBack, INSTRUMENTS_THEME["accordion"]))
        cls.ui.PianoSelect.clicked.connect(lambda : cls.__change_instrument(cls.ui.PianoBack, INSTRUMENTS_THEME["piano"]))
        cls.ui.HarpSelect.clicked.connect(lambda : cls.__change_instrument(cls.ui.HarpBack, INSTRUMENTS_THEME["harp"]))
        cls.ui.VibraPhoneSelect.clicked.connect(lambda : cls.__change_instrument(cls.ui.VibraPhoneBack, INSTRUMENTS_THEME["vibra_phone"]))

    @classmethod
    def __change_instrument(cls, now_instrument, widget_theme):
        instrument_backs = cls.get_instrument_backs(cls.ui)

        cls.ui.change_instrument_theme_animation.change_theme(widget_theme, "instrument")
        cls.ui.change_total_theme_animation.change_theme(widget_theme, "total")

        cls.ui.current_theme = widget_theme["style"]

        cls.ui.before_instrument.setStyleSheet(UNSELECTED_INSTRUMENT_STYLE)
        now_instrument.setStyleSheet(SELECTED_INSTRUMENT_STYLE)

        cls.ui.before_instrument = now_instrument
        cls.ui.selected_instrument = instrument_backs.index(now_instrument)
        select_instrument(cls.ui.selected_instrument)

    @staticmethod
    def get_instrument_backs(ui):
        return [
            ui.PianoBack,
            ui.HarpBack,
            ui.OrganBack,
            ui.BassGuitarBack,
            ui.AccordionBack,
            ui.VibraPhoneBack
        ]