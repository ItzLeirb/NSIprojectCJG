from game import *
from main import *

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


# test detecterVictoireBasGaucheHautDroite Gabriel

assert detecterVictoireBasGaucheHautDroite(grille, 3, 2, 2)==True
grille = [
    [0, 0, 0, 0, 0, 2],
    [0, 0, 0, 0, 2, 1],
    [0, 0, 0, 1, 1, 2],
    [0, 0, 2, 1, 2, 1],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
assert detecterVictoireBasGaucheHautDroite(grille, 3, 2, 2)==False
grille = [
    [0, 0, 0, 0, 0, 2],
    [0, 0, 0, 0, 1, 1],
    [0, 0, 0, 2, 1, 2],
    [0, 0, 2, 1, 2, 1],
    [0, 2, 0, 0, 0, 1],
    [2, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
assert detecterVictoireBasGaucheHautDroite(grille, 2, 3, 2)==True
grille = [
    [0, 0, 0, 0, 0, 2],
    [0, 0, 0, 0, 1, 1],
    [0, 0, 0, 1, 1, 2],
    [0, 0, 1, 1, 2, 1],
    [0, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
assert detecterVictoireBasGaucheHautDroite(grille, 2, 3, 1)==True
grille = [
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 1],
    [0, 0, 0, 1, 1, 2],
    [0, 0, 1, 1, 2, 1],
    [0, 2, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
assert detecterVictoireBasGaucheHautDroite(grille, 2, 3, 1)==True
grille = [
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 1],
    [0, 0, 0, 1, 1, 2],
    [0, 0, 2, 1, 2, 1],
    [0, 2, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
assert detecterVictoireBasGaucheHautDroite(grille, 2, 3, 1)==False

# test detecterVictoireHautGaucheBasDroite Gabriel

grille = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 2, 1, 2, 1],
    [0, 0, 0, 2, 1, 2],
    [0, 0, 0, 0, 2, 1],
    [0, 0, 0, 0, 0, 2]
]
assert detecterVictoireHautGaucheBasDroite(grille, 3, 2, 2)==True
grille = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 2, 1, 2, 1],
    [0, 0, 0, 1, 1, 2],
    [0, 0, 0, 0, 2, 1],
    [0, 0, 0, 0, 0, 2]
]
assert detecterVictoireHautGaucheBasDroite(grille, 3, 2, 2)==False
grille = [
    [0, 0, 0, 0, 0, 0],
    [2, 0, 0, 0, 0, 0],
    [0, 2, 0, 0, 0, 1],
    [0, 0, 2, 1, 2, 1],
    [0, 0, 0, 2, 1, 2],
    [0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 2]
]
assert detecterVictoireHautGaucheBasDroite(grille, 4, 3, 2)==True
grille = [
    [0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1],
    [0, 0, 1, 1, 2, 1],
    [0, 0, 0, 1, 1, 2],
    [0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 2]
]
assert detecterVictoireHautGaucheBasDroite(grille, 4, 3, 1)==True
grille = [
    [0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0],
    [0, 2, 0, 0, 0, 1],
    [0, 0, 1, 1, 2, 1],
    [0, 0, 0, 1, 1, 2],
    [0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 1]
]
assert detecterVictoireHautGaucheBasDroite(grille, 4, 3, 1)==True
grille = [
    [0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0],
    [0, 2, 0, 0, 0, 1],
    [0, 0, 2, 1, 2, 1],
    [0, 0, 0, 1, 1, 2],
    [0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 1]
]
assert detecterVictoireHautGaucheBasDroite(grille, 4, 3, 1)==False


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
assert detecterVictoireVerticale(grille, 6, 2, 1)==True
grille = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 2]
]
assert detecterVictoireVerticale(grille, 6, 1, 1)==True
grille = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1]
]
assert detecterVictoireVerticale(grille, 6, 1, 1)==True
grille = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [1, 1, 2, 1, 1, 1]
]
assert detecterVictoireVerticale(grille, 6, 0, 1)==False
grille = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 1, 2, 2, 2]
]
assert detecterVictoireVerticale(grille, 6, 2, 1)==False
grille = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1]
]
assert detecterVictoireVerticale(grille, 6, 3, 1)==False

