import pygame
from time import sleep

from Piece import Piece


updated_rects = []  # Liste des rectangles de l'écran qui ont été mis à jour

# Constantes pour la taille de l'écran et de la grille de jeu
SCREEN_WIDTH = 720  # Largeur de l'écran
SCREEN_HEIGHT = 480  # Taille de l'écran
GRID_SIZE = (SCREEN_WIDTH - 250) // 8  # Taille d'une case du plateau de jeu

# Couleurs
WHITE = (255, 255, 255)  # Blanc
BLACK = (0, 0, 0)  # Noir
GRAY = (128, 128, 128)  # Gris
GREEN = (0, 255, 0)  # Vert
RED = (255, 0, 0)  # Rouge
BROWN = (165, 42, 42)  # Marron

# Chargement du background
BACKGROUND_IMG = pygame.image.load('Background.png')  # Charge l'image du background
BACKGROUND_IMG = pygame.transform.scale(BACKGROUND_IMG,
                                        (SCREEN_WIDTH + 350, SCREEN_HEIGHT + 40))  # Redimensionne l'image du background

BACKGROUND_IMG2 = pygame.image.load('Background2.png')  # Charge l'image du background
BACKGROUND_IMG2 = pygame.transform.scale(BACKGROUND_IMG2,
                                         (SCREEN_WIDTH, SCREEN_HEIGHT))  # Redimensionne l'image du background

# Chargement des images des pièces
DEFAULT_IMAGE_SIZE = (64, 64)
PAWN_WHITE_IMG = pygame.image.load('pieces/pawn_white.png')
PAWN_WHITE_IMG = pygame.transform.scale(PAWN_WHITE_IMG, DEFAULT_IMAGE_SIZE)

PAWN_BLACK_IMG = pygame.image.load('pieces/pawn_black.png')
PAWN_BLACK_IMG = pygame.transform.scale(PAWN_BLACK_IMG, DEFAULT_IMAGE_SIZE)

ROOK_WHITE_IMG = pygame.image.load('pieces/rook_white.png')
ROOK_WHITE_IMG = pygame.transform.scale(ROOK_WHITE_IMG, DEFAULT_IMAGE_SIZE)

ROOK_BLACK_IMG = pygame.image.load('pieces/rook_black.png')
ROOK_BLACK_IMG = pygame.transform.scale(ROOK_BLACK_IMG, DEFAULT_IMAGE_SIZE)

KNIGHT_WHITE_IMG = pygame.image.load('pieces/knight_white.png')
KNIGHT_WHITE_IMG = pygame.transform.scale(KNIGHT_WHITE_IMG, DEFAULT_IMAGE_SIZE)

KNIGHT_BLACK_IMG = pygame.image.load('pieces/knight_black.png')
KNIGHT_BLACK_IMG = pygame.transform.scale(KNIGHT_BLACK_IMG, DEFAULT_IMAGE_SIZE)

BISHOP_WHITE_IMG = pygame.image.load('pieces/bishop_white.png')
BISHOP_WHITE_IMG = pygame.transform.scale(BISHOP_WHITE_IMG, DEFAULT_IMAGE_SIZE)

BISHOP_BLACK_IMG = pygame.image.load('pieces/bishop_black.png')
BISHOP_BLACK_IMG = pygame.transform.scale(BISHOP_BLACK_IMG, DEFAULT_IMAGE_SIZE)

QUEEN_WHITE_IMG = pygame.image.load('pieces/queen_white.png')
QUEEN_WHITE_IMG = pygame.transform.scale(QUEEN_WHITE_IMG, DEFAULT_IMAGE_SIZE)

QUEEN_BLACK_IMG = pygame.image.load('pieces/queen_black.png')
QUEEN_BLACK_IMG = pygame.transform.scale(QUEEN_BLACK_IMG, DEFAULT_IMAGE_SIZE)

KING_WHITE_IMG = pygame.image.load('pieces/king_white.png')
KING_WHITE_IMG = pygame.transform.scale(KING_WHITE_IMG, DEFAULT_IMAGE_SIZE)

KING_BLACK_IMG = pygame.image.load('pieces/king_black.png')
KING_BLACK_IMG = pygame.transform.scale(KING_BLACK_IMG, DEFAULT_IMAGE_SIZE)



