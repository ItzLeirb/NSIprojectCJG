import pygame as pg
from game import *  # Importer les fonctions de logique du jeu

# Initialisation de Pygame
pg.init()

# Configuration de l'écran et des textures
# Vous pouvez modifier ces valeurs pour ajuster la taille de l'écran ou des textures
SCREEN_WIDTH = 700  # Largeur de l'écran
SCREEN_HEIGHT = 600  # Hauteur de l'écran
TILE_SIZE = 100      # Taille d'une cellule de la grille

# Charger les images
grid_image = pg.image.load("grille.png")
yellow_token = pg.image.load("jaune.png")
red_token = pg.image.load("rouge.png")

# Redimensionner les images selon la taille de l'écran
grid_image = pg.transform.scale(grid_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
yellow_token = pg.transform.scale(yellow_token, (TILE_SIZE, TILE_SIZE))
red_token = pg.transform.scale(red_token, (TILE_SIZE, TILE_SIZE))

# Configurer l'écran
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("Puissance 4")

# Variables de jeu
grid = [[0 for _ in range(6)] for _ in range(7)]  # Grille initiale
current_player = 1  # Le joueur 1 commence
running = True

# Fonction pour dessiner la grille et les jetons
def draw_game():
    screen.blit(grid_image, (0, 0))  # Afficher la grille
    for col in range(7):
        for row in range(6):
            if grid[col][row] == 1:
                screen.blit(yellow_token, (col * TILE_SIZE, (5 - row) * TILE_SIZE))
            elif grid[col][row] == 2:
                screen.blit(red_token, (col * TILE_SIZE, (5 - row) * TILE_SIZE))

# Fonction pour obtenir la colonne cliquée
def get_column_from_mouse(pos):
    x, _ = pos
    return x // TILE_SIZE

# Boucle principale du jeu
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            col = get_column_from_mouse(event.pos)
            if 0 <= col < 7:
                grid, row = ajouterJeton(grid, col, current_player)
                # Vérifier si le joueur actuel a gagné
                if (detecterVictoireVerticale(grid, col, row, current_player) or
                    detecterVictoireHorizontale(grid, row, current_player) or
                    detecterVictoireBasGaucheHautDroite(grid, col, row, current_player) or
                    detecterVictoireHautGaucheBasDroite(grid, col, row, current_player)):
                    print(f"Joueur {current_player} a gagné !")
                    running = False
                # Changer de joueur
                current_player = 3 - current_player

    # Affichage
    draw_game()
    pg.display.flip()

pg.quit()
