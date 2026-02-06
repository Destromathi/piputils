# utils.py
import random

def roll_damage(weapon):
    return random.randint(weapon.min_dmg, weapon.max_dmg)

def special_hit(chance):
    return random.random() < chance
