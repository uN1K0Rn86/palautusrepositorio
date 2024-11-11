from player_reader import PlayerReader
from player_stats import PlayerStats
from rich.console import Console
from rich.table import Table
from rich import print as rprint
from rich.prompt import Prompt

def main():
    console = Console()
    rprint("[italic]NHL statistics by nationality[/italic]")
    season = Prompt.ask("[bold]Select season:[/bold] [green]2018-19 / 2019-20 / 2020-21 / 2021-22 / 2022-23 / 2023-24 / 2024-25 [/green]")
    nationality = Prompt.ask("[bold]Select nationality: [/bold] [green]AUT / CZE / AUS / SWE / GRE / DEN / SUI / SVK / NOR / RUS / CAN / LAT / BLR / SLO / USA / FIN / GBR")
    
    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality(nationality)

    table = Table(title=f"Top scorers of {nationality} season {season}")
    table.add_column("name")
    table.add_column("team")
    table.add_column("goals")
    table.add_column("assists")
    table.add_column("points")
    for player in players:
        table.add_row(player.name, player.team, str(player.goals), str(player.assists), str(player.goals + player.assists))

    console.print(table)

if __name__ == "__main__":
    main()
