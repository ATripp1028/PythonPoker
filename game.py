from random import shuffle

from textual.containers import Horizontal, Vertical
from textual.reactive import reactive
from textual.widget import Widget

from card import Card
from constants import HAND_SIZE, RANKS, SUITS, GameStage
from player import Player
from sidebar import Sidebar


class Game(Widget):
    DEFAULT_CSS = """
    Player      { height: 1fr }
    #players    { width: 3fr }
    #sidebar    { width: 1fr }
    Game        { height: 1fr }
    """

    pot = reactive(0)
    game_stage = reactive(GameStage.BETTING_1)

    def __init__(self):
        super().__init__()
        self.deck: list[Card] = []
        self.dealer: Player = Player("dealer")
        self.player: Player = Player("player", True)

    def compose(self):
        yield Horizontal(
            Vertical(
                self.dealer,
                self.player,
                id="players"
            ),
            Sidebar("sidebar"),
            id="game"
        )

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
