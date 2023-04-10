import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
import chess

model = load_model('mon_modele.h5')


def play_against_model(model):
    # Initialisation du jeu d'échecs
    board = chess.Board()

    while not board.is_game_over():
        if board.turn == chess.WHITE:
            # C'est au tour du joueur humain
            print(board)
            move = input("Votre mouvement (au format 'e2e4'): ")
            move = chess.Move.from_uci(move)
        else:
            # C'est au tour du modèle
            prediction = model.predict(np.array([board_to_array(board)]))
            legal_moves = list(board.legal_moves)
            legal_moves = [move.uci() for move in legal_moves]
            legal_moves.sort()
            move_uci = legal_moves[np.argmax(prediction)]
            move = chess.Move.from_uci(move_uci)

        # Vérification de la validité du mouvement
        if move not in board.legal_moves:
            print("Mouvement invalide!")
            continue

        # Application du mouvement
        board.push(move)

        # Affichage du plateau
        print(board)

    # Affichage du résultat final
    print("Partie terminée!")
    if board.is_checkmate():
        print("Echec et mat!")
    elif board.is_stalemate():
        print("Partie nulle (pat)!")
    elif board.is_insufficient_material():
        print("Partie nulle (matériel insuffisant)!")
    else:
        print("Résultat inconnu!")


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


play_against_model(model)
