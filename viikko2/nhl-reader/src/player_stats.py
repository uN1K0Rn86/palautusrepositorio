from player import Player

class PlayerStats:
    def __init__(self, reader):
        self.players = reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        nat_players = list(filter(lambda player: player.nationality == nationality, self.players))
        nat_players.sort(key=lambda player: player.goals+player.assists, reverse=True)

        return nat_players