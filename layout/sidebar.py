from textual.app import RenderResult
from textual.content import Content
from textual.widget import Widget

from model.game import Game


class Sidebar(Widget):
    def __init__(self, id: str, game: Game) -> None:
        super().__init__(id=id)
        self.game: Game = game

    def render(self) -> RenderResult:
        return Content(text=f"Pot: {self.game.pot}")
