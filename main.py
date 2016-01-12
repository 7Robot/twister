import pygame
import os
pygame.mixer.init()
pygame.mixer.music.load("1.wav")
pygame.mixer.music.queue("2.wav")

for x in range(0, 3):
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue

