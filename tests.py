from game import *
from main import affichageConsole

# test trouverDistances
grille = [[0]*6]*7

assert trouverDistances(grille, 0, 0) == (0, 4, 0, 4)
assert trouverDistances(grille, 6, 5) == (4, 0, 4, 0)
assert trouverDistances(grille, 5, 0) == (0, 4, 4, 1)
assert trouverDistances(grille, 0, 4) == (4, 1, 0, 4)
assert trouverDistances(grille, 3, 3) == (3, 2, 3, 3)

# test affichage

grille = [
    [0, 0, 0, 0, 0, 2],
    [0, 0, 0, 0, 2, 1],
    [0, 0, 0, 2, 1, 2],
    [0, 0, 2, 1, 2, 1],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
affichageConsole(grille, 1)


# test isDiagonalBottomLeftToTopRightWin Gabriel

assert isDiagonalBottomLeftToTopRightWin(grille, 3, 2, 2)==True
grille = [
    [0, 0, 0, 0, 0, 2],
    [0, 0, 0, 0, 2, 1],
    [0, 0, 0, 1, 1, 2],
    [0, 0, 2, 1, 2, 1],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
assert isDiagonalBottomLeftToTopRightWin(grille, 3, 2, 2)==False
grille = [
    [0, 0, 0, 0, 0, 2],
    [0, 0, 0, 0, 1, 1],
    [0, 0, 0, 2, 1, 2],
    [0, 0, 2, 1, 2, 1],
    [0, 2, 0, 0, 0, 1],
    [2, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
assert isDiagonalBottomLeftToTopRightWin(grille, 2, 3, 2)==True
grille = [
    [0, 0, 0, 0, 0, 2],
    [0, 0, 0, 0, 1, 1],
    [0, 0, 0, 1, 1, 2],
    [0, 0, 1, 1, 2, 1],
    [0, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
assert isDiagonalBottomLeftToTopRightWin(grille, 2, 3, 1)==True
grille = [
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 1],
    [0, 0, 0, 1, 1, 2],
    [0, 0, 1, 1, 2, 1],
    [0, 2, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
assert isDiagonalBottomLeftToTopRightWin(grille, 2, 3, 1)==True
grille = [
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 1],
    [0, 0, 0, 1, 1, 2],
    [0, 0, 2, 1, 2, 1],
    [0, 2, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
assert isDiagonalBottomLeftToTopRightWin(grille, 2, 3, 1)==False

# test isDiagonalTopLeftToBottomRightWin Gabriel

grille = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 2, 1, 2, 1],
    [0, 0, 0, 2, 1, 2],
    [0, 0, 0, 0, 2, 1],
    [0, 0, 0, 0, 0, 2]
]
assert isDiagonalTopLeftToBottomRightWin(grille, 3, 2, 2)==True
grille = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 2, 1, 2, 1],
    [0, 0, 0, 1, 1, 2],
    [0, 0, 0, 0, 2, 1],
    [0, 0, 0, 0, 0, 2]
]
assert isDiagonalTopLeftToBottomRightWin(grille, 3, 2, 2)==False
grille = [
    [0, 0, 0, 0, 0, 0],
    [2, 0, 0, 0, 0, 0],
    [0, 2, 0, 0, 0, 1],
    [0, 0, 2, 1, 2, 1],
    [0, 0, 0, 2, 1, 2],
    [0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 2]
]
assert isDiagonalTopLeftToBottomRightWin(grille, 4, 3, 2)==True
grille = [
    [0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1],
    [0, 0, 1, 1, 2, 1],
    [0, 0, 0, 1, 1, 2],
    [0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 2]
]
assert isDiagonalTopLeftToBottomRightWin(grille, 4, 3, 1)==True
grille = [
    [0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0],
    [0, 2, 0, 0, 0, 1],
    [0, 0, 1, 1, 2, 1],
    [0, 0, 0, 1, 1, 2],
    [0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 1]
]
assert isDiagonalTopLeftToBottomRightWin(grille, 4, 3, 1)==True
grille = [
    [0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0],
    [0, 2, 0, 0, 0, 1],
    [0, 0, 2, 1, 2, 1],
    [0, 0, 0, 1, 1, 2],
    [0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 1]
]
assert isDiagonalTopLeftToBottomRightWin(grille, 4, 3, 1)==False


# test isVertacalWin Cyprien & Jules

grille = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1]
]
assert isVerticalWin(grille, 6, 2, 1)==True
grille = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 2]
]
assert isVerticalWin(grille, 6, 1, 1)==True
grille = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1]
]
assert isVerticalWin(grille, 6, 1, 1)==True
grille = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [1, 1, 2, 1, 1, 1]
]
assert isVerticalWin(grille, 6, 0, 1)==False
grille = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 1, 2, 2, 2]
]
assert isVerticalWin(grille, 6, 2, 1)==False
grille = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1]
]
assert isVerticalWin(grille, 6, 3, 1)==False

# tests isHorizontalWin() Gabriel

grille = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1]
]
assert isHorizontalWin(grille, 5, 1)==True

grille = [
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
assert isHorizontalWin(grille, 5, 1)==True

grille = [
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1]
]
assert isHorizontalWin(grille, 5, 1)==False

grille = [
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 2],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1]
]
assert isHorizontalWin(grille, 5, 1)==False

grille = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
assert isHorizontalWin(grille, 5, 1)==False

# test ajouterJeton()

grille = [[0]*6]*7

for joueur in [1, 2]:
    for index_colonne in range(7):
        g1 = grille
        g1[index_colonne][-1] = joueur
        assert ajouterJeton(grille, index_colonne, joueur) == g1

for index_colonne, colonne in enumerate(grille):
    for index_ligne, jeton in enumerate(colonne):
        grille = ajouterJeton(grille, index_colonne, 1)        

assert grille == [[1]*6]*7

print('Tous les tests sont passés')