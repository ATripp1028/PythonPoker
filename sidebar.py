from rich.panel import Panel
from rich.text import Text
from textual.app import RenderResult
from textual.widget import Widget


class Sidebar(Widget):
    def __init__(self, id: str) -> None:
        super().__init__(id=id)

    def render(self) -> RenderResult:
        text = Text("Test")

        return Panel(text)
