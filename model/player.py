from model.hand import Hand


class Player:
    def __init__(self, is_human: bool = False):
        self.hand = Hand()
        self.chips: int = 1000
        self.bet: int = 0
        self.is_human = is_human

    def bet_chips(self, chips: int):
        self.bet = chips
        self.chips -= self.bet
