from rich.align import Align
from rich.columns import Columns
from rich.console import Group
from rich.panel import Panel
from rich.text import Text
from textual.app import RenderResult
from textual.widget import Widget

from layout.card_box import CardBox
from model.card import Card
from model.player import Player


class PlayerPanel(Widget):
    def __init__(self, player: Player, id: str):
        super().__init__(id=id)
        self.player: Player = player
        self.cards: list[Card] = player.hand.cards

    def render(self) -> RenderResult:
        slots: list[Group] = []
        for i, card in enumerate(self.cards):
            label = Text(f"[{i + 1}]", "dim")
            slots.append(Group(CardBox(card), Align.center(label, width=7)))

        return Panel(Columns(slots, padding=(0, 1)))
