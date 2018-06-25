
# coding: utf-8

# In[13]:


from card import ALL_CARDS
import random
from agent import Agent
from card import *
from card import _suit
from game import Game
from collections import Counter

def nn(x):
    return 15 if x == 1 else x

class MyAgent(Agent):
    def play(self, cards_you_have, cards_played, heart_broken, info):
        cards = Game.get_legal_moves(cards_you_have, cards_played, heart_broken)      
        cs = cards[:]
        if len(info.rounds) == 0:
            cs = sorted(cs, key = lambda c: _suit[c.suit] * 15 - nn(c.number))
            if len(cs) == 1:
                return cs[0]
            elif _suit[cs[0].suit] == 0:
                return cs[0]
            elif Card('♠', 12) in cs:
                return Card('♠', 12)
            else:
                cnt = Counter(cs)
                s = min([cnt[x], x] for x in cnt)[1]
                cs = sorted(cs, key = lambda c: (_suit[c.suit] != s))
                return cs[0]
        elif len(info.rounds) == 2 or 3 or 4 or 5:
            if len(cards_played) == 0: # my turn                                       
                cs = sorted(cs, key = lambda c: nn(c.number) * 5 - _suit[c.suit])
                return cs[0]
            if _suit[cards_played[0].suit] == 2:                                    
                if Card('♠', 13) in cards_played or Card('♠', 1) in cards_played:
                    if Card('♠', 12) in cs:
                        return Card('♠', 12)
                cs = sorted(cs, key = lambda c: -(_suit[c.suit] * 15 + nn(c.number)))
                if _suit[cs[0].suit] == 3:
                    return cs[0]
                cs = sorted(cs, key = lambda c: nn(c.number))
                return cs[-1]
            if _suit[cards_played[0].suit] == 3:
                cs = sorted(cs, key = lambda c: nn(c.number))
                if _suit[cs[0].suit] == 3:
                    return cs[0]
                return cs[-1]
            else:
                if Card('♠', 12) in cs:
                    return Card('♠', 12)
                cs = sorted(cs, key = lambda c: -nn(c.number))
                return cs[0]
        else:
            if len(cards_played) == 0: 
                cs = sorted(cs, key = lambda c: nn(c.number) * 5 - _suit[c.suit])
                return cs[0]
            
            elif _suit[cards_played[0].suit] == 2:                   
                if Card('♠', 13) in cards_played or Card('♠', 1) in cards_played:
                    if Card('♠', 12) in cs:
                        return Card('♠', 12)
                cs = sorted(cs, key = lambda c: -(_suit[c.suit] * 15 + nn(c.number)))
                if _suit[cs[0].suit] == 3:
                    return cs[0]
                cs = sorted(cs, key = lambda c: nn(c.number))
                return cs[0]
            elif _suit[cards_played[0].suit] == 3:
                cs = sorted(cs, key = lambda c: nn(c.number))
                if _suit[cs[0].suit] == 3:
                    return cs[0]
                return cs[0]
            else:
                if Card('♠', 12) in cs:
                    return Card('♠', 12)
                cs = sorted(cs, key = lambda c: nn(c.number))
                return cs[0]
        return random.choice(cards)
    





    '''
    decide cards you want to pass to the player next to you
    0->1, 1->2, 2->3, 3->0
    cards: list of cards in your hand
    '''
    def pass_cards(self, cards):
        res = [] # result
        cs = cards[:] # copy
        if Card('♠', 12) in cards: # spade 12 in hand
            cs.remove(Card('♠', 12))
            res.append(Card('♠', 12))
        cs = sorted(cs, key = lambda c: -(_suit[c.suit] * 15 + nn(c.number)))
        while len(res) < 3:
            res.append(cs[0])
            del cs[0]
        return res