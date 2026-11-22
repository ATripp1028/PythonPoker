from rich.layout import Layout
from rich.panel import Panel
from textual.app import RenderResult
from textual.widget import Widget
from textual.widgets import Input

from hand import Hand


class Player(Widget):
    def __init__(self, id: str, is_human: bool = False):
        super().__init__(id=id)
        self.hand = Hand()
        self.chips: int = 1000
        self.bet: int = 0
        self.is_human = is_human

    def bet_chips(self, chips: int):
        self.bet = chips
        self.chips -= self.bet

    def render(self) -> RenderResult:
        return Panel(self.hand)
