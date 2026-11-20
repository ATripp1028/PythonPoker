from random import shuffle

from rich.layout import Layout
from rich.panel import Panel

from card import Card
from constants import HAND_SIZE, RANKS, SUITS
from hand import Hand


class Game(object):
    def __init__(self):
        self.deck: list[Card] = []
        self.dealer_hand: Hand = Hand()
        self.player_hand: Hand = Hand()
        self.running: bool = True

    def __rich__(self):
        layout = Layout()
        layout.split(
            Layout(Panel(self.dealer_hand), name="Dealer"),
            Layout(Panel(self.player_hand), name="Player")
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
            self.player_hand.draw_card(deck.pop())
            self.dealer_hand.draw_card(deck.pop())

        return self.player_hand, self.dealer_hand

    def run_game_loop(self) -> bool:
        return True

    def run_game(self):
        while self.running:
            if not self.run_game_loop():
                return
