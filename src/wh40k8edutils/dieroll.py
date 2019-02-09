'''
A class to represent a single die roll, keeping track of re-rolls and
modified values

@author: David
'''

import random

class DieRoll:
    '''
    classdocs
    '''
    
    d6_values = [1,2,3,4,5,6]
    d3_values = [1,2,3]

    def __init__(self):
        '''
        Constructor
        '''
        self.orig_value = random.choice(self.d6_values)
        self.mod_value = self.orig_value
        self.rerolled = False
        
    def reroll(self):
        self.orig_value = random.choice(self.d6_values)
        self.mod_value = self.orig_value
        self.rerolled = True
        
    def apply_mod(self, modifier: int):
        self.mod_value += modifier
        
    def has_passed(self, passval: int):
        if self.mod_value >= passval:
            return True
        else:
            return False