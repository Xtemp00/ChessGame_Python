import chess
import pygame
import numpy as np
import time

from tensorflow.keras.models import load_model
model = load_model('mon_modele.h5')
def InitInterface():
    pygame.init()
    pygame.display.set_caption("Chess")
    screen = pygame.display.set_mode((800, 800))
    return screen

def DrawBoard(screen):
    screen.fill((255, 255, 255))
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                pygame.draw.rect(screen, (128, 128, 128), (i * 100, j * 100, 100, 100))
            else:
                pygame.draw.rect(screen, (165, 42, 42), (i * 100, j * 100, 100, 100))


def DrawPieces(screen, board):
    pieces = {'P': pygame.image.load('../pieces/pawn_white.png'), 'N': pygame.image.load('../pieces/knight_white.png'), 'B': pygame.image.load('../pieces/bishop_white.png'), 'R': pygame.image.load('../pieces/rook_white.png'), 'Q': pygame.image.load('../pieces/queen_white.png'), 'K': pygame.image.load('../pieces/king_white.png')
              , 'p': pygame.image.load('../pieces/pawn_black.png'), 'n': pygame.image.load('../pieces/knight_black.png'), 'b': pygame.image.load('../pieces/bishop_black.png'), 'r': pygame.image.load('../pieces/rook_black.png'), 'q': pygame.image.load('../pieces/queen_black.png'), 'k': pygame.image.load('../pieces/king_black.png')}
    for i in range(8):
        for j in range(8):
            piece = board.piece_at(chess.square(i, j))
            if piece is not None:
                # On redimensionne la pièce
                pieces[piece.symbol()] = pygame.transform.scale(pieces[piece.symbol()], (100, 100))
                # On affiche la pièce blanche en bas et les noirs en haut
                screen.blit(pieces[piece.symbol()], (i * 100, (7 - j) * 100))


def board_to_array(board):
    pieces = {'P': 0, 'N': 1, 'B': 2, 'R': 3, 'Q': 4, 'K': 5,
              'p': 6, 'n': 7, 'b': 8, 'r': 9, 'q': 10, 'k': 11, '.': 12}
    board_array = np.zeros((8, 8, 12), dtype=np.uint8)

    for row in range(8):
        for col in range(8):
            piece = board.piece_at(chess.square(col, 7-row))
            if piece is not None:
                board_array[row, col, pieces[piece.symbol()]] = 1

    return board_array



# On lance l'interface dans le main
if __name__ == '__main__':
    screen = InitInterface()
    board = chess.Board()
    DrawBoard(screen)
    DrawPieces(screen, board)
    pygame.display.flip()
    tour = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # On regarde si une pièce est sélectionnée
        if pygame.mouse.get_pressed()[0] and tour == 0:
            # On récupère la position de la souris
            pos = pygame.mouse.get_pos()
            # On récupère la case correspondante
            square = (pos[0] // 100, pos[1] // 100)
            # On récupère la pièce présente sur cette case
            piece = board.piece_at(chess.square(square[0], 7 - square[1]))
            # On regarde que la pièce est bien de la couleur du joueur cette a dire blanche
            if piece is not None and piece.color == chess.WHITE:
                # On affiche la pièce sélectionnée et sa position
                print(piece.symbol(), square)
                # On a la position initial de la pièce
                initial_square = square
                # On récupère la position final de la pièce
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            exit()
                    if pygame.mouse.get_pressed()[0]:
                        pos = pygame.mouse.get_pos()
                        square = (pos[0] // 100, pos[1] // 100)
                        # On regarde que la case est bien différente de la case initiale
                        if square != initial_square:
                            # On regarde que la case est bien vide
                            # Déplacement de la pièce
                            colonne = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
                            move = str(colonne[initial_square[0]]) + str(8-initial_square[1]) + str(colonne[square[0]]) + str(8-square[1])
                            move = chess.Move.from_uci(move)
                            if move in board.legal_moves:
                                board.push(move)
                                print(board)
                                DrawBoard(screen)
                                DrawPieces(screen, board)
                                pygame.display.flip()
                                tour = 1
                                continue

                            break
                        elif pygame.mouse.get_pressed()[2]:
                            break
        elif tour == 1:
            # on attend 1 seconde
            time.sleep(1)
            print("C'est au tour du modèle")
            # C'est au tour du modèle
            prediction = model.predict(np.array([board_to_array(board)]))
            legal_moves = list(board.legal_moves)
            legal_moves = [move.uci() for move in legal_moves]
            legal_moves.sort()
            move_uci = legal_moves[np.argmax(prediction)]
            move = chess.Move.from_uci(move_uci)
            board.push(move)
            DrawBoard(screen)
            DrawPieces(screen, board)
            pygame.display.flip()
            tour = 0
