from rich.align import Align
from rich.console import Group
from rich.columns import Columns
from rich.text import Text

from card import Card


class Hand:
    def __init__(self) -> None:
        self.cards: list[Card] = []

    def __str__(self) -> str:
        card_names: list[str] = []
        for card in self.cards:
            card_names.append(str(card))
        return ", ".join(card_names)

    def __rich__(self):
        slots: list[Group] = []
        for i in range(0, len(self.cards)):
            label = Text(f"[{i + 1}]", "dim")
            slots.append(Group(self.cards[i], Align.center(label, width=7)))
        return Columns(slots, padding=(0,1))

    def draw_card(self, card: Card):
        self.cards.append(card)
