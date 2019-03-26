'''

A list of rolls representing a batch of rolls

@author: David Taylor
'''

import random
from typing import List
from wh40k8edutils.dieroll import DieRoll

class RollList:
    ''' Primitive for a batch of die rolls with same stats
        This class represents a batch of die rolls, with the same pass value
        and modifiers (e.g. the to hit roll for a unit).
        
        Instance variables:
            num_rolls = Number of rolls in the batch
            passvalue = Number >= the requirement for a pass
            reroll_values = List of values to do re-rolls for.
            mod = Integer modifier to rolls. Applied after rerolls
            onealwaysfails = Will a roll of a one always fail regardless of
                             modifiers (e.g. armor checks)
            rolls = list of DieRoll objects
    '''


    def __init__(self, num_rolls: int, passvalue: int,
                 reroll_values: List[int] = None, mod: int = 0,
                 onealwaysfails: bool = False, isd3: bool = False ):
        '''
        Constructor
        '''
        if num_rolls < 0: # can't roll zero dice
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
            if isd3:
                self.rolls.append(DieRoll(isd3=True))
            else:
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
                item.mod_value = 0

    def count_passes(self) -> int:
        result = 0
        for item in self.rolls:
            if item.has_passed(self.passvalue):
                result += 1
        return result
            
    def count_failures(self) -> int:
        result = 0
        for item in self.rolls:
            if not item.has_passed(self.passvalue):
                result += 1
        return result
    
    def count_mod_values(self, num: int):
        result = 0
        for item in self.rolls:
            if item.mod_value == num:
                result += 1
        
        return result
    
    def count_values(self, num: int):
        result = 0
        for item in self.rolls:
            if item.rerolled_value == num:
                result += 1
        
        return result
    
    def sum_values(self):
        result = 0
        for item in self.rolls:
            result += item.mod_value
            
        return result

    def __repr__(self):
        return "<RollList num_rolls:%d rolls:%s reroll_values:%s mod:%d passvalue:%d onealwaysfails:%s>"\
            % (self.num_rolls, str(self.rolls), str(self.reroll_values),
               self.mod, self.passvalue, str(self.onealwaysfails))
