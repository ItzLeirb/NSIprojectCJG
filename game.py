# main functions
from settings import *

# la grille:
"""
   0  1  2  3  4  5  6
0
1
2
3
4
5
"""

# Gabriel
def ajouterJeton(grille: list[list[int]], index_colonne: int,
                 joueur: int) -> tuple[list[list[int]], int]:
    """
    entree : grille: la grille, 
             colonne: la colonne jouee
             joueur: le numero du joueur
    choisir la colonne, le jeton doit tomber ( verifier toutes les [num colone][elt] pour placer le jeton au L[num colone][remplie - 1]
    ajoute un jeton X ou O selon le joueur
    sortie : affiche la Liste modifiee (jeton ajoute dans le tableau)
    """
    for index_ligne, jeton in enumerate(grille[index_colonne] + [5]):
        if jeton != 0:  # la case de la grille n'est vide
            grille[index_colonne][index_ligne-1] = joueur
            break

    return grille, index_ligne-1

# Gabriel test ok
def isVerticalWin(grille: list[list[int]], index_colonne: int, index_ligne: int, joueur: int) -> bool:
    """
    verifie si un enchainement de 4 jetons n'as pas ete cree verticalement
    entree : grille type: list, 
             index_colone type: int, 
             index_ligne type: int,
             joueur type: int
    sortie: True si 4 jetons sont alignes, False dans l'autre cas
    """
    nombre_daffilee = 0
    for jeton in grille[index_colonne][index_ligne:]:
        if jeton == 0: continue

        if jeton == joueur:
            nombre_daffilee += 1
            if nombre_daffilee >= 4:
                return True
        else:
            break
    return nombre_daffilee >= 4

# Cyprien test ok
def isHorizontalWin(grille: list[list[int]], index_ligne: int, joueur: int) -> bool:
    """
    verifie si un enchainement de 4 jetons n'as pas ete cree horizontalement
    entree : grille type: list, 
             index_ligne type: int,
             joueur type: int
    sortie: True si 4 jetons sont alignes, False dans l'autre cas
    """
    nombre_daffilee = 0
    for index_jeton in range(len(grille)):
        if grille[index_jeton][index_ligne] == joueur:
            nombre_daffilee += 1
            if nombre_daffilee >= 4:
                return True
        else:
            nombre_daffilee = 0
    return False

# Gabriel test ok
def trouverDistances(grille: list[list[int]], index_colonne: int, index_ligne: int) -> tuple[int]:
    """
    trouve les distances entre la case [index_colonne][index_ligne] et les 4 bords de la grille
    entree : grille type: list, 
             index_colone type: int, 
             index_ligne type: int,
    sortie: distance_haut, distance_bas, distance_gauche, distance_droite 
            type: int les distances entre les bords respectifs entre 0 et 4 (compris)
    """
    
    distance_haut = min(index_ligne, 4)
    distance_bas = min(len(grille[index_colonne])-1 - index_ligne, 4)
    distance_gauche = min(index_colonne, 4)
    distance_droite = min(len(grille)-1 - index_colonne, 4)
    
    return distance_haut, distance_bas, distance_gauche, distance_droite

# Julle testé
def isDiagonalBottomLeftToTopRightWin(grille: list[list[int]], index_colonne: int, index_ligne: int, joueur: int) -> bool:
    """
    verifie si un enchainement de 4 jetons n'as pas ete cree dans une diagonale allant de en bas 
    a gauche à en haut a droite 
    entree : grille type: list, 
             index_colone type: int, 
             index_ligne type: int,
             joueur type: int
    sortie: True si 4 jetons sont alignes, False dans l'autre cas
    """
    
    distance_haut, distance_bas, distance_gauche, distance_droite = trouverDistances(grille, index_colonne, index_ligne)
    
    ecart_bas_gauche = min(distance_bas, distance_gauche)
    ecart_haut_droite = min(distance_haut, distance_droite)
    
    nombre_daffilee = 0        
    for i in range(-ecart_bas_gauche, ecart_haut_droite+1):
        if grille[index_colonne + i][index_ligne - i] == joueur:
            nombre_daffilee += 1
            if nombre_daffilee >= 4:
                return True
        else:
            nombre_daffilee = 0
            
    return False
   

# Cyprien test ok
def isDiagonalTopLeftToBottomRightWin(grille: list[list[int]], index_colonne: int, index_ligne: int, joueur: int) -> bool:
    """
    verifie si un enchainement de 4 jetons n'as pas ete cree dans une diagonale allant de en haut 
    a gauche a en bas a droite 
    entree : grille type: list, 
         index_colone type: int, 
         index_ligne type: int,
         joueur type: int
    sortie: True si 4 jetons sont alignes, False dans l'autre cas
    """
    
    distance_haut, distance_bas, distance_gauche, distance_droite = trouverDistances(grille, index_colonne, index_ligne)
    
    ecart_haut_gauche = min(distance_haut, distance_gauche)
    ecart_bas_droite = min(distance_bas, distance_droite)
    
    nombre_daffilee = 0
    for i in range(-ecart_haut_gauche, ecart_bas_droite+1):
        if grille[index_colonne + i][index_ligne + i] == joueur:
            nombre_daffilee += 1
            if nombre_daffilee >= 4:
                return True
        else:
            nombre_daffilee = 0
    return False
        

# Gabriel
def setupJoueur() -> dict:
    """
    Permet au joueurs de rentrer leurs noms et les associes a un numero grace a un dictionaire
    sortie: dictionaire 
    """
    joueurs = {
        1 : input(f"Nom du joueur {JOUEURS_IMAGE[1]}"),
        2 : input(f"Nom du joueur {JOUEURS_IMAGE[2]}")
    }

    return joueurs

# Gabriel
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

