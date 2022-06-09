import asyncio
from bluetooth import BluetoothSocket, RFCOMM
from PyQt5.QtGui import QPixmap

from features.music.player import music_player
from constants import (
    DEVICE_READY_STATUS_STYLE,
    DEVICE_READY_STATUS_ICON_STYLE,
    DEVICE_DISABLE_STATUS_STYLE,
    DEVICE_DISABLE_STATUS_ICON_STYLE
)


def serial_socket(ui):
    icon_pixmap = QPixmap()
    socket = BluetoothSocket( RFCOMM )

    try:
        socket.connect(("98:DA:60:03:C9:9C", 1))
        print("bluetooth connected!")
        ui.DeviceStatusLabel.setText("Ready")
        ui.DeviceStatusLabel.setStyleSheet(DEVICE_READY_STATUS_STYLE)
        ui.DeviceStatus.setStyleSheet(DEVICE_READY_STATUS_STYLE)
        ui.DeviceStatusIcon.setStyleSheet(DEVICE_READY_STATUS_ICON_STYLE)
        icon_pixmap.load("style/icons/ready.png")
    except:
        ui.DeviceStatusLabel.setText("Disable")
        ui.DeviceStatusLabel.setStyleSheet(DEVICE_DISABLE_STATUS_STYLE)
        ui.DeviceStatus.setStyleSheet(DEVICE_DISABLE_STATUS_STYLE)
        ui.DeviceStatusIcon.setStyleSheet(DEVICE_DISABLE_STATUS_ICON_STYLE)
        icon_pixmap.load("style/icons/disable.png")

    ui.DeviceStatusIcon.setPixmap(icon_pixmap)

    lst = [0 for i in range(8)]
    before_lst = [0 for i in range(8)]

    while True:
        i = socket.recv(2048).decode('utf-8')
        if lst != i:
            before_lst = lst
            lst = i
            asyncio.run(music_player(lst, before_lst, ui.device_key_status))
            asyncio.run(device_status(lst, ui))
            # device_status(lst, ui)

async def device_status(lst, ui):
    ui_status = [ui.Status1, ui.Status2, ui.Status3, ui.Status4, ui.Status5, ui.Status6, ui.Status7, ui.Status8]

    for _ui, _status in zip(ui_status, lst):
        await device_status_change(_status, _ui)
    # for i in range(8):
    #     if lst[i] == '0' or lst[i] == '1':
    #         status[i].setStyleSheet(DEVICE_READY_STATUS_STYLE)
    #     elif lst[i] == '2':
    #         status[i].setStyleSheet(DEVICE_DISABLE_STATUS_STYLE)

async def device_status_change(status, ui):
    if status == '0' or status == '1':
        ui.setStyleSheet(DEVICE_READY_STATUS_STYLE)
    elif status == '2':
        ui.setStyleSheet(DEVICE_DISABLE_STATUS_STYLE)