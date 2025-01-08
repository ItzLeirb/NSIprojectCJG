import pygame as pg
from os import path

from game import *
from settings import *

# pygame setup
pg.init()
screen = pg.display.set_mode((1280, 720))
clock = pg.time.Clock()
running = True

# constantes pour pygame
MAIN_DIR = path.dirname('__main__')
IMG_DIR = path.join(MAIN_DIR, 'img')

# chargement des images
jeton_jaune = pg.image.load(path.join(IMG_DIR, 'jaune.png')) 
jeton_rouge = pg.image.load(path.join(IMG_DIR, 'rouge.png')) 
grille_image = pg.image.load(path.join(IMG_DIR, 'grille.png'))

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pg.display.flip()

    clock.tick(60)  # limits FPS to 60

pg.quit()