from textual.app import App, ComposeResult
from textual.widgets import Footer, Header

from game import Game
from table import Table


class PyPoker(App):
    CSS = """
    Screen  { background: black; }
    """
    BINDINGS = [('ctrl+q', "quit", "Quit")]

    def __init__(self):
        super().__init__()
        self.game: Game = Game()
        deck = self.game.build_deck()
        self.game.shuffle_deck()
        self.game.deal_cards()

    def compose(self) -> ComposeResult:
        yield Header()
        yield Table(self.game)
        yield Footer()

if __name__ == "__main__":
    PyPoker().run()
