from datetime import datetime

from rich.layout import Layout
from rich.panel import Panel
from rich.table import Table
from textual.app import App, ComposeResult
from textual.widgets import Input, Static

from game import Game


def make_layout():
    layout = Layout(name="root")
    layout.split(
        Layout(name="header", size=3),
        Layout(name="main", ratio=1),
        Layout(name="footer", size=7),
    )

    return layout

class Header:
    """Display header with clock."""

    def __rich__(self) -> Panel:
        grid = Table.grid(expand=True)
        grid.add_column(justify="center", ratio=1)
        grid.add_column(justify="right")
        grid.add_row(
            "[b]PyPoker[/b]",
            datetime.now().ctime().replace(":", "[blink]:[/]"),
        )
        return Panel(grid, style="black on red")

class PyPoker(App):
    CSS = """
    Screen  { background: black; }
    #header { height: 3; }
    #main   { height: 1fr; }
    #bet    { dock: bottom; }
    """
    BINDINGS = [('ctrl+q', "quit", "Quit")]

    def __init__(self):
        super().__init__()
        self.game: Game = Game()
        deck = self.game.build_deck()
        self.game.shuffle_deck()
        self.game.deal_cards(deck)

    def compose(self) -> ComposeResult:
        yield Static(Header(), id="header")
        yield Static(self.game, id="main")
        yield Input(placeholder="Enter bet...", id="bet")

    def on_mount(self):
        self.set_interval(1, lambda: self.query_one("#header", Static).update(Header()))

    def on_input_submitted(self, event: Input.Submitted):
        bet = event.value
        event.input.value = ""
        self.query_one("#main", Static).refresh() # I have a feeling I'll need to
        # refactor this later to fix stuttering/flickering

if __name__ == "__main__":
    PyPoker().run()
