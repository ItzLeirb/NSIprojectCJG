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

TAILLE_JETON = 17

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
        return (jeton_jaune, ((ORIGINE_GRILLE[0] + TAILLE_JETON * coordonees_grille[0]) * TAILLE_COEFFICIENT, (ORIGINE_GRILLE[1] + TAILLE_JETON * coordonees_grille[1]) * TAILLE_COEFFICIENT))
    if index_joueur == 2:
        return (jeton_rouge, ((ORIGINE_GRILLE[0] + TAILLE_JETON * coordonees_grille[0]) * TAILLE_COEFFICIENT, (ORIGINE_GRILLE[1] + TAILLE_JETON * coordonees_grille[1]) * TAILLE_COEFFICIENT))
    return None

if __name__ == '__main__':
    # pygame setup
    pg.init()
    fenetre = pg.display.set_mode(TAILLE_FENETRE)
    pg.display.set_caption("Puissance 4")
    clock = pg.time.Clock()
    running = True
    
    grille = [[0 for i in range(6)] for i in range(7)]
    joueur = 0
    nombre_coups = 0
    tous_jetons = []
    
    while running:            
        # poll for events
        index_colonne = -1
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.KEYDOWN:
                if event.type == pg.K_1:
                    index_colonne = 1
                elif event.type == pg.K_2:
                    index_colonne = 2
                elif event.type == pg.K_3:
                    index_colonne = 3
                elif event.type == pg.K_4:
                    index_colonne = 4
                elif event.type == pg.K_5:
                    index_colonne = 5
                elif event.type == pg.K_6:
                    index_colonne = 6
                elif event.type == pg.K_7:
                    index_colonne = 7
            if event.type == pg.MOUSEBUTTONUP:
                position_souris = pg.mouse.get_pos()
                # Check si la position de la souris est valable (sur une colonne)
                if position_souris[1] > ORIGINE_GRILLE[1] * TAILLE_COEFFICIENT and (ORIGINE_GRILLE[0]-1) * TAILLE_COEFFICIENT <= position_souris[0] <= (ORIGINE_GRILLE[0] + TAILLE_JETON * 7) * TAILLE_COEFFICIENT:
                    position_souris_x = position_souris[0] - (ORIGINE_GRILLE[0]-1) * TAILLE_COEFFICIENT
                    index_colonne = position_souris_x // (TAILLE_JETON * TAILLE_COEFFICIENT)
        if index_colonne >= 0:
            # Change le joueur
            joueur += 1
            if joueur > 2:
                joueur = 1
                
            grille, index_ligne = ajouterJeton(grille, index_colonne, joueur)
            tous_jetons.append(positionnerJeton(joueur, (index_colonne, index_ligne)))
            # Vérifier si le joueur actuel a gagné
            if (detecterVictoireVerticale(grille, index_colonne, index_ligne, joueur) or
                detecterVictoireHorizontale(grille, index_ligne, joueur) or
                detecterVictoireBasGaucheHautDroite(grille, index_colonne, index_ligne, joueur) or
                detecterVictoireHautGaucheBasDroite(grille, index_colonne, index_ligne, joueur)):
                print(f"Joueur {[0,"jaune", "rouge"][joueur]} a gagné !")
                running = False
    
        # affichage
        grille_image.blits(tous_jetons)
    
        fenetre.blit(grille_image, (0,0))
        
        # flip() the display to put your work on fenetre
        pg.display.flip()
    
        clock.tick(60)  # limits FPS to 60
    
    pg.quit()