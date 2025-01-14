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
    for index_colonne in range(len(grille[0])):
        coups.append((index_colonne, trouverLigne(index_colonne)))
    
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

def compterJetonsAlignes():
    pass

def evaluation(grille: list[list[int]], joueur: int, victoire: bool) -> int:
    """
    Évalue la grille pour donner un score au joueur.
    Ici, on utilise une méthode simple basée sur le nombre de jetons alignés.
    """
    score = 0
    
    if victoire:
        score += 50

    # Exemple : Ajoutez vos propres heuristiques
    for index_colonne in range(len(grille)):
        for index_ligne in range(len(grille[0])):
            score += compterOptions() - 1
            score += 2 * compterJetonsAlignes() ** 2
                
    return score

def minimax(grille, profondeur, maximiser, joueur, autre_joueur, alpha, beta, est_fini: bool, dernier_coup: tuple):
    """
    Evalue les coups possibles du bot
    """
    if profondeur == 0 or detecterVictoireVerticale(grille, dernier_coup[0], dernier_coup[1], joueur) == True or detecterVictoireHorizontale(grille, dernier_coup[1], joueur) == True or detecterVictoireBasGaucheHautDroite(grille, dernier_coup[0], dernier_coup[1], joueur) == True or detecterVictoireHautGaucheBasDroite(grille, dernier_coup[0], dernier_coup[1], joueur) == True:  # Vérifie si la profondeur est atteinte ou si la partie est terminée
        score = evaluation(grille, joueur, (detecterVictoireVerticale(grille, dernier_coup[0], dernier_coup[1], joueur) == True or detecterVictoireHorizontale(grille, dernier_coup[1], joueur) == True or detecterVictoireBasGaucheHautDroite(grille, dernier_coup[0], dernier_coup[1], joueur) == True or detecterVictoireHautGaucheBasDroite(grille, dernier_coup[0], dernier_coup[1], joueur) == True))
        return score, None

    if maximiser:
        meilleur_score = -math.inf
        meilleure_colonne = None
        for index_colonne in range(7):
            if grille[index_colonne][0] == 0:  # Colonne jouable
                ligne = trouverLigne(grille, index_colonne)
                grille[index_colonne][ligne] = joueur
                score, _ = minimax(grille, profondeur - 1, False, joueur, autre_joueur, alpha, beta, est_fini, (index_colonne, ligne))
                # valorise les coups proches du centre avec une fonction gaussienne
                score += 10 * math.exp(- (index_colonne - 3)**2 / (2 * 5**2))
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
            if grille[index_colonne][0] == 0:  # Colonne jouable
                ligne = trouverLigne(grille, index_colonne)
                grille[index_colonne][ligne] = autre_joueur
                score, _ = minimax(grille, profondeur - 1, True, joueur, autre_joueur, alpha, beta, est_fini, (index_colonne, ligne))
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
    Appelle Minimax pour choisir une colonne.
    """
    _, colonne = minimax(grille, profondeur, True, joueur, autre_joueur, -math.inf, math.inf, est_fini, (0,0))
    print(_, colonne)
    return colonne

