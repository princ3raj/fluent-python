
''' Implemented a Deck of Cards
    which also implements __getitem__ which inturns get 
    used by for loops, random.choice function and many more.
    __len__ special method is also implemented 
    which in turns gives the ability
    to find the length of a collection/container.
    it can also access elements by its index which 
    uses __getitem__ method to retrieve the value
    our deck also supports slicing as it 
    delegates the task to [] operator
'''

import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

suit_values = dict(spades = 3, hearts = 2, diamonds = 1, club = 0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds club hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks ]
    
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]
