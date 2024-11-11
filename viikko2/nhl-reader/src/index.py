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

    print("Players from FIN:\n")

    for player in fin_players:
        print(f"{player.name} team {player.team} goals {player.goals} assists {player.assists}")

if __name__ == "__main__":
    main()
