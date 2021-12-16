# This is a simple implementation of card game War,
#   that doesn't involve any use of classes.
# Still, it is sufficient to capture the whole idea of War.

# TODO: use class - some have been written... accidently
# with card objects
# see draft paper

import random
# len(cardSet) should be even; otherwise, the game would be unfair
cardSet = [str(rank)+suit for rank in range(2,10) for suit in '♠♣♥♦'] 
deck = cardSet.copy()
random.shuffle(deck)

# for each game,
pl1 = {'name':'pl1', 'currentCard':'', 'nDefeated':0}
pl2 = {'name':'pl2', 'currentCard':'', 'nDefeated':0}
while cardSet:
    '''for each round'''
    pl1.currentCard = deck.pop()
    pl2.currentCard = deck.pop()
    if pl1.currentCard < pl2.currentCard:
        pl1.nDefeated +=1
    elif pl1.currentCard > pl2.currentCard:
        pl2.nDefeated +=1

print('No cards in deck. The result is:')
if pl1.nDefeated<pl2.nDefeated:
    print(f'{pl1.name} wins!')
elif pl1.nDefeated>pl2.nDefeated:
    print(f'{pl2.name} wins!')
else:
    print('Draw!')