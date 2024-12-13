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