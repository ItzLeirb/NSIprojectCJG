from game import *
from main import affichageConsole


# test affichage

grille = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 2, 1, 2, 1],
    [0, 0, 0, 2, 1, 2],
    [0, 0, 0, 0, 2, 1],
    [0, 0, 0, 0, 0, 2]
]
affichageConsole(grille, 1)

# test isDiagonalBottomLeftToTopRightWin

assert isDiagonalBottomLeftToTopRightWin(grille, 3, 2, 2)==True
grille = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 2, 1, 2, 1],
    [0, 0, 0, 1, 1, 2],
    [0, 0, 0, 0, 2, 1],
    [0, 0, 0, 0, 0, 2]
]
assert isDiagonalBottomLeftToTopRightWin(grille, 3, 2, 2)==False
grille = [
    [0, 0, 0, 0, 0, 0],
    [2, 0, 0, 0, 0, 0],
    [0, 2, 0, 0, 0, 1],
    [0, 0, 2, 1, 2, 1],
    [0, 0, 0, 2, 1, 2],
    [0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 2]
]
assert isDiagonalBottomLeftToTopRightWin(grille, 4, 3, 2)==True
grille = [
    [0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1],
    [0, 0, 1, 1, 2, 1],
    [0, 0, 0, 1, 1, 2],
    [0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 2]
]
assert isDiagonalBottomLeftToTopRightWin(grille, 4, 3, 1)==True
grille = [
    [0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0],
    [0, 2, 0, 0, 0, 1],
    [0, 0, 1, 1, 2, 1],
    [0, 0, 0, 1, 1, 2],
    [0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 1]
]
assert isDiagonalBottomLeftToTopRightWin(grille, 4, 3, 1)==True
grille = [
    [0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0],
    [0, 2, 0, 0, 0, 1],
    [0, 0, 2, 1, 2, 1],
    [0, 0, 0, 1, 1, 2],
    [0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 1]
]
assert isDiagonalBottomLeftToTopRightWin(grille, 4, 3, 1)==True


