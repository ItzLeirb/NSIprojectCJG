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
    Renvoie une grille ou le jeton du joueur a ete joue a une certaine colonne, puis fait "tomber" le jeton.
    ajoute un jeton 1 ou 2 selon le joueur
    
    Entrees:   
        grille: la grille, un tableau (type: list) de listes (type: list) de nombres (type: int) qui representent les joueurs, 
        colonne: la colonne ou le joueur a joue (type: int)
        joueur: le numero du joueur (type: int)
        
    Sortie:
        grille modifiee (jeton ajoute dans le tableau) (type: list de list de int)
    """
    # Itere a travers toute la colonne
    for index_ligne, jeton in enumerate(grille[index_colonne] + [5]): # Le 5 est arbitraire, mais n'est ni 0, ni 1, ni 2 et marque la fin de la colonne
        if jeton != 0:  # la case de la grille n'est vide
            grille[index_colonne][index_ligne-1] = joueur
            break

    return grille, index_ligne-1

# Gabriel test ok
def detecterVictoireVerticale(grille: list[list[int]], index_colonne: int, index_ligne: int, joueur: int) -> bool:
    """
    Verifie si un enchainement de 4 jetons a ete cree verticalement
    
    Entree: 
        grille (type: list de list de int) le tableau a deux dimensions qui represente la grille, 
        index_colonne: (type: int) l'index de la colonne ou le dernier jeton a ete place, 
        index_ligne: (type: int) l'index de la ligne ou le dernier jeton a ete place,
        joueur: (type: int) le numero du joueur (compris entre 1 et 2)
    
    Sortie: 
        True si 4 jetons sont alignes, False sinon
    """
    nombre_daffilee = 0
    # Itere a travers la colonne index_colonne a partir de la ligne index_ligne.
    for jeton in grille[index_colonne][index_ligne:]:
        if jeton == 0: continue # ignore les cases vides (qui ne sont pas censees exister)
        
        # Compte le nombre de jetons identiques d'affilee et renvoie True si il y en a 4 ou plus
        if jeton == joueur:
            nombre_daffilee += 1
            if nombre_daffilee >= 4:
                return True
        else:
            return False # Arrête de compter si un jeton de l'autre joueur s'intercale avant d'avoir 4 jetons alignes.
    return False

# Cyprien test ok
def detecterVictoireHorizontale(grille: list[list[int]], index_ligne: int, joueur: int) -> bool:
    """
    Verifie si un enchainement de 4 jetons n'as pas ete cree horizontalement
    
    Entree: 
        grille type: list, 
        index_ligne type: int,
        joueur type: int
    Sortie: 
        True si 4 jetons sont alignes, False dans l'autre cas
    """
    nombre_daffilee = 0
    
    # Itere a travers la ligne jouee
    for index_jeton in range(len(grille)):
        # Compte le nombre de jetons identiques d'affilee et renvoie True si il y en a 4 ou plus
        if grille[index_jeton][index_ligne] == joueur:
            nombre_daffilee += 1
            if nombre_daffilee >= 4:
                return True
        else:
            nombre_daffilee = 0 # Repars a 0 si un jeton manque
            
    return False

# Gabriel test ok
def trouverDistances(grille: list[list[int]], index_colonne: int, index_ligne: int) -> tuple[int]:
    """
    Trouve les distances entre la case [index_colonne][index_ligne] et les 4 bords de la grille
    
    Entree: 
        grille type: list, 
        index_colone type: int, 
        index_ligne type: int,
    Sortie: 
        distance_haut, distance_bas, distance_gauche, distance_droite 
        type: int les distances entre les bords respectifs entre 0 et 4 (compris)
    """
    
    # Calcule separement les distances
    distance_haut = min(index_ligne, 4)
    distance_bas = min(len(grille[index_colonne])-1 - index_ligne, 4)
    distance_gauche = min(index_colonne, 4)
    distance_droite = min(len(grille)-1 - index_colonne, 4)
    
    return distance_haut, distance_bas, distance_gauche, distance_droite

# Julle test ok
def detecterVictoireBasGaucheHautDroite(grille: list[list[int]], index_colonne: int, index_ligne: int, joueur: int) -> bool:
    """
    Verifie si un enchainement de 4 jetons n'as pas ete cree dans une diagonale allant de en bas 
    a gauche a en haut a droite 
    
    Entree: 
        grille type: list, 
        index_colone type: int, 
        index_ligne type: int,
        joueur type: int
    Sortie: 
        True si 4 jetons sont alignes, False dans l'autre cas
    """
    
    # evalue les distances avec trouverDistances()
    distance_haut, distance_bas, distance_gauche, distance_droite = trouverDistances(grille, index_colonne, index_ligne)
    
    # Calcule la distance diagonale avec les bords de la grille
    ecart_bas_gauche = min(distance_bas, distance_gauche)
    ecart_haut_droite = min(distance_haut, distance_droite)
    
    nombre_daffilee = 0        
    
    # Itere a travers la diagonale  de bord a bord 
    for i in range(-ecart_bas_gauche, ecart_haut_droite+1):
        # Compte le nombre de jetons identiques d'affilee et renvoie True si il y en a 4 ou plus
        if grille[index_colonne + i][index_ligne - i] == joueur:
            nombre_daffilee += 1
            if nombre_daffilee >= 4:
                return True
        else:
            nombre_daffilee = 0 # Repars a 0 si un jeton autre s'est intercale
    return False
   

# Cyprien test ok
def detecterVictoireHautGaucheBasDroite(grille: list[list[int]], index_colonne: int, index_ligne: int, joueur: int) -> bool:
    """
    Verifie si un enchainement de 4 jetons n'as pas ete cree dans une diagonale allant de en haut 
    a gauche a en bas a droite 
    
    Entree: 
        grille type: list, 
        index_colone type: int, 
        index_ligne type: int,
        joueur type: int
    Sortie: 
        True si 4 jetons sont alignes, False dans l'autre cas
    """
    
    # evalue les distances avec trouverDistances()
    distance_haut, distance_bas, distance_gauche, distance_droite = trouverDistances(grille, index_colonne, index_ligne)
    
    # Calcule la distance diagonale avec les bords de la grille
    ecart_haut_gauche = min(distance_haut, distance_gauche)
    ecart_bas_droite = min(distance_bas, distance_droite)
    
    nombre_daffilee = 0
    
    # Itere a travers la diagonale  de bord a bord
    for i in range(-ecart_haut_gauche, ecart_bas_droite+1):
        # Compte le nombre de jetons identiques d'affilee et renvoie True si il y en a 4 ou plus
        if grille[index_colonne + i][index_ligne + i] == joueur:
            nombre_daffilee += 1
            if nombre_daffilee >= 4:
                return True
        else:
            nombre_daffilee = 0 
    return False

def trouverLigne(grille, colonne):
    for ligne in range(5, -1, -1):
        if grille[colonne][ligne] == 0:
            return ligne
    return None 

def estFini(grille, joueur, autre_joueur):
    for colonne in range(7):
        for ligne in range(6):
            if grille[colonne][ligne] != 0:
                if detecterVictoireVerticale(grille, colonne, ligne, joueur) or \
                   detecterVictoireHorizontale(grille, ligne, joueur) or \
                   detecterVictoireBasGaucheHautDroite(grille, colonne, ligne, joueur) or \
                   detecterVictoireHautGaucheBasDroite(grille, colonne, ligne, joueur):
                    return True
    return False

