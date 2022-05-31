import asyncio
from bluetooth import BluetoothSocket, RFCOMM
from PyQt5.QtGui import QPixmap

from music.player import music_player
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

    while True:
        i = socket.recv(1024).decode('utf-8')
        if lst != i:
            lst = i
            asyncio.run(music_player(lst))
            device_status(lst, ui)

def device_status(lst, ui):
    status = [ui.Status1, ui.Status2, ui.Status3, ui.Status4, ui.Status5, ui.Status6, ui.Status7, ui.Status8]

    print(lst)

    for i in range(8):
        print(lst[i])
        print(type(lst[i]))
        if lst[i] == '0' or '1':
            status[i].setStyleSheet(DEVICE_READY_STATUS_STYLE)
        elif lst[i] == '2':
            print("-------------------")
            status[i].setStyleSheet(DEVICE_DISABLE_STATUS_STYLE)