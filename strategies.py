class BaseStrategy:
    def choose_bid(self, hand):
        return hand[-1]

class HumanStrategy(BaseStrategy):
    def choose_bid(self, hand):
        print("Your hand:", hand)
        bid = input("Choose a card to bid: ")
        while bid not in hand:
            print("Invalid bid. Choose a card from your hand.")
            bid = input("Choose a card to bid: ")
        return bid

class SimpleAI(BaseStrategy):
    def choose_bid(self, hand):
        return hand[-1]
