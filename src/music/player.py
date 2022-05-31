import pygame

from constants import INSTRUMENTS

pygame.mixer.pre_init(channels=8) 
pygame.mixer.init()
pygame.init()

music_keys = ["do.wav", "re.wav", "mi.wav", "fa.wav", "sol.wav", "la.wav", "si.wav", "high_do.wav"]

key_lst = [pygame.mixer.Sound(f"music/instruments/{INSTRUMENTS[3]}/{key}") for key in music_keys]
channel_lst = [pygame.mixer.Channel(i) for i in range(8)]

def select_instrument(instrument_num):
    global key_lst
    key_lst = [pygame.mixer.Sound(f"music/instruments/{INSTRUMENTS[instrument_num]}/{key}") for key in music_keys]

    if INSTRUMENTS[instrument_num] == "Accordion" or "Vibra_phone" or "Grandpiano":
        for key in key_lst:
            key.set_volume(0.4)

async def music_player(lst):
    for i in range(8):
        await music_play(lst, i)


async def music_play(lst, key_index):
    if lst[key_index] == '1':
        channel_lst[key_index].play(key_lst[key_index])