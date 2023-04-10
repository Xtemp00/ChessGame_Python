# Endroit où est STockFish StockFish/stockfish_15.1_win_x64_avx2/stockfish-windows-2022-x86-64-avx2.exe
# Dans ce fichier on entraine l'ia avec tensorflow pour jouer contre elle-même et sauvegarder son fichier de poids neuronos
import chess.engine
import chess
import numpy as np
import tensorflow as tf

engine = chess.engine.SimpleEngine.popen_uci("StockFish/stockfish_15.1_win_x64_avx2/stockfish-windows-2022-x86-64-avx2.exe")

# Définition du modèle
model = tf.keras.Sequential([
    # Couche d'entrée
    tf.keras.layers.InputLayer(input_shape=(8, 8, 18)),

    # Convolution 2D pour extraire les caractéristiques de l'état du plateau
    tf.keras.layers.Conv2D(filters=32, kernel_size=(3, 3), activation='relu', padding='same'),
    tf.keras.layers.Conv2D(filters=32, kernel_size=(3, 3), activation='relu', padding='same'),
    tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),

    tf.keras.layers.Conv2D(filters=64, kernel_size=(3, 3), activation='relu', padding='same'),
    tf.keras.layers.Conv2D(filters=64, kernel_size=(3, 3), activation='relu', padding='same'),
    tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),

    # Couche entièrement connectée pour apprendre les motifs de jeu
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),

    # Couche de sortie pour la classification
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# Compilation du modèle
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

X = []
y = []
def board_to_input(board):
    state = np.zeros((8, 8, 18))
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
for i in range(1):
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