# tests detecterVictoireHorizontale() Jules

grille = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1]
]
assert detecterVictoireHorizontale(grille, 5, 1)==True

grille = [
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
assert detecterVictoireHorizontale(grille, 5, 1)==True

grille = [
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1]
]
assert detecterVictoireHorizontale(grille, 5, 1)==False

grille = [
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 2],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1]
]
assert detecterVictoireHorizontale(grille, 5, 1)==False

grille = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
assert detecterVictoireHorizontale(grille, 5, 1)==False

# test ajouterJeton()

for joueur in [1, 2]:
    for index_colonne in range(7):
        g1 = [[0]*6 for i in range(7)]
        g1[index_colonne][-1] = joueur
        # print(f"{ajouterJeton([[0]*6 for i in range(7)], index_colonne, joueur)}, {index_colonne}, {joueur}")
        assert ajouterJeton([[0]*6 for i in range(7)], index_colonne, joueur) == (g1, 5)

grille = [[0]*6 for i in range(7)]

for index_colonne, colonne in enumerate(grille):
    for index_ligne, jeton in enumerate(colonne):
        grille, _ = ajouterJeton(grille, index_colonne, 1)  # _ est une variable inutile      

assert grille == [[1]*6]*7

# tests trouverNom : Gabriel

# print(trouverNom(1))
# print(trouverNom(2))

# Resultat du test 1 : Entree : "aaaaaa" ; Resultat attendu : "aaaaaa" ; Sortie : "aaaaaa" --> test reussi
# Resultat du test 2 : Entree : "11" ; Resultat attendu : "11" ; Sortie : "11" --> test reussi
# Resultat du test 3 : Entree : "" , "A" ; Resultat attendu : "A" avec une demande de réentrer un nom ; Sortie : "A" avec une demande de réentrer un nom --> test reussi
# Resultat du test 3 : Entree : "" , "" , "A" ; Resultat attendu : "A" avec deux demandes de réentrer un nom ; Sortie : "A" avec deux demandes de réentrer un nom --> test reussi


# tests setupJoueur : Cyprien 

# print(setupJoueur())

# Resultat du test 1 : Entree : "aaaaaa" , "b" ; Resultat attendu : {1: 'aaaaaa', 2: 'b'} ; Sortie : {1: 'aaaaaa', 2: 'b'} --> test reussi
# Resultat du test 2 : Entree : "11" , "11" ; Resultat attendu : {1: '11', 2: '11'} ; Sortie : {1: '11', 2: '11'} --> test reussi
# Resultat du test 3 : Entree : "BBB" , "AAA" ; Resultat attendu : {1: 'BBB', 2: 'AAA'} ; Sortie : {1: 'BBB', 2: 'AAA'} --> test reussi
# Resultat du test 4 : Entree : "11" , "aAa" ; Resultat attendu : {1: '11', 2: 'aAa'} ; Sortie : {1: '11', 2: 'aAa'} --> test reussi
# Resultat du test 5 : Entree : "!!!:;" , "^$,?!" ; Resultat attendu : {1: '!!!:;', 2: '^$,?!'} ; Sortie : {1: '111:;', 2: '^$,?!'} --> test reussi



# tests trouverColonne Cyprien

# print(trouverColonne("Joueur!!!!!!!!!"))

# Resultat du test 1 : Entree : 0 ; Resultat attendu : 0 ; Sortie : 0 --> test reussi
# Resultat du test 2 : Entree : 3 ; Resultat attendu : 3 ; Sortie : 3 --> test reussi
# Resultat du test 3 : Entree : 6 ; Resultat attendu : 6 ; Sortie : 6 --> test reussi
# Resultat du test 4 : Entree : -1 ; Resultat attendu : demande au joueur de rentrer une colonne valide ; Sortie : demande au joueur de rentrer une colonne valide --> test reussi
# Resultat du test 5 : Entree : 7 ; Resultat attendu : demande au joueur de rentrer une colonne valide ; Sortie : demande au joueur de rentrer une colonne valide --> test reussi






print('Tous les tests sont passés')