import pygame

# Initialisation de Pygame
pygame.init()

updated_rects = []

# Constantes pour la taille de l'écran et de la grille de jeu
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 480
GRID_SIZE = SCREEN_WIDTH // 8

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)

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


# Classe pour représenter les pièces du jeu d'échecs
class Piece:  # Piece est une classe qui contient une couleur, une image et un type
    def __init__(self, color, image,
                 type, id):  # color est une chaîne de caractères, image est un objet de la classe pygame.Surface
        self.color = color
        self.image = image
        self.type = type
        self.id = id

    def draw(self, screen, x, y):  # x et y sont les coordonnées de la case où dessiner la pièce
        screen.blit(self.image, (x, y))
        updated_rects.append(pygame.Rect(x, y, GRID_SIZE, GRID_SIZE))


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


class Board:  # Board est une classe qui contient une liste de pièces
    def __init__(self, screen):  # screen est un objet de la classe pygame.Surface
        self.grid = []  # self.grid est une liste de pièces
        for i in range(8):
            row = []  # row est une liste de pièces
            for j in range(8):
                row.append(None)
            self.grid.append(row)  # self.grid est une liste de pièces

        # Placement des pièces initiales
        self.grid[0][0] = Piece('black', ROOK_BLACK_IMG, "rook",1)
        self.grid[0][1] = Piece('black', KNIGHT_BLACK_IMG, "knight",2)
        self.grid[0][2] = Piece('black', BISHOP_BLACK_IMG, "bishop",3)
        self.grid[0][3] = Piece('black', QUEEN_BLACK_IMG, "queen",4)
        self.grid[0][4] = Piece('black', KING_BLACK_IMG, "king",5)
        self.grid[0][5] = Piece('black', BISHOP_BLACK_IMG, "bishop",6)
        self.grid[0][6] = Piece('black', KNIGHT_BLACK_IMG, "knight",7)
        self.grid[0][7] = Piece('black', ROOK_BLACK_IMG, "rook",8)
        self.grid[1][0] = Piece('black', PAWN_BLACK_IMG, "pawn",9)
        self.grid[1][1] = Piece('black', PAWN_BLACK_IMG, "pawn",10)
        self.grid[1][2] = Piece('black', PAWN_BLACK_IMG, "pawn",11)
        self.grid[1][3] = Piece('black', PAWN_BLACK_IMG, "pawn",12)
        self.grid[1][4] = Piece('black', PAWN_BLACK_IMG, "pawn",13)
        self.grid[1][5] = Piece('black', PAWN_BLACK_IMG, "pawn",14)
        self.grid[1][6] = Piece('black', PAWN_BLACK_IMG, "pawn",15)
        self.grid[1][7] = Piece('black', PAWN_BLACK_IMG, "pawn",16)
        self.grid[7][0] = Piece('white', ROOK_WHITE_IMG, "rook",17)
        self.grid[7][1] = Piece('white', KNIGHT_WHITE_IMG, "knight",18)
        self.grid[7][2] = Piece('white', BISHOP_WHITE_IMG, "bishop",19)
        self.grid[7][3] = Piece('white', QUEEN_WHITE_IMG, "queen",20)
        self.grid[7][4] = Piece('white', KING_WHITE_IMG, "king",21)
        self.grid[7][5] = Piece('white', BISHOP_WHITE_IMG, "bishop",22)
        self.grid[7][6] = Piece('white', KNIGHT_WHITE_IMG, "knight",23)
        self.grid[7][7] = Piece('white', ROOK_WHITE_IMG, "rook",24)
        self.grid[6][0] = Piece('white', PAWN_WHITE_IMG, "pawn",25)
        self.grid[6][1] = Piece('white', PAWN_WHITE_IMG, "pawn",26)
        self.grid[6][2] = Piece('white', PAWN_WHITE_IMG, "pawn",27)
        self.grid[6][3] = Piece('white', PAWN_WHITE_IMG, "pawn",28)
        self.grid[6][4] = Piece('white', PAWN_WHITE_IMG, "pawn",29)
        self.grid[6][5] = Piece('white', PAWN_WHITE_IMG, "pawn",30)
        self.grid[6][6] = Piece('white', PAWN_WHITE_IMG, "pawn",31)
        self.grid[6][7] = Piece('white', PAWN_WHITE_IMG, "pawn",32)

    def draw(self, screen):  # Fonction pour dessiner le plateau de jeu
        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 0:  # Pour dessiner les cases blanches et noires
                    pygame.draw.rect(screen, GRAY, (j * GRID_SIZE, i * GRID_SIZE, GRID_SIZE, GRID_SIZE))
                else:
                    pygame.draw.rect(screen, WHITE, (j * GRID_SIZE, i * GRID_SIZE, GRID_SIZE, GRID_SIZE))
                if self.grid[i][j] is not None:  # Pour dessiner les pièces
                    x = j * GRID_SIZE
                    y = i * GRID_SIZE
                    self.grid[i][j].draw(screen, x, y)  # On dessine la pièce
        pygame.display.update(updated_rects)  # On met à jour l'affichage


