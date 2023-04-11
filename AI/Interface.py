# Fichier pour faire jouer l'ia et la mettre en lien avec notre jeu

from tensorflow.keras.models import load_model
import numpy as np
import chess
import Game

model = load_model('mon_modele.h5')

# On récupère le plateau de jeu de notre jeu
def get_board():
    return Game.board

# On convertit le plateau de jeu en tableau
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

# On récupère le mouvement de l'ia
def get_move():
    # On récupère le plateau de jeu
    board = get_board()

    # On récupère les mouvements possibles
    legal_moves = list(board.legal_moves)
    legal_moves = [move.uci() for move in legal_moves]
    legal_moves.sort()

    # On récupère la prédiction de l'ia
    prediction = model.predict(np.array([board_to_array(board)]))

    # On récupère le mouvement à jouer
    move_uci = legal_moves[np.argmax(prediction)]

    # On retourne le mouvement
    return chess.Move.from_uci(move_uci)