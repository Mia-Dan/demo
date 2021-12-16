# Card game: War (2-PL)
# War is a kids game, relying exclusively on luck of the draw. 
# "Much like real war it's incredibly long and pointless." 

'''Game Rule: 
# Originally written by Ana, but I make a few edits to make it more clear.
Each round, each player will take one card from deck and compare it with the other player. 
    The one with the higher card wins the round, and gives their card to the other player. 
The winner is determined - after numerous rounds - when the deck is empty. 
    The winner is the person with fewer cards in their hand.
'''

# TODO: use a class card
# TODO: implement different card games, like elona's Black Jack

import random

class CardDeck:
    def __init__(self, cardSet=[]):
        '''shuffle cards'''
        self.deck = cardSet.copy()
        random.shuffle(self.deck)

    def getCard(self):
        '''Get a card from one side of deck(list)'''
        if self.deck: return self.deck.pop() 
        else: return

    def compareCards(self, card1, card2):
        ''' Compare 2 cards, return the larger one
            Supposing rank is compared first (2<3<...<9), 
            when rank is equal, compare suit (assume ♠<♣<♥<♦).
            Given each card is unique in a deck, 2 cards will never be equal'''
        if card1 < card2: return card2
        elif card1 > card2: return card1

class Player:
    def __init__(self, name='ano'):
        self.name = name
        self.hand = []
    def addCard2Hand(self, card):
        if card: self.hand.append(card)
    def removeCardFromHand(self, card):
        self.hand.remove(card)
    def handSize(self):
        return len(self.hand)

cardSet = [str(rank)+suit for rank in range(2,10) for suit in '♠♣♥♦'] # for simplicy, AKQJs are excluded
deck = CardDeck(cardSet=cardSet)
pl1 = Player('pl1')
pl2 = Player('pl2')
roundCount = 0

while True:
    pl1Card = deck.getCard()
    pl2Card = deck.getCard()
    pl1.addCard2Hand(pl1Card)
    pl2.addCard2Hand(pl2Card)

    if pl2Card == None:
        print('No cards in deck. The result is:')
        print(f"{pl1.name} has {pl1.handSize()} cards.")
        print(f"{pl2.name} has {pl2.handSize()} cards.")
        if pl1.handSize() > pl2.handSize(): print(f"{pl1.name} wins!")
        elif pl1.handSize() < pl2.handSize(): print(f"{pl2.name} wins!")
        elif pl1.handSize() == pl2.handSize(): print("A tie!")
        break

    else:
        roundCount += 1
        print(f"Round {roundCount}: \t{pl1.name} gets {pl1Card}, {pl2.name} gets {pl2Card}\t", end='')
        if deck.compareCards(pl1Card, pl2Card) == pl1Card:
            pl1.removeCardFromHand(pl1Card)
            pl2.addCard2Hand(pl1Card)
            print(f"Winner: {pl1.name}!")
        else:
            pl2.removeCardFromHand(pl2Card)
            pl1.addCard2Hand(pl2Card)
            print(f"Winner: {pl2.name}!")




