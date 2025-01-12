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

# Gabriel test ok
def positionnerJeton(index_joueur: int, coordonees_grille: tuple[int, int]):
    """
    Renvoie l'image placee d'un jeton pouvant etre interpretee par pygame.
    
    Entree:
        index_joueur (type: int): l'index du joueur (1 ou 2) pour choisir la couleur du jeton
        coordonees_grille (type: tuple[int, int]): les coordonees du jeton joue sur la grille

    Sortie:
        un (type: tuple[pg.image, tuple[int, int]]) contenant l'image du jeton joue, ainsi que ses coordonnees sur la fenetre ou None si le joueur n'existe pas
    """
    
    if index_joueur == 1:
        return (jeton_jaune, ((ORIGINE_GRILLE[0] + 17 * coordonees_grille[0]) * TAILLE_COEFFICIENT, (ORIGINE_GRILLE[1] + 17 * coordonees_grille[1]) * TAILLE_COEFFICIENT))
    if index_joueur == 2:
        return (jeton_rouge, ((ORIGINE_GRILLE[0] + 17 * coordonees_grille[0]) * TAILLE_COEFFICIENT, (ORIGINE_GRILLE[1] + 17 * coordonees_grille[1]) * TAILLE_COEFFICIENT))
    return None

if __name__ == '__main__':
    
    # pygame setup
    pg.init()
    fenetre = pg.display.set_mode(TAILLE_FENETRE)
    clock = pg.time.Clock()
    running = True
    
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
    
        # RENDER YOUR GAME HERE
        grille_image.blits()
    
        fenetre.blit(grille_image, (0,0))
        
        # flip() the display to put your work on fenetre
        pg.display.flip()
    
        clock.tick(60)  # limits FPS to 60
    
    pg.quit()