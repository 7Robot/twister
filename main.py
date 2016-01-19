import pygame
import os
from os import listdir
from os.path import isfile, join

import time
import random

pygame.mixer.init()


initphrases = [f for f in listdir('0_start/') if isfile(join('0_start/', f))]
players = [f for f in listdir('1_player/') if isfile(join('1_player/', f))]
actions = [f for f in listdir('2_action/') if isfile(join('2_action/', f))]
facons = [f for f in listdir('3_facon/') if isfile(join('3_facon/', f))]
bodyparts = ['1.ogg','1.ogg','1.ogg','1.ogg','2.ogg','2.ogg','2.ogg','2.ogg','3.ogg','3.ogg','3.ogg','3.ogg','4.ogg','4.ogg','4.ogg','4.ogg','5.ogg','6.ogg','7.ogg']
sides = ["left", "right"]
colors = [f for f in listdir('8_color/') if isfile(join('8_color/', f))]
maleadj = [f for f in listdir('5_adj/m/') if isfile(join('5_adj/m/', f))]
femaleadj = [f for f in listdir('5_adj/f/') if isfile(join('5_adj/f/', f))]




print "Runnung twister generator in ifinite loop, press Ctrl+C to exit"

turn = 1

start = pygame.mixer.Sound("0_start/"+random.choice(initphrases))

start.play()
while pygame.mixer.get_busy() == True:
    continue

while (True):
    side = random.choice(sides)
    player = pygame.mixer.Sound("1_player/"+random.choice(players))
    action = pygame.mixer.Sound("2_action/"+random.choice(actions))
    facon = pygame.mixer.Sound("3_facon/"+random.choice(facons))
    genderref = "6_bodypart/"+random.choice(bodyparts)
    bodypart = pygame.mixer.Sound(genderref)
    color = pygame.mixer.Sound("8_color/"+random.choice(colors))

    if genderref == "6_bodypart/1.ogg" or genderref == "6_bodypart/2.ogg" or genderref == "6_bodypart/7.ogg":
        gender = "male"

    elif genderref == "6_bodypart/3.ogg" or genderref == "6_bodypart/4.ogg" or genderref == "6_bodypart/5.ogg":
        gender = "female"

    else:
        gender = "plural"

    if gender == "male":
        taton = "4_taton/2.ogg"
        adjective = pygame.mixer.Sound('5_adj/m/'+ random.choice(maleadj))

    elif gender == "female":
        taton = "4_taton/1.ogg"
        adjective = pygame.mixer.Sound('5_adj/f/'+ random.choice(femaleadj))

    else:
        taton = "4_taton/3.ogg"
        adjective = pygame.mixer.Sound('5_adj/m/'+ random.choice(maleadj))

    pronom = pygame.mixer.Sound(taton)



    #
    # print genderref
    # print gender
    # print side
    # print adjective
    if turn != 1:
        player.play()
        while pygame.mixer.get_busy() == True:
            continue

    action.play()
    while pygame.mixer.get_busy() == True:
        continue

    facon.play()
    while pygame.mixer.get_busy() == True:
        continue

    pronom.play()
    while pygame.mixer.get_busy() == True:
        continue

    adjective.play()
    while pygame.mixer.get_busy() == True:
        continue


    bodypart.play()
    while pygame.mixer.get_busy() == True:
        continue

    color.play()
    while pygame.mixer.get_busy() == True:
        continue
    turn += 1
    time.sleep(2)

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