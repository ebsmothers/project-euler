# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 13:35:48 2015

@author: evansmothers
"""

''' Class representing a poker hand'''

ranklist = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
suitlist = ['C','D','H','S']

f = open("Documents/poker.txt","r")
pokerfile = f.read()
f.close()

class HandofCards(object):
        
    def __init__(self,cards):
        self.cards = cards
    
    def __repr__(self):
        return '<%s: %s %s %s %s %s>' %(self.__class__.__name__,self.cards[0],\
        self.cards[1],self.cards[2],self.cards[3],self.cards[4])
        
    def SortHand(self):
        ranks = [self.card.rank for self.card in self.cards]
        suits = [self.card.suit for self.card in self.cards]
        hand = [[ranks[x],suits[x]] for x in range(5)]
        sortedhand = sorted(hand,key = lambda x: ranklist.index(x[0]))
        return sortedhand
        
    def DetermineHand(self):
        hand = self.SortHand()
        ''' Check for royal flush'''
        if hand[0][0] == 'T' and hand[1][0] == 'J' and hand[2][0] == 'Q' \
        and hand[3][0] == 'K' and hand[4][0] == 'A' and hand [0][1] == \
        hand[1][1] == hand[2][1] == hand[3][1] == hand[4][1]:
            return [9,hand[4][0],hand[3][0],hand[2][0],hand[1][0],hand[0][0]] 
        elif ranklist.index(hand[4][0]) >= 4 and \
        hand[0][0] == ranklist[ranklist.index(hand[4][0]) - 4] and \
        hand[0][0] != hand[1][0] and hand[1][0] != hand[2][0] and \
        hand[2][0] != hand[3][0] and hand[3][0] != hand[4][0] and \
        hand[0][1] == hand[1][1] and hand[1][1] == hand[2][1] \
        and hand[2][1] == hand[3][1] and hand[3][1] == hand[4][1]:
            return [8,hand[4][0],hand[3][0],hand[2][0],hand[1][0],hand[0][0]] 
        elif hand[0][0] == hand[3][0]:
            return [7,hand[3][0],hand[2][0],hand[1][0],hand[0][0],hand[4][0]] 
        elif hand[1][0] == hand[4][0]:
            return [7,hand[4][0],hand[3][0],hand[2][0],hand[1][0],hand[0][0]]
        elif hand[0][0] == hand[2][0] and hand[3][0] == hand[4][0]:
            return [6,hand[2][0],hand[1][0],hand[0][0],hand[4][0],hand[3][0]]
        elif  hand[2][0] == hand[4][0] and hand[0][0] == hand[1][0]:
            return [6,hand[2][0],hand[3][0],hand[4][0],hand[0][0],hand[1][0]]
        elif hand[0][1] == hand[1][1] and hand[1][1] == hand[2][1] and \
        hand[2][1] == hand[3][1] and hand[3][1] == hand[4][1]:
            return [5,hand[4][0],hand[3][0],hand[2][0],hand[1][0],hand[0][0]] 
        elif ranklist.index(hand[4][0]) >= 4 and \
        hand[0][0] == ranklist[ranklist.index(hand[4][0])-4] and\
        hand[0][0] != hand[1][0] and hand[1][0] != hand[2][0] and\
        hand[2][0] != hand[3][0] and hand[3][0] != hand[4][0]:
            return [4,hand[4][0],hand[3][0],hand[2][0],hand[1][0],hand[0][0]] 
        elif hand[0][0] == hand[2][0]:
            return [3,hand[2][0],hand[1][0],hand[0][0],hand[4][0],hand[3][0]]
        elif hand[1][0] == hand[3][0]:
            return [3,hand[1][0],hand[2][0],hand[3][0],hand[4][0],hand[0][0]]
        elif hand[2][0] == hand[4][0]:
            return [3,hand[4][0],hand[3][0],hand[2][0],hand[1][0],hand[0][0]]
        elif hand[0][0] == hand[1][0] and hand[2][0] == hand[3][0]:
            return [2,hand[3][0],hand[2][0],hand[1][0],hand[0][0],hand[4][0]] 
        elif hand[0][0] == hand[1][0] and hand[3][0] == hand[4][0]:
            return [2,hand[4][0],hand[3][0],hand[1][0],hand[0][0],hand[2][0]]
        elif hand[1][0] == hand[2][0] and hand[3][0] == hand[4][0]:
            return [2,hand[4][0],hand[3][0],hand[2][0],hand[1][0],hand[0][0]]
        elif hand[0][0] == hand[1][0]:
            return [1,hand[1][0],hand[0][0],hand[4][0],hand[3][0],hand[2][0]]
        elif hand[1][0] == hand[2][0]:
            return [1,hand[2][0],hand[1][0],hand[4][0],hand[3][0],hand[0][0]]
        elif hand[2][0] == hand[3][0]:
            return [1,hand[3][0],hand[2][0],hand[4][0],hand[1][0],hand[0][0]]
        elif hand[3][0] == hand[4][0]:
            return [1,hand[4][0],hand[3][0],hand[2][0],hand[1][0],hand[0][0]]
        else:
            return [0,hand[4][0],hand[3][0],hand[2][0],hand[1][0],hand[0][0]] 
              
        
        
        
        
        
    
''' Class representing an individual card'''   
class Card(object):
    
    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit
        
    def __repr__(self):
        return '<%s: %s %s>' % (self.__class__.__name__,self.rank,self.suit)


player1wins = 0   
     
for i in range(1000):
    player1strn = pokerfile[30*i:30*i+15]
    print(player1strn)
    player2strn = pokerfile[30*i+15:30*i+30]
    print(player2strn)
    player1card1 = Card(player1strn[0],player1strn[1])
    player1card2 = Card(player1strn[3],player1strn[4])
    player1card3 = Card(player1strn[6],player1strn[7])
    player1card4 = Card(player1strn[9],player1strn[10])
    player1card5 = Card(player1strn[12],player1strn[13])
    player2card1 = Card(player2strn[0],player2strn[1])
    player2card2 = Card(player2strn[3],player2strn[4])
    player2card3 = Card(player2strn[6],player2strn[7])
    player2card4 = Card(player2strn[9],player2strn[10])
    player2card5 = Card(player2strn[12],player2strn[13])
    player1cards = [player1card1,player1card2,player1card3,player1card4, \
    player1card5]
    player2cards = [player2card1,player2card2,player2card3,player2card4, \
    player2card5]
    player1hand = HandofCards(player1cards)
    player2hand = HandofCards(player2cards)
    print(player1hand.DetermineHand()[0])
    print(player2hand.DetermineHand()[0])
    
    if player1hand.DetermineHand()[0] > player2hand.DetermineHand()[0]:
        print('Player 1 wins hand {}'.format(i))
        player1wins += 1
    elif player1hand.DetermineHand()[0] == player2hand.DetermineHand()[0] \
    and ranklist.index(player1hand.DetermineHand()[1]) > \
    ranklist.index(player2hand.DetermineHand()[1]):
        print('Player 1 wins hand {}'.format(i))
        player1wins += 1
    elif player1hand.DetermineHand()[0] == player2hand.DetermineHand()[0] \
    and ranklist.index(player1hand.DetermineHand()[1]) == \
    ranklist.index(player2hand.DetermineHand()[1]) and \
    ranklist.index(player1hand.DetermineHand()[2]) > \
    ranklist.index(player2hand.DetermineHand()[2]):
        print('Player 1 wins hand {}'.format(i))
        player1wins += 1
    elif player1hand.DetermineHand()[0] == player2hand.DetermineHand()[0] \
    and ranklist.index(player1hand.DetermineHand()[1]) == \
    ranklist.index(player2hand.DetermineHand()[1]) and \
    ranklist.index(player1hand.DetermineHand()[2]) == \
    ranklist.index(player2hand.DetermineHand()[2]) and \
    ranklist.index(player1hand.DetermineHand()[3]) > \
    ranklist.index(player2hand.DetermineHand()[3]):
        print('Player 1 wins hand {}'.format(i))
        player1wins += 1
    elif player1hand.DetermineHand()[0] == player2hand.DetermineHand()[0] \
    and ranklist.index(player1hand.DetermineHand()[1]) == \
    ranklist.index(player2hand.DetermineHand()[1]) and \
    ranklist.index(player1hand.DetermineHand()[2]) == \
    ranklist.index(player2hand.DetermineHand()[2]) and \
    ranklist.index(player1hand.DetermineHand()[3]) == \
    ranklist.index(player2hand.DetermineHand()[3]) and \
    ranklist.index(player1hand.DetermineHand()[4]) > \
    ranklist.index(player2hand.DetermineHand()[4]):
        print('Player 1 wins hand {}'.format(i))
        player1wins += 1
    elif player1hand.DetermineHand()[0] == player2hand.DetermineHand()[0] \
    and ranklist.index(player1hand.DetermineHand()[1]) == \
    ranklist.index(player2hand.DetermineHand()[1]) and \
    ranklist.index(player1hand.DetermineHand()[2]) == \
    ranklist.index(player2hand.DetermineHand()[2]) and \
    ranklist.index(player1hand.DetermineHand()[3]) == \
    ranklist.index(player2hand.DetermineHand()[3]) and \
    ranklist.index(player1hand.DetermineHand()[4]) == \
    ranklist.index(player2hand.DetermineHand()[4]) and \
    ranklist.index(player1hand.DetermineHand()[5]) > \
    ranklist.index(player2hand.DetermineHand()[5]):
        print('Player 1 wins hand {}'.format(i))
        player1wins += 1
print(player1wins)
 
'''card1 = Card('4','S')
card2 = Card('2','C')
card3 = Card('3','D')
card4 = Card('8','H')
card5 = Card('T','S')
cards = [card1,card2,card3,card4,card5]
hand = HandofCards(cards)
print(hand.DetermineHand())'''



   