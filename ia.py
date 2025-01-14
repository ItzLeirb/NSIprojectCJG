import math
from game import *

def tousLesCoups(grille: list[list[int]]):
    """
    Renvoie la liste de tous les coups possibles

    Entree:
        grille (list[list[int]]): la grille

    Sorties:
        list de tuples: la liste des coups possibles
    """
    coups = []
    for index_colonne in range(len(grille)):
        index_ligne = trouverLigne(grille, index_colonne)
        if index_ligne is None: continue
        coups.append((index_colonne, index_ligne))
    
    return coups

def compterOptions(grille: list[list[int]], dernier_coup: tuple[int, int]) -> int:
    """
    Compte et renvoie le nombre de coups possibles alignes avec le dernier coup

    Entree:
        grille (list[list[int]]): la grille
        dernier_coup (tuple[int, int]): le dernier couple

    Sortie:
        int: le nombre d'options
    """
    nombre_options = 0
    for coup in tousLesCoups(grille):
        # check si le dernier coup est aligne avec l'option (meme ligne, colonne, ou diagonale)
        if dernier_coup[0] == coup[0] or dernier_coup[1] == coup[1] or dernier_coup[1]-dernier_coup[0] == coup[1]-coup[0] or dernier_coup[1]+dernier_coup[0] == coup[1]+coup[0]:
            nombre_options += 1
    
    return nombre_options

def compterJetonsAlignes(grille: list[list[int]], dernier_coup: tuple[int, int], joueur: int) -> int:
    """
    Compte et renvoie le nb de jetons identiques alignes avec le dernier coup

    Entree:
        grille (list[list[int]]): la grille
        dernier_coup (tuple[int, int]): le dernier coup
        joueur (int): le joueur (l'IA)

    Sortie:
        int: _description_
    """
    score = 0
    
    # vertical
    compte = 0
    for index_ligne in range(dernier_coup[1], 6):
        if grille[dernier_coup[0]][index_ligne] != joueur:
            break
        compte += 1
    score += compte
    
    # horizontal gauche
    compte = 0
    for index_colonne in range(dernier_coup[1], max(dernier_coup[1]-3, 0), -1): # va de droite a gauche
        if grille[index_colonne][dernier_coup[1]] == 3 - joueur: # arrete si le jeton est de l'adversaire
            break
        compte += 1
    score += compte
    
    # horizontal droite
    compte = 0
    for index_colonne in range(dernier_coup[1], min(dernier_coup[1]+3, 0)):
        if grille[index_colonne][dernier_coup[1]] == 3 - joueur: # arrete si le jeton est de l'adversaire
            break
        compte += 1
    score += compte
    
    # diagonales
    distance_haut, distance_bas, distance_gauche, distance_droite = trouverDistances(grille, dernier_coup[0], dernier_coup[1])
    
    # diagonale haut-gauche
    compte = 0
    for modificateur in range(min(distance_haut, distance_gauche)):
        if grille[dernier_coup[0] - modificateur][dernier_coup[1] - modificateur] == 3 - joueur: # arrete si le jeton est de l'adversaire
            break
        compte += 1
    score += compte
    
    # diagonale haut-droite
    compte = 0
    for modificateur in range(min(distance_haut, distance_droite)):
        if grille[dernier_coup[0] + modificateur][dernier_coup[1] - modificateur] == 3 - joueur: # arrete si le jeton est de l'adversaire
            break
        compte += 1
    score += compte
    
    # diagonale bas-gauche
    compte = 0
    for modificateur in range(min(distance_bas, distance_gauche)):
        if grille[dernier_coup[0] - modificateur][dernier_coup[1] + modificateur] == 3 - joueur: # arrete si le jeton est de l'adversaire
            break
        compte += 1
    score += compte
    
    # diagonale bas-droite
    compte = 0
    for modificateur in range(min(distance_bas, distance_droite)):
        if grille[dernier_coup[0] + modificateur][dernier_coup[1] + modificateur] == 3 - joueur: # arrete si le jeton est de l'adversaire
            break
        compte += 1
    score += compte
        
    return score

def evaluation(grille: list[list[int]], joueur: int, victoire: bool, dernier_coup: tuple[int, int]) -> int:
    """
    Evalue le dernier coup potentiel

    Entree:
        grille (list[list[int]]): la grille
        joueur (int): le numero du bot
        victoire (bool): True si la partie est remportee par qq1
        dernier_coup (tuple[int, int]): le dernier coup

    Sortie:
        int: le score evalue
    """
    score = 0
    
    if victoire:
        score += 250

    for index_colonne in range(len(grille)):
        for index_ligne in range(len(grille[0])):
            score += compterOptions(grille, dernier_coup) - 1
            score += compterJetonsAlignes(grille, dernier_coup, grille[dernier_coup[0]][dernier_coup[1]]) # valeur arbitraire
                
    return score

