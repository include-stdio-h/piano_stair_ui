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


music_status = [1 for i in range(8)]
lst = [0 for i in range(8)]

def serial_socket(ui):
    global lst, music_status
    icon_pixmap = QPixmap()
    arduino = serial.Serial(port='/dev/ttyUSB8', baudrate=9600)
    # arduino = serial.Serial(port='COM6', baudrate=9600, timeout=.1)

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
    
    arduino_thread = threading.Thread(target=socket_thread, args=(arduino, ))
    arduino_thread.start()

    while True:
        start_time = time.time()
        if sum(music_status) == 8:
            music_status = [0 for i in range(8)]
            # lst = i
            # device_status(lst, ui)
            # time.sleep(0.1)

        # if sum(music_status) == 8:
        #     music_status = [0 for i in range(8)]
        #     arduino.write(bytes('1', 'utf-8'))
        #     i = arduino.readline().decode('utf-8')
        #     print(i)
        #     print(len(i))
        #     if len(i) == 12:
        #         lst = i
        #         device_status(lst, ui)
        #         time.sleep(0.1)
        # else:
        #     arduino.write(bytes('2', 'utf-8'))

def device_status(lst, ui):
    status = [ui.Status1, ui.Status2, ui.Status3, ui.Status4, ui.Status5, ui.Status6, ui.Status7, ui.Status8]

    for i in range(8):
        if lst[i] == '0' or '1':
            status[i].setStyleSheet(DEVICE_READY_STATUS_STYLE)
        elif lst[i] == '2':
            status[i].setStyleSheet(DEVICE_DISABLE_STATUS_STYLE)
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
            if lst[key_index] == '1':
                print(f"{music_keys[key_index]}")
                channel_lst[key_index].play(key_lst[key_index])
                music_status[key_index] = 1
                while lst[key_index] == '1':
                    pass
            else:
                music_status[key_index] = 1

def socket_thread(arduino):
    global lst
    while True:
        i = arduino.readline().decode('utf-8')
        print(i)
        print(len(i))
        lock = threading.Lock()
        if lst != i:
            lock.acquire()
            lst = i
            if sum(music_status) == 8:
                time.sleep(0.05)
                lock.release()
