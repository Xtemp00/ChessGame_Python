# On importe la librairie chess.com
import chessdotcom

# On affiche le leaderboard
def leaderboard():
    data = chessdotcom.get_leaderboards()
    print(data.json)

print(leaderboard())