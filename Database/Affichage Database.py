# On code un Programme capable de lire un fichier .db et d'en sortir un affichage
# On Commence par récupérer le fichier .db
import sqlite3
def get_db():
    conn = sqlite3.connect('Chess.db')
    return conn

# On récupère les données de la table Players
def get_players():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Players")
    data = cur.fetchall()
    conn.close()
    return data

# On affiche les données de la table Players
def display_players():
    data = get_players()
    print("Id_Player", "Name_Player", "nb_games", "nb_wins", "nb_defeats", "nb_draws")
    for row in data:
        print(row[0], row[1], row[2], row[3], row[4], row[5])

# On récupère les données de la table Games
def get_games():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Games")
    data = cur.fetchall()
    conn.close()
    return data

# On affiche les données de la table Games
def display_games():
    data = get_games()
    print("Id_Game", "Id_Player", "Result")
    for row in data:
        print(row[0], row[1], row[2])

# On récupère les données de la table Moves
def get_moves():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Moves")
    data = cur.fetchall()
    conn.close()
    return data

# On affiche les données de la table Moves
def display_moves():
    data = get_moves()
    print("Id_Move", "Id_Game", "Id_Player", "Number_Move", "Move_depart", "Move_arrivee", "Type_Piece")
    for row in data:
        print(row[0], row[1], row[2], row[3], row[4], row[5])

display_players()
display_games()
display_moves()