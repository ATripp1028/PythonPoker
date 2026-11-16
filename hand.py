from card import Card


class Hand:
    def __init__(self) -> None:
        self.cards = []

    def __str__(self) -> str:
        card_names = []
        for card in self.cards:
            card_names.append(str(card))
        return ", ".join(card_names)

    def draw_card(self, card: Card):
        self.cards.append(card)
