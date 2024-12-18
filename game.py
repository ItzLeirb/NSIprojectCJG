# main functions
from settings import *

# la grille:
"""
   0  1  2  3  4  5  6  7
0
1
2
3
4
5
6
"""

# Gabriel
def ajouterJeton(grille: list[list[int]], colonne: int,
                 joueur: int) -> list[list[int]]:
    """
    entree : grille: la grille, 
             colonne: la colonne jouee
             joueur: le numero du joueur
    choisir la colonne, verifier que la colone est valide ( existance et remplissage ), le jeton   doit tomber ( verifier toutes les [num colone][elt] pour placer le jeton au L[num colone][remplie - 1]
    ajoute un jeton X ou O selon le joueur
    en cas de colonne invalide, le coups doit etre rejoue <- non, fait dans tour()
    sortie : affiche la Liste modifiee (jeton ajoute dans le tableau)
    """
    for ligne, jeton in enumerate(grille[colonne]):
        if jeton != 0:  #la case de la grille n'est vide
            grille[colonne][ligne-1] = joueur
            break

# Gabriel
def isVerticalWin(grille: list[list[int]], colonne: int, ligne: int, joueur: int) -> bool:
    nombre_daffilee = 0
    for jeton in grille[colonne][ligne:]:
        if jeton == 0: continue

        if jeton == joueur:
            nombre_daffilee += 1
            if nombre_daffilee >= 4:
                return True
        else:
            break
    return nombre_daffilee >= 4

# Cyprien
def isHorizontalWin(grille: list[list[int]], colonne: int, ligne: int, joueur: int) -> bool:
    nombre_daffilee = 0
    for jeton in range(len(grille[colonne])):
        if colonne[i][ligne] == joueur:
            nombre_daffilee += 1
            if nombre_daffilee >= 4:
                return True
        else:
            nombre_daffilee = 0
    return False
<<<<<<< HEAD
=======
        
# Julle test par Gabriel
>>>>>>> e75db8750dd6faf2c573d1a2283f5e4db646d9d8
def isDiagonalBottomLeftToTopRightWin(grille: list[list[int]], colonne: int, ligne: int, joueur: int) -> bool:
   nombre_daffilee = 0
   for i in range(8):
    if grille[colonne + 4 - i][ligne - 4 + i] == joueur:
        nombre_daffilee += 1
        if nombre_daffilee >= 4:
            return True
    else:
        nombre_daffilee = 0
    return False

# Cyprien
def isDiagonalTopLeftToBottomRightWin(grille: list[list[int]], colonne: int, ligne: int, joueur: int) -> bool:
    nombre_daffilee = 0
    ecart = -4
    while ligne - ecart < 0 or colonne - ecart < 0:
        ecart += 1
    for i in range (ecart,4):
        if grille[colonne - 1][ligne - 1] == joueur:
            nombre_daffilee += 1
            if nombre_daffilee >= 4:
                return True
        else:
            nombre_daffilee = 0
    return False

        

# Gabriel
def setupJoueur() -> dict[str:int]:
    joueurs = {
        1 : input(f"Nom du joueur {JOUEURS[1]}"),
        2 : input(f"Nom du joueur {JOUEURS[2]}")
    }

    return joueurs