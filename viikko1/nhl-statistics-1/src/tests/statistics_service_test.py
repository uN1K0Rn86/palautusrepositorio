import unittest
from statistics_service import StatisticsService
from player import Player
from enum import Enum

class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_found(self):
        jerry = self.stats.search("Kurri")
        self.assertEqual(jerry.name, Player("Kurri", "EDM", 37, 53).name)

    def test_search_none(self):
        modano = self.stats.search("Modano")
        self.assertEqual(modano, None)

    def test_team(self):
        edm = self.stats.team("EDM")
        self.assertEqual(edm[0].name, "Semenko")

    def test_top(self):
        points = self.stats.top(4)
        self.assertEqual(points[4].name, "Semenko")

    def test_top_goals(self):
        goals = self.stats.top(4, SortBy.GOALS)
        self.assertEqual(goals[0].name, "Lemieux")

    def test_top_assists(self):
        assists = self.stats.top(4, SortBy.ASSISTS)
        self.assertEqual(assists[1].name, "Yzerman")