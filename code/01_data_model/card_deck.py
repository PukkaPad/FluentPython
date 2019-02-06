# -*- coding: utf-8 -*-
import collections
from random import choice

# Use collections.namedtuple to build a class to represent individual cards
Card = collections.namedtuple('Card', ['rank', 'suit'])
# For example:
# beer_card = Card('7', 'diamonds')
# print(beer_card) # Card(rank='7', suit='diamonds')

class FrenchDeck:
    '''Class to represent a deck of playing cards.'''
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    #print (ranks)
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

deck = FrenchDeck()
print (f'Length of deck is {len(deck)}.')

print ('Reading specific cards from deck: ')
print(f"First card is {deck[0]}")
print(f"Last card is {deck[-1]}")

print("Using Python's function 'random.choice' to pick random items")

print ( f"Random choice of card is  {choice(deck)}")
print ( f"Random choice of card is  {choice(deck)}")

print(f"Slicing is also supported\nTop 3 cards are: ")
print(deck[:3])

print("Start at index 12 and skip 13 cards:")
print(deck[12::13])

in_deck = Card('Q', 'hearts') in deck
print(in_deck)

# print("Iteration is also possible:")
# for card in deck:
#     print(card)

# print("Iteration is also possible (including in reverse):")
# for card in reversed(deck):
#     print(card)

# use __getitem__ to slice the cards:
deck[:3]

deck[12::13]

# # __getitem__ deck is also iterable:
# for card in deck: # doctest: +ELLIPSIS
#     print (card)

# for card in reversed(deck): # doctest: +ELLIPSIS
#     print(card)

# # collection has __contains__ method
# Card('Q', 'hearts') in deck
# Card('7', 'beasts') in deck

# # ranking cards:
# suit_values = dict(spades = 3, hearts = 2, diamonds = 1, clubs = 0)

# def spades_high(cards):
#     rank_value = FrenchDeck.ranks.index(card.rank)
#     return rank_value * len(suit_values) + suit_values[card.suit]

# for card in sorted(deck, key=spades_high):
#     print(card)




