from textual.widget import Widget
from textual.widgets import Static

from constants import SUIT_GLYPHS, SUIT_PALETTES
from model.card import Card


class CardBox(Widget):
    DEFAULT_CSS = """
    Static  { border: round white; width: auto; text-align: center; text-style: dim }
    """
    def __init__(self, card: Card, id: str):
        super().__init__()
        self.card: Card = card
        self.id: str = id

    # def __rich__(self) -> Panel:
    #     suit_symbol = SUIT_GLYPHS[self.card.suit]
    #     color = f"bold {SUIT_PALETTES['classic'][self.card.suit]}"
    #     body = Text()
    #     short_rank = self.get_short_rank()
    #     body.append(f"{short_rank}\n\n", style=color)
    #     body.append(f"   {suit_symbol}\n\n", style=color)
    #     body.append(
    #         f"     {'' if short_rank == '10' else ' '}{short_rank}", style=color
    #     )
    #     return Panel(body, box=box.ROUNDED, width=9, padding=0, border_style="white")

    def compose(self):
        suit_symbol = SUIT_GLYPHS[self.card.suit]
        short_rank = self.get_short_rank()
        body = "\n".join([
            f"{short_rank}",
            "",
            f"   {suit_symbol}",
            "",
            f"     {'' if short_rank == '10' else ' '}{short_rank}"
        ])
        yield Static(content=body, id=self.id)

    def on_mount(self):
        card = self.query_one(f"#{self.id}", Static)
        card.styles.color = f"{SUIT_PALETTES['classic'][self.card.suit]}"
        card.styles.text_style = "bold"


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
