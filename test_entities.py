import pygame
from entities import *

# Ici c'est du pygame : comme du p5, en plus rapide


GRID_SIZE = 5
SCREEN_WIDTH, SCREEN_HEIGHT = GRID_WIDTH * GRID_SIZE, GRID_HEIGHT * GRID_SIZE
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
pygame.init()  # on init pygame
surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # fenetre d'écran
clock = pygame.time.Clock()  # horloge
FPS = 60


def draw_predators() -> None:
    for predator in Predator.population:
        pygame.draw.rect(surface, RED, (predator.x * GRID_SIZE, predator.y * GRID_SIZE, GRID_SIZE, GRID_SIZE))
        # pygame.draw.rect(surface sur laquelle on dessine, couleur, (top,left,width,height))


def draw_aliens() -> None:
    for alien in Alien.population:
        pygame.draw.rect(surface, BLUE, (alien.x * GRID_SIZE, alien.y * GRID_SIZE, GRID_SIZE, GRID_SIZE))


def draw() -> None:
    surface.fill(BLACK)  # on efface tout
    draw_aliens()
    draw_predators()  # et on recommence


# ici on crée les bebêtes

Alien(0, GRID_HEIGHT - 1)
Alien(GRID_WIDTH - 1, 0)
Alien(GRID_WIDTH // 2, GRID_HEIGHT // 2)
Alien(GRID_WIDTH // 2 - 3, GRID_HEIGHT // 2 + 3)
Predator(0, 0)
Predator(GRID_WIDTH - 1, GRID_HEIGHT - 1)



# voilà une boucle pygame typique :

go_on = True
while go_on:
    for event in pygame.event.get(): # on traite la file d'évènements
        if event.type == pygame.QUIT: # si on a un évènement de type quitter
            go_on = False # on casse la boucle while
    draw() # on dessine
    pygame.display.update() #IMPORTANT : on update l'écran
    clock.tick(FPS) # l'horloge fait bip FPS fois par seconde donc on attend qu'elle bippe

pygame.quit() # Un coup de balai en partant ça ne fait pas de mal.
