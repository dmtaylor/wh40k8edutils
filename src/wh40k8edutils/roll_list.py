'''

A list of rolls representing a batch of rolls

@author: David
'''

from typing import List
from wh40k8edutils.dieroll import DieRoll

class RollList:
    '''
    classdocs
    '''


    def __init__(self, num_rolls: int, passvalue: int,
                 reroll_values: List[int] = None, mod: int = 0 ):
        '''
        Constructor
        '''
        if num_rolls <= 0:
            raise ValueError('Invalid roll number', num_rolls)
        self.num_rolls = num_rolls
        self.passvalue = passvalue
        self.reroll_values = reroll_values
        self.mod = mod
        
        self.rolls = []
        for _ in range(self.num_rolls):
            self.rolls.append(DieRoll())
        