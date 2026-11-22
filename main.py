from textual.app import App, ComposeResult
from textual.widgets import Footer, Header

from game import Game


class PyPoker(App):
    CSS = """
    Screen  { background: black; }
    #header { height: 3; }
    #main   { height: 1fr; }
    """
    BINDINGS = [('ctrl+q', "quit", "Quit")]

    def __init__(self):
        super().__init__()
        self.game: Game = Game()
        deck = self.game.build_deck()
        self.game.shuffle_deck()
        self.game.deal_cards(deck)

    def compose(self) -> ComposeResult:
        yield Header()
        yield self.game
        yield Footer()

if __name__ == "__main__":
    PyPoker().run()