def minimax(grille: list[list[int]], profondeur: int, maximiser: bool, joueur: int, autre_joueur: int, alpha: float, beta: float, est_fini: bool, dernier_coup: tuple):
    """
    Controle l'evaluation du bot

    Entree:
        grille (list[list[int]]): la grille
        profondeur (int): la profondeur de la recherche
        maximiser (bool): True si c'est au tour du bot dans sa recherche
        joueur (int): le numero de l'ia
        autre_joueur (int): le numero de l'autre joueur
        alpha (float): l'alpha de la derniere recursion
        beta (float): le beta de la derniere recursion
        est_fini (bool): True si la partie est finie
        dernier_coup (tuple): le dernier coup joue

    Sortie:
    """
    if profondeur == 0 or detecterVictoireVerticale(grille, dernier_coup[0], dernier_coup[1], joueur) == True or detecterVictoireHorizontale(grille, dernier_coup[1], joueur) == True or detecterVictoireBasGaucheHautDroite(grille, dernier_coup[0], dernier_coup[1], joueur) == True or detecterVictoireHautGaucheBasDroite(grille, dernier_coup[0], dernier_coup[1], joueur) == True:  # Vérifie si la profondeur est atteinte ou si la partie est terminée
        score = evaluation(grille, joueur, (detecterVictoireVerticale(grille, dernier_coup[0], dernier_coup[1], joueur) == True or detecterVictoireHorizontale(grille, dernier_coup[1], joueur) == True or detecterVictoireBasGaucheHautDroite(grille, dernier_coup[0], dernier_coup[1], joueur) == True or detecterVictoireHautGaucheBasDroite(grille, dernier_coup[0], dernier_coup[1], joueur) == True), dernier_coup)
        return score, None

    if maximiser:
        meilleur_score = -math.inf
        meilleure_colonne = None
        for index_colonne in range(7):
            if grille[index_colonne][0] >= 0:  # Colonne jouable
                ligne = trouverLigne(grille, index_colonne)
                if ligne is None: continue
                grille[index_colonne][ligne] = joueur
                score, _ = minimax(grille, profondeur - 1, False, joueur, autre_joueur, alpha, beta, est_fini, (index_colonne, ligne))
                # valorise les coups proches du centre avec une fonction gaussienne
                score += 5 * math.exp(- (index_colonne - 3)**2 / (2 * 5**2))
                grille[index_colonne][ligne] = 0  # Annule le coup
                if score > meilleur_score:
                    meilleur_score = score
                    meilleure_colonne = index_colonne
                alpha = max(alpha, score)
                if beta <= alpha:
                    break
        return meilleur_score, meilleure_colonne
    else:
        pire_score = math.inf
        pire_colonne = None
        for index_colonne in range(7):
            if grille[index_colonne][0] >= 0:  # Colonne jouable
                ligne = trouverLigne(grille, index_colonne)
                if ligne is None: continue
                grille[index_colonne][ligne] = autre_joueur
                score, _ = minimax(grille, profondeur - 1, True, joueur, autre_joueur, alpha, beta, est_fini, (index_colonne, ligne))
                # valorise les coups proches du centre avec une fonction gaussienne
                score -= 10 * math.exp(- (index_colonne - 3)**2 / (2 * 5**2))
                grille[index_colonne][ligne] = 0  # Annule le coup
                if score < pire_score:
                    pire_score = score
                    pire_colonne = index_colonne
                beta = min(beta, score)
                if beta <= alpha:
                    break
        return pire_score, pire_colonne



def ia_choisir_colonne(grille: list[list[int]], joueur: int, autre_joueur: int, est_fini: bool, profondeur: int = 4) -> int:
    """
    Gere l'IA

    Entree:
        grille (list[list[int]]): la grille
        joueur (int): le numero de l'IA
        autre_joueur (int): le numero de l'autre joueur
        est_fini (bool): True si la partie est finie, False sinon
        profondeur (int, optional): la profondeur de recherche maximale (4 par defaut)

    Sortie:
        int: la colonne jouee
    """
    _, colonne = minimax(grille, profondeur, True, joueur, autre_joueur, -math.inf, math.inf, est_fini, (0,0))
    print(colonne)
    return colonne

