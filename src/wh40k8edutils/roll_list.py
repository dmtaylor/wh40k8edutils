'''

A list of rolls representing a batch of rolls

@author: David Taylor
'''

import random
from typing import List
from wh40k8edutils.dieroll import DieRoll

class RollList:
    '''
    classdocs
    '''


    def __init__(self, num_rolls: int, passvalue: int,
                 reroll_values: List[int] = None, mod: int = 0,
                 onealwaysfails: bool = False ):
        '''
        Constructor
        '''
        if num_rolls <= 0: # can't roll zero dice
            raise ValueError('Invalid roll number', num_rolls)
        self.num_rolls = num_rolls
        if passvalue <= 1: # No such thing as a natural 1+ roll
            raise ValueError('Invalid pass value')
        self.passvalue = passvalue
        self.reroll_values = reroll_values
        self.mod = mod
        self.onealwaysfails = onealwaysfails
        
        random.seed()
        self.rolls = []
        for _ in range(self.num_rolls):
            self.rolls.append(DieRoll())
            
        self.do_rerolls()
        self.apply_mod()
        
    
    def do_rerolls(self):
        if self.reroll_values == None:
            return
        for item in self.rolls:
            if item.orig_value in self.reroll_values and item.rerolled == False:
                item.reroll()
                
    def apply_mod(self):
        for item in self.rolls:
            item.apply_mod(self.mod)
            if self.onealwaysfails and item.orig_value == 1:
                item.mod_value = 1

    def count_passes(self) -> int:
        result = 0
        #self.do_rerolls()
        #self.apply_mod()
        for item in self.rolls:
            if item.has_passed(self.passvalue):
                result += 1
        return result
            
    def count_failures(self) -> int:
        result = 0
        #self.do_rerolls()
        #self.apply_mod()
        for item in self.rolls:
            if not item.has_passed(self.passvalue):
                result += 1
        return result
