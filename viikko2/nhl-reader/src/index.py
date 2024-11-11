import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players"
    response = requests.get(url).json()

    fin_players = []

    for player_dict in response:
        player = Player(player_dict)
        if player.nationality == "FIN":
            fin_players.append(player)

    fin_players.sort(key=lambda player: player.goals+player.assists, reverse=True)

    print("Players from FIN:\n")

    for player in fin_players:
        print(player)

if __name__ == "__main__":
    main()
