from random import shuffle

from rich.layout import Layout
from rich.panel import Panel
from textual.widget import Widget

from card import Card
from constants import HAND_SIZE, RANKS, SUITS, GameStage
from player import Player


class Game(Widget):
    def __init__(self):
        super().__init__()
        self.deck: list[Card] = []
        self.dealer: Player = Player()
        self.player: Player = Player(True)
        self.running: bool = True
        self.game_stage: GameStage = GameStage.BETTING_1
        self.pot: int = 0

    def render(self):
        layout = Layout()
        layout.split_row(
            Layout(name="Players", ratio=3),
            Panel(f"Pot: {self.pot}")
        )
        layout["Players"].split(
            Layout(Panel(self.dealer.hand), name="Dealer"),
            Layout(Panel(self.player.hand), name="Player")
        )

        return layout

    def build_deck(self):
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(Card(rank, suit))

        return self.deck

    def shuffle_deck(self):
        shuffle(self.deck)

    def deal_cards(self, deck: list[Card]):
        for _i in range(0, HAND_SIZE):
            self.player.hand.draw_card(deck.pop())
            self.dealer.hand.draw_card(deck.pop())

        return self.player.hand, self.dealer.hand
