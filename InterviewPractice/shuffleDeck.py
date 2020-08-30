import itertools, random

from pprint import pprint

# Make a deck of cards
#deck = list(itertools.product(range(1,14), ['Spade','Heart','Diamond','Club']))

deck = []
for value in range(1, 14):
    for face in ['Spade', 'Heart', 'Diamond', 'Club']:
        deck.append((value, face))

random.shuffle(deck)

# Draw 5 cards:
print('You Got')
for i in range(5):
    index = random.randint(0, len(deck))
    print(deck[index][0], "of ", deck[index][1])
    deck.pop(index)

print(len(deck))