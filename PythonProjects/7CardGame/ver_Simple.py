# This is a simple implementation of card game War,
#   that doesn't involve any use of classes.
# Still, it is sufficient to capture the whole idea of War.

import random
# len(cardSet) should be even; otherwise, the game would be unfair
cardSet = [str(rank)+suit for rank in range(2,10) for suit in '♠♣♥♦'] 
deck = cardSet.copy()
random.shuffle(deck)
# print(deck)

'''for each game'''
pl1 = {'name':'pl1', 'currentCard':'', 'nDefeated':0}
pl2 = {'name':'pl2', 'currentCard':'', 'nDefeated':0}
roundCount = 0
while deck:
    '''for each round'''
    pl1['currentCard'] = deck.pop()
    pl2['currentCard'] = deck.pop()
    if pl1['currentCard'] < pl2['currentCard']:
        pl1['nDefeated'] +=1; winner = pl2['name']
    elif pl1['currentCard'] > pl2['currentCard']:
        pl2['nDefeated'] +=1; winner = pl1['name']
    roundCount += 1
    print(f"Round {roundCount}: \t{pl1['name']} gets {pl1['currentCard']}, {pl2['name']} gets {pl2['currentCard']}\tWinner: {winner}! ")

print('No cards in deck. The result is:')
if pl1['nDefeated']<pl2['nDefeated']:
    print(f"{pl1['name']} wins!")
elif pl1['nDefeated']>pl2['nDefeated']:
    print(f"{pl2['name']} wins!")
else:
    print('Draw!')
