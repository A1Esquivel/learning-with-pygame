import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Corvids Adventure')
clock = pygame.time.Clock()
test_font = pygame.font.Font('fonts/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('Graphics/Sky.png')
ground_surface = pygame.image.load('Graphics/Ground.png')
text_surface = test_font.render('Corvids Adventure', False, 'Black')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0,300))
    screen.blit(text_surface,(300,50))
    pygame.display.update()
    clock.tick(60)