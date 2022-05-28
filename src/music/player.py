import pygame
import time

from constants import INSTRUMENTS

pygame.init()
pygame.mixer.pre_init(44100, 16, 2, 4096) 
pygame.mixer.init()


do = pygame.mixer.Sound(f"music/instruments{INSTRUMENTS[3]}/do.wav")
re = pygame.mixer.Sound(f"music/instruments{INSTRUMENTS[3]}/re.wav")
mi = pygame.mixer.Sound(f"music/instruments{INSTRUMENTS[3]}/mi.wav")
fa = pygame.mixer.Sound(f"music/instruments{INSTRUMENTS[3]}/fa.wav")
sol = pygame.mixer.Sound(f"music/instruments{INSTRUMENTS[3]}/sol.wav")
la = pygame.mixer.Sound(f"music/instruments{INSTRUMENTS[3]}/la.wav")
si = pygame.mixer.Sound(f"music/instruments{INSTRUMENTS[3]}/si.wav")
high_do = pygame.mixer.Sound(f"music/instruments{INSTRUMENTS[3]}/high_do.wav")

def select_instrument(instrument_num):
    global do, re, mi, fa, sol, la, si, high_do
    print(instrument_num)
    do = pygame.mixer.Sound(f"music/instruments{INSTRUMENTS[instrument_num]}/do.wav")
    re = pygame.mixer.Sound(f"music/instruments{INSTRUMENTS[instrument_num]}/re.wav")
    mi = pygame.mixer.Sound(f"music/instruments{INSTRUMENTS[instrument_num]}/mi.wav")
    fa = pygame.mixer.Sound(f"music/instruments{INSTRUMENTS[instrument_num]}/fa.wav")
    sol = pygame.mixer.Sound(f"music/instruments{INSTRUMENTS[instrument_num]}/sol.wav")
    la = pygame.mixer.Sound(f"music/instruments{INSTRUMENTS[instrument_num]}/la.wav")
    si = pygame.mixer.Sound(f"music/instruments{INSTRUMENTS[instrument_num]}/si.wav")
    high_do = pygame.mixer.Sound(f"music/instruments{INSTRUMENTS[instrument_num]}/high_do.wav")


def do_play(lst):
   while True:
        if lst[1] == '1':
            do.play()
            while lst[1] == '1':
                time.sleep(0.08)

def re_play(lst):
    while True:
        
        if lst[3] == '1':
            
            re.play()
            
            while lst[3] == '1':
                time.sleep(0.08)

def mi_play(lst):
    while True:
        
        if lst[5] == '1':

            mi.play()
            
            while lst[5] == '1':
                time.sleep(0.08)

def fa_play(lst):
    while True:
       
        if lst[7] == '1':
           
            fa.play()
            
            while lst[7] == '1':
                time.sleep(0.08)

def sol_play(lst):
    while True:
        
        if lst[9] == '1':
            
            sol.play()
            
            while lst[9] == '1':
                time.sleep(0.08)

def la_play(lst):
    while True:
        
        if lst[11] == '1':
            
            la.play()
            
            while lst[11] == '1':
                time.sleep(0.08)

def si_play(lst):
    while True:
        
        if lst[13] == '1':
            
            si.play()
            
            while lst[13] == '1':
                time.sleep(0.08)

def high_do_play(lst):
    while True:
        
        if lst[15] == '1':
            
            high_do.play()
            
            while lst[15] == '1':
                time.sleep(0.08)
