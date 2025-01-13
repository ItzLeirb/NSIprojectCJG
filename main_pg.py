import pygame as pg
from os import path

from game import *
from settings import *

# constantes pour pygame
MAIN_DIR = path.dirname('__main__')
IMG_DIR = path.join(MAIN_DIR, 'img')

SIZE_MULTIPLIER = 2
WIDTH = 128 * SIZE_MULTIPLIER
HEIGHT = 128 * SIZE_MULTIPLIER

# pygame setup
pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()
running = True

# chargement des images
jeton_jaune = pg.image.load(path.join(IMG_DIR, 'jaune.png')).convert() 
jeton_rouge = pg.image.load(path.join(IMG_DIR, 'rouge.png')).convert() 
grille_image = pg.image.load(path.join(IMG_DIR, 'grille.png')).convert()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # RENDER YOUR GAME HERE
    screen.blit(grille_image, (0,0))

    # flip() the display to put your work on screen
    pg.display.flip()

    clock.tick(60)  # limits FPS to 60

pg.quit()