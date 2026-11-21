from random import shuffle

from rich.layout import Layout
from rich.panel import Panel

from card import Card
from constants import HAND_SIZE, RANKS, SUITS, GameStage
from player import Player


class Game(object):
    def __init__(self):
        self.deck: list[Card] = []
        self.dealer: Player = Player()
        self.player: Player = Player(True)
        self.running: bool = True
        self.game_stage: GameStage = GameStage.BETTING_1
        self.pot: int = 0

    def __rich__(self):
        layout = Layout()
        layout.split(
            Layout(Panel(self.dealer.hand), name="Dealer"),
            Layout(Panel(self.player.hand), name="Player")
        )

        return layout

    def handle_q_press(self):
        self.running = False

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

    def run_game_loop(self) -> bool:
        return True

    def run_game(self):
        while self.running:
            if not self.run_game_loop():
                return
