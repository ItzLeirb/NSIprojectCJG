# project
from game import *
from settings import *

# Gabriel tests ok
def affichageConsole(grille: list[list[int]], joueur: int):
    """
    affiche l'état actuel de la grille dans la console 
    Entrée : grille type: list, 
             joueur type: int
    """
    print("  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | ")
    for ligne in range(len(grille[0])):
        ligne_texte = f"{ligne} | "
        for colonne in range(len(grille)):
            ligne_texte += f"{JOUEURS_IMAGE[grille[colonne][ligne]]} | "
        print(ligne_texte)
    
    print("")
    print(f"Au tour du joueur {joueur % 2 + 1}")
    

# Cyprien
def jeu():
    """
    Fait tourner la partie entière.
    Coordonne les différentes fonctions pour faire fonctioner le jeu.
    """
    # Création de la grille, mise en place des variables importantes
    grille = [[0]*6]*7
    joueurs = setupJoueur()
    running = True
    joueur = 0
    nombre_coups = 0
    
    # La boucle principale
    while running == True:
        # Change le joueur
        joueur += 1
        if joueur > 2:
            joueur = 1

        # Fait jouer le joueur
        index_colonne = trouverColonne(joueurs[joueur])
        grille, index_ligne = ajouterJeton(grille, index_colonne, joueur)

        # Vérifie si la partie est finie (victoire ou match nul)
        nombre_coups += 1
        if isVerticalWin(grille, index_colonne, index_ligne, joueur) == True or isHorizontalWin(grille, index_ligne, joueur) == True or isDiagonalBottomLeftToTopRightWin(grille, index_colonne, index_ligne, joueur) == True or isDiagonalTopLeftToBottomRightWin(grille, index_colonne, index_ligne, joueur) == True: 
            running == False
        elif nombre_coups >= 42:
            running == False


if __name__ == '__main__':
    jeu()