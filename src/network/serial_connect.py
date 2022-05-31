import time
import serial
import asyncio
import pygame
from PyQt5.QtGui import QPixmap

from constants import (
    DEVICE_READY_STATUS_STYLE,
    DEVICE_READY_STATUS_ICON_STYLE,
    DEVICE_DISABLE_STATUS_STYLE,
    DEVICE_DISABLE_STATUS_ICON_STYLE
)

from music.player import music_player


def serial_socket(ui):
    icon_pixmap = QPixmap()
    arduino = serial.Serial(port='COM6', baudrate=9600)
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

    lst = [0 for i in range(8)]

    while True:
        start_time = time.time()
        i = arduino.readline().decode('utf-8')
        if lst != i:
            lst = i
            asyncio.run(music_player(lst))
            device_status(lst, ui)

def device_status(lst, ui):
    status = [ui.Status1, ui.Status2, ui.Status3, ui.Status4, ui.Status5, ui.Status6, ui.Status7, ui.Status8]

    for i in range(8):
        if lst[i] == '0' or '1':
            status[i].setStyleSheet(DEVICE_READY_STATUS_STYLE)
        elif lst[i] == '2':
            status[i].setStyleSheet(DEVICE_DISABLE_STATUS_STYLE)