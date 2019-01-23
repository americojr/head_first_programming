#Modulo que sera responsavel por tocar uma musica

import pygame.mixer

sounds = pygame.mixer
sounds.init()

def wait_finish(channel):
    while channel.get_busy():
        pass

def play(music):
    s = sounds.Sound(music)
    wait_finish(s.play())
