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
    # Crée un curseur pour exécuter des requêtes SQL
    # On ajoute le joueur dans la base de donnée
    cur.execute("INSERT INTO Games (Id_Player, Result) VALUES (?, ?, ?)", (Id_Player, Result))
    # On valide les changements
    conn.commit()

# On Ajoute les coups d'une partie unique du joueur dans la table mouvement
def add_move(Nom_Joueur, Move):
    Id_Player = ApiChess.get_id_player(Nom_Joueur)
    # Crée un curseur pour exécuter des requêtes SQL
    # On ajoute le joueur dans la base de donnée
    cur.execute("INSERT INTO Moves (Id_Player, Move) VALUES (?, ?)", (Id_Player, Move))
    # On valide les changements
    conn.commit()

# On ajoute tout les mouvements de toutes parties dans la table mouvement
def add_moves(Nom_Joueur):
    # On récupère les coups de toutes les parties du joueur
    Moves = ApiChess.moves_getter(Nom_Joueur)
    # On ajoute les coups d'une partie dans la table mouvement
    for Move in Moves:
        # On parcours les coups d'une partie
        for move in Move:
            # On ajoute un coup dans la table mouvement
            add_move(Nom_Joueur, move)



#Fonction d'ajout complet d'un joueur
def Main(Nom_Joueur):
    Joueur(Nom_Joueur)
    add_game(Nom_Joueur)


Main("Xtemp70")
conn.close()