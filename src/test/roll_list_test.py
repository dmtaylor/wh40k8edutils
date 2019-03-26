'''
Created on Feb 17, 2019

@author: David Taylor
'''
import unittest
import logging
from wh40k8edutils.roll_list import RollList


class RollListTest(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)
        logging.basicConfig()
        logging.getLogger("RollListTest").setLevel(logging.DEBUG)

    def test_basic_roll(self):
        log = logging.getLogger("RollListTest")
        rolls = RollList(5, 3)
        log.debug(rolls)
        self.assertEquals(rolls.num_rolls, 5)
        self.assertEquals(rolls.passvalue, 3)
        self.assertEquals(len(rolls.rolls), 5)
    
    def test_invalid_rollnum(self):
        with self.assertRaises(ValueError):
            _ = RollList(-1, 2)
            
    def test_invalid_passvalue(self):
        with self.assertRaises(ValueError):
            _ = RollList(3, 1)
        with self.assertRaises(ValueError):
            _ = RollList(3, -1)

    def test_reroll(self):
        log = logging.getLogger("RollListTest")
        rerolls = [1, 2]
        rollt = RollList(6, 3, reroll_values=rerolls)
        log.debug(rollt)
        for item in rollt.rolls:
            if item.orig_value in rerolls:
                self.assertEquals(item.rerolled, True)
    
    def test_modifiers(self):
        log = logging.getLogger("RollListTest")
        modt = 1
        rollt = RollList(5, 3, mod=modt)
        log.debug(rollt)
        for item in rollt.rolls:
            self.assertEquals(item.mod_value, item.orig_value + modt)

    def test_countpasses_failures(self):
        log = logging.getLogger("RollListTest")
        t_passval = 3
        rollt = RollList(7, t_passval)
        log.debug(rollt)
        passcount = 0
        failcount = 0
        for item in rollt.rolls:
            if item.mod_value >= t_passval:
                passcount += 1
            else:
                failcount += 1
                
        self.assertEquals(rollt.count_passes(), passcount)
        self.assertEquals(rollt.count_failures(), failcount)

if __name__ == "__main__":
    unittest.main()