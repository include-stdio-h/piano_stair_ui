import pygame
import time

from constants import INSTRUMENTS

pygame.init()
pygame.mixer.pre_init(44100, 16, 2, 4096) 
pygame.mixer.init()

music_keys = ["do.wav", "re.wav", "mi.wav", "fa.wav", "sol.wav", "la.wav", "si.wav", "high_do.wav"]

key_lst = [pygame.mixer.Sound(f"music/instruments{INSTRUMENTS[3]}/{key}") for key in music_keys]

def select_instrument(instrument_num):
    global key_lst
    key_lst = [pygame.mixer.Sound(f"music/instruments{INSTRUMENTS[instrument_num]}/{key}") for key in music_keys]
    # do = pygame.mixer.Sound(f"music/instruments{INSTRUMENTS[instrument_num]}/do.wav")
    # re = pygame.mixer.Sound(f"music/instruments{INSTRUMENTS[instrument_num]}/re.wav")
    # mi = pygame.mixer.Sound(f"music/instruments{INSTRUMENTS[instrument_num]}/mi.wav")
    # fa = pygame.mixer.Sound(f"music/instruments{INSTRUMENTS[instrument_num]}/fa.wav")
    # sol = pygame.mixer.Sound(f"music/instruments{INSTRUMENTS[instrument_num]}/sol.wav")
    # la = pygame.mixer.Sound(f"music/instruments{INSTRUMENTS[instrument_num]}/la.wav")
    # si = pygame.mixer.Sound(f"music/instruments{INSTRUMENTS[instrument_num]}/si.wav")
    # high_do = pygame.mixer.Sound(f"music/instruments{INSTRUMENTS[instrument_num]}/high_do.wav")


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
