mport pygame
from pygame.locals import*
pygame.image.load('OIP.png')

white = (255, 64, 64)
w = 640
h = 480
screen = pygame.display.set_mode((w, h))
screen.fill((white))
running = 1

while running:
    screen.fill((white))

    pygame.display.flip()

    
