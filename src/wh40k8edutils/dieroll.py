'''
A class to represent a single die roll, keeping track of re-rolls and
modified values

@author: David Taylor
'''

import random

class DieRoll:
    ''' Class representing an individual die roll
        This class represents a single die roll, and tracks all the required
        information.
        
        Class variables:
            d6_values: faces on a d6
            d3_values: faces on a d3
        
        Instance variables:
            isd3: is a roll of a d3 rather than the typical d6
            orig_value: unmodified value of roll
            rerolled_value: value after any rerolls, for tracking
            mod_value: value after all modifiers taken into account
            rerolled: Has this die been re-rolled? A die can only be rerolled
                    once.
                    
    '''
    
    d6_values = [1,2,3,4,5,6]
    d3_values = [1,2,3]

    def __init__(self, isd3: bool = False):
        '''
        Constructor
        '''
        self.isd3 = isd3
        if isd3:
            self.orig_value = random.choice(self.d3_values)
        else:
            self.orig_value = random.choice(self.d6_values)
        self.rerolled_value = self.orig_value
        self.mod_value = self.orig_value
        self.rerolled = False
        
    def reroll(self):
        self.rerolled_value = random.choice(self.d6_values)
        self.mod_value = self.rerolled_value
        self.rerolled = True

    def apply_mod(self, modifier: int):
        self.mod_value += modifier
        
    def has_passed(self, passval: int):
        if self.mod_value >= passval:
            return True
        else:
            return False
        
    def __repr__(self):
        return "<DieRoll isd3:%s orig_value:%d rerolled_value:%d mod_value:%d rerolled:%s>"\
             % (self.isd3, self.orig_value, self.rerolled_value, self.mod_value, self.rerolled)