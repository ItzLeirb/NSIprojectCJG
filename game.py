# main functions

# main functions

def ajouterJeton(grille: list[list[int]], colonne: int,
                 joueur: int) -> list[list[int]]:
    """
    entrée : grille: la grille, 
             colonne: la colonne jouee
             joueur: le numero du joueur
    choisir la colonne, verifier que la colone est valide ( existance et remplissage ), le jeton   doit tomber ( verifier toutes les [num colone][elt] pour placer le jeton au L[num colone][remplie - 1]
    ajoute un jeton X ou O selon le joueur
    en cas de colonne invalide, le coups doit etre rejoué <- non, fait dans tour()
    sortie : affiche la Liste modifiée (jeton ajouté dans le tableau)
    """
    for ligne, jeton in enumerate(grille[colonne]):
        if jeton != 0:  #la case de la grille n'est vide
            grille[colonne][ligne - 1] = joueur

def isVerticalWin(grille: list[list[int]], colonne: int, ligne: int, joueur: int) -> bool:
    nombre_daffilee = 0
    for ligne in grille[colonne]:
        

def isHorizontalWin(grille: list[list[int]], colonne: int, ligne: int, joueur: int) -> bool:
    pass

def isDiagonalBottomLeftToTopRightWin(grille: list[list[int]], colonne: int, ligne: int, joueur: int) -> bool:
    pass

def isDiagonalTopLeftToBottomRightWin(grille: list[list[int]], colonne: int, ligne: int, joueur: int) -> bool:
    pass

def setupJoueur() -> tuple[int]:
    pass