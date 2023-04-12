# Endroit où est STockFish StockFish/stockfish_15.1_win_x64_avx2/stockfish-windows-2022-x86-64-avx2.exe
# Dans ce fichier on entraine l'ia avec tensorflow pour jouer contre elle-même et sauvegarder son fichier de poids neuronos
import os

import chess.engine
import chess
import numpy as np
from tensorflow.keras.models import load_model
import pygame

engine = chess.engine.SimpleEngine.popen_uci("StockFish/stockfish_15.1_win_x64_avx2/stockfish-windows-2022-x86-64-avx2.exe")
model = load_model('mon_modele.h5')


X = []
y = []

def InitInterface():
    pygame.init()
    pygame.display.set_caption("Training IA")
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

def board_to_input(board):
    state = np.zeros((8, 8, 12))
    pieces = {'P': 0, 'N': 1, 'B': 2, 'R': 3, 'Q': 4, 'K': 5,
              'p': 6, 'n': 7, 'b': 8, 'r': 9, 'q': 10, 'k': 11}
    for i in range(64):
        if board.piece_at(i):
            piece = str(board.piece_at(i))
            color = int(board.piece_at(i).color)
            state[i // 8, i % 8, color * 6 + pieces[piece]] = 1
    return state

# Fonction pour évaluer le plateau de jeu
def evaluate_board(board):
    state = board_to_input(board)
    prediction = model.predict(np.array([state]))
    return prediction[0][0]

# Fonction pour générer un mouvement à partir du plateau de jeu
def get_move(board):
    result = engine.play(board, chess.engine.Limit(time=2.0))
    return result.move


# On va faire une fonction pour jouer contre l'ia et le voir de manière graphique
def Training(nb_entraînements):
    os.remove("mon_modele.h5"")
    screen = InitInterface()

    # Boucle principale d'apprentissage
    for i in range(nb_entraînements):
        # Créer un nouveau plateau de jeu
        board = chess.Board()

        # Boucle de jeu
        while not board.is_game_over():
            # Générer un mouvement à partir du plateau de jeu
            move = get_move(board)

            # Jouer le mouvement sur le plateau de jeu
            board.push(move)
            print(board)
            DrawBoard(screen)
            DrawPieces(screen, board)
            pygame.display.flip()

            # Évaluer le plateau de jeu
            score = evaluate_board(board)

            # Ajouter la récompense au score
            if board.result() == "1-0":
                score += 1
            elif board.result() == "0-1":
                score -= 1

            # Enregistrer le plateau de jeu et le score
            # pour l'apprentissage par renforcement
            X.append(board_to_input(board))
            y.append(score)

        # Entraîner le modèle sur les données collectées
        model.fit(np.array(X), np.array(y), batch_size=128, epochs=5000)
    model.save('mon_modele.h5')


if __name__ == "__main__":
    Training(5)