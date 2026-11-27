from textual.containers import Horizontal, Vertical
from textual.widget import Widget
from textual.widgets import Input

from layout.player_panel import PlayerPanel
from layout.sidebar import Sidebar
from model.game import Game
from model.player import Player


class Table(Widget):
    DEFAULT_CSS = """
    PlayerPanel     { height: 1fr; border: round; border-title-align: center }
    #game           { height: 1fr }
    #players        { width: 3fr }
    #dealer         { border: round red }
    #you            { border: round green }
    #sidebar        { width: 1fr; border: round white }
    .hidden         { visibility: hidden }
    .error          { border: round red }
    """

    def __init__(self, game: Game):
        super().__init__()
        self.game: Game = game
        self.dealer: Player = game.dealer
        self.player: Player = game.player

    def compose(self):
        with Horizontal(id="game"):
            with Vertical(id="players"):
                yield PlayerPanel(player=self.dealer, id="dealer", title="Dealer")
                yield PlayerPanel(player=self.player, id="you", title="You")
            yield Sidebar("sidebar", game=self.game)

    def on_input_submitted(self, event: Input.Changed):
        print(event)
        if event.validation_result is None:
            return
        if event.validation_result.is_valid:
            self.game.bet(self.player, int(event.value))
            self.hide_betting_input()
            self.update()

    def hide_betting_input(self):
        self.query_one("#bet", Input).add_class("hidden")

    def update(self):
        self.query_one("#sidebar", Sidebar).refresh()
