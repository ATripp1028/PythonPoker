from rich.panel import Panel
from rich.table import Table

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
        pass

    def draw_card(self, card: Card):
        self.cards.append(card)
