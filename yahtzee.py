#import packages
from random import randint
import numpy as np
import pygame as pg

 
 #define the Dice class
class Dice:
    def __init__(self):
        self.current_throw = [randint(1, 6) for i in range(0, 5)]       
    def roll(self, throw):
        for j in [int(i) - 1 for i in throw]:
            self.current_throw[j] = randint(1, 6) 
    def manual_set(self, a):
        self.current_throw = a

class Aces:
    def __init__(self):
        self.name = 'Aces'
        self.possible = False
        self.points = 0
        self.filled = False
    def is_possible(self, current_throw):
        unique, counts= np.unique(current_throw, return_counts = True)
        self.possible = any(unique == 1)
    def score(self, current_throw):
        self.points = np.sum([x for x in current_throw if x == 1])
        
class Twos:
    def __init__(self):
        self.name = 'Twos'
        self.possible = False
        self.points = 0
        self.filled = False
    def is_possible(self, current_throw):
        unique, counts= np.unique(current_throw, return_counts = True)
        self.possible = any(unique == 2)
    def score(self, current_throw):
        self.points = np.sum([x for x in current_throw if x == 2])

class Threes:
    def __init__(self):
        self.name = 'Threes'
        self.possible = False
        self.points = 0
        self.filled = False
    def is_possible(self, current_throw):
        unique, counts= np.unique(current_throw, return_counts = True)
        self.possible = any(unique == 3)
    def score(self, current_throw):
        self.points = np.sum([x for x in current_throw if x == 3])
        
class Fours:
    def __init__(self):
        self.name = 'Fours'
        self.possible = False
        self.points = 0
        self.filled = False
    def is_possible(self, current_throw):
        unique, counts= np.unique(current_throw, return_counts = True)
        self.possible = any(unique == 4)
    def score(self, current_throw):
        self.points = np.sum([x for x in current_throw if x == 4])
        
class Fives:
    def __init__(self):
        self.name = 'Fives'
        self.possible = False
        self.points = 0
        self.filled = False
    def is_possible(self, current_throw):
        unique, counts= np.unique(current_throw, return_counts = True)
        self.possible = any(unique == 5)
    def score(self, current_throw):
        self.points = np.sum([x for x in current_throw if x == 5])
        
class Sixes:
    def __init__(self):
        self.name = 'Sixes'
        self.possible = False
        self.points = 0
        self.filled = False
    def is_possible(self, current_throw):
        unique, counts= np.unique(current_throw, return_counts = True)
        self.possible = any(unique == 6)
    def score(self, current_throw):
        self.points = np.sum([x for x in current_throw if x == 6])
        
class Three_of_kind:
    def __init__(self):
        self.name = 'Three of a kind'
        self.possible = False
        self.points = 0
        self.filled = False
    def is_possible(self, current_throw):
        unique, counts= np.unique(current_throw, return_counts = True)
        self.possible = any(counts >= 3)
    def score(self, current_throw):
        self.points = np.sum(current_throw)
            
class Four_of_kind:
    def __init__(self):
        self.name = 'Four of a kind'
        self.possible = False
        self.points = 0
        self.filled = False
    def is_possible(self, current_throw):
        unique, counts = np.unique(current_throw, return_counts = True)
        self.possible = any(counts >= 4)
    def score(self, current_throw):
        self.points = np.sum(current_throw)      

class Full_house:
    def __init__(self):
        self.name = 'Full House'
        self.possible = False
        self.points = 0
        self.filled = False
    def is_possible(self, current_throw):
        unique, counts = np.unique(current_throw, return_counts = True)
        self.possible = any(counts == 3) and any(counts == 2) and len(unique == 2)
    def score(self, current_throw):
        self.points = 25  

class Small_straight:
    def __init__(self):
        self.name = 'Small Straight'
        self.possible = False
        self.points = 0
        self.filled = False
    def is_possible(self, current_throw):
        s = ''.join(map(str, np.unique(np.sort(current_throw))))
        self.possible = '1234' in s or '2345' in s or '3456' in s
    def score(self, current_throw):
        self.points = 30  
    
class Large_straight:
    def __init__(self):
        self.name = 'Large Straight'
        self.possible = False
        self.points = 0
        self.filled = False
    def is_possible(self, current_throw):
        s = ''.join(map(str, np.sort(current_throw)))
        self.possible = s in ['12345', '23456']
    def score(self, current_throw):
        self.points = 40 

class Yahtzee:
    def __init__(self):
        self.name = 'Yahtzee'
        self.possible = False
        self.points = 0
        self.filled = False
    def is_possible(self, current_throw):
        unique, counts = np.unique(current_throw, return_counts = True)
        self.possible = any(counts == 5)
    def score(self, current_throw):
        self.points = 50

class Chance:
    def __init__(self):
        self.name = 'Chance'
        self.possible = False
        self.points = 0
        self.filled = False
    def is_possible(self, current_throw):
        self.possible = True
    def score(self, current_throw):
        self.points = np.sum(current_throw)
        

class Scorecard:
    def __init__(self):
        self.categories = [Aces(), Twos(), Threes(), Fours(), Fives(), Sixes(), Three_of_kind(), Four_of_kind(), Full_house(), Small_straight(), Large_straight(), Yahtzee(), Chance()]
        self.scores = np.zeros([len(self.categories)])


scorecard = Scorecard()
for turn in range(0, 14):
    
    # present throw, ask input player, roll again
    num_throws = 3
    for i in range(0, num_throws):
        if i == 0:
            player1 = Dice()
            #player1.manual_set([6,2,5,4,3])
        else:
            keep_dice = np.array(input('Press y if you want to keep all the dice, press any key if you want to roll the dice again '))
            if keep_dice == 'y':
                print('Your throw is: ', player1.current_throw)
                break
            throw_again_idx = np.array(input('Which di(c)e would you like to roll again? use a space between the numbers (e.g. 1 2 5) ').split())
    
            player1.roll(throw_again_idx) 
            
            
        print('You rolled: ', player1.current_throw)
    
    
    for i, category in enumerate(scorecard.categories):
        category.is_possible(player1.current_throw)
        category.score(player1.current_throw)
        
        if category.possible and not category.filled:
            # keep track of possible records
            print(i, category.name, 'points: ', category.points)
    
    
    while True:     
        answer = int(input('Which Category do you like to fill in?'))
        
        if not scorecard.categories[answer].filled:
            scorecard.categories[answer].filled = True
            scorecard.scores[answer] = scorecard.categories[answer].points
            break
        else:
            print('Already filled, please try again...')
    
    
    
    for i, category in enumerate(scorecard.categories):
        print(category.filled)
    print(scorecard.scores)