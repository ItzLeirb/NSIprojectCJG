import pygame as pg
from os import path

from game import *
from settings import *

# constantes pour pygame
MAIN_DIR = path.dirname('__main__')
IMG_DIR = path.join(MAIN_DIR, 'img')

TAILLE_COEFFICIENT = 6
TAILLE = 128 * TAILLE_COEFFICIENT
TAILLE_FENETRE = (TAILLE, TAILLE)

ORIGINE_GRILLE = (5, 26)

# chargement des images
jeton_jaune = pg.transform.scale(pg.image.load(path.join(IMG_DIR, 'jaune.png')), (TAILLE / 8, TAILLE / 8)) # taille du jeton par rapport à la grille
jeton_rouge = pg.transform.scale(pg.image.load(path.join(IMG_DIR, 'rouge.png')), (TAILLE / 8, TAILLE / 8)) # taille du jeton par rapport à la grille
grille_image = pg.transform.scale(pg.image.load(path.join(IMG_DIR, 'grille.png')), TAILLE_FENETRE)

# pygame setup
pg.init()
fenetre = pg.display.set_mode(TAILLE_FENETRE)
clock = pg.time.Clock()
running = True

def positionnerJeton():
    pass

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # RENDER YOUR GAME HERE
    grille_image.blits([
        (jeton_jaune, ((ORIGINE_GRILLE[0] + 17 * 0) * TAILLE_COEFFICIENT, (ORIGINE_GRILLE[1] + 17 * 5) * TAILLE_COEFFICIENT)),
        (jeton_rouge, ((ORIGINE_GRILLE[0] + 17 * 2) * TAILLE_COEFFICIENT, (ORIGINE_GRILLE[1] + 17 * 5) * TAILLE_COEFFICIENT)),
        (jeton_jaune, ((ORIGINE_GRILLE[0] + 17 * 5) * TAILLE_COEFFICIENT, (ORIGINE_GRILLE[1] + 17 * 5) * TAILLE_COEFFICIENT))
    ])

    fenetre.blit(grille_image, (0,0))
    
    # flip() the display to put your work on fenetre
    pg.display.flip()

    clock.tick(60)  # limits FPS to 60

pg.quit()