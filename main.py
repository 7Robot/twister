import pygame
import os
import time
import random

pygame.mixer.init()

players = ['player/daniel.ogg', 'player/pepino.ogg']
bodyparts = ['body/ton pied.ogg', 'body/ta main.ogg']
colors = ['color/bleu.ogg', 'color/rouge.ogg', 'color/jeune.ogg', 'color/vert.ogg']
sides = ['side/gauche', 'side/droite']


player = pygame.mixer.Sound(players[1])
bodypart = pygame.mixer.Sound(bodyparts[1])
color = pygame.mixer.Sound(colors[2])
side = pygame.mixer.Sound(sides[1])

mets = pygame.mixer.Sound('mets.ogg')
surle = pygame.mixer.Sound('sur le.ogg')

player.play()
while pygame.mixer.get_busy() == True:
    continue

mets.play()
while pygame.mixer.get_busy() == True:
    continue

bodypart.play()
while pygame.mixer.get_busy() == True:
    continue

surle.play()
while pygame.mixer.get_busy() == True:
    continue
time.sleep(0.5)

color.play()
while pygame.mixer.get_busy() == True:
    continue
pygame.mixer.quit()


# pygame.mixer.music.load("player/daniel.ogg")
# pygame.mixer.music.queue("mets ton.ogg")
# pygame.mixer.music.queue("body/pied.ogg")
# pygame.mixer.music.queue("sur le.ogg")
# pygame.mixer.music.queue("color/bleu.ogg")
#
#
# pygame.mixer.music.play()
# while pygame.mixer.music.get_busy() == True:
#     continue