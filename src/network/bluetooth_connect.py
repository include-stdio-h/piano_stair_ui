import threading
import pygame
import time
from bluetooth import BluetoothSocket, RFCOMM
from PyQt5.QtGui import QPixmap

from music.player import music_player, socket_read
from constants import (
    DEVICE_READY_STATUS_STYLE,
    DEVICE_READY_STATUS_ICON_STYLE,
    DEVICE_DISABLE_STATUS_STYLE,
    DEVICE_DISABLE_STATUS_ICON_STYLE
)

import pygame

from constants import INSTRUMENTS


music_keys = ["do.wav", "re.wav", "mi.wav", "fa.wav", "sol.wav", "la.wav", "si.wav", "high_do.wav"]

key_lst = [pygame.mixer.Sound(f"music/instruments/{INSTRUMENTS[3]}/{key}") for key in music_keys]
channel_lst = [pygame.mixer.Channel(i) for i in range(8)]

pygame.mixer.pre_init(channels=8) 
pygame.mixer.init()
pygame.init()


lst = [0 for i in range(10)]

def bluetooth_socket(ui):
    global lst
    print("Here")
    icon_pixmap = QPixmap()

    socket = BluetoothSocket( RFCOMM )
    try:
        print("There")
        # socket.connect(("98:D3:71:F9:6A:40", 1))
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

    music_threads = [threading.Thread(target=music_player, args=(i, )) for i in range(8)]

    for i in music_threads:
        i.start()

    while True:
        i = socket.recv(4096).decode('utf-8')
        lst = i
        socket_read(lst)
        device_status(i, ui)

    socket.close()


def device_status(lst, ui):
    status = [ui.Status1, ui.Status2, ui.Status3, ui.Status4, ui.Status5, ui.Status6, ui.Status7, ui.Status8]

    for i in range(1,9):
        if lst[i] == '0' or lst[i] == '1':
            status[i-1].setStyleSheet(DEVICE_READY_STATUS_STYLE)
        elif lst[i] == '2':
            status[i-1].setStyleSheet(DEVICE_DISABLE_STATUS_STYLE)
    return

def select_instrument(instrument_num):
    global key_lst
    key_lst = [pygame.mixer.Sound(f"music/instruments/{INSTRUMENTS[instrument_num]}/{key}") for key in music_keys]

    if INSTRUMENTS[instrument_num] == "Accordion" or "Vibra_phone" or "Grandpiano":
        for key in key_lst:
            key.set_volume(0.4)

def music_player(key_index):
    while True:
        if lst[key_index+1] == '1':
            channel_lst[key_index].play(key_lst[key_index])
            while lst[key_index+1] == '1':
                pass