import math
from game import *
from main import *

def evaluation(grille: list[list[int]], joueur: int) -> int:
    """
    Évalue la grille pour donner un score au joueur.
    Ici, on utilise une méthode simple basée sur le nombre de jetons alignés.
    """
    score = 0

    # Exemple : Ajoutez vos propres heuristiques
    for col in range(len(grille)):
        for row in range(len(grille[0])):
            if grille[col][row] == joueur:
                score += 10  # Exemple : +10 par jeton du joueur
            elif grille[col][row] != 0:
                score -= 5  # Exemple : -5 par jeton adverse
    return score


def minimax(grille, profondeur, maximiser, joueur, autre_joueur, alpha, beta):
    """
    
    """
    if profondeur == 0 or estFini(grille, joueur, autre_joueur):  # Vérifie si la profondeur est atteinte ou si la partie est terminée
        score = evaluation(grille, joueur, autre_joueur)
        return score, None

    if maximiser:
        meilleur_score = -math.inf
        meilleure_colonne = None
        for colonne in range(7):
            if grille[colonne][0] == 0:  # Colonne jouable
                ligne = trouverLigne(grille, colonne)
                grille[colonne][ligne] = joueur
                score, _ = minimax(grille, profondeur - 1, False, joueur, autre_joueur, alpha, beta)
                grille[colonne][ligne] = 0  # Annule le coup
                if score > meilleur_score:
                    meilleur_score = score
                    meilleure_colonne = colonne
                alpha = max(alpha, score)
                if beta <= alpha:
                    break
        return meilleur_score, meilleure_colonne
    else:
        pire_score = math.inf
        pire_colonne = None
        for colonne in range(7):
            if grille[colonne][0] == 0:  # Colonne jouable
                ligne = trouverLigne(grille, colonne)
                grille[colonne][ligne] = autre_joueur
                score, _ = minimax(grille, profondeur - 1, True, joueur, autre_joueur, alpha, beta)
                grille[colonne][ligne] = 0  # Annule le coup
                if score < pire_score:
                    pire_score = score
                    pire_colonne = colonne
                beta = min(beta, score)
                if beta <= alpha:
                    break
        return pire_score, pire_colonne



def ia_choisir_colonne(grille: list[list[int]], joueur: int, autre_joueur: int, profondeur: int = 4) -> int:
    """
    Appelle Minimax pour choisir une colonne.
    """
    _, colonne = minimax(grille, profondeur, True, joueur, autre_joueur, -math.inf, math.inf)
    return colonne

