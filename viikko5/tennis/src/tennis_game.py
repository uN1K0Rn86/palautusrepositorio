class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1_score = 0
        self.p2_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.p1_score = self.p1_score + 1
        else:
            self.p2_score = self.p2_score + 1

    def get_score(self):
        return ScoreFactory(self).retrieve()

class ScoreFactory:
    def __init__(self, game):
        self.p1_score = game.p1_score
        self.p2_score = game.p2_score
        self.win_threshold = 4

    def retrieve(self):
        if self.p1_score == self.p2_score:
            return Even(self.p1_score).deliver()

        elif self.p1_score >= self.win_threshold or self.p2_score >= self.win_threshold:
            return Advantage(self.p1_score, self.p2_score).deliver()

        else:
            return InProgress(self.p1_score, self.p2_score).deliver()
        
class Even:
    def __init__(self, p1_score):
        self.p1_score = p1_score

        self.scores = {
            0: "Love-All",
            1: "Fifteen-All",
            2: "Thirty-All"
        }

    def deliver(self):
        if self.p1_score in self.scores:
            return self.scores[self.p1_score]
        else:
            return "Deuce"
        
class Advantage:
    def __init__(self, p1_score, p2_score):
        self.adv = p1_score - p2_score

    def deliver(self):
        if self.adv == 1:
            return "Advantage player1"
        elif self.adv == -1:
            return "Advantage player2"
        elif self.adv >= 2:
            return "Win for player1"
        else: 
            return "Win for player2"
        
class InProgress:
    def __init__(self, p1_score, p2_score):
        self.p1_score = p1_score
        self.p2_score = p2_score

        self.scores = {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty"
        }

    def deliver(self):
        return f"{self.scores[self.p1_score]}-{self.scores[self.p2_score]}"