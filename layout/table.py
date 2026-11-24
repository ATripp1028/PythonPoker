from textual.containers import Horizontal, Vertical
from textual.widget import Widget

from layout.player_panel import PlayerPanel
from layout.sidebar import Sidebar
from model.game import Game
from model.player import Player


class Table(Widget):
    DEFAULT_CSS = """
    PlayerPanel     { height: 1fr }
    #game           { height: 1fr }
    #players        { width: 3fr }
    #sidebar        { width: 1fr }
    """

    def __init__(self, game: Game):
        super().__init__()
        self.game: Game = game
        self.dealer: Player = game.dealer
        self.player: Player = game.player

    def compose(self):
        yield Horizontal(
            Vertical(
                PlayerPanel(self.dealer, "dealer"),
                PlayerPanel(player=self.player, id="player"),
                id="players",
            ),
            Sidebar("sidebar"),
            id="game",
        )
