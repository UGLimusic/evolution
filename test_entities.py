import pygame
from entities import *

GRID_SIZE = 5
SCREEN_WIDTH, SCREEN_HEIGHT = GRID_WIDTH * GRID_SIZE, GRID_HEIGHT * GRID_SIZE
BLUE = (0, 0, 255)
RED = (255, 0, 0)

pygame.init()
surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
FPS = 60


def draw_predators():
    for predator in Predator.population:
        pygame.draw.rect(surface, RED, (predator.x * GRID_SIZE, predator.y * GRID_SIZE, GRID_SIZE, GRID_SIZE))


def draw_aliens():
    for alien in Alien.population:
        pygame.draw.rect(surface, BLUE, (alien.x * GRID_SIZE, alien.y * GRID_SIZE, GRID_SIZE, GRID_SIZE))


def draw():
    surface.fill((0, 0, 0, 10))
    Alien.update_all()
    Predator.update_all()
    draw_aliens()
    draw_predators()


Alien(0, GRID_HEIGHT - 1)
Alien(GRID_WIDTH - 1, 0)
Alien(GRID_WIDTH // 2, GRID_HEIGHT // 2)
Alien(GRID_WIDTH // 2 - 3, GRID_HEIGHT // 2 + 3)
Predator(0, 0)
Predator(GRID_WIDTH - 1, GRID_HEIGHT - 1)

go_on = True

while go_on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            go_on = False
    draw()
    pygame.display.update()
    clock.tick(60)
pygame.quit()
