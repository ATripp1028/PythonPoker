from textual.widget import Widget
from textual.widgets import Static

from constants import SUIT_GLYPHS, SUIT_PALETTES
from model.card import Card


class CardBox(Widget):
    DEFAULT_CSS = """
    Static  { border: round white; width: 9; text-align: center }
    .red    { color: red }
    .white  { color: white }
    .orange { color: darkorange }
    .blue   { color: dodgerblue }
    """
    def __init__(self, card: Card, id: str):
        super().__init__()
        self.card: Card = card
        self.id: str = id

    def compose(self):
        suit_symbol = SUIT_GLYPHS[self.card.suit]
        short_rank = self.get_short_rank()
        body = "\n".join([
            f"{short_rank}      ",
            "",
            f"{suit_symbol}",
            "",
            f"     {'' if short_rank == '10' else ' '}{short_rank}"
        ])
        yield Static(
            content=body,
            classes=f"{SUIT_PALETTES['classic'][self.card.suit]}"
        )

    def get_short_rank(self) -> str:
        match self.card.rank:
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
