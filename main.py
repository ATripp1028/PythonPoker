from card import Card
from constants import HAND_SIZE, RANKS, SUITS
from hand import Hand
import random
from rich import print


def deal_cards(deck: list[Card]):
    your_hand = Hand()
    dealer_hand = Hand()

    for __i in range(0, HAND_SIZE):
        your_hand.draw_card(deck.pop())
        dealer_hand.draw_card(deck.pop())

    return your_hand, dealer_hand


def main():
    print("Welcome to PythonPoker!")

    deck: list[Card] = []

    for suit in SUITS:
        for rank in RANKS:
            deck.append(Card(rank, suit))

    random.shuffle(deck)

    your_hand, dealer_hand = deal_cards(deck)

    print(dealer_hand)
    print(your_hand)


if __name__ == "__main__":
    main()
