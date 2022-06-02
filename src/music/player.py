import pygame

from constants import INSTRUMENTS, MUSIC_KEY_FILES


pygame.mixer.pre_init(channels=8) 
pygame.mixer.init()
pygame.init()

key_lst = [pygame.mixer.Sound(f"music/instruments/{INSTRUMENTS[3]}/{key}") for key in MUSIC_KEY_FILES]
channel_lst = [pygame.mixer.Channel(i) for i in range(8)]
volume = 8

def select_instrument(instrument_num):
    global key_lst
    key_lst = [pygame.mixer.Sound(f"music/instruments/{INSTRUMENTS[instrument_num]}/{key}") for key in MUSIC_KEY_FILES]
    volume_setting(volume/10)

def volume_setting(new_volume):
    global key_lst, volume
    volume = new_volume

    for key in key_lst:
        key.set_volume(volume/10)

async def music_player(lst, before_lst, device_key_status):
    for i in range(8):
        if lst[i] != before_lst[i]:
            await music_play(lst[i], i, device_key_status[i]["key"])

async def music_play(key_status, channel_index,key_index):
    if key_status == '1':
        channel_lst[channel_index].play(key_lst[key_index])