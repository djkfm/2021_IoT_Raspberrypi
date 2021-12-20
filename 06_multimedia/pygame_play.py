import pygame

pygame.init()

pygame.mixer.music.load('example.wav')

while True:
    cmd = input('play: p, pause: pp, unpause: up, stop: s, suit: q >')
    if cmd == 'p':
        pygame.mixer.music.play()
    elif cmd == 'pp':
        pygame.mixer.music.pause()
    elif cmd == 'up':
        pygame.mixer.music.unpause()
    elif cmd == 's':
        pygame.mixer.music.stop()
    elif cmd == 'q':
        break
    else:
        print("wrong")

        pygame.mixer.music.unload()