def get_grid_size():  # Fonction qui permet de récupérer la taille de la grille
    return GRID_SIZE


class Game:  # Classe pour représenter le jeu
    def __init__(self):  # Fonction d'initialisation
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Jeu d'échec")
        self.board = Board(self.screen)
        self.selected_piece = None
        self.running = True

    def handle_events(self):  # Fonction qui gère les événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:  # Si on clique sur la souris
                x, y = pygame.mouse.get_pos()  # On récupère les coordonnées de la souris
                row = y // GRID_SIZE  # On calcule la ligne
                col = x // GRID_SIZE  # On calcule la colonne
                self.select_piece(row, col)  # On sélectionne la pièce

    def select_piece(self, row, col):  # Fonction qui permet de sélectionner une pièce
        piece = self.board.grid[row][col]  # On récupère la pièce
        if piece is not None:  # Si la pièce n'est pas vide
            self.selected_piece = (row, col)  # On sélectionne la pièce
        elif self.selected_piece is not None:  # Si une pièce est sélectionnée
            self.move(row, col)  # On déplace la pièce

    """def move_piece(self, row, col):  # Fonction qui permet de déplacer une pièce
        if self.selected_piece is not None:  # Si une pièce est sélectionnée
            piece_row, piece_col = self.selected_piece  # On récupère les coordonnées de la pièce
            piece = self.board.grid[piece_row][piece_col]  # On récupère la pièce
            self.board.grid[piece_row][piece_col] = None  # On vide la case de départ
            self.board.grid[row][col] = piece  # On place la pièce sur la case d'arrivée
            self.selected_piece = None  # On déselectionne la pièce"""

    def pawn_move(self, row, col): # Fonction qui permet de déplacer un pion
        if self.selected_piece is not None: # Si une pièce est sélectionnée
            piece_row, piece_col = self.selected_piece # On récupère les coordonnées de la pièce
            piece = self.board.grid[piece_row][piece_col] # On récupère la pièce
            piece2 = self.board.grid[piece_row][piece_col-1]
            if piece.type == "pawn": # Si la pièce est un pion
                if self.board.grid[row - 1][col] is not None and self.board.grid[row - 1][col].color == "black":  # Si la case d'arrivée est vide
                    self.board.grid[piece_row][piece_col] = None  # On vide la case de départ
                    self.board.grid[row][col] = piece  # On place la pièce sur la case d'arrivée
                    self.selected_piece = None  # On déselectionne la pièce
                if self.board.grid[row + 1][col] is not None and self.board.grid[row + 1][col].color == "white": # Si la case d'arrivée est vide
                    self.board.grid[piece_row][piece_col] = None  # On vide la case de départ
                    self.board.grid[row][col] = piece  # On place la pièce sur la case d'arrivée
                    self.selected_piece = None  # On déselectionne la pièce

    def rook_move(self, row, col): # Fonction qui permet de déplacer une tour
        if self.selected_piece is not None: # Si une pièce est sélectionnée
            piece_row, piece_col = self.selected_piece # On récupère les coordonnées de la pièce
            piece = self.board.grid[piece_row][piece_col] # On récupère la pièce
            if piece.type == "rook": # Si la pièce est une tour
                if self.board.grid[row][col] is not None and self.board.grid[row][col].color == "black": # Si la case d'arrivée est vide
                    self.board.grid[piece_row][piece_col] = None  # On vide la case de départ

    def knight_move(self, row, col): # Fonction qui permet de déplacer un cavalier
        if self.selected_piece is not None:
            piece_row, piece_col = self.selected_piece
            piece = self.board.grid[piece_row][piece_col]
            if piece.type == "knight":
                if self.board.grid[row + 2][col + 1] is not None:
                    self.board.grid[piece_row][piece_col] = None  # On vide la case de départ
                    self.board.grid[row][col] = piece  # On place la pièce sur la case d'arrivée
                    self.selected_piece = None  # On déselectionne la pièce
                elif self.board.grid[row + 2][col - 1] is not None:
                    self.board.grid[piece_row][piece_col] = None  # On vide la case de départ
                    self.board.grid[row][col] = piece  # On place la pièce sur la case d'arrivée
                    self.selected_piece = None  # On déselectionne la pièce
                elif self.board.grid[row - 2][col + 1] is not None:
                    self.board.grid[piece_row][piece_col] = None  # On vide la case de départ
                    self.board.grid[row][col] = piece  # On place la pièce sur la case d'arrivée
                    self.selected_piece = None  # On déselectionne la pièce
                elif self.board.grid[row - 2][col - 1] is not None:
                    self.board.grid[piece_row][piece_col] = None  # On vide la case de départ
                    self.board.grid[row][col] = piece  # On place la pièce sur la case d'arrivée
                    self.selected_piece = None  # On déselectionne la pièce
                elif self.board.grid[row + 1][col + 2] is not None:
                    self.board.grid[piece_row][piece_col] = None
                    self.board.grid[row][col] = piece
                    self.selected_piece = None
                elif self.board.grid[row + 1][col - 2] is not None:
                    self.board.grid[piece_row][piece_col] = None
                    self.board.grid[row][col] = piece
                    self.selected_piece = None
                elif self.board.grid[row - 1][col + 2] is not None:
                    self.board.grid[piece_row][piece_col] = None
                    self.board.grid[row][col] = piece
                    self.selected_piece = None
                elif self.board.grid[row - 1][col - 2] is not None:
                    self.board.grid[piece_row][piece_col] = None
                    self.board.grid[row][col] = piece
                    self.selected_piece = None

    def bishop_move(self, row, col): # Fonction qui permet de déplacer un fou
        if self.selected_piece is not None:
            piece_row, piece_col = self.selected_piece
            piece = self.board.grid[piece_row][piece_col]
            if piece.type == "bishop":
                if self.board.grid[row][col] is not None and self.board.grid[row][col].color == "black":
                    self.board.grid[row][col] = None
                elif self.board.grid[row][col] is not None and self.board.grid[row][col].color == "black":
                    self.board.grid[row][col] = None

    def queen_move(self, row, col): # Fonction qui permet de déplacer une reine
        if self.selected_piece is not None:
            piece_row, piece_col = self.selected_piece
            piece = self.board.grid[piece_row][piece_col]
            if piece.type == "queen":
                if self.board.grid[row][col] is not None and self.board.grid[row][col].color == "black":
                    self.board.grid[row][col] = None
                elif self.board.grid[row][col] is not None and self.board.grid[row][col].color == "black":
                    self.board.grid[row][col] = None

    def king_move(self, row, col): # Fonction qui permet de déplacer un roi
        if self.selected_piece is not None:
            piece_row, piece_col = self.selected_piece
            piece = self.board.grid[piece_row][piece_col]
            if piece.type == "king":
                if self.board.grid[row + 1][col] is not None :
                    self.board.grid[piece_row][piece_col] = None  # On vide la case de départ
                    self.board.grid[row][col] = piece  # On place la pièce sur la case d'arrivée
                    self.selected_piece = None  # On déselectionne la pièce
                elif self.board.grid[row - 1][col] is not None :
                    self.board.grid[piece_row][piece_col] = None  # On vide la case de départ
                    self.board.grid[row][col] = piece  # On place la pièce sur la case d'arrivée
                    self.selected_piece = None  # On déselectionne la pièce
                elif self.board.grid[row][col + 1] is not None :
                    self.board.grid[piece_row][piece_col] = None  # On vide la case de départ
                    self.board.grid[row][col] = piece  # On place la pièce sur la case d'arrivée
                    self.selected_piece = None  # On déselectionne la pièce
                elif self.board.grid[row][col - 1] is not None :
                    self.board.grid[piece_row][piece_col] = None  # On vide la case de départ
                    self.board.grid[row][col] = piece  # On place la pièce sur la case d'arrivée
                    self.selected_piece = None  # On déselectionne la pièce
                elif self.board.grid[row + 1][col + 1] is not None :
                    self.board.grid[piece_row][piece_col] = None  # On vide la case de départ
                    self.board.grid[row][col] = piece  # On place la pièce sur la case d'arrivée
                    self.selected_piece = None  # On déselectionne la pièce
                elif self.board.grid[row + 1][col - 1] is not None :
                    self.board.grid[piece_row][piece_col] = None  # On vide la case de départ
                    self.board.grid[row][col] = piece  # On place la pièce sur la case d'arrivée
                    self.selected_piece = None  # On déselectionne la pièce
                elif self.board.grid[row - 1][col + 1] is not None :
                    self.board.grid[piece_row][piece_col] = None  # On vide la case de départ
                    self.board.grid[row][col] = piece  # On place la pièce sur la case d'arrivée
                    self.selected_piece = None  # On déselectionne la pièce
                elif self.board.grid[row - 1][col - 1] is not None :
                    self.board.grid[piece_row][piece_col] = None  # On vide la case de départ
                    self.board.grid[row][col] = piece  # On place la pièce sur la case d'arrivée
                    self.selected_piece = None  # On déselectionne la pièce
    def move(self, row, col): # Fonction qui permet de déplacer une pièce
        if self.selected_piece is not None: # Si une pièce est sélectionnée
            piece_row, piece_col = self.selected_piece # On récupère les coordonnées de la pièce
            piece = self.board.grid[piece_row][piece_col] # On récupère la pièce
            if piece.type == "pawn": # Si la pièce est un pion
                self.pawn_move(row, col) # On appelle la fonction qui permet de déplacer un pion
            elif piece.type == "rook": # Si la pièce est une tour
                self.rook_move(row, col) # On appelle la fonction qui permet de déplacer une tour
            elif piece.type == "knight": # Si la pièce est un cavalier
                self.knight_move(row, col) # On appelle la fonction qui permet de déplacer un cavalier
            elif piece.type == "bishop": # Si la pièce est un fou
                self.bishop_move(row, col) # On appelle la fonction qui permet de déplacer un fou
            elif piece.type == "queen": # Si la pièce est une reine
                self.queen_move(row, col) # On appelle la fonction qui permet de déplacer une reine
            elif piece.type == "king": # Si la pièce est un roi
                self.king_move(row, col) # On appelle la fonction qui permet de déplacer un roi
            self.selected_piece = None # On déselectionne la pièce
        else: # Si aucune pièce n'est sélectionnée
            if self.board.grid[row][col] is not None and self.board.grid[row][col].color == "white": # Si la case sélectionnée contient une pièce blanche
                self.selected_piece = (row, col)

    def update(self):  # Fonction qui permet de mettre à jour le jeu
        self.board.draw(self.screen)  # On dessine le plateau de jeu

    # Ajout des getter et setter (ps : je pensait pas que la dodo pourrait m'apprendre des trucs utiles)
    def get_piece(self, row, col):  # Fonction qui permet de récupérer une pièce
        return self.board.grid[row][col]

    def get_selected_piece(self):  # Fonction qui permet de récupérer la pièce sélectionnée
        if self.selected_piece is not None:
            return self.get_piece(*self.selected_piece)
        return None

    def get_board(self):  # Fonction qui permet de récupérer le plateau de jeu
        return self.board

    def get_screen(self):  # Fonction qui permet de récupérer l'écran
        return self.screen

    def get_running(self):  # Fonction qui permet de récupérer l'état du jeu
        return self.running

    def get_grid(self):  # Fonction qui permet de récupérer la grille
        return self.board.grid

    def get_screen_width(self):  # Fonction qui permet de récupérer la largeur de l'écran
        return SCREEN_WIDTH

    def get_screen_height(self):  # Fonction qui permet de récupérer la hauteur de l'écran
        return SCREEN_HEIGHT

    def set_piece(self, row, col, piece):  # Fonction qui permet de placer une pièce
        self.board.grid[row][col] = piece

    def set_selected_piece(self, row, col):  # Fonction qui permet de sélectionner une pièce
        self.selected_piece = (row, col)

    def set_board(self, board):  # Fonction qui permet de placer le plateau de jeu
        self.board = board

    def set_screen(self, screen):  # Fonction qui permet de placer l'écran
        self.screen = screen

    def set_running(self, running):  # Fonction qui permet de changer l'état du jeu
        self.running = running

    def set_grid(self, grid):  # Fonction qui permet de placer la grille
        self.board.grid = grid

    def set_grid_size(self, grid_size):  # Fonction qui permet de placer la taille de la grille
        GRID_SIZE = grid_size

    def set_screen_width(self, screen_width):  # Fonction qui permet de placer la largeur de l'écran
        SCREEN_WIDTH = screen_width

    def set_screen_height(self, screen_height):  # Fonction qui permet de placer la hauteur de l'écran
        SCREEN_HEIGHT = screen_height
        
    def set_grid(self, grid):
        self.grid = grid

    def reset(self):  # Fonction qui permet de réinitialiser le jeu
        self.board = Board(self.screen)
        self.selected_piece = None
        self.running = True

    def run(self):  # Fonction qui permet de lancer le jeu
        while self.running:
            self.handle_events()
            self.screen.fill(BLACK)
            self.board.draw(self.screen)
            pygame.display.flip()
        pygame.quit()


