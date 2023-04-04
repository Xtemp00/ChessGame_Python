import pygame
from time import sleep
from Game import Game
from AI import AI

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



class Main_Screen:  # Classe pour représenter l'écran d'accueil
    def __init__(self):  # Fonction d'initialisation
        self.screen = pygame.display.set_mode((SCREEN_WIDTH - 240, SCREEN_HEIGHT))  # On crée une fenêtre
        self.screen.blit(BACKGROUND_IMG, (-150, 0))  # On affiche l'image de fond
        pygame.display.flip()
        pygame.display.set_caption("Jeu d'échec")  # On donne un titre à la fenêtre
        self.running = True  # Variable qui permet de savoir si le jeu est lancé ou non

    def handle_events(self):  # Fonction qui gère les événements
        for event in pygame.event.get():  # On parcours la liste des événements reçus
            if event.type == pygame.QUIT:  # Si on clique sur la croix
                self.running = False  # On quitte le jeu
            elif event.type == pygame.MOUSEBUTTONDOWN:  # Si on clique sur la souris
                x, y = pygame.mouse.get_pos()  # On récupère les coordonnées de la souris
                print(x, y)  # On affiche les coordonnées de la souris
                if x > 150 and x < 340 and y > 300 and y < 400:  # Si on clique sur le bouton "Jouer"
                    game = Game()  # On lance le jeu
                    AI()  # On lance l'IA
                    game.run()  # On lance le jeu

    def draw(self):  # Fonction qui permet de dessiner l'écran d'accueil
        font = pygame.font.SysFont('comicsans', 70)  # On définit la police
        text = font.render("Jeu d'échec", 1, WHITE)  # On écrit le texte
        self.screen.blit(text, (SCREEN_WIDTH / 2 - text.get_width() / 2, 100))  # On affiche le texte
        pygame.draw.rect(self.screen, WHITE, (150, 300, 190, 100))  # On dessine le bouton "Jouer"
        font = pygame.font.SysFont('comicsans', 50)  # On définit la police
        text = font.render("Jouer", 1, BLACK)  # On écrit le texte
        self.screen.blit(text, ((SCREEN_WIDTH - 240) / 2 - text.get_width() / 2, 310))  # On affiche le texte
        pygame.display.update()  # On met à jour l'affichage

    def run(self):  # Fonction qui permet de lancer l'écran d'accueil
        while self.running:  # Tant que l'écran d'accueil est lancé
            self.handle_events()  # On gère les évènements
            self.draw()  # On dessine l'écran d'accueil
        pygame.quit()  # On quitte pygame


