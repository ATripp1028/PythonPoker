from textual.widget import Widget
from textual.widgets import Input

from layout.card_row import CardRow
from model.card import Card
from model.player import Player


class PlayerPanel(Widget):
    DEFAULT_CSS = """
    #cards_and_numbers  { align: center top }
    """
    def __init__(self, player: Player, id: str, title: str):
        super().__init__(id=id)
        self.player: Player = player
        self.cards: list[Card] = player.hand.cards
        self.is_human: bool = player.is_human
        self.border_title: str = title

    def compose(self):
        yield CardRow(self.player.hand.cards)
        yield Input()
