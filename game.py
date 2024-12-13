# main functions

# Gabriel
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
            break

# Gabriel
def isVerticalWin(grille: list[list[int]], colonne: int, ligne: int, joueur: int) -> bool:
    nombre_daffilee = 0
    for jeton in grille[colonne][ligne:]:
        if jeton == 0: continue

        if jeton == joueur:
            nombre_daffilee += 1
            if nombre_daffilee >= 4:
                return True
        else:
            break
    return nombre_daffilee >= 4

def isHorizontalWin(grille: list[list[int]], colonne: int, ligne: int, joueur: int) -> bool:
    pass

def isDiagonalBottomLeftToTopRightWin(grille: list[list[int]], colonne: int, ligne: int, joueur: int) -> bool:
    pass

def isDiagonalTopLeftToBottomRightWin(grille: list[list[int]], colonne: int, ligne: int, joueur: int) -> bool:
    pass

def setupJoueur() -> tuple[int]:
    pass