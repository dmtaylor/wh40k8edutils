'''
Created on Feb 28, 2019

@author: David
'''


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
    