class Board:  # Board est une classe qui contient une liste de pièces
    def __init__(self, screen):  # screen est un objet de la classe pygame.Surface
        self.grid = []  # self.grid est une liste de pièces
        for i in range(8):  # i est un entier
            row = []  # row est une liste de pièces
            for j in range(8):  # j est un entier
                row.append(None)  # row est une liste de pièces
            self.grid.append(row)  # self.grid est une liste de pièces

        # Placement des pièces initiales
        self.grid[0][0] = Piece('black', ROOK_BLACK_IMG, "rook", 1, 0, 0,0)
        self.grid[0][1] = Piece('black', KNIGHT_BLACK_IMG, "knight", 2, 0, 1,0)
        self.grid[0][2] = Piece('black', BISHOP_BLACK_IMG, "bishop", 3, 0, 2,0)
        self.grid[0][4] = Piece('black', QUEEN_BLACK_IMG, "queen", 4, 0, 4,0)
        self.grid[0][3] = Piece('black', KING_BLACK_IMG, "king", 5, 0, 3,0)
        self.grid[0][5] = Piece('black', BISHOP_BLACK_IMG, "bishop", 6, 0, 5,0)
        self.grid[0][6] = Piece('black', KNIGHT_BLACK_IMG, "knight", 7, 0, 6,0)
        self.grid[0][7] = Piece('black', ROOK_BLACK_IMG, "rook", 8, 0, 7,0)
        self.grid[1][0] = Piece('black', PAWN_BLACK_IMG, "pawn", 9, 1, 0,0)
        self.grid[1][1] = Piece('black', PAWN_BLACK_IMG, "pawn", 10, 1, 1,0)
        self.grid[1][2] = Piece('black', PAWN_BLACK_IMG, "pawn", 11, 1, 2,0)
        self.grid[1][3] = Piece('black', PAWN_BLACK_IMG, "pawn", 12, 1, 3,0)
        self.grid[1][4] = Piece('black', PAWN_BLACK_IMG, "pawn", 13, 1, 4,0)
        self.grid[1][5] = Piece('black', PAWN_BLACK_IMG, "pawn", 14, 1, 5,0)
        self.grid[1][6] = Piece('black', PAWN_BLACK_IMG, "pawn", 15, 1, 6,0)
        self.grid[1][7] = Piece('black', PAWN_BLACK_IMG, "pawn", 16, 1, 7,0)
        self.grid[7][0] = Piece('white', ROOK_WHITE_IMG, "rook", 17, 7, 0,0)
        self.grid[7][1] = Piece('white', KNIGHT_WHITE_IMG, "knight", 18, 7, 1,0)
        self.grid[7][2] = Piece('white', BISHOP_WHITE_IMG, "bishop", 19, 7, 2,0)
        self.grid[7][4] = Piece('white', QUEEN_WHITE_IMG, "queen", 20, 7, 4,0)
        self.grid[7][3] = Piece('white', KING_WHITE_IMG, "king", 21, 7, 3,0)
        self.grid[7][5] = Piece('white', BISHOP_WHITE_IMG, "bishop", 22, 7, 5,0)
        self.grid[7][6] = Piece('white', KNIGHT_WHITE_IMG, "knight", 23, 7, 6,0)
        self.grid[7][7] = Piece('white', ROOK_WHITE_IMG, "rook", 24, 7, 7,0)
        self.grid[6][0] = Piece('white', PAWN_WHITE_IMG, "pawn", 25, 6, 0,0)
        self.grid[6][1] = Piece('white', PAWN_WHITE_IMG, "pawn", 26, 6, 1,0)
        self.grid[6][2] = Piece('white', PAWN_WHITE_IMG, "pawn", 27, 6, 2,0)
        self.grid[6][3] = Piece('white', PAWN_WHITE_IMG, "pawn", 28, 6, 3,0)
        self.grid[6][4] = Piece('white', PAWN_WHITE_IMG, "pawn", 29, 6, 4,0)
        self.grid[6][5] = Piece('white', PAWN_WHITE_IMG, "pawn", 30, 6, 5,0)
        self.grid[6][6] = Piece('white', PAWN_WHITE_IMG, "pawn", 31, 6, 6,0)
        self.grid[6][7] = Piece('white', PAWN_WHITE_IMG, "pawn", 32, 6, 7,0)

    def draw(self, screen):  # Fonction pour dessiner le plateau de jeu
        for i in range(8):  # Pour chaque case du plateau
            for j in range(8):  # Pour chaque case du plateau
                if (i + j) % 2 == 0:  # Pour dessiner les cases blanches et noires
                    pygame.draw.rect(screen, GRAY,
                                     (j * GRID_SIZE, i * GRID_SIZE, GRID_SIZE, GRID_SIZE))  # On dessine la case
                else:
                    pygame.draw.rect(screen, WHITE,
                                     (j * GRID_SIZE, i * GRID_SIZE, GRID_SIZE, GRID_SIZE))  # On dessine la case
                if self.grid[i][j] is not None:  # Pour dessiner les pièces
                    x = j * GRID_SIZE  # On récupère les coordonnées de la pièce
                    y = i * GRID_SIZE  # On récupère les coordonnées de la pièce
                    self.grid[i][j].draw(screen, x, y)  # On dessine la pièce
        pygame.display.update(updated_rects)  # On met à jour l'affichage


def get_grid_size():  # Fonction qui permet de récupérer la taille de la grille
    return GRID_SIZE

