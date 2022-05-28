import threading
import time
import pygame
from bluetooth import BluetoothSocket, RFCOMM
from PyQt5.QtGui import QPixmap

import music.player as mpl
from constants import (
    DEVICE_READY_STATUS_STYLE,
    DEVICE_READY_STATUS_ICON_STYLE,
    DEVICE_DISABLE_STATUS_STYLE,
    DEVICE_DISABLE_STATUS_ICON_STYLE
)


def bluetooth_socket(ui):
    icon_pixmap = QPixmap()

    pygame.init()
    pygame.mixer.init()
    socket = BluetoothSocket( RFCOMM )
    try:
        socket.connect(("98:D3:71:F9:6A:40", 1))
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

    data = list()
    lst = [0] * 17

    music_play_functions = [mpl.do_play, mpl.re_play, mpl.mi_play, mpl.fa_play, mpl.sol_play, mpl.la_play, mpl.si_play, mpl.high_do_play]

    music_threads = [threading.Thread(target=music_func, args=(lst,)) for music_func in music_play_functions]

    for i in music_threads: 
        i.start()

    while True:
        for i in socket.recv(1024):
            i = chr(i).encode('utf-8').decode('utf-8')
            data.append(i)
            if i == ']':
                device_status(data, ui)
                time.sleep(0.08)
                data = list()

    socket.close()


def device_status(lst, ui):
    status = [ui.Status1, ui.Status2, ui.Status3, ui.Status4, ui.Status5, ui.Status6, ui.Status7, ui.Status8]
    
    count = 1

    for i in range(len(lst)):
        if lst[i] == '0' or lst[i] == '1':
            status[i-count].setStyleSheet(DEVICE_READY_STATUS_STYLE)
            count += 1
        elif lst[i] == '2':
            status[i-count].setStyleSheet(DEVICE_DISABLE_STATUS_STYLE)
            count += 1

