# On importe la librairie chess.com
import chessdotcom

annee = 2023
mois = 4
# On affiche le leaderboard
def leaderboard():
    data = chessdotcom.get_leaderboards()
    print(data.json)

# Importation d'une partie d'un Joueur dans une base de donnée
def import_player_game_history(player_name):
    games = []
    # On récupère l'historique de jeu d'un joueur
    for i in range (2017,2024):
        for j in range (1,13):
            if i <= annee and j <= mois:
                data = chessdotcom.get_player_games_by_month(player_name, i, j)
                # On récupère les données de la partie
                data = data.json
                # On récupère les parties
                if data['games'] != []:
                    # On  ajout dans games les années et le mois depuis data
                    games.append(data['games'])

    print(games)

print(import_player_game_history("Xtemp70"))