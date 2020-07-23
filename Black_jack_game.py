# black Jack game

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

ranks = ('Two', 'Three', 'Four', 'Five', 'Six','Seven', 'Eight', 'Nine',
         'Ten', 'Three','Jack', 'Queen', 'King', 'Ace')


values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6,'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10,'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}


playing = True


# 1 card class

class Card():
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank


    def __str__(self):
        return f'{self.rank} of {self.suit}'

test_card = Card('Ace','Two')
print(test_card)

# 2 Deck class

class Deck():

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return 'The deck has : '+deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card

test_deck = Deck()
test_deck.shuffle()
print(test_deck)

# 3 Hand class

class Hand():

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]

        # track aces

        if card.rank == 'Ace':
            self.aces += 1

    def got_aces(self):

        while self.value >21 and self.aces:

            self.value -= 10
            self.aces -= 1

# player

test_player = Hand()
get_card = test_deck.deal()
print(get_card)
test_player.add_card(get_card)
print(test_player.value)

#4 chip class

class Chips():

    def __init__(self,total = 100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

# 5 function for games : function toke games

def take_bet(chips):

    while True:
        try:
            chips.bet = int(input('Hoe much you like to bet in this game : '))

        except :
            print('Enter your value in integer ')

        else:

            if chips.bet > chips.total:
                print('you have not as much chips ')

            else:
                break

def hit(deck,hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.got_aces()

def hit_or_stand(deck,hand):
    global playing

    while True:

        x= input('Hit or Stand ? enter h and s respectively : ')

        if x[0].lower() == 'h':       # 0 denote x ke first elenent ko zero bana do
            hit(deck,hand)

        elif x[0].lower() == 's':
            print('Player wants to stand deal turns ')
            playing = False

        else:
            print("I don't uderstand , plese enter h and s : ")
            continue

        break

# show some or all

def show_some(player,dealer):
    print('\n Dealer hand : ')
    print('< Card Hidden>')
    print('',dealer.cards[1])
    print("\n player's Hand : ",*player.cards, sep= '\n')

def show_all(player,dealer):
    print('\n Dealer Hand : ')
    print('Dealer Hand = ',dealer.value)
    print('n player hand : ',*player.cards, sep= '\n')
    print('players hand = ',player.value)





# player win sanario

def player_wins(player,dealer,chips):
    print('Player Busted!')
    chips.lose_bet()


def player_lose(player,dealer,chips):
    print('Player win ')
    chips.win_bet()


def dealer_wins(player,dealer,chips):
    print('Dealer win')
    chips.win_bet()

def dealer_lose(player,dealer,chips):
    print('Dealer lose')
    chips.lose_bet()

def push(player,dealer):
    print('Its a Push')


# 6 Bulding the logic of the game

while True:
    print('Welcome to the club')

    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())


    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # set player chip
    player_chips = Chips()

    # ask for bet
    take_bet(player_chips)

    # show card

    show_some(player_hand,dealer_hand)

    while playing:
        hit_or_stand(deck,player_hand)
        show_some(player_hand,dealer_hand)

    # cateria for 21

        if player_hand.value > 21:
            player_lose(player_hand,dealer_hand,player_chips)
            break

    # if player has not loss , ask delar to play

        if player_hand.value >= 21:

            while dealer_hand.value < player_hand.value:
                hit(deck,dealer_hand)

    # show all card

        show_all(player_hand,dealer_hand)

    # code for diffreant wonning case

        if dealer_hand.value <21:
            dealer_lose(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)

        else:
            push(player_hand,dealer_hand)

    # inform the playerabout situation

        print(f'\n player total chips are {player_chips.total}')

    # ask the ply to again

    new_game = input('Would you like to play [y/n] : ')

    if new_game[0].lower() == 'y':
        playing = True

        continue

    else:
        print('Thank you for playing , please dont come again')
        break
































































































