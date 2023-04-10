#Fichier permettant de créer la Database d'un jeu d'echec
# Il y aura 3 tables:
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
#   - Resultat

# - La table des mouvements :
#  - Id_Mouvement
#   - Id_Partie
#   - Id_Joueur
#   - Position_depart
#   - Position_arrivee
#   - Type_piece


# On utilise Mysql pour créer la base de donnée
# Importation des modules nécessaires
import sqlite3

# Crée une connexion à la base de données
conn = sqlite3.connect('Chess.db')

# Crée un curseur pour exécuter des requêtes SQL
cur = conn.cursor()

# Crée une table
cur.execute('''CREATE TABLE IF NOT EXISTS Players
                  (Id_Player INTEGER PRIMARY KEY AUTOINCREMENT,
                     Name_Player TEXT NOT NULL,
                        nb_games INTEGER NOT NULL,
                            nb_wins INTEGER NOT NULL,
                                nb_defeats INTEGER NOT NULL,
                                    nb_draws INTEGER NOT NULL)''')

# Crée une table
cur.execute('''CREATE TABLE IF NOT EXISTS Games
                    (Id_Game INTEGER PRIMARY KEY AUTOINCREMENT,
                        Id_Player INTEGER NOT NULL,
                            Result TEXT NOT NULL)''')

# Crée une table Moves
# Avec un mouvement de départ et le mouvement d'arrivée
cur.execute('''CREATE TABLE IF NOT EXISTS Moves
                    (Id_Mouvement INTEGER PRIMARY KEY AUTOINCREMENT,
                        Id_Game INTEGER NOT NULL,
                            Id_Player INTEGER NOT NULL,
                                Number_Move INTEGER NOT NULL,
                                    Move_depart TEXT NOT NULL,
                                        Move_arrivee TEXT NOT NULL,
                                            Type_Piece TEXT NOT NULL)''')

# Valide les changements et ferme la connexion
conn.commit()
conn.close()
