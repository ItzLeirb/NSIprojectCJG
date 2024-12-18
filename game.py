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
    choisir la colonne, le jeton   doit tomber ( verifier toutes les [num colone][elt] pour placer le jeton au L[num colone][remplie - 1]
    ajoute un jeton X ou O selon le joueur
    en cas de colonne invalide, le coups doit etre rejoue <- non, fait dans tour()
    sortie : affiche la Liste modifiee (jeton ajoute dans le tableau)
    """
    for index_ligne, jeton in enumerate(grille[colonne]):
        if jeton != 0:  #la case de la grille n'est vide
            grille[colonne][index_ligne-1] = joueur
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

# Julle test par Gabriel
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
def setupJoueur() -> dict:
    joueurs = {
        1 : input(f"Nom du joueur {JOUEURS[1]}"),
        2 : input(f"Nom du joueur {JOUEURS[2]}")
    }

    return joueurs

def trouverColonne(nom_joueur: str) -> int:
    """
    choisit la colonne + verifie si valide

    Entrée: nom_joueur, le nom du joueur qui choisit la colonne
    Sortie: le numéro de la colonne
    """

    print(f"Choisis la colonne où tu veux jouer {nom_joueur} (compris entre 0 et 6) :")
    colonne = int(input(""))

    valides = [i for i in range(7)]
    while colonne not in valides:
        print(f"La colonne choisie n'est pas valide. Choisis la colonne où tu veux jouer {nom_joueur} (compris entre 0 et 6) :")
        colonne = int(input(""))
    
    return colonne


# Cyprien le best
def tour():
    # PLZZZZZ faites la liste ici je sais plus les dimentions @JULESSSSSSSS
    joueurs = setupJoueur()
    running = True
    joueur = 0
    while running == True:
        joueur += 1
        if joueur > 2:
            joueur = 1

    grille == ajouterJeton(grille, trouverColonne(joueurs[joueur]),joueur)