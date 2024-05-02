import random

class DiamondsGame:
    def __init__(self, num_players):
        self.num_players = num_players
        self.deck = self.create_deck()
        self.hands = self.deal_hands()
        self.scores = [0] * num_players
        self.current_round = 0
    
    def create_deck(self):
        suits = ['S', 'H', 'D', 'C']
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        deck = [(value, suit) for suit in suits for value in values]
        random.shuffle(deck)
        return deck
    
    def deal_hands(self):
        hands = [self.deck[i::self.num_players] for i in range(self.num_players)]
        return hands
    
    def start_game(self):
        while not self.game_over():
            self.play_round()
        self.calculate_scores()
    
    def play_round(self):
        current_card = self.deck.pop()
        bids = []
        for i in range(self.num_players):
            bid = self.hands[i].pop()
            bids.append((bid, i))
        bids.sort(reverse=True)
        winning_bid = bids[0]
        if bids.count(winning_bid) > 1:
            points = 1
        else:
            points = self.card_value(current_card)
        self.scores[winning_bid[1]] += points
        self.current_round += 1
    
    def card_value(self, card):
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        return values.index(card[0]) + 2
    
    def calculate_scores(self):
        print("Final scores:")
        for i, score in enumerate(self.scores):
            print(f"Player {i+1}: {score}")
    
    def game_over(self):
        return self.current_round == len(self.hands[0])
