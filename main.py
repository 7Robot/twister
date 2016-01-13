import pygame
import os
import time
pygame.mixer.init()

s = pygame.mixer.Sound('body/pied.ogg')


s.play()

time.sleep(5)

pygame.mixer.quit()


# pygame.mixer.music.load("player/Daniel.ogg")
# pygame.mixer.music.queue("mets ton.ogg")
# pygame.mixer.music.queue("body/pied.ogg")
# pygame.mixer.music.queue("sur le.ogg")
# pygame.mixer.music.queue("color/bleu.ogg")
#
#
# pygame.mixer.music.play()
# while pygame.mixer.music.get_busy() == True:
#     continue