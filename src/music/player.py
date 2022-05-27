import pygame
import time

pygame.init()
pygame.mixer.pre_init(44100, 16, 2, 4096) 
pygame.mixer.init()

do = pygame.mixer.Sound("/home/pi/project/piano_stair_ui-main/piano_stair_ui-main/src/music/do.wav")
re = pygame.mixer.Sound("/home/pi/project/piano_stair_ui-main/piano_stair_ui-main/src/music/re.wav")
mi = pygame.mixer.Sound("/home/pi/project/piano_stair_ui-main/piano_stair_ui-main/src/music/mi.wav")
fa = pygame.mixer.Sound("/home/pi/project/piano_stair_ui-main/piano_stair_ui-main/src/music/fa.wav")
sol = pygame.mixer.Sound("/home/pi/project/piano_stair_ui-main/piano_stair_ui-main/src/music/sol.wav")
la = pygame.mixer.Sound("/home/pi/project/piano_stair_ui-main/piano_stair_ui-main/src/music/la.wav")
si = pygame.mixer.Sound("/home/pi/project/piano_stair_ui-main/piano_stair_ui-main/src/music/si.wav")
high_do = pygame.mixer.Sound("/home/pi/project/piano_stair_ui-main/piano_stair_ui-main/src/music/high_do.wav")


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
