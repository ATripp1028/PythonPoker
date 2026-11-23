from random import shuffle

from constants import HAND_SIZE, RANKS, SUITS, GameStage
from model.card import Card
from model.player import Player


class Game:
    def __init__(self):
        super().__init__()
        self.deck: list[Card] = []
        self.dealer: Player = Player()
        self.player: Player = Player(True)
        self.pot: int = 0
        self.game_stage: GameStage = GameStage.BETTING_1

    def build_deck(self):
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(Card(rank, suit))

        return self.deck

    def shuffle_deck(self):
        shuffle(self.deck)

    def deal_cards(self):
        for _i in range(0, HAND_SIZE):
            self.player.hand.draw_card(self.deck.pop())
            self.dealer.hand.draw_card(self.deck.pop())

        return self.player.hand, self.dealer.hand
