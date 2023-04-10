# Modèles de données
# Il y a 3 tables:
# - La table des joueurs :
#   - Id_Joueurs
#   - Nom_Joueurs
#   - nb_parties
#   - nb_victoires
#   - nb_defaites
#   - nb_nulles
# - La table des parties :
#   - Id_Partie
#   - Id_Joueur
#   - Id_Adversaire
#   - Resultat

# - La table des mouvements :
#   - Id_Partie
#   - Id_Joueur
#   - Id_Adversaire
#   - Mouvement

# On utilse la base de donnée SQLite pour créer la base de donnée
# Importation des modules nécessaires
import sqlite3
import ApiChess
import os

# Crée une connexion à la base de données
conn = sqlite3.connect('Chess.db')
cur = conn.cursor()

# On ajout un joueur dans la base de donnée
def add_player(player_name, nb_games, nb_wins, nb_defeats, nb_draws):
    # Crée un curseur pour exécuter des requêtes SQL
    # On vérifie si le joueur existe déjà dans la base de donnée
    cur.execute("SELECT * FROM Players WHERE Name_Player = ?", (player_name,))
    # On récupère les données de la requête
    data = cur.fetchall()
    # Si le joueur n'existe pas dans la base de donnée
    if data == []:
        # On ajoute le joueur dans la base de donnée
        cur.execute("INSERT INTO Players (Name_Player, nb_games, nb_wins, nb_defeats, nb_draws) VALUES (?, ?, ?, ?, ?)", (player_name, nb_games, nb_wins, nb_defeats, nb_draws))
        # On valide les changements
        conn.commit()

# On va ajouter une fonction principal pour tout ajouter
def Joueur(Nom_Joueur):
    # On ajoute un joueur dans la base de donnée
    total_games = ApiChess.total_games(Nom_Joueur)
    total_wins = ApiChess.won_games(Nom_Joueur)
    total_defeats = ApiChess.lost_games(Nom_Joueur)
    total_draws = ApiChess.draw_games(Nom_Joueur)
    add_player(Nom_Joueur, total_games, total_wins, total_defeats, total_draws)


# On récupère l'Id du joueur
def get_id_player(player_name):
    # Crée un curseur pour exécuter des requêtes SQL
    # On récupère l'Id du joueur
    cur.execute("SELECT Id_Player FROM Players WHERE Name_Player = ?", (player_name,))
    # On récupère les données de la requête
    data = cur.fetchall()
    # On ferme la connexion
    # On retourne l'Id du joueur
    return data[0][0]

# Ajout de toutes les partie du Joueur dans la table Partie
def add_game(Nom_Joueur):
    Id_Player = get_id_player(Nom_Joueur)
    Result = ApiChess.result_getter(Nom_Joueur)
    for result in Result:
        # On ajoute une partie dans la table partie
        # Crée un curseur pour exécuter des requêtes SQL
        # On ajoute le joueur dans la base de donnée
        cur.execute("INSERT INTO Games (Id_Player, Result) VALUES (?, ?)", (Id_Player, result))
        # On valide les changements
    conn.commit()

# On ajoute tout les mouvement d'une partie a la table Mouvement
# la table ressemble a ceci
# - La table des mouvements :# Avec un mouvement de départ et le mouvement d'arrivée
# cur.execute('''CREATE TABLE IF NOT EXISTS Moves
#                     (Id_Game INTEGER NOT NULL,
#                         Id_Player INTEGER NOT NULL,
#                             Number_Move INTEGER NOT NULL,
#                                 Move_depart TEXT NOT NULL,
#                                     Move_arrivee TEXT NOT NULL,
#                                         Type_Piece TEXT NOT NULL)''')

def add_all_move(Nom_Joueur):
    # On récupère l'Id du joueur
    Id_Player = get_id_player(Nom_Joueur)
    # On récupère tout les Id des parties du joueur
    cur.execute("SELECT Id_Game FROM Games WHERE Id_Player = ?", (Id_Player,))
    # On récupère les données de la requête
    data = cur.fetchall()
    # On récupère tout les mouvements de chaque partie
    for Id_Game in data:
        # On récupère tout les mouvements de la partie
        Moves = ApiChess.moves_getter_unique_pgn(Nom_Joueur, Id_Game[0])
        # On récupère le nombre de mouvement
        nb_moves = len(Moves)
        # On ajoute tout les mouvements dans la table Mouvement
        for move in Moves:
            # On récupère le mouvement de départ
            Move_depart = move[1][0]
            # On récupère le mouvement d'arrivée
            Move_arrivee = move[1][1]
            # On récupère le type de pièce
            Type_Piece = move[0]
            # On ajoute le mouvement dans la table Mouvement
            cur.execute("INSERT INTO Moves (Id_Game, Id_Player, Number_Move, Move_depart, Move_arrivee, Type_Piece) VALUES (?, ?, ?, ?, ?, ?)", (Id_Game[0], Id_Player, nb_moves, Move_depart, Move_arrivee, Type_Piece))
            # On valide les changements
            conn.commit()
            # On décrémente le nombre de mouvement
            nb_moves -= 1


#Fonction d'ajout complet d'un joueur
def Main(Nom_Joueur):
    Joueur(Nom_Joueur)
    add_game(Nom_Joueur)
    add_all_move(Nom_Joueur)
    conn.close()

ApiChess.import_player_game_history("Xtemp70")
Main("Nino_brgs")
