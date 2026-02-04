import random
from items import WEAPONS, ARMORS

def roll_bonus():
    return random.choices(["+1", "+2", "+3"], [60, 30, 10])[0]

def roll_loot():
    """
    Arpoo lootia: aseet, armor tai potion.
    Bonusmuoto on aina ' ITEM +X ' jotta muu peli ei kaadu.
    """
    r = random.random()

    if r < 0.4:  # 40% ase
        return random.choice(WEAPONS) + " " + roll_bonus()  # OK nyt

    elif r < 0.6:  # 20% armor
        armor = random.choice(list(ARMORS.keys()))
        if armor in ["Hattu", "Paita", "Hanskat", "Kengät", "Kilpi"]:
            armor = armor + " " + roll_bonus()
        return armor

    else:  # 40% potion
        return "Potion"
