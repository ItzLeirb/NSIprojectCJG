# project
from game import *
from settings import *

# Gabriel
def affichageConsole(grille: list[list[int]], joueur: int):
    print("  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | ")
    for ligne in range(len(grille[0])):
        ligne_texte = f"{ligne} | "
        for colonne in range(len(grille)):
            ligne_texte += f"{JOUEUR_IMAGE[grille[colonne][ligne]]} | "
        print(ligne_texte)
    
    print("")
    print(f"Au tour du joueur {joueur % 2 + 1}")
    

# Cyprien le best
def tour():
    """
    Fait tourner la partie entiere
    """
    grille = [[0]*6]*7
    joueurs = setupJoueur()
    running = True
    joueur = 0
    while running == True:
        joueur += 1
        if joueur > 2:
            joueur = 1

        index_colonne = trouverColonne(joueurs[joueur])
        grille, index_ligne = ajouterJeton(grille, index_colonne, joueur)
    
        if isVerticalWin(grille, index_colonne, index_ligne, joueur) == True or isHorizontalWin(grille, index_colonne, index_ligne, joueur) == True or isDiagonalBottomLeftToTopRightWin(grille, index_colonne, index_ligne, joueur) == True or isDiagonalTopLeftToBottomRightWin(grille, index_colonne, index_ligne, joueur) == True: 
            running == False
