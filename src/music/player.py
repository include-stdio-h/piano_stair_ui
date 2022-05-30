import pygame
import time

from constants import INSTRUMENTS

pygame.init()
pygame.mixer.pre_init(44100, 16, 2, 4096) 
pygame.mixer.init()

music_keys = ["do.wav", "re.wav", "mi.wav", "fa.wav", "sol.wav", "la.wav", "si.wav", "high_do.wav"]

key_lst = [pygame.mixer.Sound(f"music/instruments/{INSTRUMENTS[3]}/{key}") for key in music_keys]
channel_lst = [pygame.mixer.Channel(i) for i in range(8)]

def select_instrument(instrument_num):
    global key_lst
    key_lst = [pygame.mixer.Sound(f"music/instruments/{INSTRUMENTS[instrument_num]}/{key}") for key in music_keys]

    if INSTRUMENTS[instrument_num] == "Accordion" or "Vibra_phone" or "Grandpiano":
        for key in key_lst:
            key.set_volume(0.4)

def music_player(socket_lst, key_index, test_lst):
    while True:
        if test_lst[key_index] == 0:
            if socket_lst[key_index*2+1] == '1':
                # channel_lst[key_index].play(key_lst[key_index])
                test_lst[key_index] = 1
                while socket_lst[key_index*2+1] == '1':
                    pass
            test_lst[key_index] = 1

def do_play(lst):
   while True:
        if lst[1] == '1':
            key_lst[0].play()
            while lst[1] == '1':
                time.sleep(0.08)

def re_play(lst):
    while True:
        if lst[3] == '1':
            key_lst[1].play()
            while lst[3] == '1':
                time.sleep(0.08)

def mi_play(lst):
    while True:
        if lst[5] == '1':
            key_lst[2].play()
            while lst[5] == '1':
                time.sleep(0.08)

def fa_play(lst):
    while True:
        if lst[7] == '1':
            key_lst[3].play()
            while lst[7] == '1':
                time.sleep(0.08)

def sol_play(lst):
    while True:
        if lst[9] == '1':
            key_lst[4].play()
            while lst[9] == '1':
                time.sleep(0.08)

def la_play(lst):
    while True:
        if lst[11] == '1':
            key_lst[5].play()
            while lst[11] == '1':
                time.sleep(0.08)

def si_play(lst):
    while True:
        if lst[13] == '1':
            key_lst[6].play()
            while lst[13] == '1':
                time.sleep(0.08)

def high_do_play(lst):
    while True:
        if lst[15] == '1':
            key_lst[7].play()
            while lst[15] == '1':
                time.sleep(0.08)
