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

    def __rich__(self):
        layout = Layout()
        layout.split(
            Layout(name="Dealer", ratio=1),
            Layout(name="Player", ratio=1)
        )

        return Panel(layout)


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
