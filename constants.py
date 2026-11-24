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
        "Hearts": "red3",
        "Diamonds": "red3",
        "Clubs": "white",
    },
    "four_color": {
        "Spades": "black",
        "Hearts": "red3",
        "Diamonds": "dark_orange3",
        "Clubs": "dodger_blue2",
    },
}
HAND_SIZE = 5


class GameStage(Enum):
    BETTING_1 = 1
    DISCARD = 2
    BETTING_2 = 3
