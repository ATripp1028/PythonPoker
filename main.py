from datetime import datetime

from rich import print
from rich.layout import Layout
from rich.live import Live
from rich.panel import Panel
from rich.table import Table

from game import Game


def make_layout():
    layout = Layout(name="root")
    layout.split(
        Layout(name="header", size=3),
        Layout(name="main", ratio=1),
        Layout(name="footer", size=7),
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

def main():
    print("Welcome to PythonPoker!")

    layout = make_layout()
    game = Game()

    deck = game.build_deck()
    game.shuffle_deck()

    game.deal_cards(deck)

    layout["header"].update(Header())
    layout["main"].update(game)

    with Live(layout, refresh_per_second=10, screen=True):
        while True:
            continue


if __name__ == "__main__":
    main()
