import pygame.mixer

sounds = pygame.mixer
sounds.init()

def wait_finish(channel):
    while channel.get_busy():
        pass

s = sounds.Sound("ohno.wav")
wait_finish(s.play())
