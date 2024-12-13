from game import *
from main import afficherGrilleConsole


grille = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 2, 0, 0, 0],
    [0, 0, 1, 2, 1, 0, 0, 0],
    [0, 1, 2, 1, 2, 0, 0, 0],
]

afficherGrilleConsole(grille)