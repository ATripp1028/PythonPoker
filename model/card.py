class Card:
    def __init__(self, rank: str, suit: str) -> None:
        self.rank: str = rank
        self.suit: str = suit

    def __str__(self) -> str:
        return f"{self.rank} of {self.suit}"
