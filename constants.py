from enum import Enum

RANKS = ["Ace", "King", "Queen", "Jack", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
SUITS = ["Spades", "Hearts", "Diamonds", "Clubs"]
SUIT_GLYPHS = {
    "Spades": "\u2660",
    "Hearts": "\u2665",
    "Diamonds": "\u2666",
    "Clubs": "\u2663",
}
SUIT_PALETTES = {
    "classic": {
        "Spades": "white",
        "Hearts": "red",
        "Diamonds": "red",
        "Clubs": "white",
    },
    "four_color": {
        "Spades": "white",
        "Hearts": "red",
        "Diamonds": "orange",
        "Clubs": "blue",
    },
}
HAND_SIZE = 5


class GameStage(Enum):
    BETTING_1 = 1
    DISCARD = 2
    BETTING_2 = 3
