from ast import arg
import threading
import time
import pygame
from bluetooth import BluetoothSocket, RFCOMM
from PyQt5.QtGui import QPixmap

import music.player as mpl
from music.player import select_instrument
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

    data = ''
    lst = [0] * 17

    #select_instrument(ui.selected_instrument)
    #print(ui.selected_instrument)

    t1 = threading.Thread(target=mpl.do_play, args=(lst,))
    t1.start()
    t2 = threading.Thread(target=mpl.re_play, args=(lst,))
    t2.start()
    t3 = threading.Thread(target=mpl.mi_play, args=(lst,))
    t3.start()
    t4 = threading.Thread(target=mpl.fa_play, args=(lst,))
    t4.start()
    t5 = threading.Thread(target=mpl.sol_play, args=(lst,))
    t5.start()
    t6 = threading.Thread(target=mpl.la_play, args=(lst,))
    t6.start()
    t7 = threading.Thread(target=mpl.si_play, args=(lst,))
    t7.start()
    t8 = threading.Thread(target=mpl.high_do_play, args=(lst,))
    t8.start()

    while True:
        for i in socket.recv(1024):
            i = chr(i).encode('utf-8').decode('utf-8')
            #i = i.encode('utf-8')
            data += i
            if i == ']':
                data = list(data)
                for h in range(len(data)):
                    lst[h] = data[h]
                print(lst)
                device_status(lst, ui)
                time.sleep(0.08)
                data = ''

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

