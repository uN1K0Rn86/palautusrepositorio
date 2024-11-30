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
        win_threshold = 4
        score = ""
        temp_score = 0

        if self.p1_score == self.p2_score:
            score = ScoreFactory(self).retrieve("even")

        elif self.p1_score >= win_threshold or self.p2_score >= win_threshold:
            score = ScoreFactory(self).retrieve("adv")

        else:
            for i in range(1, 3):
                if i == 1:
                    temp_score = self.p1_score
                else:
                    score = score + "-"
                    temp_score = self.p2_score

                if temp_score == 0:
                    score = score + "Love"
                elif temp_score == 1:
                    score = score + "Fifteen"
                elif temp_score == 2:
                    score = score + "Thirty"
                elif temp_score == 3:
                    score = score + "Forty"

        return score

class ScoreFactory:
    def __init__(self, game):
        self.p1_score = game.p1_score
        self.p2_score = game.p2_score
        self.win_threshold = 4

    def retrieve(self, prev_score):
        if prev_score == "even":
            return Even(self.p1_score).deliver()
        elif self.p1_score >= self.win_threshold or self.p2_score >= self.win_threshold:
            return Advantage(self.p1_score, self.p2_score).deliver()
        
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