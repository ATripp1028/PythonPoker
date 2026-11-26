from textual.containers import Horizontal, Vertical
from textual.widget import Widget
from textual.widgets import Static

from layout.card_box import CardBox
from model.card import Card
from model.player import Player


class PlayerPanel(Widget):
    DEFAULT_CSS = """
    CardBox                 { width: auto; height: auto }
    #cards_and_numbers      { align: center top }
    .card-slot {
        width: auto;
        margin-right: 1
    }
    .card-label             { text-align: center }
    """
    def __init__(self, player: Player, id: str, title: str):
        super().__init__(id=id)
        self.player: Player = player
        self.cards: list[Card] = player.hand.cards
        self.is_human: bool = player.is_human
        self.border_title: str = title

    def compose(self):
        with Horizontal(id="cards_and_numbers"):
            for i, card in enumerate(self.cards):
                with Vertical(id=f"card-{i}", classes="card-slot"):
                    yield CardBox(card, f"card-{i}")
                    yield Static(
                        f"[{i + 1}]", id=f"card-{i}-label", classes="card-label"
                    )
