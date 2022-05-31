import threading
import time
import pygame
from bluetooth import *

pygame.init()
pygame.mixer.init()
socket = BluetoothSocket( RFCOMM )
socket.connect(("98:D3:71:F9:6A:40", 1))
print("bluetooth connected!")

data = '' #문자열을 저장할 변수
lst = [0] * 17 #리스트 

do = pygame.mixer.Sound("music/instruments/Grandpiano/do.wav")
re = pygame.mixer.Sound("music/instruments/Grandpiano/re.wav")
mi = pygame.mixer.Sound("music/instruments/Grandpiano/mi.wav")
fa = pygame.mixer.Sound("music/instruments/Grandpiano/fa.wav")
sol = pygame.mixer.Sound("music/instruments/Grandpiano/sol.wav")
la = pygame.mixer.Sound("music/instruments/Grandpiano/la.wav")
si = pygame.mixer.Sound("music/instruments/Grandpiano/si.wav")
high_do = pygame.mixer.Sound("music/instruments/Grandpiano/high_do.wav")

def do_play():
   while True:
        if lst[1] == '1':

            do.play()

            while lst[1] == '1':
                time.sleep(0.08)

def re_play():
    while True:
        
        if lst[3] == '1':
            
            re.play()
            
            while lst[3] == '1':
                time.sleep(0.08)

def mi_play():
    while True:
        
        if lst[5] == '1':

            mi.play()
            
            while lst[5] == '1':
                time.sleep(0.08)

def fa_play():
    while True:
       
        if lst[7] == '1':
           
            fa.play()
            
            while lst[7] == '1':
                time.sleep(0.08)

def sol_play():
    while True:
        
        if lst[9] == '1':
            
            sol.play()
            
            while lst[9] == '1':
                time.sleep(0.08)

def la_play():
    while True:
        
        if lst[11] == '1':
            
            la.play()
            
            while lst[11] == '1':
                time.sleep(0.08)

def si_play():
    while True:
        
        if lst[13] == '1':
            
            si.play()
            
            while lst[13] == '1':
                time.sleep(0.08)

def high_do_play():
    while True:
        
        if lst[15] == '1':
            
            high_do.play()
            
            while lst[15] == '1':
                time.sleep(0.08)
                

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
    for i in socket.recv(1024):
        i = chr(i).encode('utf-8').decode('utf-8') #아스키코드를 문자열로 변환
        data += i #data에 문자열을 합치기
        if i == ']':
            data = list(data) #data를 리스트로 변경
            for h in range(len(data)): 
                lst[h] = data[h]
                print(lst)
            time.sleep(0.08)
            data = ''

socket.close()