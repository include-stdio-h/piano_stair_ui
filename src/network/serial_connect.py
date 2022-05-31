import threading
import pygame
import time
import serial
from PyQt5.QtGui import QPixmap

from constants import (
    DEVICE_READY_STATUS_STYLE,
    DEVICE_READY_STATUS_ICON_STYLE,
    DEVICE_DISABLE_STATUS_STYLE,
    DEVICE_DISABLE_STATUS_ICON_STYLE
)

import pygame

from constants import INSTRUMENTS

pygame.mixer.pre_init(channels=8) 
pygame.mixer.init()
pygame.init()

music_keys = ["do.wav", "re.wav", "mi.wav", "fa.wav", "sol.wav", "la.wav", "si.wav", "high_do.wav"]

key_lst = [pygame.mixer.Sound(f"music/instruments/{INSTRUMENTS[3]}/{key}") for key in music_keys]
channel_lst = [pygame.mixer.Channel(i) for i in range(8)]


music_status = [0 for i in range(8)]
lst = [0 for i in range(10)]

def serial_socket(ui):
    global lst
    icon_pixmap = QPixmap()
    arduino = serial.Serial('/dev/ttyUSB0', 9600)

    if arduino.readable():
        print("Serial connected!")
        ui.DeviceStatusLabel.setText("Ready")
        ui.DeviceStatusLabel.setStyleSheet(DEVICE_READY_STATUS_STYLE)
        ui.DeviceStatus.setStyleSheet(DEVICE_READY_STATUS_STYLE)
        ui.DeviceStatusIcon.setStyleSheet(DEVICE_READY_STATUS_ICON_STYLE)
        icon_pixmap.load("style/icons/ready.png")
    else:
        ui.DeviceStatusLabel.setText("Disable")
        ui.DeviceStatusLabel.setStyleSheet(DEVICE_DISABLE_STATUS_STYLE)
        ui.DeviceStatus.setStyleSheet(DEVICE_DISABLE_STATUS_STYLE)
        ui.DeviceStatusIcon.setStyleSheet(DEVICE_DISABLE_STATUS_ICON_STYLE)
        icon_pixmap.load("style/icons/disable.png")
        while arduino.readable(): 
            arduino = serial.Serial('/dev/ttyUSB0', 9600)
            print("Re-connecting")
            time.sleep(3)

    ui.DeviceStatusIcon.setPixmap(icon_pixmap)

    music_threads = list()
    for i in range(8):
        music_threads.append(threading.Thread(target=music_player, args=(i, )))
        music_threads[i].start()

    while True:
        start_time = time.time()
        print(music_status)
        if sum(music_status) == 8:
            i = arduino.readline().decode('utf-8')
            print(time.time() - start_time)
            # print(i)
            lst = i
        # device_status(i, ui)

def device_status(lst, ui):
    status = [ui.Status1, ui.Status2, ui.Status3, ui.Status4, ui.Status5, ui.Status6, ui.Status7, ui.Status8]

    for i in range(1,9):
        if lst[i] == '0' or '1':
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
    global music_status
    while True:
        if music_status[key_index] == 0:
            if lst[key_index+1] == '1':
                channel_lst[key_index].play(key_lst[key_index])
                music_status[key_index] = 1
                while lst[key_index+1] == '1':
                    pass
            music_status[key_index] = 1