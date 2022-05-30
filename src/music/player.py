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
            print("??????")
            if socket_lst[key_index*2+1] == '1':
                print("&&&&&&")
                print(music_keys[key_index])
                # channel_lst[key_index].play(key_lst[key_index])
                test_lst[key_index] = 1
                while socket_lst[key_index*2+1] == '1':
                    pass
            test_lst[key_index] = 1