'''
Test for determining effectiveness of gauss vs tesla against different
armor saves

@author: David
'''

import os
import platform
import csv
#from tabulate import tabulate
from wh40k8edutils import attackroll
from numpy import save

'''
Global opts on for test
'''
tesla_roll_opts = {'tesla_rule': True}
tesla_mwbd_roll_opts = {'tesla_rule': True, 'necron_mwbd': True}
gauss_roll_opts = {}
iterations = 10000
immortal_count = 10
immortal_in_rapid = immortal_count

def tesla_roll(target_toughness: int, target_save: int):
    volley = immortal_count * 2
    total_shots = 0
    total_hits = 0
    total_wounds = 0
    total_damage = 0
    for _ in range(0, iterations):
        vres = attackroll.roll(volley, 3, 5, target_toughness, target_save, 0, 1, 
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
    
    return ("Tesla", target_toughness, target_save,
            total_shots, total_hits, total_wounds, total_damage, avg_hits,
            avg_wounds, avg_damage, hit_rate, wound_rate, damage_rate)

def gauss_roll(target_toughness: int, target_save: int):
    volley = (immortal_in_rapid * 2) + (immortal_count - immortal_in_rapid)
    total_shots = 0
    total_hits = 0
    total_wounds = 0
    total_damage = 0
    for _ in range(0, iterations):
        vres = attackroll.roll(volley, 3, 5, target_toughness, target_save, 2, 1, 
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
    
    return ("Gauss", target_toughness, target_save, total_shots, total_hits, total_wounds,
            total_damage, avg_hits,
            avg_wounds, avg_damage, hit_rate, wound_rate, damage_rate)

def main():
    header = ("Type", "Toughness", "Sv", "Total shots", "Total Hits",
              "Total Wounds","Total Damage", 
              "Average Hits", "Average Wounds", "Average Damage", "Hit Rate",
              "Wound Rate", "Damage Rate")
    
    table = []
    
    for toughness in range(4,7):
        for save in range(2, 7):
            table.append(tesla_roll(toughness, save))
            table.append(gauss_roll(toughness, save))
            print("Rolls for toughness=%d sv=%d" % (toughness, save))
            
    if os.path.isfile("teslavsgauss_results.csv"):
        os.remove("teslavsgauss_results.csv")
        
    # windows newline fix
    if platform.system() == 'Windows':
        f = open("teslavsgauss_results.csv", 'w', newline='')
    else:
        f = open("teslavsgauss_results.csv", 'w')
            
    f_csv = csv.writer(f)
    f_csv.writerow(header)
    f_csv.writerows(table)
    
    f.close()

if __name__ == '__main__':
    main()