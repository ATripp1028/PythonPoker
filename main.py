import random
from datetime import datetime

from rich import print
from rich.layout import Layout
from rich.live import Live
from rich.panel import Panel
from rich.table import Table

from card import Card
from constants import HAND_SIZE, RANKS, SUITS
from hand import Hand


def make_layout():
    layout = Layout(name="root")
    layout.split(
        Layout(name="header", size=3),
        Layout(name="main", ratio=1),
        Layout(name="footer", size=7),
    )
    layout["main"].split(
        Layout(name="Dealer", ratio=1),
        Layout(name="Player", ratio=1)
    )

    return layout

class Header:
    """Display header with clock."""

    def __rich__(self) -> Panel:
        grid = Table.grid(expand=True)
        grid.add_column(justify="center", ratio=1)
        grid.add_column(justify="right")
        grid.add_row(
            "[b]PyPoker[/b]",
            datetime.now().ctime().replace(":", "[blink]:[/]"),
        )
        return Panel(grid, style="black on red")

def build_hands(player_hand, dealer_hand):
    pass

def deal_cards(deck: list[Card]):
    your_hand = Hand()
    dealer_hand = Hand()

    for __i in range(0, HAND_SIZE):
        your_hand.draw_card(deck.pop())
        dealer_hand.draw_card(deck.pop())

    return your_hand, dealer_hand


def main():
    print("Welcome to PythonPoker!")

    layout = make_layout()

    deck: list[Card] = []

    for suit in SUITS:
        for rank in RANKS:
            deck.append(Card(rank, suit))

    random.shuffle(deck)

    your_hand, dealer_hand = deal_cards(deck)

    layout["header"].update(Header())

    with Live(layout, refresh_per_second=10, screen=True):
        while True:
            continue


if __name__ == "__main__":
    main()
