# Dans ce fichier on test l'ia pour quel joue contre nous même
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
            prediction = model.predict(np.array([chess.board_to_array(board)]))
            move = np.argmax(prediction)
            move = chess.Move.from_uci(chess.Move.from_uci(move))

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

play_against_model(model)