class AI:
    def __init__(self):
        # On va récupérer le plateau d'échec sous forme de tableau
        game = Game()
        self.grid = game.get_grid()
        self.Affichage_type()

    def Affichage_type(self):
        AI_grid = [[0 for i in range(8)] for j in range(8)]
        for i in range(8):
            for j in range(8):
                if self.grid[i][j] is not None:
                    AI_grid[i][j] = [self.grid[i][j].get_type(), self.grid[i][j].get_color(), i, j]
                else:
                    AI_grid[i][j] = ["None", i, j]
            print("")
        print(AI_grid)
        
    def Input(self,x,y):
        # Coordoner de d'arriver x,y 
        self.x
        self.y
        game = Game()
        self.grid = game.get_grid()
        for i in range (8):
            for j in range(8):
                if self.grid[x][y] is not None :
                    # Déplacement de la pièces a la position final
                    game.set_grid(grid)
                
                

    def get_grid(self):
        return self.grid

    def set_grid(self, grid):
        self.grid = grid

    def get_AI_grid(self):
        return self.AI_grid

    def set_AI_grid(self, AI_grid):
        self.AI_grid = AI_grid


class Main_Screen:  # Classe pour représenter l'écran d'accueil
    def __init__(self):  # Fonction d'initialisation
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Jeu d'échec")
        self.running = True

    def handle_events(self):  # Fonction qui gère les événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:  # Si on clique sur la souris
                x, y = pygame.mouse.get_pos()  # On récupère les coordonnées de la souris
                print(x, y)
                if x > 150 and x < 340 and y > 300 and y < 400:  # Si on clique sur le bouton "Jouer"
                    game = Game()  # On lance le jeu
                    AI()
                    game.run()

    def draw(self):  # Fonction qui permet de dessiner l'écran d'accueil
        self.screen.fill(BLACK)
        font = pygame.font.SysFont('comicsans', 70)  # On définit la police
        text = font.render("Jeu d'échec", 1, WHITE)  # On écrit le texte
        self.screen.blit(text, (SCREEN_WIDTH / 2 - text.get_width() / 2, 100))  # On affiche le texte
        pygame.draw.rect(self.screen, WHITE, (150, 300, 190, 100))  # On dessine le bouton "Jouer"
        font = pygame.font.SysFont('comicsans', 50)  # On définit la police
        text = font.render("Jouer", 1, BLACK)  # On écrit le texte
        self.screen.blit(text, (SCREEN_WIDTH / 2 - text.get_width() / 2, 310))  # On affiche le texte
        pygame.display.update()  # On met à jour l'affichage

    def run(self):  # Fonction qui permet de lancer l'écran d'accueil
        while self.running:
            self.handle_events()
            self.draw()
        pygame.quit()


if __name__ == '__main__':  # Si on lance le script
    pygame.init()
    main_screen = Main_Screen()  # On lance l'écran d'accueil
    main_screen.run()
