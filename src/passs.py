import pygame
import random
import datetime
import time
import keyboard
import threading

pygame.mixer.init(frequency = 44100, size = -16, channels = 1, buffer = 2**12)

channel1 = pygame.mixer.Channel(0)
channel2 = pygame.mixer.Channel(1)
channel3 = pygame.mixer.Channel(2)
channel4 = pygame.mixer.Channel(3)
channel5 = pygame.mixer.Channel(4)
channel6 = pygame.mixer.Channel(5)
channel7 = pygame.mixer.Channel(6)
channel8 = pygame.mixer.Channel(7)

musical = ["/Grandpiano", "/Harp", "/Organ",
           "/Trumpet", "/12_lines_of_guitar",
           "/Accordion", "/Vibra_phone"]



music = ["/do.wav","/re.wav", "/mi.wav", 
         "/fa.wav", "/sol.wav", "/la.wav", 
         "/si.wav", "/high_do.wav"]

print(musical)

def do_play():
    while True:
        if keyboard.is_pressed("q"):
            channel1.play(do)
            time.sleep(0.5)
            
def re_play():
    
    while True:
        if keyboard.is_pressed("w"):
            channel2.play(re)
            time.sleep(0.5)
            
def mi_play():
    
    while True:
        if keyboard.is_pressed("e"):
            channel3.play(mi)
            time.sleep(0.5)
            
def fa_play():
    
    while True:
        if keyboard.is_pressed("r"):
            channel4.play(fa)
            time.sleep(0.5)
            
def sol_play():
    
    while True:
        if keyboard.is_pressed("t"):
            channel5.play(sol)
            time.sleep(0.5)
            
def la_play():
    
    while True:
        if keyboard.is_pressed("y"):
            channel6.play(la)
            time.sleep(0.5)
            
def si_play():

    while True:
        if keyboard.is_pressed("u"):
            channel7.play(si)
            time.sleep(0.5)
            
def high_do_play():
    
    while True:
        if keyboard.is_pressed("i"):
            channel8.play(high_do)
            time.sleep(0.5)
            

threads = []

t1 = threading.Thread(target=do_play)
t1.start()
t2 = threading.Thread(target=re_play)
t2.start()
t3 = threading.Thread(target=mi_play)
t3.start()
t4 = threading.Thread(target=fa_play)
t4.start()
t5 = threading.Thread(target=sol_play)
t5.start()
t6 = threading.Thread(target=la_play)
t6.start()
t7 = threading.Thread(target=si_play)
t7.start()
t8 = threading.Thread(target=high_do_play)
t8.start()

while True:

    day = 6
    do = pygame.mixer.Sound("music\instruments"+musical[0]+music[0])
    re = pygame.mixer.Sound("music\instruments"+musical[0]+music[1])
    mi = pygame.mixer.Sound("music\instruments"+musical[0]+music[2])
    fa = pygame.mixer.Sound("music\instruments"+musical[0]+music[3])
    sol = pygame.mixer.Sound("music\instruments"+musical[0]+music[4])
    la = pygame.mixer.Sound("music\instruments"+musical[0]+music[5])    
    si = pygame.mixer.Sound("music\instruments"+musical[0]+music[6])    
    high_do = pygame.mixer.Sound("music\instruments"+musical[0]+music[7])
    if musical[day] == "/Trumpet":
        sound = 0.3
    else:
        sound = 1
        
    do.set_volume(sound)
    re.set_volume(sound)
    mi.set_volume(sound)
    fa.set_volume(sound)
    sol.set_volume(sound)
    la.set_volume(sound)
    si.set_volume(sound)
    high_do.set_volume(sound)
정환님에게 메시지 쓰기
