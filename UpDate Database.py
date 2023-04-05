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






import Databases
import ApiChess
import mysql.connector

connection_params = Databases.connection_params

# On importe 1 Joueurs dans la base de données
def import_player(player_name):
    nb_parties = ApiChess.total_games(player_name)
    nb_victoires = ApiChess.won_games(player_name)
    nb_defaites = ApiChess.lost_games(player_name)
    nb_nulles = nb_parties - nb_victoires - nb_defaites
    with mysql.connector.connect(**connection_params) as db :
        cursor = db.cursor()
        cursor.execute("INSERT INTO Joueurs (Nom_Joueurs, nb_parties, nb_victoires, nb_defaites, nb_nulles) VALUES (%s, %s, %s, %s, %s)", (player_name, nb_parties, nb_victoires, nb_defaites, nb_nulles))
        db.commit()
        pass


