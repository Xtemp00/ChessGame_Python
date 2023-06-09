import pygame
from Board import Board
from Piece import Piece
from Player import Player

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


class Game:  # Classe pour représenter le jeu
    def __init__(self):  # Fonction d'initialisation
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # On crée une fenêtre
        pygame.display.set_caption("Jeu d'échec")  # On donne un titre à la fenêtre
        self.board = Board(self.screen)  # On crée un plateau de jeu
        self.selected_piece = None  # Pour savoir quelle pièce est sélectionnée
        self.running = True  # Pour savoir si le jeu est en cours
        self.screen.blit(BACKGROUND_IMG2, (0, 0))  # On affiche l'image de fond
        self.draw()
        self.position = 60
        self.afficher = []
        self.player = Player("white", 1)  # On crée un joueur
        self.player2 = Player("black", 0)  # On crée un joueur
        pygame.display.flip()  # On met à jour l'affichage

    def draw(self):  # Fonction qui permet de dessiner l'écran d'accueil
        font = pygame.font.SysFont('comicsans', 30)  # On définit la police
        text = font.render("Coups Jouer : ", 1, WHITE)  # On écrit le texte
        self.screen.blit(text, (500, 5))  # On affiche le texte

    # On Enregistre les coups joués
    def Coups_Joues(self, row, col, row2, col2, piece):
        colonne = ["A", "B", "C", "D", "E", "F", "G", "H"]
        if piece is not None:
            coup = ("La Pièces " + piece.type + " En " + str(colonne[col]) + str(row) + " Vers " + str(
                row) + str(colonne[col2]))
            for i in range(len(coup)):
                print(coup[i], end=" ")
            font = pygame.font.SysFont('comicsans', 20)
            # Affiche les 15 dernier coup jouer dans la fenêtre
            for i in range(10):

                text1 = (str(colonne[col2]) + str(row2) + " -> " + str(colonne[col]) + str(row))

                if text1 not in self.afficher:
                    text = font.render(text1, 1, WHITE)
                    self.screen.blit(text, (500, self.position))
                    self.position += 30
                    self.afficher.append(text1)

                # Lorsque le tableau a atteint 10, on supprime le premier élément et on décale tous les autres
                if len(self.afficher) > 10:
                    self.afficher.pop(0)
                    self.position -= 30
                    self.screen.blit(BACKGROUND_IMG2, (0, 0))
                    self.draw()
                    for i in range(len(self.afficher)):
                        text = font.render(self.afficher[i], 1, WHITE)
                        self.screen.blit(text, (500, self.position - 30 * (len(self.afficher) - i)))

    def choose_player(self):
        font = pygame.font.SysFont('comicsans', 30)
        text = font.render("Choisissez votre couleur", 1, WHITE)
        text2 = font.render("Blanc", 1, WHITE)
        text3 = font.render("Noir", 1, WHITE)
        pygame.draw.rect(self.screen, BLACK, (100, 300, 100, 50))
        pygame.draw.rect(self.screen, BLACK, (500, 300, 100, 50))
        self.screen.blit(text2, (50 + 200 // 2 - text2.get_width() // 2, 300 + 50 // 2 - text2.get_height() // 2))
        self.screen.blit(text3, (450 + 200 // 2 - text3.get_width() // 2, 300 + 50 // 2 - text3.get_height() // 2))
        self.screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - text.get_height() // 2))
        pygame.display.update()
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if 100 < x < 200 and 300 < y < 350:
                        self.player = Player("white", 1)
                        self.player2 = Player("black", 0)
                        run = False
                    if 500 < x < 600 and 300 < y < 350:
                        self.player = Player("black", 1)
                        self.player2 = Player("white", 0)
                        run = False

    def handle_events(self):  # Fonction qui gère les événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Si on clique sur la souris
                x, y = pygame.mouse.get_pos()  # On récupère les coordonnées de la souris
                row = y // GRID_SIZE  # On calcule la ligne
                col = x // GRID_SIZE  # On calcule la colonne
                run = True
                self.select_piece(row, col)  # On sélectionne la pièce
                if self.selected_piece is not None:
                    piece = self.board.grid[row][col]
                    if piece.color == self.player.color and self.player.turn != 1:
                        self.selected_piece = None
                    elif piece.color == self.player2.color and self.player2.turn != 1:
                        self.selected_piece = None

                # On vérifie si le roi est en échec
                """king_posb = self.get_piece_position(5)
                king_posw = self.get_piece_position(21)
                self.checkb(king_posb[0], king_posb[1])
                self.checkw(king_posw[0], king_posw[1])"""

                self.get_tab_piece()  # On récupère les pièces de chaque joueur
                # On regarde la pièce sélectionnée et on la met en Hightlight tant que un second click n'est pas détecter puis on déplace la pièce au click

                while run:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            run = False
                            self.running = False
                        # Si on detect un click gauche on déplace la pièce
                        elif event.type == pygame.MOUSEBUTTONDOWN:
                            x, y = pygame.mouse.get_pos()
                            row = y // GRID_SIZE
                            col = x // GRID_SIZE
                            self.move(row, col)
                            self.get_tab_piece()
                            run = False
                            self.running = True
                            # On vérifie si le roi est en échec
                            king_posb = self.get_piece_position(5)
                            king_posw = self.get_piece_position(21)
                            self.checkb(king_posb[0], king_posb[1])
                            self.checkw(king_posw[0], king_posw[1])
                            self.checkmate()
                    if self.selected_piece is not None:
                        piece = self.board.grid[self.selected_piece[0]][self.selected_piece[1]]
                        # appeler la fonction highlight_moves par pieces avec les coordonnées de la pièce sélectionnée
                        if piece is not None:
                            if piece.type == "pawn":
                                self.highlight_moves_pawn(self.selected_piece[0], self.selected_piece[1])
                            if piece.type == "rook":
                                self.highlight_moves_rook(self.selected_piece[0], self.selected_piece[1])
                            if piece.type == "knight":
                                self.highlight_moves_knight(self.selected_piece[0], self.selected_piece[1])
                            if piece.type == "bishop":
                                self.highlight_moves_bishop(self.selected_piece[0], self.selected_piece[1])
                            if piece.type == "queen":
                                self.highlight_moves_queen(self.selected_piece[0], self.selected_piece[1])
                            if piece.type == "king":
                                self.highlight_moves_king(self.selected_piece[0], self.selected_piece[1])

    def select_piece(self, row, col):  # Fonction qui permet de sélectionner une pièce
        piece = self.board.grid[row][col]  # On récupère la pièce
        if self.selected_piece is None:
            if piece is not None:  # Si la pièce n'est pas vide
                if self.player.color == piece.color:
                    self.selected_piece = (row, col)  # On sélectionne la pièce
                elif self.player2.color == piece.color:
                    self.selected_piece = (row, col)

        elif self.selected_piece is not None:  # Si une pièce est sélectionnée
            self.move(row, col)  # On déplace la pièce
            # self.tour_par_tour()

    def pawn_move(self, row, col):  # Fonction qui permet de déplacer un pion
        if self.selected_piece is not None:  # Si une pièce est sélectionnée
            piece_row, piece_col = self.selected_piece  # On récupère les coordonnées de la pièce
            piece = self.board.grid[piece_row][piece_col]  # On récupère la pièce
            self.en_passant(piece_row, piece_col)
            self.en_passant(row, col)
            if piece.type == "pawn":  # Si la pièce est un pion
                if piece.color == "white" and (self.player.turn and self.player.color == "white") or (
                        self.player2.turn and self.player2.color == "white"):  # Si la pièce est blanche
                    if row == piece_row - 1 and col == piece_col and self.board.grid[row][col] is None:
                        # On affiche le carré ou le pions peut se déplacer
                        # Déplacement normal d'un pion blanc
                        self.board.grid[piece_row][piece_col] = None  # On vide la case de départ
                        self.board.grid[row][col] = piece  # On place la pièce sur la case d'arrivée
                        self.selected_piece = None  # On déselectionne la pièce
                    elif piece_row == 6 and row == piece_row - 2 and col == piece_col and self.board.grid[row][
                        col] is None and self.board.grid[row + 1][col] is None:
                        # Déplacement initial d'un pion blanc
                        self.board.grid[piece_row][piece_col] = None  # On vide la case de départ
                        self.board.grid[row][col] = piece  # On place la pièce sur la case d'arrivée
                        self.selected_piece = None  # On déselectionne la pièce
                    elif row == piece_row - 1 and abs(col - piece_col) == 1 and self.board.grid[row][
                        col] is not None and self.board.grid[row][col].color == "black":
                        # Prise en diagonale d'un pion noir par un pion blanc
                        self.board.grid[piece_row][piece_col] = None  # On vide la case de départ
                        self.board.grid[row][col] = piece  # On place la pièce sur la case d'arrivée
                        self.selected_piece = None  # On déselectionne la pièce
                if piece.color == "black" and (self.player.turn and self.player.color == "black") or (
                        self.player2.turn and self.player2.color == "black"):
                    if row == piece_row + 1 and col == piece_col and self.board.grid[row][col] is None:
                        # Déplacement normal d'un pion noir
                        self.board.grid[piece_row][piece_col] = None  # On vide la case de départ
                        self.board.grid[row][col] = piece  # On place la pièce sur la case d'arrivée
                        self.selected_piece = None  # On déselectionne la pièce
                    elif piece_row == 1 and row == piece_row + 2 and col == piece_col and self.board.grid[row][
                        col] is None and self.board.grid[row - 1][col] is None:
                        # Déplacement initial d'un pion noir
                        self.board.grid[piece_row][piece_col] = None  # On vide la case de départ
                        self.board.grid[row][col] = piece  # On place la pièce sur la case d'arrivée
                        self.selected_piece = None  # On déselectionne la pièce
                    elif row == piece_row + 1 and abs(col - piece_col) == 1 and self.board.grid[row][
                        col] is not None and self.board.grid[row][col].color == "white":
                        # Prise en diagonale d'un pion blanc par un pion noir
                        self.board.grid[piece_row][piece_col] = None  # On vide la case de départ
                        self.board.grid[row][col] = piece  # On place la pièce sur la case d'arrivée
                        self.selected_piece = None  # On déselectionne la pièce
            piece.move += 1  # On incrémente le nombre de déplacement de la pièce
        self.pawn_promotion(row, col)
        self.Coups_Joues(row, col, piece_row, piece_col, piece)

    def rook_move(self, row, col):
        if self.selected_piece is not None:
            piece_row, piece_col = self.selected_piece
            piece = self.board.grid[piece_row][piece_col]
            if piece.type == "rook" and piece.color == "white" and (
                    self.player.turn and self.player.color == "white") or (
                    self.player2.turn and self.player2.color == "white"):
                if row == piece_row and col != piece_col:
                    if col > piece_col:
                        for i in range(piece_col + 1, col):
                            if self.board.grid[row][i] is not None:
                                return
                    else:
                        for i in range(col + 1, piece_col):
                            if self.board.grid[row][i] is not None:
                                return
                    if self.board.grid[row][col] is None or self.board.grid[row][
                        col].color != piece.color:  # Ajout de la vérification de la couleur de la pièce cible
                        self.board.grid[piece_row][piece_col] = None
                        self.board.grid[row][col] = piece
                        self.selected_piece = None
                elif row != piece_row and col == piece_col:
                    if row > piece_row:
                        for i in range(piece_row + 1, row):
                            if self.board.grid[i][col] is not None:
                                return
                    else:
                        for i in range(row + 1, piece_row):
                            if self.board.grid[i][col] is not None:
                                return
                    if self.board.grid[row][col] is None or self.board.grid[row][
                        col].color != piece.color:  # Ajout de la vérification de la couleur de la pièce cible
                        self.board.grid[piece_row][piece_col] = None
                        self.board.grid[row][col] = piece
                        self.selected_piece = None
            if piece.type == "rook" and piece.color == "black" and (
                    self.player.turn and self.player.color == "black") or (
                    self.player2.turn and self.player2.color == "black"):
                if col > piece_col:
                    for i in range(piece_col + 1, col):
                        if self.board.grid[row][i] is not None:
                            return
                else:
                    for i in range(col + 1, piece_col):
                        if self.board.grid[row][i] is not None:
                            return
                if self.board.grid[row][col] is None or self.board.grid[row][
                    col].color != piece.color:  # Ajout de la vérification de la couleur de la pièce cible
                    self.board.grid[piece_row][piece_col] = None
                    self.board.grid[row][col] = piece
                    self.selected_piece = None
            elif row != piece_row and col == piece_col:
                if row > piece_row:
                    for i in range(piece_row + 1, row):
                        if self.board.grid[i][col] is not None:
                            return
                else:
                    for i in range(row + 1, piece_row):
                        if self.board.grid[i][col] is not None:
                            return
                if self.board.grid[row][col] is None or self.board.grid[row][
                    col].color != piece.color:  # Ajout de la vérification de la couleur de la pièce cible
                    self.board.grid[piece_row][piece_col] = None
                    self.board.grid[row][col] = piece
                    self.selected_piece = None
            piece.move += 1
        self.Coups_Joues(row, col, piece_row, piece_col, piece)

    def knight_move(self, row, col):  # Fonction qui permet de déplacer un cavalier
        if self.selected_piece is not None:  # Si une pièce est sélectionnée
            piece_row, piece_col = self.selected_piece  # On récupère les coordonnées de la pièce
            piece = self.board.grid[piece_row][piece_col]  # On récupère la pièce
            if piece.type == "knight" and piece.color == "white" and (
                    self.player.turn and self.player.color == "white") or (
                    self.player2.turn and self.player2.color == "white"):
                # Vérification des déplacements valides pour un cavalier
                if ((row == piece_row + 2 and col == piece_col + 1) or
                        (row == piece_row + 2 and col == piece_col - 1) or
                        (row == piece_row - 2 and col == piece_col + 1) or
                        (row == piece_row - 2 and col == piece_col - 1) or
                        (row == piece_row + 1 and col == piece_col + 2) or
                        (row == piece_row + 1 and col == piece_col - 2) or
                        (row == piece_row - 1 and col == piece_col + 2) or
                        (row == piece_row - 1 and col == piece_col - 2)):

                    # Vérification si la case d'arrivée est vide ou contient une pièce adverse
                    if self.board.grid[row][col] is None or self.board.grid[row][col].color != piece.color:
                        self.board.grid[piece_row][piece_col] = None  # On vide la case de départ
                        self.board.grid[row][col] = piece  # On place la pièce sur la case d'arrivée
                        self.selected_piece = None  # On déselectionne la pièce
            if piece.type == "knight" and piece.color == "black" and (
                    self.player.turn and self.player.color == "black") or (
                    self.player2.turn and self.player2.color == "black"):
                # Vérification des déplacements valides pour un cavalier
                if ((row == piece_row + 2 and col == piece_col + 1) or
                        (row == piece_row + 2 and col == piece_col - 1) or
                        (row == piece_row - 2 and col == piece_col + 1) or
                        (row == piece_row - 2 and col == piece_col - 1) or
                        (row == piece_row + 1 and col == piece_col + 2) or
                        (row == piece_row + 1 and col == piece_col - 2) or
                        (row == piece_row - 1 and col == piece_col + 2) or
                        (row == piece_row - 1 and col == piece_col - 2)):

                    # Vérification si la case d'arrivée est vide ou contient une pièce adverse
                    if self.board.grid[row][col] is None or self.board.grid[row][col].color != piece.color:
                        self.board.grid[piece_row][piece_col] = None  # On vide la case de départ
                        self.board.grid[row][col] = piece  # On place la pièce sur la case d'arrivée
                        self.selected_piece = None  # On déselectionne la pièce
            piece.move += 1
        self.Coups_Joues(row, col, piece_row, piece_col, piece)

    def bishop_move(self, row, col):  # Fonction qui permet de déplacer un fou
        if self.selected_piece is not None:  # Si une pièce est sélectionnée
            piece_row, piece_col = self.selected_piece  # On récupère les coordonnées de la pièce
            piece = self.board.grid[piece_row][piece_col]  # On récupère la pièce
            if piece.type == "bishop" and piece.color == "white" and (
                    self.player.turn and self.player.color == "white") or (
                    self.player2.turn and self.player2.color == "white"):  # Si la pièce est un fou
                if self.board.grid[row][col] is None or self.board.grid[row][
                    col].color != piece.color:  # Si la case d'arrivée est vide ou contient une pièce de couleur
                    # différente
                    if abs(row - piece_row) == abs(col - piece_col):  # Si le déplacement est diagonal
                        # Vérification que le fou ne saute pas par dessus une pièce
                        if row > piece_row and col > piece_col:  # Si le déplacement est en bas à droite
                            for i in range(1,
                                           row - piece_row):  # On vérifie que la case d'arrivée est vide ou contient
                                # une pièce de couleur différente
                                if self.board.grid[piece_row + i][piece_col + i] is not None:  # Si la case est occupée
                                    return  # Si le déplacement est valide
                        elif row > piece_row and col < piece_col:  # Si le déplacement est en bas à gauche
                            for i in range(1,
                                           row - piece_row):  # On vérifie que la case d'arrivée est vide ou contient
                                # une pièce de couleur différente
                                if self.board.grid[piece_row + i][piece_col - i] is not None:  # Si la case est occupée
                                    return  # Si le déplacement est valide
                        elif row < piece_row and col > piece_col:  # Si le déplacement est en haut à droite
                            for i in range(1,
                                           piece_row - row):  # On vérifie que la case d'arrivée est vide ou contient
                                # une pièce de couleur différente
                                if self.board.grid[piece_row - i][piece_col + i] is not None:  # Si la case est occupée
                                    return  # Si le déplacement est valide
                        elif row < piece_row and col < piece_col:  # Si le déplacement est en haut à gauche
                            for i in range(1,
                                           piece_row - row):  # On vérifie que la case d'arrivée est vide ou contient
                                # une pièce de couleur différente
                                if self.board.grid[piece_row - i][piece_col - i] is not None:  # Si la case est occupée
                                    return  # Si le déplacement est valide
                        self.board.grid[piece_row][piece_col] = None  # On vide la case de départ
                        self.board.grid[row][col] = piece  # On place la pièce sur la case d'arrivée
                        self.selected_piece = None  # On déselectionne la pièce
            if piece.type == "bishop" and piece.color == "black" and (
                    self.player.turn and self.player.color == "black") or (
                    self.player2.turn and self.player2.color == "black"):  # Si la pièce est un fou
                if self.board.grid[row][col] is None or self.board.grid[row][
                    col].color != piece.color:  # Si la case d'arrivée est vide ou contient une pièce de
                    # couleur différente
                    if abs(row - piece_row) == abs(col - piece_col):  # Si le déplacement est diagonal
                        # Vérification que le fou ne saute pas par dessus une pièce
                        if row > piece_row and col > piece_col:  # Si le déplacement est en bas à droite
                            for i in range(1,
                                           row - piece_row):  # On vérifie que la case d'arrivée est vide ou contient
                                # une pièce de couleur différente
                                if self.board.grid[piece_row + i][piece_col + i] is not None:  # Si la case est occupée
                                    return  # Si le déplacement est valide
                        elif row > piece_row and col < piece_col:  # Si le déplacement est en bas à gauche
                            for i in range(1,
                                           row - piece_row):  # On vérifie que la case d'arrivée est vide ou contient
                                # une pièce de couleur différente
                                if self.board.grid[piece_row + i][piece_col - i] is not None:  # Si la case est occupée
                                    return  # Si le déplacement est valide
                        elif row < piece_row and col > piece_col:  # Si le déplacement est en haut à droite
                            for i in range(1,
                                           piece_row - row):  # On vérifie que la case d'arrivée est vide ou contient
                                # une pièce de couleur différente
                                if self.board.grid[piece_row - i][piece_col + i] is not None:  # Si la case est occupée
                                    return  # Si le déplacement est valide
                        elif row < piece_row and col < piece_col:  # Si le déplacement est en haut à gauche
                            for i in range(1,
                                           piece_row - row):  # On vérifie que la case d'arrivée est vide ou contient
                                # une pièce de couleur différente
                                if self.board.grid[piece_row - i][piece_col - i] is not None:  # Si la case est occupée
                                    return  # Si le déplacement est valide
                        self.board.grid[piece_row][piece_col] = None  # On vide la case de départ
                        self.board.grid[row][col] = piece  # On place la pièce sur la case d'arrivée
                        self.selected_piece = None  # On déselectionne la pièce
            piece.move += 1  # On incrémente le nombre de déplacement de la pièce
        self.Coups_Joues(row, col, piece_row, piece_col, piece)

    def queen_move(self, row, col):  # Fonction qui permet de déplacer une reine
        if self.selected_piece is not None:  # Si une pièce est sélectionnée
            piece_row, piece_col = self.selected_piece  # On récupère les coordonnées de la pièce
            piece = self.board.grid[piece_row][piece_col]  # On récupère la pièce
            if piece.type == "queen" and piece.color == "white" and (
                    self.player.turn and self.player.color == "white") or (
                    self.player2.turn and self.player2.color == "white"):  # Si la pièce est une reine
                if self.board.grid[row][col] is None or self.board.grid[row][
                    col].color != piece.color:  # Si la case d'arrivée est vide ou contient une pièce de couleur
                    # différente
                    if row == piece_row or col == piece_col or abs(row - piece_row) == abs(
                            col - piece_col):  # Si le déplacement est horizontal, vertical ou diagonal
                        # Vérification que la reine ne saute pas par-dessus d'autres pièces
                        if row == piece_row:  # Déplacement horizontal
                            if col > piece_col:  # Déplacement vers la droite
                                for i in range(piece_col + 1,
                                               col):  # On parcourt les cases entre la case de départ et la case
                                    # d'arrivée
                                    if self.board.grid[row][i] is not None:  # Si une case n'est pas vide
                                        return  # On ne déplace pas la pièce
                            else:  # Déplacement vers la gauche
                                for i in range(col + 1,
                                               piece_col):  # On parcourt les cases entre la case de départ et la
                                    # case d'arrivée
                                    if self.board.grid[row][i] is not None:  # Si une case n'est pas vide
                                        return  # On ne déplace pas la pièce
                        elif col == piece_col:  # Déplacement vertical
                            if row > piece_row:  # Déplacement vers le bas
                                for i in range(piece_row + 1,
                                               row):  # On parcourt les cases entre la case de départ et la case
                                    # d'arrivée
                                    if self.board.grid[i][col] is not None:  # Si une case n'est pas vide
                                        return  # On ne déplace pas la pièce
                            else:  # Déplacement vers le haut
                                for i in range(row + 1,
                                               piece_row):  # On parcourt les cases entre la case de départ et la
                                    # case d'arrivée
                                    if self.board.grid[i][col] is not None:  # Si une case n'est pas vide
                                        return  # On ne déplace pas la pièce
                        else:  # Déplacement diagonal
                            if row > piece_row:  # Déplacement vers le bas
                                if col > piece_col:  # Déplacement vers la droite
                                    for i in range(1,
                                                   row - piece_row):  # On parcourt les cases entre la case de départ
                                        # et la case d'arrivée
                                        if self.board.grid[piece_row + i][
                                            piece_col + i] is not None:  # Si une case n'est pas vide
                                            return  # On ne déplace pas la pièce
                                else:  # Déplacement vers la gauche
                                    for i in range(1,
                                                   row - piece_row):  # On parcourt les cases entre la case de départ
                                        # et la case d'arrivée
                                        if self.board.grid[piece_row + i][
                                            piece_col - i] is not None:  # Si une case n'est pas vide
                                            return  # On ne déplace pas la pièce
                            else:  # Déplacement vers le haut
                                if col > piece_col:  # Déplacement vers la droite
                                    for i in range(1,
                                                   piece_row - row):  # On parcourt les cases entre la case de départ
                                        # et la case d'arrivée
                                        if self.board.grid[piece_row - i][
                                            piece_col + i] is not None:  # Si une case n'est pas vide
                                            return  # On ne déplace pas la pièce
                                else:  # Déplacement vers la gauche
                                    for i in range(1,
                                                   piece_row - row):  # On parcourt les cases entre la case de départ
                                        # et la case d'arrivée
                                        if self.board.grid[piece_row - i][
                                            piece_col - i] is not None:  # Si une case n'est pas vide
                                            return  # On ne déplace pas la pièce
                        # Si la reine ne saute pas par-dessus d'autres pièces, on effectue le déplacement
                        self.board.grid[row][col] = piece  # On place la pièce sur la case d'arrivée
                        self.board.grid[piece_row][piece_col] = None  # On vide la case de départ
                        self.selected_piece = None  # On déselectionne la pièce
            if piece.type == "queen" and piece.color == "white" and (
                    self.player.turn and self.player.color == "white") or (
                    self.player2.turn and self.player2.color == "black"):
                if self.board.grid[row][col] is None or self.board.grid[row][
                    col].color != piece.color:  # Si la case d'arrivée est vide ou contient une pièce de couleur
                    # différente
                    if row == piece_row or col == piece_col or abs(row - piece_row) == abs(
                            col - piece_col):  # Si le déplacement est horizontal, vertical ou diagonal
                        # Vérification que la reine ne saute pas par-dessus d'autres pièces
                        if row == piece_row:  # Déplacement horizontal
                            if col > piece_col:  # Déplacement vers la droite
                                for i in range(piece_col + 1,
                                               col):  # On parcourt les cases entre la case de départ et la case
                                    # d'arrivée
                                    if self.board.grid[row][i] is not None:  # Si une case n'est pas vide
                                        return  # On ne déplace pas la pièce
                            else:  # Déplacement vers la gauche
                                for i in range(col + 1,
                                               piece_col):  # On parcourt les cases entre la case de départ et la
                                    # case d'arrivée
                                    if self.board.grid[row][i] is not None:  # Si une case n'est pas vide
                                        return  # On ne déplace pas la pièce
                        elif col == piece_col:  # Déplacement vertical
                            if row > piece_row:  # Déplacement vers le bas
                                for i in range(piece_row + 1,
                                               row):  # On parcourt les cases entre la case de départ et la case
                                    # d'arrivée
                                    if self.board.grid[i][col] is not None:  # Si une case n'est pas vide
                                        return  # On ne déplace pas la pièce
                            else:  # Déplacement vers le haut
                                for i in range(row + 1,
                                               piece_row):  # On parcourt les cases entre la case de départ et la case d'arrivée
                                    if self.board.grid[i][col] is not None:  # Si une case n'est pas vide
                                        return  # On ne déplace pas la pièce
                        else:  # Déplacement diagonal
                            if row > piece_row:  # Déplacement vers le bas
                                if col > piece_col:  # Déplacement vers la droite
                                    for i in range(1,
                                                   row - piece_row):  # On parcourt les cases entre la case de départ et la case d'arrivée
                                        if self.board.grid[piece_row + i][
                                            piece_col + i] is not None:  # Si une case n'est pas vide
                                            return  # On ne déplace pas la pièce
                                else:  # Déplacement vers la gauche
                                    for i in range(1,
                                                   row - piece_row):  # On parcourt les cases entre la case de départ et la case d'arrivée
                                        if self.board.grid[piece_row + i][
                                            piece_col - i] is not None:  # Si une case n'est pas vide
                                            return  # On ne déplace pas la pièce
                            else:  # Déplacement vers le haut
                                if col > piece_col:  # Déplacement vers la droite
                                    for i in range(1,
                                                   piece_row - row):  # On parcourt les cases entre la case de départ et la case d'arrivée
                                        if self.board.grid[piece_row - i][
                                            piece_col + i] is not None:  # Si une case n'est pas vide
                                            return  # On ne déplace pas la pièce
                                else:  # Déplacement vers la gauche
                                    for i in range(1,
                                                   piece_row - row):  # On parcourt les cases entre la case de départ et la case d'arrivée
                                        if self.board.grid[piece_row - i][
                                            piece_col - i] is not None:  # Si une case n'est pas vide
                                            return  # On ne déplace pas la pièce
                        # Si la reine ne saute pas par-dessus d'autres pièces, on effectue le déplacement
                        self.board.grid[row][col] = piece  # On place la pièce sur la case d'arrivée
                        self.board.grid[piece_row][piece_col] = None  # On vide la case de départ
                        self.selected_piece = None  # On déselectionne la pièce
            piece.move += 1  # On incrémente le nombre de déplacement de la pièce
        self.Coups_Joues(row, col, piece_row, piece_col, piece)

    def king_move(self, row, col):  # Fonction qui permet de déplacer un roi
        if self.selected_piece is not None:  # Si une pièce est sélectionnée
            piece_row, piece_col = self.selected_piece  # On récupère les coordonnées de la pièce
            piece = self.board.grid[piece_row][piece_col]  # On récupère la pièce
            self.castling(row, col)  # On vérifie si le roi peut effectuer un roque
            if piece.type == "king" and piece.color == "white" and (
                    self.player.turn and self.player.color == "white") or (
                    self.player2.turn and self.player2.color == "white"):  # Si la pièce est un roi
                if abs(row - piece_row) <= 1 and abs(col - piece_col) <= 1 and (row, col) != (
                        piece_row, piece_col):  # Si le déplacement est valide
                    if self.board.grid[row][col] is None or self.board.grid[row][
                        col].color != piece.color:  # Si la case d'arrivée est vide ou contient une pièce adverse
                        self.board.grid[piece_row][piece_col] = None  # On vide la case de départ
                        self.board.grid[row][col] = piece  # On place la pièce sur la case d'arrivée
                        self.selected_piece = None  # On déselectionne la pièce
            if piece.type == "king" and piece.color == "white" and (
                    self.player.turn and self.player.color == "white") or (
                    self.player2.turn and self.player2.color == "black"):
                if abs(row - piece_row) <= 1 and abs(col - piece_col) <= 1 and (row, col) != (
                        piece_row, piece_col):  # Si le déplacement est valide
                    if self.board.grid[row][col] is None or self.board.grid[row][
                        col].color != piece.color:  # Si la case d'arrivée est vide ou contient une pièce adverse
                        self.board.grid[piece_row][piece_col] = None  # On vide la case de départ
                        self.board.grid[row][col] = piece  # On place la pièce sur la case d'arrivée
                        self.selected_piece = None  # On déselectionne la pièce
            piece.move += 1  # On incrémente le nombre de déplacement de la pièce
        # self.Coups_Joues(row, col, piece_row, piece_col, piece)

    # crée une fonction castling qui permet de faire le roque
    def castling(self, row, col):
        if self.selected_piece is not None and self.board.grid[row][col] is not None:  # Si une pièce est sélectionnée
            piece_row, piece_col = self.selected_piece  # On récupère les coordonnées de la pièce
            piece = self.board.grid[piece_row][piece_col]  # On récupère la pièce
            if piece.type == "king" and piece.color == "white" and (
                    self.player.turn and self.player.color == "white") or (
                    self.player2.turn and self.player2.color == "white"):  # Si la pièce est un roi
                if self.board.grid[7][0] is not None and self.board.grid[7][0].type == "rook" and self.board.grid[7][
                    0].color == "white" and piece.move == 0 and self.board.grid[7][1] is None and \
                        self.board.grid[7][2] is None and self.board.grid[row][
                    col].type == "rook":  # Si la tour n'a pas bougé et que les cases entre le roi et la tour sont vides
                    self.board.grid[7][0] = None  # On vide la case de départ de la tour
                    self.board.grid[7][3] = None  # On vide la case de départ du roi
                    self.board.grid[7][2] = Piece('white', ROOK_WHITE_IMG, "rook", 21, 7, 2,
                                                  0)  # On place la tour sur la case d'arrivée
                    self.board.grid[7][1] = Piece('white', KING_WHITE_IMG, "king", 5, 7, 3,
                                                  0)  # On place le roi sur la case d'arrivée
                    self.selected_piece = None  # On déselectionne la pièce
                if self.board.grid[7][7] is not None and self.board.grid[7][7].type == "rook" and self.board.grid[7][
                    7].color == "white" and piece.move == 0 and self.board.grid[7][6] is None and \
                        self.board.grid[7][5] is None and self.board.grid[row][
                    col].type == "rook":  # Si la tour n'a pas bougé et que les cases entre le roi et la tour sont vides
                    self.board.grid[7][7] = None  # On vide la case de départ de la tour
                    self.board.grid[7][3] = None  # On vide la case de départ du roi
                    self.board.grid[7][4] = Piece('white', ROOK_WHITE_IMG, "rook", 21, 7, 6,
                                                  0)  # On place la tour sur la case d'arrivée
                    self.board.grid[7][5] = Piece('white', KING_WHITE_IMG, "king", 5, 7, 5,
                                                  0)  # On place le roi sur la case d'arrivée
                    self.selected_piece = None  # On déselectionne la pièce
            if piece.type == "king" and piece.color == "black" and (
                    self.player.turn and self.player.color == "black") or (
                    self.player2.turn and self.player2.color == "black"):  # Si la pièce est un roi
                if self.board.grid[0][0] is not None and self.board.grid[0][0].type == "rook" and self.board.grid[0][
                    0].color == "black" and piece.move == 0 and self.board.grid[0][1] is None and \
                        self.board.grid[0][
                            2] is None:  # Si la tour n'a pas bougé et que les cases entre le roi et la tour sont vides
                    self.board.grid[0][0] = None  # On vide la case de départ de la tour
                    self.board.grid[0][3] = None  # On vide la case de départ du roi
                    self.board.grid[0][2] = Piece('black', ROOK_BLACK_IMG, "rook", 7, 0, 2,
                                                  0)  # On place la tour sur la case d'arrivée
                    self.board.grid[0][1] = Piece('black', KING_BLACK_IMG, "king", 23, 0, 3,
                                                  0)  # On place le roi sur la case d'arrivée
                    self.selected_piece = None  # On déselectionne la pièce
                if self.board.grid[0][7] is not None and self.board.grid[0][7].type == "rook" and self.board.grid[0][
                    7].color == "black" and piece.move == 0 and self.board.grid[0][6] is None and \
                        self.board.grid[0][
                            5] is None:  # Si la tour n'a pas bougé et que les cases entre le roi et la tour sont vides
                    self.board.grid[0][7] = None  # On vide la case de départ de la tour
                    self.board.grid[0][3] = None  # On vide la case de départ du roi
                    self.board.grid[0][4] = Piece('black', ROOK_BLACK_IMG, "rook", 7, 0, 6,
                                                  0)  # On place la tour sur la case d'arrivée
                    self.board.grid[0][5] = Piece('black', KING_BLACK_IMG, "king", 23, 0, 5,
                                                  0)  # On place le roi sur la case d'arrivée
                    self.selected_piece = None  # On déselectionne la pièce

    # Fonction qui permet de verifer et de faire le en passant pour les pions
    def en_passant(self, row, col):
        piece = self.board.grid[row][col]
        if piece is not None:
            if piece.type == "pawn":
                if col != 0 and col != 7:
                    if piece.color == "white":
                        if self.board.grid[row][col - 1] is not None:
                            if self.board.grid[row][col - 1].type == "pawn" and self.board.grid[row][
                                col - 1].color == "black":
                                if self.board.grid[row][col - 1].move == 1:
                                    self.board.grid[row][col - 1] = None
                                    self.board.grid[row - 1][col - 1] = piece
                                    self.board.grid[row][col] = None
                                    self.selected_piece = None
                        if self.board.grid[row][col + 1] is not None:
                            if self.board.grid[row][col + 1].type == "pawn" and self.board.grid[row][
                                col + 1].color == "black":
                                if self.board.grid[row][col + 1].move == 1:
                                    self.board.grid[row][col + 1] = None
                                    self.board.grid[row - 1][col + 1] = piece
                                    self.board.grid[row][col] = None
                                    self.selected_piece = None
                    else:
                        if self.board.grid[row][col - 1] is not None:
                            if self.board.grid[row][col - 1].type == "pawn" and self.board.grid[row][
                                col - 1].color == "white":
                                if self.board.grid[row][col - 1].move == 1:
                                    self.board.grid[row][col - 1] = None
                                    self.board.grid[row + 1][col - 1] = piece
                                    self.board.grid[row][col] = None
                                    self.selected_piece = None
                        if self.board.grid[row][col + 1] is not None:
                            if self.board.grid[row][col + 1].type == "pawn" and self.board.grid[row][
                                col + 1].color == "white":
                                if self.board.grid[row][col + 1].move == 1:
                                    self.board.grid[row][col + 1] = None
                                    self.board.grid[row + 1][col + 1] = piece
                                    self.board.grid[row][col] = None
                                    self.selected_piece = None
                elif col == 0:
                    if piece.color == "white":
                        if self.board.grid[row][col + 1] is not None:
                            if self.board.grid[row][col + 1].type == "pawn" and self.board.grid[row][
                                col + 1].color == "black":
                                if self.board.grid[row][col + 1].move == 1:
                                    self.board.grid[row][col + 1] = None
                                    self.board.grid[row - 1][col + 1] = piece
                                    self.board.grid[row][col] = None
                                    self.selected_piece = None
                    else:
                        if self.board.grid[row][col + 1] is not None:
                            if self.board.grid[row][col + 1].type == "pawn" and self.board.grid[row][
                                col + 1].color == "white":
                                if self.board.grid[row][col + 1].move == 1:
                                    self.board.grid[row][col + 1] = None
                                    self.board.grid[row - 1][col + 1] = piece
                                    self.board.grid[row][col] = None
                                    self.selected_piece = None
                else:
                    if piece.color == "white":
                        if self.board.grid[row][col - 1] is not None:
                            if self.board.grid[row][col - 1].type == "pawn" and self.board.grid[row][
                                col - 1].color == "black":
                                if self.board.grid[row][col - 1].move == 1:
                                    self.board.grid[row][col - 1] = None
                                    self.board.grid[row + 1][col - 1] = piece
                                    self.board.grid[row][col] = None
                                    self.selected_piece = None
                    else:
                        if self.board.grid[row][col - 1] is not None:
                            if self.board.grid[row][col - 1].type == "pawn" and self.board.grid[row][
                                col - 1].color == "white":
                                if self.board.grid[row][col - 1].move == 1:
                                    self.board.grid[row][col - 1] = None
                                    self.board.grid[row + 1][col - 1] = piece
                                    self.board.grid[row][col] = None
                                    self.selected_piece = None



    def pawn_promotion(self, row, col):
        piece = self.board.grid[row][col]
        if piece is not None:
            if piece.type == "pawn":
                if piece.color == "black":
                    if row == 7:
                        self.board.grid[row][col] = Piece('black', QUEEN_BLACK_IMG, "queen", 4, row, col,
                                                          piece.move + 1)
                else:
                    if row == 0:
                        self.board.grid[row][col] = Piece('white', QUEEN_WHITE_IMG, "queen", 20, row, col,
                                                          piece.move + 1)

    def highlight_moves_pawn(self, row,
                             col):  # Fonction qui permet de mettre en évidence les déplacements possibles d'un pion
        piece = self.board.grid[row][col]  # On récupère la pièce
        if piece is not None:  # Si la case n'est pas vide
            if piece.color == "black":  # Si la pièce est blanche
                if row == 1:  # Si le pion est sur sa ligne de départ
                    if self.board.grid[row + 1][col] is None:  # Si la case devant le pion est vide
                        self.draw_highlight(row + 1, col)  # On met en évidence la case
                        if self.board.grid[row + 2][col] is None:  # Si la case devant le pion est vide
                            self.draw_highlight(row + 2, col)  # On met en évidence la case
                else:  # Si le pion n'est pas sur sa ligne de départ
                    if self.board.grid[row + 1][col] is None:  # Si la case devant le pion est vide
                        self.draw_highlight(row + 1, col)  # On met en évidence la case
                if col > 0:  # Si le pion n'est pas sur la colonne de gauche
                    if self.board.grid[row + 1][col - 1] is not None and self.board.grid[row + 1][
                        col - 1].color != piece.color:  # Si la case devant le pion est occupée par une pièce adverse
                        self.draw_highlight(row + 1, col - 1)  # On met en évidence la case
                if col < 7:  # Si le pion n'est pas sur la colonne de droite
                    if self.board.grid[row + 1][col + 1] is not None and self.board.grid[row + 1][
                        col + 1].color != piece.color:  # Si la case devant le pion est occupée par une pièce adverse
                        self.draw_highlight(row + 1, col + 1)  # On met en évidence la case
            else:  # Si la pièce est blanche
                if row == 6:  # Si le pion est sur sa ligne de départ
                    if self.board.grid[row - 1][col] is None:  # Si la case devant le pion est vide
                        self.draw_highlight(row - 1, col)
                        if self.board.grid[row - 2][col] is None:  # Si la case devant le pion est vide
                            self.draw_highlight(row - 2, col)  # On met en évidence la case
                else:  # Si le pion n'est pas sur sa ligne de départ
                    if self.board.grid[row - 1][col] is None:  # Si la case devant le pion est vide
                        self.draw_highlight(row - 1, col)  # On met en évidence la case
                if col > 0:  # Si le pion n'est pas sur la colonne de gauche
                    if self.board.grid[row - 1][col - 1] is not None and self.board.grid[row - 1][
                        col - 1].color != piece.color:  # Si la case devant le pion est occupée par une pièce adverse
                        self.draw_highlight(row - 1, col - 1)  # On met en évidence la case
                if col < 7:  # Si le pion n'est pas sur la colonne de droite
                    if self.board.grid[row - 1][col + 1] is not None and self.board.grid[row - 1][
                        col + 1].color != piece.color:  # Si la case devant le pion est occupée par une pièce adverse
                        self.draw_highlight(row - 1, col + 1)  # On met en évidence la case

    def highlight_moves_rook(self, row,
                             col):  # Fonction qui permet de mettre en évidence les déplacements possibles d'une tour
        piece = self.board.grid[row][col]  # On récupère la pièce
        if piece is not None:  # Si la case n'est pas vide
            for i in range(1, 8):  # On parcourt les cases devant la tour
                if row + i < 8:  # Si la case est dans l'échiquier
                    if self.board.grid[row + i][col] is None:  # Si la case est vide
                        self.draw_highlight(row + i, col)  # On met en évidence la case
                    else:  # Si la case est occupée
                        if self.board.grid[row + i][col].color != piece.color:  # Si la pièce est adverse
                            self.draw_highlight(row + i, col)  # On met en évidence la case
                        break  # On arrête de parcourir les cases devant la tour
                else:  # Si la case n'est pas dans l'échiquier
                    break  # On arrête de parcourir les cases devant la tour
            for i in range(1, 8):  # On parcourt les cases derrière la tour
                if row - i >= 0:  # Si la case est dans l'échiquier

                    if self.board.grid[row - i][col] is None:  # Si la case est vide
                        self.draw_highlight(row - i, col)  # On met en évidence la case
                    else:  # Si la case est occupée
                        if self.board.grid[row - i][col].color != piece.color:  # Si la pièce est adverse
                            self.draw_highlight(row - i, col)  # On met en évidence la case
                        break  # On arrête de parcourir les cases derrière la tour
                else:  # Si la case n'est pas dans l'échiquier
                    break  # On arrête de parcourir les cases derrière la tour
            for i in range(1, 8):  # On parcourt les cases à droite de la tour
                if col + i < 8:  # Si la case est dans l'échiquier
                    if self.board.grid[row][col + i] is None:  # Si la case est vide
                        self.draw_highlight(row, col + i)  # On met en évidence la case

                    else:  # Si la case est occupée
                        if self.board.grid[row][col + i].color != piece.color:  # Si la pièce est adverse
                            self.draw_highlight(row, col + i)  # On met en évidence la case
                        break  # On arrête de parcourir les cases à droite de la tour
                else:  # Si la case n'est pas dans l'échiquier
                    break  # On arrête de parcourir les cases à droite de la tour
            for i in range(1, 8):  # On parcourt les cases à gauche de la tour
                if col - i >= 0:  # Si la case est dans l'échiquier
                    if self.board.grid[row][col - i] is None:  # Si la case est vide
                        self.draw_highlight(row, col - i)  # On met en évidence la case
                    else:  # Si la case est occupée
                        if self.board.grid[row][col - i].color != piece.color:  # Si la pièce est adverse
                            self.draw_highlight(row, col - i)  # On met en évidence la case
                        break  # On arrête de parcourir les cases à gauche de la tour
                else:  # Si la case n'est pas dans l'échiquier
                    break  # On arrête de parcourir les cases à gauche de la tour

    def highlight_moves_bishop(self, row,
                               col):  # Fonction qui permet de mettre en évidence les déplacements possibles d'un fou
        piece = self.board.grid[row][col]  # On récupère la pièce
        if piece is not None:  # Si la case n'est pas vide
            for i in range(1, 8):  # On parcourt les cases en haut à droite du fou
                if row + i < 8 and col + i < 8:  # Si la case est dans l'échiquier
                    if self.board.grid[row + i][col + i] is None:  # Si la case est vide
                        self.draw_highlight(row + i, col + i)  # On met en évidence la case
                    else:  # Si la case est occupée
                        if self.board.grid[row + i][col + i].color != piece.color:  # Si la pièce est adverse
                            self.draw_highlight(row + i, col + i)  # On met en évidence la case
                        break  # On arrête de parcourir les cases en haut à droite du fou
                else:  # Si la case n'est pas dans l'échiquier
                    break  # On arrête de parcourir les cases en haut à droite du fou
            for i in range(1, 8):  # On parcourt les cases en haut à gauche du fou
                if row + i < 8 and col - i >= 0:  # Si la case est dans l'échiquier
                    if self.board.grid[row + i][col - i] is None:  # Si la case est vide
                        self.draw_highlight(row + i, col - i)  # On met en évidence la case
                    else:  # Si la case est occupée
                        if self.board.grid[row + i][col - i].color != piece.color:  # Si la pièce est adverse
                            self.draw_highlight(row + i, col - i)  # On met en évidence la case
                        break  # On arrête de parcourir les cases en haut à gauche du fou
                else:  # Si la case n'est pas dans l'échiquier
                    break  # On arrête de parcourir les cases en haut à gauche du fou
            for i in range(1, 8):  # On parcourt les cases en bas à droite du fou
                if row - i >= 0 and col + i < 8:  # Si la case est dans l'échiquier
                    if self.board.grid[row - i][col + i] is None:  # Si la case est vide
                        self.draw_highlight(row - i, col + i)  # On met en évidence la case
                    else:  # Si la case est occupée
                        if self.board.grid[row - i][col + i].color != piece.color:  # Si la pièce est adverse
                            self.draw_highlight(row - i, col + i)  # On met en évidence la case
                        break  # On arrête de parcourir les cases en bas à droite du fou
                else:  # Si la case n'est pas dans l'échiquier
                    break  # On arrête de parcourir les cases en bas à droite du fou
            for i in range(1, 8):  # On parcourt les cases en bas à gauche du fou
                if row - i >= 0 and col - i >= 0:  # Si la case est dans l'échiquier
                    if self.board.grid[row - i][col - i] is None:  # Si la case est vide
                        self.draw_highlight(row - i, col - i)  # On met en évidence la case
                    else:  # Si la case est occupée
                        if self.board.grid[row - i][col - i].color != piece.color:  # Si la pièce est adverse
                            self.draw_highlight(row - i, col - i)  # On met en évidence la case
                        break  # On arrête de parcourir les cases en bas à gauche du fou
                else:  # Si la case n'est pas dans l'échiquier
                    break  # On arrête de parcourir les cases en bas à gauche du fou

    def highlight_moves_knight(self, row,
                               col):  # Fonction qui permet de mettre en évidence les déplacements possibles d'un cavalier
        piece = self.board.grid[row][col]  # On récupère la pièce
        if piece is not None:  # Si la case n'est pas vide
            for i in range(-2, 3):  # On parcourt les cases autour du cavalier
                for j in range(-2, 3):  # On parcourt les cases autour du cavalier
                    if abs(i) + abs(j) == 3:  # Si la case est à 3 cases du cavalier
                        if row + i >= 0 and row + i < 8 and col + j >= 0 and col + j < 8:  # Si la case est dans l'échiquier
                            if self.board.grid[row + i][col + j] is None:  # Si la case est vide
                                self.draw_highlight(row + i, col + j)  # On met en évidence la case
                            else:  # Si la case est occupée
                                if self.board.grid[row + i][col + j].color != piece.color:  # Si la pièce est adverse
                                    self.draw_highlight(row + i, col + j)  # On met en évidence la case

    def highlight_moves_queen(self, row,
                              col):  # Fonction qui permet de mettre en évidence les déplacements possibles d'une reine
        self.highlight_moves_rook(row, col)  # On met en évidence les déplacements possibles de la tour
        self.highlight_moves_bishop(row, col)  # On met en évidence les déplacements possibles du fou

    def highlight_moves_king(self, row,
                             col):  # Fonction qui permet de mettre en évidence les déplacements possibles d'un roi
        piece = self.board.grid[row][col]  # On récupère la pièce
        if piece is not None:  # Si la case n'est pas vide
            for i in range(-1, 2):  # On parcourt les cases autour du roi
                for j in range(-1, 2):  # On parcourt les cases autour du roi
                    if row + i >= 0 and row + i < 8 and col + j >= 0 and col + j < 8:  # Si la case est dans l'échiquier
                        if self.board.grid[row + i][col + j] is None:  # Si la case est vide
                            self.draw_highlight(row + i, col + j)

                        else:
                            if self.board.grid[row + i][col + j].color != piece.color:
                                self.draw_highlight(row + i, col + j)

    def draw_highlight(self, row, col):
        pygame.draw.rect(self.screen, BROWN,
                         (col * GRID_SIZE + 16, row * GRID_SIZE + 16, GRID_SIZE % 32, GRID_SIZE % 32))
        pygame.display.update()
        pygame.display.update(updated_rects)  # On met à jour l'affichage



    def move(self, row, col):  # Fonction qui permet de déplacer une pièce
        if self.selected_piece is not None:  # Si une pièce est sélectionnée
            piece_row, piece_col = self.selected_piece  # On récupère les coordonnées de la pièce
            piece = self.board.grid[piece_row][piece_col]  # On récupère la pièce
            if piece.type == "pawn" and (row != piece_row or col != piece_col):  # Si la pièce est un pion
                self.pawn_move(row, col)  # On appelle la fonction qui permet de déplacer un pion
                self.turn()  # On change de joueur
            elif piece.type == "rook" and (row != piece_row or col != piece_col):  # Si la pièce est une tour
                self.rook_move(row, col)  # On appelle la fonction qui permet de déplacer une tour
                self.turn()
            elif piece.type == "knight" and (row != piece_row or col != piece_col):  # Si la pièce est un cavalier
                self.knight_move(row, col)  # On appelle la fonction qui permet de déplacer un cavalier
                self.turn()
            elif piece.type == "bishop" and (row != piece_row or col != piece_col):  # Si la pièce est un fou
                self.bishop_move(row, col)  # On appelle la fonction qui permet de déplacer un fou
                self.turn()
            elif piece.type == "queen" and (row != piece_row or col != piece_col):  # Si la pièce est une reine
                self.queen_move(row, col)  # On appelle la fonction qui permet de déplacer une reine
                self.turn()
            elif piece.type == "king" and (row != piece_row or col != piece_col):  # Si la pièce est un roi
                self.king_move(row, col)  # On appelle la fonction qui permet de déplacer un roi
                self.turn()
            self.selected_piece = None  # On déselectionne la pièce


        else:  # Si aucune pièce n'est sélectionnée
            if self.board.grid[row][col] is not None and self.board.grid[row][
                col].color == "white":  # Si la case sélectionnée contient une pièce blanche
                piece = self.board.grid[row][col]  # On récupère la pièce
                if self.selected_piece is None:
                    if piece is not None:  # Si la pièce n'est pas vide
                        if self.player.color == piece.color:
                            self.selected_piece = (row, col)  # On sélectionne la pièce
                        elif self.player2.color == piece.color:
                            self.selected_piece = (row, col)



    def update(self):  # Fonction qui permet de mettre à jour le jeu
        self.board.draw(self.screen)  # On dessine le plateau de jeu

    def get_tab_piece(self):
        tab = []
        for row in range(8):
            for col in range(8):
                if self.board.grid[row][col] is not None:
                    tab.append(self.board.grid[row][col])
        return tab

    def get_moves(self, row, col):
        piece = self.board.grid[row][col]
        if piece is not None:
            if piece.type == "pawn":
                return self.pawn_moves(row, col)
            elif piece.type == "rook":
                return self.rook_moves(row, col)
            elif piece.type == "knight":
                return self.knight_moves(row, col)
            elif piece.type == "bishop":
                return self.bishop_moves(row, col)
            elif piece.type == "queen":
                return self.queen_moves(row, col)
            elif piece.type == "king":
                return self.king_moves(row, col)

    def pawn_moves(self, row, col):
        moves = []
        piece = self.board.grid[row][col]
        if piece.color == "white":
            if row - 1 >= 0:
                if self.board.grid[row - 1][col] is None:
                    moves.append((row - 1, col))
                    if row == 6:
                        if self.board.grid[row - 2][col] is None:
                            moves.append((row - 2, col))
                if col - 1 >= 0:
                    if self.board.grid[row - 1][col - 1] is not None:
                        if self.board.grid[row - 1][col - 1].color == "black":
                            moves.append((row - 1, col - 1))
                if col + 1 < 8:
                    if self.board.grid[row - 1][col + 1] is not None:
                        if self.board.grid[row - 1][col + 1].color == "black":
                            moves.append((row - 1, col + 1))
        else:
            if row + 1 < 8:
                if self.board.grid[row + 1][col] is None:
                    moves.append((row + 1, col))
                    if row == 1:
                        if self.board.grid[row + 2][col] is None:
                            moves.append((row + 2, col))
                if col - 1 >= 0:
                    if self.board.grid[row + 1][col - 1] is not None:
                        if self.board.grid[row + 1][col - 1].color == "white":
                            moves.append((row + 1, col - 1))
                if col + 1 < 8:
                    if self.board.grid[row + 1][col + 1] is not None:
                        if self.board.grid[row + 1][col + 1].color == "white":
                            moves.append((row + 1, col + 1))
        return moves

    def rook_moves(self, row, col):
        moves = []
        piece = self.board.grid[row][col]
        if piece.color == "white":
            for i in range(row - 1, -1, -1):
                if self.board.grid[i][col] is None:
                    moves.append((i, col))
                else:
                    if self.board.grid[i][col].color == "black":
                        moves.append((i, col))
                    break
            for i in range(row + 1, 8):
                if self.board.grid[i][col] is None:
                    moves.append((i, col))
                else:
                    if self.board.grid[i][col].color == "black":
                        moves.append((i, col))
                    break
            for i in range(col - 1, -1, -1):
                if self.board.grid[row][i] is None:
                    moves.append((row, i))
                else:
                    if self.board.grid[row][i].color == "black":
                        moves.append((row, i))
                    break
            for i in range(col + 1, 8):
                if self.board.grid[row][i] is None:
                    moves.append((row, i))
                else:
                    if self.board.grid[row][i].color == "black":
                        moves.append((row, i))
                    break
        else:
            for i in range(row - 1, -1, -1):
                if self.board.grid[i][col] is None:
                    moves.append((i, col))
                else:
                    if self.board.grid[i][col].color == "white":
                        moves.append((i, col))
                    break
            for i in range(row + 1, 8):
                if self.board.grid[i][col] is None:
                    moves.append((i, col))
                else:
                    if self.board.grid[i][col].color == "white":
                        moves.append((i, col))
                    break
            for i in range(col - 1, -1, -1):
                if self.board.grid[row][i] is None:
                    moves.append((row, i))
                else:
                    if self.board.grid[row][i].color == "white":
                        moves.append((row, i))
                    break
            for i in range(col + 1, 8):
                if self.board.grid[row][i] is None:
                    moves.append((row, i))
                else:
                    if self.board.grid[row][i].color == "white":
                        moves.append((row, i))
                    break
        return moves

    def knight_moves(self, row, col):
        moves = []
        piece = self.board.grid[row][col]
        if piece.color == "white":
            if row - 2 >= 0:
                if col - 1 >= 0:
                    if self.board.grid[row - 2][col - 1] is None:
                        moves.append((row - 2, col - 1))
                    else:
                        if self.board.grid[row - 2][col - 1].color == "black":
                            moves.append((row - 2, col - 1))
                if col + 1 < 8:
                    if self.board.grid[row - 2][col + 1] is None:
                        moves.append((row - 2, col + 1))
                    else:
                        if self.board.grid[row - 2][col + 1].color == "black":
                            moves.append((row - 2, col + 1))
            if row + 2 < 8:
                if col - 1 >= 0:
                    if self.board.grid[row + 2][col - 1] is None:
                        moves.append((row + 2, col - 1))
                    else:
                        if self.board.grid[row + 2][col - 1].color == "black":
                            moves.append((row + 2, col - 1))
                if col + 1 < 8:
                    if self.board.grid[row + 2][col + 1] is None:
                        moves.append((row + 2, col + 1))
                    else:
                        if self.board.grid[row + 2][col + 1].color == "black":
                            moves.append((row + 2, col + 1))
            if col - 2 >= 0:
                if row - 1 >= 0:
                    if self.board.grid[row - 1][col - 2] is None:
                        moves.append((row - 1, col - 2))
                    else:
                        if self.board.grid[row - 1][col - 2].color == "black":
                            moves.append((row - 1, col - 2))
                if row + 1 < 8:
                    if self.board.grid[row + 1][col - 2] is None:
                        moves.append((row + 1, col - 2))
                    else:
                        if self.board.grid[row + 1][col - 2].color == "black":
                            moves.append((row + 1, col - 2))
            if col + 2 < 8:
                if row - 1 >= 0:
                    if self.board.grid[row - 1][col + 2] is None:
                        moves.append((row - 1, col + 2))
                    else:
                        if self.board.grid[row - 1][col + 2].color == "black":
                            moves.append((row - 1, col + 2))
                if row + 1 < 8:
                    if self.board.grid[row + 1][col + 2] is None:
                        moves.append((row + 1, col + 2))
                    else:
                        if self.board.grid[row + 1][col + 2].color == "black":
                            moves.append((row + 1, col + 2))
        else:
            if row - 2 >= 0:
                if col - 1 >= 0:
                    if self.board.grid[row - 2][col - 1] is None:
                        moves.append((row - 2, col - 1))
                    else:
                        if self.board.grid[row - 2][col - 1].color == "white":
                            moves.append((row - 2, col - 1))
                if col + 1 < 8:
                    if self.board.grid[row - 2][col + 1] is None:
                        moves.append((row - 2, col + 1))
                    else:
                        if self.board.grid[row - 2][col + 1].color == "white":
                            moves.append((row - 2, col + 1))
            if row + 2 < 8:
                if col - 1 >= 0:
                    if self.board.grid[row + 2][col - 1] is None:
                        moves.append((row + 2, col - 1))
                    else:
                        if self.board.grid[row + 2][col - 1].color == "white":
                            moves.append((row + 2, col - 1))
                if col + 1 < 8:
                    if self.board.grid[row + 2][col + 1] is None:
                        moves.append((row + 2, col + 1))
                    else:
                        if self.board.grid[row + 2][col + 1].color == "white":
                            moves.append((row + 2, col + 1))
            if col - 2 >= 0:
                if row - 1 >= 0:
                    if self.board.grid[row - 1][col - 2] is None:
                        moves.append((row - 1, col - 2))
                    else:
                        if self.board.grid[row - 1][col - 2].color == "white":
                            moves.append((row - 1, col - 2))
                if row + 1 < 8:
                    if self.board.grid[row + 1][col - 2] is None:
                        moves.append((row + 1, col - 2))
                    else:
                        if self.board.grid[row + 1][col - 2].color == "white":
                            moves.append((row + 1, col - 2))
            if col + 2 < 8:
                if row - 1 >= 0:
                    if self.board.grid[row - 1][col + 2] is None:
                        moves.append((row - 1, col + 2))
                    else:
                        if self.board.grid[row - 1][col + 2].color == "white":
                            moves.append((row - 1, col + 2))
                if row + 1 < 8:
                    if self.board.grid[row + 1][col + 2] is None:
                        moves.append((row + 1, col + 2))
                    else:
                        if self.board.grid[row + 1][col + 2].color == "white":
                            moves.append((row + 1, col + 2))
        return moves

    def bishop_moves(self, row, col):
        moves = []
        piece = self.board.grid[row][col]
        if piece.color == "white":
            # Diagonale Haut Gauche
            i = 1
            while row - i >= 0 and col - i >= 0:
                if self.board.grid[row - i][col - i] is None:
                    moves.append((row - i, col - i))
                else:
                    if self.board.grid[row - i][col - i].color == "black":
                        moves.append((row - i, col - i))
                    break
                i += 1
            # Diagonale Haut Droite
            i = 1
            while row - i >= 0 and col + i < 8:
                if self.board.grid[row - i][col + i] is None:
                    moves.append((row - i, col + i))
                else:
                    if self.board.grid[row - i][col + i].color == "black":
                        moves.append((row - i, col + i))
                    break
                i += 1
            # Diagonale Bas Gauche
            i = 1
            while row + i < 8 and col - i >= 0:
                if self.board.grid[row + i][col - i] is None:
                    moves.append((row + i, col - i))
                else:
                    if self.board.grid[row + i][col - i].color == "black":
                        moves.append((row + i, col - i))
                    break
                i += 1
            # Diagonale Bas Droite
            i = 1
            while row + i < 8 and col + i < 8:
                if self.board.grid[row + i][col + i] is None:
                    moves.append((row + i, col + i))
                else:
                    if self.board.grid[row + i][col + i].color == "black":
                        moves.append((row + i, col + i))
                    break
                i += 1
        else:
            # Diagonale Haut Gauche
            i = 1
            while row - i >= 0 and col - i >= 0:
                if self.board.grid[row - i][col - i] is None:
                    moves.append((row - i, col - i))
                else:
                    if self.board.grid[row - i][col - i].color == "white":
                        moves.append((row - i, col - i))
                    break
                i += 1
            # Diagonale Haut Droite
            i = 1
            while row - i >= 0 and col + i < 8:
                if self.board.grid[row - i][col + i] is None:
                    moves.append((row - i, col + i))
                else:
                    if self.board.grid[row - i][col + i].color == "white":
                        moves.append((row - i, col + i))
                    break
                i += 1
            # Diagonale Bas Gauche
            i = 1
            while row + i < 8 and col - i >= 0:
                if self.board.grid[row + i][col - i] is None:
                    moves.append((row + i, col - i))
                else:
                    if self.board.grid[row + i][col - i].color == "white":
                        moves.append((row + i, col - i))
                    break
                i += 1
            # Diagonale Bas Droite
            i = 1
            while row + i < 8 and col + i < 8:
                if self.board.grid[row + i][col + i] is None:
                    moves.append((row + i, col + i))
                else:
                    if self.board.grid[row + i][col + i].color == "white":
                        moves.append((row + i, col + i))
                    break
                i += 1
        return moves

    def queen_moves(self, row, col):
        moves = []
        piece = self.board.grid[row][col]
        if piece.color == "white":
            # Diagonale Haut Gauche
            i = 1
            while row - i >= 0 and col - i >= 0:
                if self.board.grid[row - i][col - i] is None:
                    moves.append((row - i, col - i))
                else:
                    if self.board.grid[row - i][col - i].color == "black":
                        moves.append((row - i, col - i))
                    break
                i += 1
            # Diagonale Haut Droite
            i = 1
            while row - i >= 0 and col + i < 8:
                if self.board.grid[row - i][col + i] is None:
                    moves.append((row - i, col + i))
                else:
                    if self.board.grid[row - i][col + i].color == "black":
                        moves.append((row - i, col + i))
                    break
                i += 1
            # Diagonale Bas Gauche
            i = 1
            while row + i < 8 and col - i >= 0:
                if self.board.grid[row + i][col - i] is None:
                    moves.append((row + i, col - i))
                else:
                    if self.board.grid[row + i][col - i].color == "black":
                        moves.append((row + i, col - i))
                    break
                i += 1
            # Diagonale Bas Droite
            i = 1
            while row + i < 8 and col + i < 8:
                if self.board.grid[row + i][col + i] is None:
                    moves.append((row + i, col + i))
                else:
                    if self.board.grid[row + i][col + i].color == "black":
                        moves.append((row + i, col + i))
                    break
                i += 1
            # Haut
            i = 1
            while row - i >= 0:
                if self.board.grid[row - i][col] is None:
                    moves.append((row - i, col))
                else:
                    if self.board.grid[row - i][col].color == "black":
                        moves.append((row - i, col))
                    break
                i += 1
            # Bas
            i = 1
            while row + i < 8:
                if self.board.grid[row + i][col] is None:
                    moves.append((row + i, col))
                else:
                    if self.board.grid[row + i][col].color == "black":
                        moves.append((row + i, col))
                    break
                i += 1
            # Gauche
            i = 1
            while col - i >= 0:
                if self.board.grid[row][col - i] is None:
                    moves.append((row, col - i))
                else:
                    if self.board.grid[row][col - i].color == "black":
                        moves.append((row, col - i))
                    break
                i += 1
            # Droite
            i = 1
            while col + i < 8:
                if self.board.grid[row][col + i] is None:
                    moves.append((row, col + i))
                else:
                    if self.board.grid[row][col + i].color == "black":
                        moves.append((row, col + i))
                    break
                i += 1
        else:
            # Diagonale Haut Gauche
            i = 1
            while row - i >= 0 and col - i >= 0:
                if self.board.grid[row - i][col - i] is None:
                    moves.append((row - i, col - i))
                else:
                    if self.board.grid[row - i][col - i].color == "white":
                        moves.append((row - i, col - i))
                    break
                i += 1
            # Diagonale Haut Droite
            i = 1
            while row - i >= 0 and col + i < 8:
                if self.board.grid[row - i][col + i] is None:
                    moves.append((row - i, col + i))
                else:
                    if self.board.grid[row - i][col + i].color == "white":
                        moves.append((row - i, col + i))
                    break
                i += 1
            # Diagonale Bas Gauche
            i = 1
            while row + i < 8 and col - i >= 0:
                if self.board.grid[row + i][col - i] is None:
                    moves.append((row + i, col - i))
                else:
                    if self.board.grid[row + i][col - i].color == "white":
                        moves.append((row + i, col - i))
                    break
                i += 1
            # Diagonale Bas Droite
            i = 1
            while row + i < 8 and col + i < 8:
                if self.board.grid[row + i][col + i] is None:
                    moves.append((row + i, col + i))
                else:
                    if self.board.grid[row + i][col + i].color == "white":
                        moves.append((row + i, col + i))
                    break
                i += 1
            # Haut
            i = 1
            while row - i >= 0:
                if self.board.grid[row - i][col] is None:
                    moves.append((row - i, col))
                else:
                    if self.board.grid[row - i][col].color == "white":
                        moves.append((row - i, col))
                    break
                i += 1
            # Bas
            i = 1
            while row + i < 8:
                if self.board.grid[row + i][col] is None:
                    moves.append((row + i, col))
                else:
                    if self.board.grid[row + i][col].color == "white":
                        moves.append((row + i, col))
                    break
                i += 1
            # Gauche
            i = 1
            while col - i >= 0:
                if self.board.grid[row][col - i] is None:
                    moves.append((row, col - i))
                else:
                    if self.board.grid[row][col - i].color == "white":
                        moves.append((row, col - i))
                    break
                i += 1
            # Droite
            i = 1
            while col + i < 8:
                if self.board.grid[row][col + i] is None:
                    moves.append((row, col + i))
                else:
                    if self.board.grid[row][col + i].color == "white":
                        moves.append((row, col + i))
                    break
                i += 1
        return moves

    def king_moves(self, row, col):
        moves = []
        piece = self.board.grid[row][col]
        if piece.color == "black":
            # Haut
            if row - 1 >= 0:
                if self.board.grid[row - 1][col] is None:
                    moves.append((row - 1, col))
                else:
                    if self.board.grid[row - 1][col].color == "white":
                        moves.append((row - 1, col))
            # Bas
            if row + 1 < 8:
                if self.board.grid[row + 1][col] is None:
                    moves.append((row + 1, col))
                else:
                    if self.board.grid[row + 1][col].color == "white":
                        moves.append((row + 1, col))
            # Gauche
            if col - 1 >= 0:
                if self.board.grid[row][col - 1] is None:
                    moves.append((row, col - 1))
                else:
                    if self.board.grid[row][col - 1].color == "white":
                        moves.append((row, col - 1))
            # Droite
            if col + 1 < 8:
                if self.board.grid[row][col + 1] is None:
                    moves.append((row, col + 1))
                else:
                    if self.board.grid[row][col + 1].color == "white":
                        moves.append((row, col + 1))
            # Diagonale Haut Gauche
            if row - 1 >= 0 and col - 1 >= 0:
                if self.board.grid[row - 1][col - 1] is None:
                    moves.append((row - 1, col - 1))
                else:
                    if self.board.grid[row - 1][col - 1].color == "white":
                        moves.append((row - 1, col - 1))
            # Diagonale Haut Droite
            if row - 1 >= 0 and col + 1 < 8:
                if self.board.grid[row - 1][col + 1] is None:
                    moves.append((row - 1, col + 1))
                else:
                    if self.board.grid[row - 1][col + 1].color == "white":
                        moves.append((row - 1, col + 1))
            # Diagonale Bas Gauche
            if row + 1 < 8 and col - 1 >= 0:
                if self.board.grid[row + 1][col - 1] is None:
                    moves.append((row + 1, col - 1))
                else:
                    if self.board.grid[row + 1][col - 1].color == "white":
                        moves.append((row + 1, col - 1))
            # Diagonale Bas Droite
            if row + 1 < 8 and col + 1 < 8:
                if self.board.grid[row + 1][col + 1] is None:
                    moves.append((row + 1, col + 1))
                else:
                    if self.board.grid[row + 1][col + 1].color == "white":
                        moves.append((row + 1, col + 1))
        else:
            # Haut
            if row - 1 >= 0:
                if self.board.grid[row - 1][col] is None:
                    moves.append((row - 1, col))
                else:
                    if self.board.grid[row - 1][col].color == "black":
                        moves.append((row - 1, col))
            # Bas
            if row + 1 < 8:
                if self.board.grid[row + 1][col] is None:
                    moves.append((row + 1, col))
                else:
                    if self.board.grid[row + 1][col].color == "black":
                        moves.append((row + 1, col))
            # Gauche
            if col - 1 >= 0:
                if self.board.grid[row][col - 1] is None:
                    moves.append((row, col - 1))
                else:
                    if self.board.grid[row][col - 1].color == "black":
                        moves.append((row, col - 1))
            # Droite
            if col + 1 < 8:
                if self.board.grid[row][col + 1] is None:
                    moves.append((row, col + 1))
                else:
                    if self.board.grid[row][col + 1].color == "black":
                        moves.append((row, col + 1))
            # Diagonale Haut Gauche
            if row - 1 >= 0 and col - 1 >= 0:
                if self.board.grid[row - 1][col - 1] is None:
                    moves.append((row - 1, col - 1))
                else:
                    if self.board.grid[row - 1][col - 1].color == "black":
                        moves.append((row - 1, col - 1))
            # Diagonale Haut Droite
            if row - 1 >= 0 and col + 1 < 8:
                if self.board.grid[row - 1][col + 1] is None:
                    moves.append((row - 1, col + 1))
                else:
                    if self.board.grid[row - 1][col + 1].color == "black":
                        moves.append((row - 1, col + 1))
            # Diagonale Bas Gauche
            if row + 1 < 8 and col - 1 >= 0:
                if self.board.grid[row + 1][col - 1] is None:
                    moves.append((row + 1, col - 1))
                else:
                    if self.board.grid[row + 1][col - 1].color == "black":
                        moves.append((row + 1, col - 1))
            # Diagonale Bas Droite
            if row + 1 < 8 and col + 1 < 8:
                if self.board.grid[row + 1][col + 1] is None:
                    moves.append((row + 1, col + 1))
                else:
                    if self.board.grid[row + 1][col + 1].color == "black":
                        moves.append((row + 1, col + 1))
        return moves

    # Crée une fonction check qui verfie d'apres les regles d'echeques si le roi est en echec
    def checkb(self, row, col):
        # On récupère la position du roi
        king_posb = (row, col)
        # On récupère la liste des pièces adverses
        tab = self.get_tab_piece()
        # On parcourt la liste des pièces adverses

        for row in range(8):
            for col in range(8):
                piece = self.get_piece(row, col)
                if piece is not None:
                    if piece.color == "white":
                        moves = self.get_moves(row, col)
                        if moves is not None:
                            for move in moves:
                                if move == king_posb:
                                    print("Echec")
                                    return True
        return False

    def checkw(self, row, col):
        # On récupère la position du roi
        king_posw = (row, col)
        # On récupère la liste des pièces adverses
        tab = self.get_tab_piece()
        # On parcourt la liste des pièces adverses

        for row in range(8):
            for col in range(8):
                piece = self.get_piece(row, col)
                if piece is not None:
                    if piece.color == "black":
                        moves = self.get_moves(row, col)
                        if moves is not None:
                            for move in moves:
                                if move == king_posw:
                                    print("Echec")
                                    return True
        return False
    # Fonction qui vérifie si le roi est en échec et mat en vérifiant que toute les cases autour du roi sont
    # soit bloquer par le plateau soit par les pieces de la meme ou alors que il soit dans la trajectoire de
    # déplacement d'une piece adverse et c'est le cas renvoyer true
    """def checkmate(self):
        king_posb = self.get_piece_position(5)
        king_posw = self.get_piece_position(21)
        tab = self.get_tab_piece()
        if self.checkb(king_posb[0], king_posb[1]):
            if (self.player.color == "black" and self.player.turn == 1) or (self.player2.color == "black" and self.player2.turn == 1):
                if king_posb[0] + 1 < 8:
                    if self.board.grid[king_posb[0] + 1][king_posb[1]] is None and self.checkb(king_posb[0] + 1, king_posb[1]) is False:
                        for row in range(8):
                            for col in range(8):
                                piece = self.get_piece(row, col)
                                if piece is not None:
                                    if piece.color == "black":
                                        moves = self.get_moves(row, col)
                                        if moves is not None:
                                            for move in moves:
                                                for i in range(8 - king_posb[0]):
                                                    if move == (king_posb[0] + i, king_posb[1]):
                                                        print("aa")
                                                        print(move)
                                                        return False
                        return False
                    if self.board.grid[king_posb[0] + 1][king_posb[1]] is not None:
                        if self.board.grid[king_posb[0] + 1][king_posb[1]].color == "white" and self.checkb(king_posb[0] + 1, king_posb[1]) is False:
                            return False
                if king_posb[0] - 1 >= 0:
                    if self.board.grid[king_posb[0] - 1][king_posb[1]] is None and self.checkb(king_posb[0] - 1, king_posb[1]) is False:
                        for row in range(8):
                            for col in range(8):
                                piece = self.get_piece(row, col)
                                if piece is not None:
                                    if piece.color == "black":
                                        moves = self.get_moves(row, col)
                                        if moves is not None:
                                            for move in moves:
                                                for i in range(8-king_posb[0]):
                                                    if move == (king_posb[0] - i, king_posb[1]):
                                                        print("bb")
                                                        return False
                        return False
                    if self.board.grid[king_posb[0] - 1][king_posb[1]] is not None:
                        if self.board.grid[king_posb[0] - 1][king_posb[1]].color == "white" and self.checkb(king_posb[0] - 1, king_posb[1]) is False:
                            return False
                if king_posb[1] + 1 < 8:
                    if self.board.grid[king_posb[0]][king_posb[1] + 1] is None and self.checkb(king_posb[0], king_posb[1] + 1) is False:
                        return False
                    if self.board.grid[king_posb[0]][king_posb[1] + 1] is not None:
                        if self.board.grid[king_posb[0]][king_posb[1] + 1].color == "white" and self.checkb(king_posb[0], king_posb[1] + 1) is False:
                            return False
                if king_posb[1] - 1 >= 0:
                    if self.board.grid[king_posb[0]][king_posb[1] - 1] is None and self.checkb(king_posb[0], king_posb[1] - 1) is False:
                        return False
                    if self.board.grid[king_posb[0]][king_posb[1] - 1] is not None:
                        if self.board.grid[king_posb[0]][king_posb[1] - 1].color == "white" and self.checkb(king_posb[0], king_posb[1] - 1) is False:
                            return False
                if king_posb[0] + 1 < 8 and king_posb[1] + 1 < 8:
                    if self.board.grid[king_posb[0] + 1][king_posb[1] + 1] is None and self.checkb(king_posb[0] + 1, king_posb[1] + 1) is False:
                        return False
                    if self.board.grid[king_posb[0] + 1][king_posb[1] + 1] is not None:
                        if self.board.grid[king_posb[0] + 1][king_posb[1] + 1].color == "white" and self.checkb(king_posb[0] + 1, king_posb[1] + 1) is False:
                            return False
                if king_posb[0] - 1 >= 0 and king_posb[1] + 1 < 8:
                    if self.board.grid[king_posb[0] - 1][king_posb[1] + 1] is None and self.checkb(king_posb[0] - 1, king_posb[1] + 1) is False:
                        return False
                    if self.board.grid[king_posb[0] - 1][king_posb[1] + 1] is not None:
                        if self.board.grid[king_posb[0] - 1][king_posb[1] + 1].color == "white" and self.checkb(king_posb[0] - 1, king_posb[1] + 1) is False:
                            return False
                if king_posb[0] + 1 < 8 and king_posb[1] - 1 >= 0:
                    if self.board.grid[king_posb[0] + 1][king_posb[1] - 1] is None and self.checkb(king_posb[0] + 1, king_posb[1] - 1) is False:
                        return False
                    if self.board.grid[king_posb[0] + 1][king_posb[1] - 1] is not None:
                        if self.board.grid[king_posb[0] + 1][king_posb[1] - 1].color == "white" and self.checkb(king_posb[0] + 1, king_posb[1] - 1) is False:
                            return False
                if king_posb[0] - 1 >= 0 and king_posb[1] - 1 >= 0:
                    if self.board.grid[king_posb[0] - 1][king_posb[1] - 1] is None and self.checkb(king_posb[0] - 1, king_posb[1] - 1) is False:
                        return False
                    if self.board.grid[king_posb[0] - 1][king_posb[1] - 1] is not None:
                        if self.board.grid[king_posb[0] - 1][king_posb[1] - 1].color == "white" and self.checkb(king_posb[0] - 1, king_posb[1] - 1) is False:
                            return False
                for piece in tab:
                    if piece.color == "white":
                        moves = self.get_moves(piece.row, piece.col)
                        if moves is not None:
                            for move in moves:
                                if move == king_posb:
                                    return False
                print("Echec et mat")
                return True
        if self.checkw(king_posw[0], king_posw[1]):
            if (self.player.color == "white" and self.player.turn == 1) or (self.player2.color == "white" and self.player2.turn == 1):
                if king_posw[0] + 1 < 8:
                    if self.board.grid[king_posw[0] + 1][king_posw[1]] is None and self.checkw(king_posw[0] + 1, king_posw[1]) is True:
                        return False
                    if self.board.grid[king_posw[0] + 1][king_posw[1]].color == "black":
                        return False
                if king_posw[0] - 1 >= 0:
                    if self.board.grid[king_posw[0] - 1][king_posw[1]] is None and self.checkw(king_posw[0] - 1, king_posw[1]) is True:
                        return False
                    if self.board.grid[king_posw[0] - 1][king_posw[1]].color == "black":
                        return False
                if king_posw[1] + 1 < 8:
                    if self.board.grid[king_posw[0]][king_posw[1] + 1] is None and self.checkw(king_posw[0], king_posw[1] + 1) is True:
                        return False
                    if self.board.grid[king_posw[0]][king_posw[1] + 1].color == "black":
                        return False
                if king_posw[1] - 1 >= 0:
                    if self.board.grid[king_posw[0]][king_posw[1] - 1] is None and self.checkw(king_posw[0], king_posw[1] - 1) is True:
                        return False
                    if self.board.grid[king_posw[0]][king_posw[1] - 1].color == "black":
                        return False
                if king_posw[0] + 1 < 8 and king_posw[1] + 1 < 8:
                    if self.board.grid[king_posw[0] + 1][king_posw[1] + 1] is None and self.checkw(king_posw[0] + 1, king_posw[1] + 1) is True:
                        return False
                    if self.board.grid[king_posw[0] + 1][king_posw[1] + 1].color == "black":
                        return False
                if king_posw[0] - 1 >= 0 and king_posw[1] + 1 < 8:
                    if self.board.grid[king_posw[0] - 1][king_posw[1] + 1] is None and self.checkw(king_posw[0] - 1, king_posw[1] + 1) is True:
                        return False
                    if self.board.grid[king_posw[0] - 1][king_posw[1] + 1].color == "black":
                        return False
                if king_posw[0 + 1] < 8 and king_posw[1] - 1 >= 0:
                    if self.board.grid[king_posw[0] + 1][king_posw[1] - 1] is None and self.checkw(king_posw[0] + 1, king_posw[1] - 1) is True:
                        return False
                    if self.board.grid[king_posw[0] + 1][king_posw[1] - 1].color == "black":
                        return False
                if king_posw[0] - 1 >= 0 and king_posw[1] - 1 >= 0:
                    if self.board.grid[king_posw[0] - 1][king_posw[1] - 1] is None and self.checkw(king_posw[0] - 1, king_posw[1] - 1 is True):
                        return False
                    if self.board.grid[king_posw[0] - 1][king_posw[1] - 1].color == "black":
                        return False
                for piece in tab:
                    if piece.color == "black":
                        moves = self.get_moves(piece.row, piece.col)
                        if moves is not None:
                            for move in moves:
                                if move == king_posw:
                                    return False
                print("Echec et mat")
                return True"""

    def checkmate(self):
        # get king positions
        king_posb = self.get_piece_position(5)
        king_posw = self.get_piece_position(21)

        # get all possible moves of all pieces on the board
        all_moves = []
        for row in range(8):
            for col in range(8):
                piece = self.get_piece(row, col)
                if piece is not None:
                    moves = self.get_moves(row, col)
                    if moves is not None:
                        for move in moves:
                            all_moves.append((row, col, move))

        # check if king can move to a safe position
        if self.player.color == "black":
            for move in [(king_posb[0] + i, king_posb[1] + j) for i in [-1, 0, 1] for j in [-1, 0, 1]]:
                if move[0] < 0 or move[0] > 7 or move[1] < 0 or move[1] > 7:
                    continue
                if self.board.grid[move[0]][move[1]] is None and not self.checkb(move[0], move[1]):
                    if not any([self.is_in_check_after_move(move[0], move[1], row, col, all_moves) for row, col, _ in
                                all_moves if self.get_piece(row, col).color == "white"]):
                        return False
                if self.board.grid[move[0]][move[1]] is not None and self.board.grid[move[0]][
                    move[1]].color == "white" and not self.checkb(move[0], move[1]):
                    if not any([self.is_in_check_after_move(move[0], move[1], row, col, all_moves) for row, col, _ in
                                all_moves if self.get_piece(row, col).color == "white"]):
                        return False
        elif self.player.color == "white":
            for move in [(king_posw[0] + i, king_posw[1] + j) for i in [-1, 0, 1] for j in [-1, 0, 1]]:
                if move[0] < 0 or move[0] > 7 or move[1] < 0 or move[1] > 7:
                    continue
                if self.board.grid[move[0]][move[1]] is None and not self.checkw(move[0], move[1]):
                    if not any([self.is_in_check_after_move(move[0], move[1], row, col, all_moves) for row, col, _ in
                                all_moves if self.get_piece(row, col).color == "black"]):
                        return False
                if self.board.grid[move[0]][move[1]] is not None and self.board.grid[move[0]][
                    move[1]].color == "black" and not self.checkw(move[0], move[1]):
                    if not any([self.is_in_check_after_move(move[0], move[1], row, col, all_moves) for row, col, _ in
                                all_moves if self.get_piece(row, col).color == "black"]):
                        return False
                if self.board.grid[king_posb[0] - 1][king_posb[1] - 1] is None and self.checkb(king_posb[0] - 1, king_posb[1] - 1) is False:
                    return False
                if self.board.grid[king_posb[0] - 1][king_posb[1] - 1] is not None:
                    if self.board.grid[king_posb[0] - 1][king_posb[1] - 1].color == "white" and self.checkb(
                            king_posb[0] - 1, king_posb[1] - 1) is False:
                        return False
            return True
        elif self.checkw(king_posw[0], king_posw[1]):
            if (self.player.color == "white" and self.player.turn == 1) or (
                    self.player2.color == "white" and self.player2.turn == 1):
                if king_posw[0] + 1 < 8:
                    if self.board.grid[king_posw[0] + 1][king_posw[1]] is None and self.checkw(king_posw[0] + 1,
                                                                                                 king_posw[1]) is False:
                        for row in range(8):
                            for col in range(8):
                                piece = self.get_piece(row, col)
                                if piece is not None:
                                    if piece.color == "white":
                                        moves = self.get_moves(row, col)
                                        if moves is not None:
                                            for move in moves:
                                                for i in range(8 - king_posw[0]):
                                                    if move == (king_posw[0] + i, king_posw[1]):
                                                        print("cc")
                                                        return False
                        return False
                    if self.board.grid[king_posw[0] + 1][king_posw[1]] is not None:
                        if self.board.grid[king_posw[0] + 1][king_posw[1]].color == "black" and self.checkw(king_posw[0] + 1,
                                                                                                            king_posw[
                                                                                                                1]) is False:
                            return False
                if king_posw[0] - 1 >= 0:
                    if self.board.grid[king_posw[0] - 1][king_posw[1]] is None and self.checkw(king_posw[0] - 1,
                                                                                               king_posw[1]) is False:
                        for row in range(8):
                            for col in range(8):
                                piece = self.get_piece(row, col)
                                if piece is not None:
                                    if piece.color == "white":
                                        moves = self.get_moves(row, col)
                                        if moves is not None:
                                            for move in moves:
                                                for i in range(8 - king_posw[0]):
                                                    if move == (king_posw[0] - i, king_posw[1]):
                                                        print("dd")
                                                        return False
                        return False
                    if self.board.grid[king_posw[0] - 1][king_posw[1]] is not None:
                        if self.board.grid[king_posw[0] - 1][king_posw[1]].color == "black" and self.checkw(king_posw[0] - 1,
                                                                                                            king_posw[
                                                                                                                1]) is False:
                            return False
                if king_posw[1] + 1 < 8:
                    if self.board.grid[king_posw[0]][king_posw[1] + 1] is None and self.checkw(king_posw[0],
                                                                                               king_posw[1] + 1) is False:
                        for row in range(8):
                            for col in range(8):
                                piece = self.get_piece(row, col)
                                if piece is not None:
                                    if piece.color == "white":
                                        moves = self.get_moves(row, col)
                                        if moves is not None:
                                            for move in moves:
                                                for i in range(8 - king_posw[0]):
                                                    if move == (king_posw[0], king_posw[1] + i):
                                                        print("ee")
                                                        return False
                        return False
                    if self.board.grid[king_posw[0] + 1][king_posw[1] + 1] is not None:
                        if self.board.grid[king_posw[0] + 1][king_posw[1] + 1].color == "black" and self.checkw(king_posw[0] + 1,
                                                                                                         king_posw[
                                                                                                             1] + 1) is False:

                            return False
                if king_posw[0] + 1 < 8 and king_posw[1] - 1 >= 0:
                    if self.board.grid[king_posw[0] + 1][king_posw[1] - 1] is None and self.checkw(king_posw[0] + 1,
                                                                                                   king_posw[1] - 1) is False:
                        return False
                    if self.board.grid[king_posw[0] + 1][king_posw[1] - 1] is not None:
                        if self.board.grid[king_posw[0] + 1][king_posw[1] - 1].color == "black" and self.checkw(
                                king_posw[0] + 1, king_posw[1] - 1) is False:
                            return False
                if king_posw[0] - 1 >= 0 and king_posw[1] + 1 < 8:
                    if self.board.grid[king_posw[0] - 1][king_posw[1] + 1] is None and self.checkw(king_posw[0] - 1,
                                                                                                   king_posw[1] + 1) is False:
                        return False
                    if self.board.grid[king_posw[0] - 1][king_posw[1] + 1] is not None:
                        if self.board.grid[king_posw[0] - 1][king_posw[1] + 1].color == "black" and self.checkw(
                                king_posw[0] - 1, king_posw[1] + 1) is False:
                            return False
                if king_posw[0] - 1 >= 0 and king_posw[1] - 1 >= 0:
                    if self.board.grid[king_posw[0] - 1][king_posw[1] - 1] is None and self.checkw(king_posw[0] - 1,
                                                                                                   king_posw[1] - 1) is False:
                        return False
                    if self.board.grid[king_posw[0] - 1][king_posw[1] - 1] is not None:
                        if self.board.grid[king_posw[0] - 1][king_posw[1] - 1].color == "black" and self.checkw(
                                king_posw[0] - 1, king_posw[1] - 1) is False:
                            return False
        elif self.checkw(king_posw[0], king_posw[1]):
            if (self.player.color == "white" and self.player.turn == 1) or (
                    self.player2.color == "white" and self.player2.turn == 1):
                if king_posw[0] + 1 < 8:
                    if self.board.grid[king_posw[0] + 1][king_posw[1]] is None and self.checkw(king_posw[0] + 1,
                                                                                               king_posw[1]) is False:
                        for row in range(8):
                            for col in range(8):
                                piece = self.get_piece(row, col)
                                if piece is not None:
                                    if piece.color == "white":
                                        moves = self.get_moves(row, col)
                                        if moves is not None:
                                            for move in moves:
                                                for i in range(8 - king_posw[0]):
                                                    if move == (king_posw[0] + i, king_posw[1]):
                                                        print("ff")
                                                        return False
                        return False
                    if self.board.grid[king_posw[0] + 1][king_posw[1]] is not None:
                        if self.board.grid[king_posw[0] + 1][king_posw[1]].color == "black" and self.checkw(king_posw[0] + 1,
                                                                                                         king_posw[
                                                                                                             1]) is False:
                            return False
                if king_posw[0] - 1 >= 0:
                    if self.board.grid[king_posw[0] - 1][king_posw[1]] is None and self.checkw(king_posw[0] - 1,
                                                                                               king_posw[1]) is False:
                        return False
                    if self.board.grid[king_posw[0] - 1][king_posw[1]] is not None:
                        if self.board.grid[king_posw[0] - 1][king_posw[1]].color == "black" and self.checkw(
                                king_posw[0] - 1, king_posw[1]) is False:
                            return False
                if king_posw[1] + 1 < 8:
                    if self.board.grid[king_posw[0]][king_posw[1] + 1] is None and self.checkw(king_posw[0],
                                                                                               king_posw[1] + 1) is False:
                        return False
                    if self.board.grid[king_posw[0]][king_posw[1] + 1] is not None:
                        if self.board.grid[king_posw[0]][king_posw[1] + 1].color == "black" and self.checkw(
                                king_posw[0], king_posw[1] + 1) is False:
                            return False
                if king_posw[1] - 1 >= 0:
                    if self.board.grid[king_posw[0]][king_posw[1] - 1] is None and self.checkw(king_posw[0],
                                                                                               king_posw[1] - 1) is False:
                        return False
                    if self.board.grid[king_posw[0]][king_posw[1] - 1] is not None:
                        if self.board.grid[king_posw[0]][king_posw[1] - 1].color == "black" and self.checkw(
                                king_posw[0], king_posw[1] - 1) is False:
                            return False
                if king_posw[0] + 1 < 8 and king_posw[1] + 1 < 8:
                    if self.board.grid[king_posw[0] + 1][king_posw[1] + 1] is None and self.checkw(king_posw[0] + 1,
                                                                                                   king_posw[1] + 1) is False:
                        return False
                    if self.board.grid[king_posw[0] + 1][king_posw[1] + 1] is not None:
                        if self.board.grid[king_posw[0] + 1][king_posw[1] + 1].color == "black" and self.checkw(
                                king_posw[0] + 1, king_posw[1] + 1) is False:
                            return False
                if king_posw[0] + 1 < 8 and king_posw[1] - 1 >= 0:
                    if self.board.grid[king_posw[0] + 1][king_posw[1] - 1] is None and self.checkw(king_posw[0] + 1,
                                                                                                   king_posw[1] - 1) is False:
                        return False
                    if self.board.grid[king_posw[0] + 1][king_posw[1] - 1] is not None:
                        if self.board.grid[king_posw[0] + 1][king_posw[1] - 1].color == "black" and self.checkw(
                                king_posw[0] + 1, king_posw[1] - 1) is False:
                            return False
                if king_posw[0] - 1 >= 0 and king_posw[1] + 1 < 8:
                    if self.board.grid[king_posw[0] - 1][king_posw[1] + 1] is None and self.checkw(king_posw[0] - 1,
                                                                                                   king_posw[1] + 1) is False:
                        return False
                    if self.board.grid[king_posw[0] - 1][king_posw[1] + 1] is not None:
                        if self.board.grid[king_posw[0] - 1][king_posw[1] + 1].color == "black" and self.checkw(
                                king_posw[0] - 1, king_posw[1] + 1) is False:
                            return False
                if king_posw[0] - 1 >= 0 and king_posw[1] - 1 >= 0:
                    if self.board.grid[king_posw[0] - 1][king_posw[1] - 1] is None and self.checkw(king_posw[0] - 1,
                                                                                                   king_posw[1] - 1) is False:
                        return False
                    if self.board.grid[king_posw[0] - 1][king_posw[1] - 1] is not None:
                        if self.board.grid[king_posw[0] - 1][king_posw[1] - 1].color == "black" and self.checkw(
                                king_posw[0] - 1, king_posw[1] - 1) is False:
                            return False
                return True





    # Ajout des getter et setter
    def get_piece(self, row, col):  # Fonction qui permet de récupérer une pièce
        return self.board.grid[row][col]  # On retourne la pièce

    def get_selected_piece(self):  # Fonction qui permet de récupérer la pièce sélectionnée
        if self.selected_piece is not None:  # Si une pièce est sélectionnée
            return self.get_piece(*self.selected_piece)  # On retourne la pièce sélectionnée
        return None  # On retourne la pièce sélectionnée

    # On récupère la position d'une pièce par son id
    def get_piece_position(self, id):
        for row in range(8):
            for col in range(8):
                if self.board.grid[row][col] is not None and self.board.grid[row][col].id == id:
                    return (row, col)
        return None

    def get_board(self):  # Fonction qui permet de récupérer le plateau de jeu
        return self.board  # On retourne le plateau de jeu

    def get_screen(self):  # Fonction qui permet de récupérer l'écran
        return self.screen  # On retourne l'écran

    def get_running(self):  # Fonction qui permet de récupérer l'état du jeu
        return self.running  # On retourne l'état du jeu

    def get_grid(self):  # Fonction qui permet de récupérer la grille
        return self.board.grid  # On retourne la grille

    def get_screen_width(self):  # Fonction qui permet de récupérer la largeur de l'écran
        return SCREEN_WIDTH  # On retourne la largeur de l'écran

    def get_screen_height(self):  # Fonction qui permet de récupérer la hauteur de l'écran
        return SCREEN_HEIGHT  # On retourne la hauteur de l'écran

    def set_piece(self, row, col, piece):  # Fonction qui permet de placer une pièce
        self.board.grid[row][col] = piece  # On place la pièce

    def set_selected_piece(self, row, col):  # Fonction qui permet de sélectionner une pièce
        self.selected_piece = (row, col)  # On sélectionne la pièce

    def set_board(self, board):  # Fonction qui permet de placer le plateau de jeu
        self.board = board  # On place le plateau de jeu

    def set_screen(self, screen):  # Fonction qui permet de placer l'écran
        self.screen = screen  # On place l'écran

    def set_running(self, running):  # Fonction qui permet de changer l'état du jeu
        self.running = running  # On change l'état du jeu

    def set_grid(self, grid):  # Fonction qui permet de placer la grille
        self.board.grid = grid  # On place la grille

    def set_grid_size(self, grid_size):  # Fonction qui permet de placer la taille de la grille
        GRID_SIZE = grid_size  # On place la taille de la grille

    def set_screen_width(self, screen_width):  # Fonction qui permet de placer la largeur de l'écran
        SCREEN_WIDTH = screen_width  # On place la largeur de l'écran

    def set_screen_height(self, screen_height):  # Fonction qui permet de placer la hauteur de l'écran
        SCREEN_HEIGHT = screen_height  # On place la hauteur de l'écran

    def set_grid(self, grid):  # Fonction qui permet de placer la grille
        self.grid = grid  # On place la grille

    def reset(self):  # Fonction qui permet de réinitialiser le jeu
        self.board = Board(self.screen)  # On réinitialise le plateau de jeu
        self.selected_piece = None  # On déselectionne la pièce
        self.running = True  # On lance le jeu

    def turn(self):  # Fonction qui permet de changer de tour
        if self.player.turn == 1:
            self.player.turn = 0
            self.player2.turn = 1
        else:
            self.player.turn = 1
            self.player2.turn = 0

    def run(self):  # Fonction qui permet de lancer le jeu
        self.choose_player()  # On choisit le joueur
        while self.running:  # Tant que le jeu est lancé
            self.handle_events()  # On gère les évènements
            self.board.draw(self.screen)  # On dessine le plateau de jeu
            pygame.display.flip()  # On met à jour l'écran
            pygame.display.update()  # On met à jour l'écran
        pygame.quit()  # On quitte pygame
