from textual.containers import Vertical
from textual.validation import Number
from textual.widget import Widget
from textual.widgets import Input

from layout.card_row import CardRow
from model.player import Player


class PlayerPanel(Widget):
    DEFAULT_CSS = """
    #cards_and_numbers  { align: center top; height: 12 }
    #bet {
        width: 100%;
        border: round blue;
        dock: bottom;
        background: transparent
    }
    CardRow             { height: auto }
    """
    def __init__(self, player: Player, id: str, title: str):
        super().__init__(id=id)
        self.player: Player = player
        self.chips: int = player.chips
        self.is_human: bool = player.is_human
        self.border_title: str = title

    def compose(self):
        with Vertical(id="panel"):
            yield CardRow(self.player.hand.cards)
            if self.is_human:
                yield Input(
                    id="bet",
                    placeholder="Enter bet...",
                    type="integer",
                    validators=[
                        Number(
                            self.chips if self.chips < 20 else 20,
                            self.chips
                        )
                    ],
                    name="Bet"
                )
