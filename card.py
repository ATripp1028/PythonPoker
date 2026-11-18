from rich import box
from rich.panel import Panel
from rich.text import Text

from constants import SUIT_GLYPHS, SUIT_PALETTES


class Card:
    def __init__(self, rank: str, suit: str) -> None:
        self.rank: str = rank
        self.suit: str = suit

    def __str__(self) -> str:
        return f"{self.rank} of {self.suit}"

    def __rich__(self) -> Panel:
        suit_symbol = SUIT_GLYPHS[self.suit]
        color = f"bold {SUIT_PALETTES['classic'][self.suit]}"
        body = Text()
        body.append(f"{self.get_short_rank()}   \n", style=color)
        body.append(f"  {suit_symbol}  \n", style=color)
        body.append(f"   {self.get_short_rank()}\n", style=color)
        return Panel(body, box=box.ROUNDED, width=7, padding=0, style="on white",
            border_style="grey50 on white")

    def get_short_rank(self) -> str:
        match (self.rank):
            case "Ace":
                return "A"
            case "King":
                return "K"
            case "Queen":
                return "Q"
            case "Jack":
                return "J"
            case _:
                return self.rank

    def get_suit_color(self) -> str:
        if self.suit == "Spades" or self.suit == "Clubs":
            return "black"
        return "red"
