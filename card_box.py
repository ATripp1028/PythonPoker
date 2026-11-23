from rich import box
from rich.panel import Panel
from rich.text import Text

from card import Card
from constants import SUIT_GLYPHS, SUIT_PALETTES


class CardBox:
    def __init__(self, card: Card):
        self.card: Card = card

    def __rich__(self) -> Panel:
        suit_symbol = SUIT_GLYPHS[self.card.suit]
        color = f"bold {SUIT_PALETTES['classic'][self.card.suit]}"
        body = Text()
        short_rank = self.get_short_rank()
        body.append(f"{short_rank}\n\n", style=color)
        body.append(f"   {suit_symbol}\n\n", style=color)
        body.append(
            f"     {'' if short_rank == '10' else ' '}{short_rank}",
            style=color
        )
        return Panel(body, box=box.ROUNDED, width=9, padding=0,
            border_style="white")

    def get_short_rank(self) -> str:
        match (self.card.rank):
            case "Ace":
                return "A"
            case "King":
                return "K"
            case "Queen":
                return "Q"
            case "Jack":
                return "J"
            case _:
                return self.card.rank
