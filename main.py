# project
from game import *
from settings import *

# Gabriel ( Cyprien pour la victoire ) tests ok
def affichageConsole(grille: list[list[int]], joueur: int, noms_joueurs: dict, etat_de_la_partie: str = 'en cours'):
    """
    Affiche l'etat actuel de la grille dans la console et affiche le vainqueur ou une egalitée en fin de partie
    
    Entrée : 
        grille (type: list de list d'int) la grille, 
        joueur (type: int) l'index du joueur,
        noms_joueurs (type: dict) le dictionnaire des noms des joueurs,
        etat_de_la_partie (type: str): l'etat de la partie
    """
    print("| 1 | 2 | 3 | 4 | 5 | 6 | 7 |")
    for ligne in range(len(grille[0])):
        ligne_texte = "| "
        for colonne in range(len(grille)):
            ligne_texte += f"{JOUEURS_IMAGE[grille[colonne][ligne]]} | "
        print(ligne_texte)
    
    if etat_de_la_partie == 'en cours':
        print("")
        print(f"Au tour du joueur {noms_joueurs[joueur]}")
    elif etat_de_la_partie == 'victoire':
        print("")
        print(f"Victoire du joueur {noms_joueurs[joueur]} !")
    elif etat_de_la_partie == 'match nul':
        print("")
        print("Egalité")
    

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
def trouverColonne(nom_joueur: str, grille: list[list[int]]) -> int:
    """
    Demande au joueur actuel la colonne dans laquelle il veut jouer, et vérifie si elle est valide

    Entrée: 
        nom_joueur: (type: str) le nom du joueur qui choisit la colonne
        grille: (type: list de list de int) la grille du jeu
    Sortie: 
        le numéro de la colonne (type: int)
    """

    # Demande la colonne où le joueur veut jouer
    print(f"Choisis la colonne où tu veux jouer {nom_joueur} (compris entre 1 et 7):")
    colonne = input("")
    
    # Vérifie si la colonne choisie est valide, la redemande si elle ne l'est pas.
    valides = [i for i in range(7)]
    est_int = False
    while not est_int:
        try:
            colonne = int(colonne) -1
            est_int = True
            if colonne in valides and grille[colonne][0] != 0 :
                print(f"La colonne choisie n'est pas valide. Choisis la colonne où tu veux jouer {nom_joueur} (compris entre 1 et 7):")
                colonne = input("")
        except:
            print(f"La colonne choisie n'est pas valide. Choisis la colonne où tu veux jouer {nom_joueur} (compris entre 1 et 7):")
            colonne = input("")
            est_int = False

    return colonne

# Cyprien
def jeu():
    """
    Fait tourner la partie entière.
    Coordonne les différentes fonctions pour faire fonctionner le jeu.
    """
    # Création de la grille, mise en place des variables importantes
    grille = [[0 for i in range(6)] for i in range(7)]
    noms_joueurs = setupJoueur()
    running = True
    joueur = 0
    nombre_coups = 0
    
    # La boucle principale
    while running == True:
        # Change le joueur
        joueur += 1
        if joueur > 2:
            joueur = 1
            
        affichageConsole(grille, joueur, noms_joueurs)

        # Fait jouer le joueur
        index_colonne = trouverColonne(noms_joueurs[joueur])
        grille, index_ligne = ajouterJeton(grille, index_colonne, joueur)

        # Vérifie si la partie est finie (victoire ou match nul)
        nombre_coups += 1
        if detecterVictoireVerticale(grille, index_colonne, index_ligne, joueur) == True or detecterVictoireHorizontale(grille, index_ligne, joueur) == True or detecterVictoireBasGaucheHautDroite(grille, index_colonne, index_ligne, joueur) == True or detecterVictoireHautGaucheBasDroite(grille, index_colonne, index_ligne, joueur) == True: 
            running = False
            affichageConsole(grille, joueur, noms_joueurs, 'victoire')
        elif nombre_coups >= 42:
            running = False
            affichageConsole(grille, joueur, noms_joueurs, 'match nul')


if __name__ == '__main__':
    jeu()