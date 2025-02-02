import collections

Card =collections.namedtuple('Card', ['rank','suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamons clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position: int):
        return self._cards[position]



if __name__ == "__main__":

    deck = FrenchDeck()
    print("\nusage of dunder method on deck to get length")
    print(len(deck))

    print("\naccess to check by __getitem__ e.g. deck[0],deck[12]")
    print(deck[0],deck[12])
    assert deck[0] == Card(rank='2', suit='spades')

    from random import choice

    print("\nchoice a random card from deck")
    print(choice(deck))

    print("\ninterate over deck")
    for card in deck: # doctest: +ELLIPSIS
        print(card)

    print("\ndeck in reversed order")
    for card in reversed(deck): # doctest: +ELLIPSIS        
        print(card)

    is_in_deck = Card('Q', "hearts") in deck
    print("\nis_in deck?",is_in_deck)
    assert is_in_deck 


    is_in_deck = Card('Q', "beasts") in deck in deck
    print("\nis_in_deck?",is_in_deck)
    assert not is_in_deck


    suit_values = dict(spades=3, hearts=2, diamons=1, clubs=0)
    def spades_high(card):
        rank_value = FrenchDeck.ranks.index(card.rank)
        return rank_value * len(suit_values) + suit_values[card.suit]

    print("\nSorted deck")
    for card in sorted(deck, key=spades_high):
        print(card)
    



