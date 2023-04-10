# Endroit où est STockFish StockFish/stockfish_15.1_win_x64_avx2/stockfish-windows-2022-x86-64-avx2.exe
# Dans ce fichier on entraine l'ia avec tensorflow pour jouer contre elle-même et sauvegarder son fichier de poids neuronos
import chess.engine
import chess
import numpy as np
from tensorflow.keras.models import load_model

engine = chess.engine.SimpleEngine.popen_uci("StockFish/stockfish_15.1_win_x64_avx2/stockfish-windows-2022-x86-64-avx2.exe")
model = load_model('mon_modele.h5')

# On entre le nombre d'entrainements
nb_entraînements = int(input("Nombre d'entrainements: "))


X = []
y = []
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
    model.fit(np.array(X), np.array(y), batch_size=32, epochs=1)

model.save('mon_modele.h5')

