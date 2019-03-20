'''
Test for determining effectiveness of gauss vs tesla against different
armor saves

@author: David
'''

import tabulate
from wh40k8edutils import attackroll

'''
Global opts on for test
'''
tesla_roll_opts = {'tesla_rule': True}
gauss_roll_opts = {}
iterations = 1
rapid_fire_range = True
immortal_count = 10

def tesla_roll(target_toughness: int, target_save: int):
    volley = immortal_count * 2
    total_shots = 0
    total_hits = 0
    total_wounds = 0
    total_damage = 0
    for _ in range(0, iterations):
        vres = attackroll(volley, 3, 5, target_toughness, target_save, 0, 1, 
                          tesla_roll_opts)
        total_shots += volley
        total_hits += vres[0]
        total_wounds += vres[1]
        total_damage += vres[3]
        
    hit_rate = round(total_hits / total_shots, 5)
    wound_rate = round(total_wounds / total_shots, 5)
    damage_rate = round(total_damage / total_shots, 5)
    avg_hits = round(total_hits / iterations, 5)
    avg_wounds = round(total_wounds / iterations, 5)
    avg_damage = round(total_damage / iterations, 5)
    
    return (total_shots, total_hits, total_wounds, total_damage, avg_hits,
            avg_wounds, avg_damage, hit_rate, wound_rate, damage_rate)

def gauss_roll(target_toughness: int, target_save: int):
    if rapid_fire_range:
        volley = immortal_count * 2
    else:
        volley = immortal_count
    total_shots = 0
    total_hits = 0
    total_wounds = 0
    total_damage = 0
    for _ in range(0, iterations):
        vres = attackroll(volley, 3, 5, target_toughness, target_save, -2, 1, 
                          gauss_roll_opts)
        total_shots += volley
        total_hits += vres[0]
        total_wounds += vres[1]
        total_damage += vres[3]
        
    hit_rate = round(total_hits / total_shots, 5)
    wound_rate = round(total_wounds / total_shots, 5)
    damage_rate = round(total_damage / total_shots, 5)
    avg_hits = round(total_hits / iterations, 5)
    avg_wounds = round(total_wounds / iterations, 5)
    avg_damage = round(total_damage / iterations, 5)
    
    return (total_shots, total_hits, total_wounds, total_damage, avg_hits,
            avg_wounds, avg_damage, hit_rate, wound_rate, damage_rate)

def main():
    pass

if __name__ == '__main__':
    main()