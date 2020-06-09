# -*- conding: UTF -8 -*-
from Machine.standard_machine import *
deck = []
create_deck(deck)
record_deck(deck, 'deck_recorded1.txt')
shuffled_deck(deck)
record_deck(deck, 'deck_recorded2.txt')
print(deck)
