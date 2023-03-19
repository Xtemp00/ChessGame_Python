import pygame

# Initialisation de Pygame
pygame.init()

# Constantes pour la taille de l'écran et de la grille de jeu
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 480
GRID_SIZE = SCREEN_WIDTH // 8

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)

# Chargement des images des pièces
PAWN_WHITE_IMG = pygame.image.load('pieces/pawn_white.png')
PAWN_BLACK_IMG = pygame.image.load('pieces/pawn_black.png')
ROOK_WHITE_IMG = pygame.image.load('pieces/rook_white.png')
ROOK_BLACK_IMG = pygame.image.load('pieces/rook_black.png')
KNIGHT_WHITE_IMG = pygame.image.load('pieces/knight_white.png')
KNIGHT_BLACK_IMG = pygame.image.load('pieces/knight_black.png')
BISHOP_WHITE_IMG = pygame.image.load('pieces/bishop_white.png')
BISHOP_BLACK_IMG = pygame.image.load('pieces/bishop_black.png')
QUEEN_WHITE_IMG = pygame.image.load('pieces/queen_white.png')
QUEEN_BLACK_IMG = pygame.image.load('pieces/queen_black.png')
KING_WHITE_IMG = pygame.image.load('pieces/king_white.png')
KING_BLACK_IMG = pygame.image.load('pieces/king_black.png')


# Classe pour représenter les pièces du jeu d'échecs
class Piece:
    def __init__(self, color, image):
        self.color = color
        self.image = image

    def draw(self, screen, x, y):
        screen.blit(self.image, (x, y))


# Classe pour représenter le plateau de jeu
class Board:
    def __init__(self):
        self.grid = []
        for i in range(8):
            row = []
            for j in range(8):
                row.append(None)
            self.grid.append(row)

        # Placement des pièces initiales
        self.grid[0][0] = Piece('black', ROOK_BLACK_IMG)
        self.grid[0][1] = Piece('black', KNIGHT_BLACK_IMG)
        self.grid[0][2] = Piece('black', BISHOP_BLACK_IMG)
        self.grid[0][3] = Piece('black', QUEEN_BLACK_IMG)
        self.grid[0][4] = Piece('black', KING_BLACK_IMG)
        self.grid[0][5] = Piece('black', BISHOP_BLACK_IMG)
        self.grid[0][6] = Piece('black', KNIGHT_BLACK_IMG)
        self.grid[0][7] = Piece('black', ROOK_BLACK_IMG)
        self.grid[1][0] = Piece('black', PAWN_BLACK_IMG)
        self.grid[1][1] = Piece('black', PAWN_BLACK_IMG)
        self.grid[1][2] = Piece('black', PAWN_BLACK_IMG)
        self.grid[1][3] = Piece('black', PAWN_BLACK_IMG)
        self.grid[1][4] = Piece('black', PAWN_BLACK_IMG)
        self.grid[1][5] = Piece('black', PAWN_BLACK_IMG)
        self.grid[1][6] = Piece('black', PAWN_BLACK_IMG)
        self.grid[1][7] = Piece('black', PAWN_BLACK_IMG)
        self.grid[7][0] = Piece('white', ROOK_WHITE_IMG)
        self.grid[7][1] = Piece('white', KNIGHT_WHITE_IMG)
        self.grid[7][2] = Piece('white', BISHOP_WHITE_IMG)
        self.grid[7][3] = Piece('white', QUEEN_WHITE_IMG)
        self.grid[7][4] = Piece('white', KING_WHITE_IMG)
        self.grid[7][5] = Piece('white', BISHOP_WHITE_IMG)
        self.grid[7][6] = Piece('white', KNIGHT_WHITE_IMG)
        self.grid[7][7] = Piece('white', ROOK_WHITE_IMG)
        self.grid[6][0] = Piece('white', PAWN_WHITE_IMG)
        self.grid[6][1] = Piece('white', PAWN_WHITE_IMG)
        self.grid[6][2] = Piece('white', PAWN_WHITE_IMG)
        self.grid[6][3] = Piece('white', PAWN_WHITE_IMG)
        self.grid[6][4] = Piece('white', PAWN_WHITE_IMG)
        self.grid[6][5] = Piece('white', PAWN_WHITE_IMG)
        self.grid[6][6] = Piece('white', PAWN_WHITE_IMG)
        self.grid[6][7] = Piece('white', PAWN_WHITE_IMG)

    def draw(self, screen):
        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 0:
                    pygame.draw.rect(screen, GRAY, (j * GRID_SIZE, i * GRID_SIZE, GRID_SIZE, GRID_SIZE))
                else:
                    pygame.draw.rect(screen, WHITE, (j * GRID_SIZE, i * GRID_SIZE, GRID_SIZE, GRID_SIZE))
                if self.grid[i][j] is not None:
                    piece = self.grid[i][j]
                    piece.draw(screen, j * GRID_SIZE, i * GRID_SIZE)


class Game:
    def __init__(self):
        self.board = Board()
        self.selected_piece = None
        self.running = True
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Chess")

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                row = y // GRID_SIZE
                col = x // GRID_SIZE
                self.select_piece(row, col)

    def select_piece(self, row, col):
        piece = self.board.grid[row][col]
        if piece is not None:
            self.selected_piece = (row, col)

    def move_piece(self, row, col):
        if self.selected_piece is not None:
            piece_row, piece_col = self.selected_piece
            piece = self.board.grid[piece_row][piece_col]
            self.board.grid[piece_row][piece_col] = None
            self.board.grid[row][col] = piece
            self.selected_piece = None

    def run(self):
        while self.running:
            self.handle_events()
            self.screen.fill(BLACK)
            self.board.draw(self.screen)
            pygame.display.flip()
        pygame.quit()


if __name__ == '__main__':
    pygame.init()
    game = Game()
    game.run()
