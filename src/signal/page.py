from constants import BLUETOOTH_PAGE_INDEX, INSTRUMENT_PAGE_INDEX, SETTING_PAGE_INDEX


class PageSignal():
    @classmethod
    def page_signal_init(cls, ui):
        cls.ui = ui

        cls.ui.BlueToothButton.clicked.connect(lambda : cls.__change_page(BLUETOOTH_PAGE_INDEX))
        cls.ui.InstrumentButton.clicked.connect(lambda : cls.__change_page(INSTRUMENT_PAGE_INDEX))
        cls.ui.SettingButton.clicked.connect(lambda : cls.__change_page(SETTING_PAGE_INDEX))

    @classmethod
    def __change_page(cls, page_index):
        cls.ui.selected_menu_updown.updown_animation(page_index)
        cls.ui.WorkSpace.setCurrentIndex(page_index)