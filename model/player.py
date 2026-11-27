from model.hand import Hand


class Player:
    def __init__(self, is_human: bool = False):
        self.hand = Hand()
        self.chips: int = 1000
        self.bet_amount: int = 0
        self.is_human = is_human
