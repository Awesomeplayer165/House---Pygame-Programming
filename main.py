import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("House Project")

while True:

    screen.fill((0, 255, 255))

    pygame.draw.polygon(screen, (150, 75, 0), ((100, 600), (100, 300), (300, 100), (500, 300), (500, 600))) # brown house architecture
    pygame.draw.rect(screen, (255, 0, 0), (300, 400, 150, 200)) # Red Door
    pygame.draw.circle(screen, (255, 255, 0), (420, 510), 15) # doorbell
    pygame.draw.circle(screen, (255, 255, 0), (525, 40), 75) # SUN

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()


    pygame.display.update()