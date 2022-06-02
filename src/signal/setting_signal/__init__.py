from .device_select import DeviceSelectSignal
from .key_setting import KeySettingSignal
from .volume import VolumeSignal


class SettingSignalHandler():
    @staticmethod
    def setting_signal_init(ui):
        DeviceSelectSignal.device_select_signal_init(ui)
        KeySettingSignal.setting_signal_init(ui)
        VolumeSignal.volume_signal_init(ui)