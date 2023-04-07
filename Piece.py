import pygame


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




class Piece:  # Piece est une classe qui contient une couleur, une image et un type
    def __init__(self, color, image,
                 type, id, row,
                 col,move):  # color est une chaîne de caractères, image est un objet de la classe pygame.Surface
        self.color = color  # color est une chaîne de caractères
        self.image = image  # image est un objet de la classe pygame.Surface
        self.type = type  # type est une chaîne de caractères
        self.id = id  # id est un entier
        self.row = row  # row est un entier
        self.col = col  # col est un entier
        self.move = move  # move est un entier

    def draw(self, screen, x, y):  # x et y sont les coordonnées de la case où dessiner la pièce
        screen.blit(self.image, (x, y))  # Dessine l'image de la pièce sur l'écran
        updated_rects.append(
            pygame.Rect(x, y, GRID_SIZE, GRID_SIZE))  # Ajout de la zone de l'écran qui a été mise à jour

    #crée une fonction get_moves qui renvoie les déplacement possible par pieces



    def get_type(self):
        return self.type

    def get_color(self):
        return self.color

    def get_image(self):
        return self.image

    def get_id(self):
        return self.image

    def set_id(self, id):
        self.id = id

    def set_image(self, image):
        self.image = image

    def set_type(self, type):
        self.type = type

    def set_color(self, color):
        self.color = color

    # Classe pour représenter le plateau de jeu
