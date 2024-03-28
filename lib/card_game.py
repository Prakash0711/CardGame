import random

class Card():
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number
    
    def print_Card(self):
        result_string = self.suit + self.number
        return result_string

class Player():
    def __init__(self):
        self.player_hand = []
    
    def print_hand(self):
        self.player_hand
    
    def add_card(self, card):
        self.player_hand.append(card)

    def remove_card(self, card):
        self.player_hand.remove(card)

#Initiate 3 other players
userplayer = Player()
player2 = Player()
player3 = Player()
player4 = Player()
playerList = [userplayer, player2, player3, player4]




#Generate cards
def generate_Cards():
    suits = ["H", "D", "S", "C"]
    card_numbers = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    result = []
    
    for suit in suits:
        for card in card_numbers:
            tempCard = Card(suit, card)
            result.append(tempCard)

    #print(f"Deck generated + {result}")
    return result

#Shuffle deck using random
def shuffle_deck(lst):
    deck = lst
    random.shuffle(deck)
    return deck

#returns a list in printable format
def print_deck(lst):
    result_list = []
    for card in lst:
        result_list.append(card.print_Card())
    print(result_list)    
    return result_list

#broken for now. The one to work on
def initial_deal_deck(deck, players):
    full_deck = shuffle_deck(deck)
    temp_list = []
    coounter = 0
    for i in range(0, len(full_deck)):
        for player in players:
            player.add_card(full_deck[i])

        counter = 0
        

    
            



deck = generate_Cards()
deck = shuffle_deck(deck)
print_deck(deck)