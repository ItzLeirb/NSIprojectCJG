import math
from game import *
from settings import *
from main import *

def evaluation(grille: list[list[int]], joueur: int) -> int:
    """
    Évalue la grille pour donner un score au joueur basé sur le nombre de jetons alignés
    """
    score = 0

    for col in range(len(grille)):
        for row in range(len(grille[0])):
            if grille[col][row] == joueur:
                score += 10  
            elif grille[col][row] != 0:
                score -= 5  
    return score


def minimax(grille: list[list[int]], profondeur: int, joueur_max: bool, joueur: int, autre_joueur: int, alpha: int, beta: int) -> tuple[int, int]:
    """
    Implémente l'algorithme Minimax avec élagage alpha-bêta pour réduire le nombre de branches explorées
    """
    if profondeur == 0 or detecterVictoireVerticale(grille, index_colonne, index_ligne, joueur) or detecterVictoireHorizontale(grille, index_colonne, index_ligne, joueur) or detecterVictoireBasGaucheHautDroite(grille, index_colonne, index_ligne, joueur) or detecterVictoireHautGaucheBasDroite(grille, index_colonne, index_ligne, joueur):
        return evaluation(grille, joueur), -1

    meilleur_score = -math.inf if joueur_max else math.inf
    meilleur_colonne = -1

    for col in range(7):  
        if grille[col][0] == 0:  
            grille_temp, ligne_temp = ajouterJeton(grille, col, joueur if joueur_max else autre_joueur)
            score, _ = minimax(grille_temp, profondeur - 1, not joueur_max, joueur, autre_joueur, alpha, beta)
            grille_temp[col][ligne_temp] = 0  

            if joueur_max:
                if score > meilleur_score:
                    meilleur_score = score
                    meilleur_colonne = col
                alpha = max(alpha, score)
            else:
                if score < meilleur_score:
                    meilleur_score = score
                    meilleur_colonne = col
                beta = min(beta, score)

            if beta <= alpha:
                break

    return meilleur_score, meilleur_colonne


def ia_choisir_colonne(grille: list[list[int]], joueur: int, autre_joueur: int, profondeur: int = 4) -> int:
    """
    Appelle Minimax pour choisir une colonne
    """
    _, colonne = minimax(grille, profondeur, True, joueur, autre_joueur, -math.inf, math.inf)
    return colonne

