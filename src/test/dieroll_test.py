'''
Created on Feb 15, 2019

@author: David
'''
import unittest
import logging
from wh40k8edutils.dieroll import DieRoll

class DieRollTest(unittest.TestCase):
    
    d6_values = [1, 2, 3, 4, 5, 6]
    d3_values = [1, 2, 3]
    
    def setUp(self):
        unittest.TestCase.setUp(self)
        logging.basicConfig()
        logging.getLogger("DieRollTest").setLevel(logging.INFO)

    def test_init_d6(self):
        log = logging.getLogger("DieRollTest")
        roll = DieRoll()
        log.debug("roll= %s" % roll)
        self.assertIsInstance(roll, DieRoll)
        self.assertIn(roll.orig_value, self.d6_values)
        self.assertEqual(roll.orig_value, roll.rerolled_value)

    def test_reroll(self):
        log = logging.getLogger("DieRollTest")
        roll = DieRoll()
        roll.reroll()
        log.debug("reroll= %s" % roll)
        self.assertEqual(roll.rerolled, True)
        self.assertIn(roll.rerolled_value, self.d6_values)
        
    def test_apply_mod(self):
        log = logging.getLogger("DieRollTest")
        roll = DieRoll()
        roll.apply_mod(-1)
        log.debug("mod_roll= %s" % roll)
        self.assertEqual(roll.mod_value, roll.rerolled_value - 1)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()