from rich.align import Align
from rich.columns import Columns
from rich.console import Group
from rich.text import Text
from textual.app import RenderResult
from textual.containers import Horizontal, Vertical
from textual.content import Content
from textual.widget import Widget
from textual.widgets import Static

from layout.card_box import CardBox
from model.card import Card
from model.player import Player


class PlayerPanel(Widget):
    DEFAULT_CSS = """
    CardBox                 { width: auto; height: auto }
    #cards_and_numbers      { align: center top }
    Vertical {
        align-horizontal: center;
        width: auto;
        margin-right: 1
    }
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
                with Vertical(id=f"card-{i}"):
                    yield CardBox(card, f"card-{i}")
                    yield Static(f"[{i + 1}]", id=f"card-{i}-label")

    # def render(self) -> RenderResult:
    #     slots: list[Group] = []
    #     for i, card in enumerate(self.cards):
    #         label = Text(f"[{i + 1}]", "dim white")
    #         slots.append(Group(CardBox(card), Align.center(label, width=7)))

    #     return Columns(slots, padding=(0, 1))
