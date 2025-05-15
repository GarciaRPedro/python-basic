#
#
#                   Algoritmo que abre e reproduz um arquivo MP3
#
#
#
import pygame
pygame.init()
pygame.mixer.music.load('python-basic/ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()
