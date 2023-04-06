# On importe la librairie chess.com
import chessdotcom

annee = 2023
mois = 4
games = []
# On affiche le leaderboard
def leaderboard():
    data = chessdotcom.get_leaderboards()
    print(data.json)

# Importation d'une partie d'un Joueur dans une base de donnée
def import_player_game_history(player_name):
    global games  # on utilise la variable globale
    # On récupère l'historique de jeu d'un joueur
    for i in range(2017, 2024):
        for j in range(1, 13):
            if i <= annee and j <= mois:
                data = chessdotcom.get_player_games_by_month(player_name, i, j)
                # On récupère les données de la partie
                data = data.json
                # On récupère les parties
                if data['games'] != []:
                    # On  ajout dans games les années et le mois depuis data
                    games.append(data['games'])

# On créer une fonction qui renvoie toutes les urls des parties en fonction du nom du joueurs
def urls_getter(player_name):
    urls = []
    for i in range (len(games)):
        for j in range (len(games[i])):
            urls.append(games[i][j]['url'])
    return urls
# On créait une fonction qui récupère la partie pgn en fonction de l'historique du joueur
def pgn_getter(player_name):
    pgn = []
    for i in range (len(games)):
        for j in range (len(games[i])):
            pgn.append(games[i][j]['pgn'])
    return pgn

# On exploite les données du fichier pgn pour en extraire les mouvements de toute les parties
def moves_getter(player_name):
    pgn = pgn_getter(player_name)
    moves = []
    # On récupère les informations de la partie a partir de la 22ème ligne
    for i in range (len(pgn)):
        pgn[i] = pgn[i].splitlines()[22:]
        # On récupère les mouvements de la partie
        for j in range (len(pgn[i])):
            moves.append(pgn[i][j])
    # On supprime le dictionnaire des temps
    return moves

# On récupère le nom des joueurs de chaque partie
def players_getter(player_name):
    players = []
    for i in range (len(games)):
        for j in range (len(games[i])):
            players.append(games[i][j]['white']['username'])
            players.append(games[i][j]['black']['username'])
    return players

# On récupère le nombre de partie total
def total_games(player_name):
    total = 0
    for i in range (len(games)):
        total += len(games[i])
    return total


# On récupère le nombre de partie gagné
def won_games(player_name):
    won = 0
    for i in range (len(games)):
        for j in range (len(games[i])):
            if games[i][j]['white']['result'] == 'win':
                # On verifie que le joueur n'est pas player_name
                if games[i][j]['white']['username'] == player_name:
                    won += 1
            elif games[i][j]['black']['result'] == 'win':
                if games[i][j]['white']['username'] == player_name:
                    won += 1
    return won

# On récupère le nombre de partie perdu
def lost_games(player_name):
    lost = 0
    for i in range (len(games)):
        for j in range (len(games[i])):
            if games[i][j]['white']['result'] == 'checkmated':
                if games[i][j]['white']['username'] == player_name:
                    lost += 1
            elif games[i][j]['black']['result'] == 'checkmated':
                if games[i][j]['white']['username'] == player_name:
                    lost += 1
    return lost

# On récupère le nombre de partie nul
def draw_games(player_name):
    draw = 0
    for i in range (len(games)):
        for j in range (len(games[i])):
            if games[i][j]['white']['result'] == 'draw':
                draw += 1
            elif games[i][j]['black']['result'] == 'draw':
                draw += 1
    return draw

#On récupère les mouvements d'un partie unique et le resultat et le nom du gagant et du perdant de la partie a partie de l'histoirique du joueur
def moves_getter_unique(player_name, game_number):
    pgn = pgn_getter(player_name)
    moves = []
    # On récupère les informations de la partie a partir de la 22ème ligne
    pgn[game_number] = pgn[game_number].splitlines()[22:]
    # On récupère les mouvements de la partie
    for j in range (len(pgn[game_number])):
        moves.append(pgn[game_number][j])

    # On récupère le nom du gagnat et perdant ou null sinon
    if moves[len(moves)-1] == '1/2-1/2':
        winner = 'draw'
        loser = 'draw'
    else:
        winner = moves[len(moves)-1].split(' ')[0]
        loser = moves[len(moves)-1].split(' ')[2]
    return moves, winner, loser


# On récupère le resultat du match si le joueur a gagné, perdu ou null
def result_getter(player_name):
    game_number = 0
    list = []
    # Pour chaque partie du joueur, on regarde si le joueur a gagné, perdu ou null
    for i in range(len(games)):
        for j in range(len(games[i])):
            if games[i][j]['white']['result'] == 'checkmated':
                if games[i][j]['white']['username'] == player_name:
                    list.append('lost')
            elif games[i][j]['black']['result'] == 'checkmated':
                if games[i][j]['white']['username'] == player_name:
                    list.append('lost')
            if games[i][j]['white']['result'] == 'win':
                # On verifie que le joueur n'est pas player_name
                if games[i][j]['white']['username'] == player_name:
                    list.append('won')
            elif games[i][j]['black']['result'] == 'win':
                if games[i][j]['white']['username'] == player_name:
                    list.append('won')
            else:
                list.append('draw')
    return list

#import_player_game_history("Xtemp70")
#print(games)