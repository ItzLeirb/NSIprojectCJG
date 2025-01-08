# project
from game import *
from settings import *

# Gabriel tests ok
def affichageConsole(grille: list[list[int]], joueur: int):
    """
    affiche l'état actuel de la grille dans la console 
    Entrée : grille type: list, 
             joueur type: int
    """
    print("  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | ")
    for ligne in range(len(grille[0])):
        ligne_texte = f"{ligne} | "
        for colonne in range(len(grille)):
            ligne_texte += f"{JOUEURS_IMAGE[grille[colonne][ligne]]} | "
        print(ligne_texte)
    
    print("")
    print(f"Au tour du joueur {joueur % 2 + 1}")
    

# Gabriel
def trouverNom(index_joueur: int):
    """
    Permet au joueur d'entrer son nom et vérifie s'il est correct (non vide)
    
    Entrée:
        index_joueur: (type: int), l'index du joueur (1 ou 2)
    Sortie:
        une chaine de caractère (type: string) le nom final du joueur
    """
    
    nom_joueur = input(f'Nom du joueur {JOUEURS_IMAGE[index_joueur]}: ')
    while nom_joueur == "":
        nom_joueur = input(f'Le nom ne doit pas être vide, entrer le nom du joueur {JOUEURS_IMAGE[index_joueur]}: ')

    return nom_joueur

# Gabriel
def setupJoueur() -> dict:
    """
    Permet au joueurs de rentrer leurs noms et les associe à un numero dans un dictionaire
    
    Sortie: 
        un dictionnaire (type: dict) qui associe à un nombre (type: int) entre 1 et 2 au nom du joueur correspondant
    """
    
    joueurs = {
        1 : trouverNom(1),
        2 : trouverNom(2)
    }

    return joueurs

# Gabriel
def trouverColonne(nom_joueur: str) -> int:
    """
    Demande au joueur actuel la colonne dans laquelle il veut jouer, et vérifie si elle est valide

    Entrée: 
        nom_joueur: (type: str) le nom du joueur qui choisit la colonne
    Sortie: 
        le numéro de la colonne (type: int)
    """

    # Demande la colonne où le joueur veut jouer
    print(f"Choisis la colonne où tu veux jouer {nom_joueur} (compris entre 0 et 6):")
    colonne = int(input(""))

    # Vérifie si la colonne choisie est valide, la redemande si elle ne l'est pas.
    valides = [i for i in range(7)]
    while colonne not in valides:
        print(f"La colonne choisie n'est pas valide. Choisis la colonne où tu veux jouer {nom_joueur} (compris entre 0 et 6):")
        colonne = int(input(""))
    
    return colonne

# Cyprien
def jeu():
    """
    Fait tourner la partie entière.
    Coordonne les différentes fonctions pour faire fonctioner le jeu.
    """
    # Création de la grille, mise en place des variables importantes
    grille = [[0]*6]*7
    joueurs = setupJoueur()
    running = True
    joueur = 0
    nombre_coups = 0
    
    # La boucle principale
    while running == True:
        # Change le joueur
        joueur += 1
        if joueur > 2:
            joueur = 1

        # Fait jouer le joueur
        index_colonne = trouverColonne(joueurs[joueur])
        grille, index_ligne = ajouterJeton(grille, index_colonne, joueur)

        # Vérifie si la partie est finie (victoire ou match nul)
        nombre_coups += 1
        if detecterVictoireVerticale(grille, index_colonne, index_ligne, joueur) == True or detecterVictoireHorizontale(grille, index_ligne, joueur) == True or detecterVictoireBasGaucheHautDroite(grille, index_colonne, index_ligne, joueur) == True or detecterVictoireHautGaucheBasDroite(grille, index_colonne, index_ligne, joueur) == True: 
            running == False
        elif nombre_coups >= 42:
            running == False


if __name__ == '__main__':
    jeu()