from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, Input, Static

from constants import GameStage
from game import Game


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
        yield Header()
        yield Static(self.game, id="main")
        yield Footer()

    def on_input_submitted(self, event: Input.Submitted):
        input = event.value

        if self.game.game_stage == GameStage.BETTING_1:
            bet = int(input)


        event.input.value = ""
        self.query_one("#main", Static).refresh() # I have a feeling I'll need to
        # refactor this later to fix stuttering/flickering

if __name__ == "__main__":
    PyPoker().run()
