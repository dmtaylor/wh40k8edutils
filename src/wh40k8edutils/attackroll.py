'''
Created on Feb 28, 2019

@author: David
'''
from wh40k8edutils.roll_list import RollList


def roll(attacknumber: int, attackskill: int, strength: int, toughness: int,
         armor: int, ap: int, damage, rollmods: dict):
    """ Primary rolling method. Takes the following args
        attacknumber: number of attacks
        attackskill: attackers skill (ws/bs)
        strength/toughness: attackers S, defenders T
        armor: defenders armor value
        ap: ap value of attacks
        damage: damage per attack, supports int, d3, and d6
        rollmods: misc modifiers for attack. Rerolls, special rules, etc
    """
    
    # number validation
    if rollmods == None:
        raise ValueError("rollmods is None")
    
    if attacknumber <= 0:
        raise ValueError("Invalid attack number", attacknumber)
    if attackskill <= 0 or attackskill >= 7:
        raise ValueError("Invalid attack skill", attackskill)
    if strength <= 0:
        raise ValueError("Invalid strength", strength)
    if toughness <= 0:
        raise ValueError("Invalid toughness", toughness)
    if armor <= 0:
        raise ValueError("Invalid armor", armor)
    if ap < 0:
        raise ValueError("Invalid ap", ap)
    
    if isinstance(damage, str):
        if damage != "d6" and damage != "d3":
            raise ValueError("Unsupported damage type", damage)
    elif isinstance(damage, int):
        if damage <= 0:
            raise ValueError("Invalid damage", damage)
    else:
        raise TypeError("Damage is unsupported type", type(damage))
    
    hits = hit_roll(attacknumber, attackskill, rollmods)
    wounds = wound_roll(hits, woundon(strength, toughness), rollmods)
    

def hit_roll(num_attacks: int, attack_skill: int, rollmods: dict):
    
    if 'hit_mod' in rollmods:
        mod = rollmods['hit_mod']
    else:
        mod = 0
        
    if 'reroll_ones_hit' in rollmods:
        rerolls = [1]
    elif 'reroll_misses_hit' in rollmods:
        rerolls = []
        for i in range(1, attack_skill):
            rerolls.append(i)
    else:
        rerolls = None
        
    attackroll = RollList(num_attacks, attack_skill, reroll_values = rerolls,
                          mod= mod)
    
    passcount = attackroll.count_passes()
    
    if 'tesla_rule' in rollmods:
        for item in attackroll.rolls:
            if item.mod_value >= 6:
                passcount += 2
    
    return passcount

def wound_roll(num_wounds: int, woundon: int, rollmods: dict):
    if 'wound_mod' in rollmods:
        mod = rollmods['wound_mod']
    else:
        mod = 0
        
    if 'reroll_ones_wound' in rollmods:
        rerolls = [1]
    elif 'reroll_misses_wound' in rollmods:
        rerolls = []
        for i in range(1,woundon):
            rerolls.append(i)
    else:
        rerolls = []
        
    woundrolls = RollList(num_wounds, woundon, reroll_values = rerolls,
                          mod = mod)
    
    return woundrolls.count_passes()

def woundon(strength:int, toughness):
    if(strength == toughness):
        return 4
    elif(strength < toughness and strength > 2*toughness):
        return 5
    elif(strength <= 2*toughness):
        return 6
    elif(toughness < strength and toughness > 2*strength):
        return 3
    elif(toughness <= 2*strength):
        return 2
    else:
        raise ValueError('Arithmetic error with woundson calc', strength,
                         toughness)
