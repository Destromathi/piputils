import random

def special_attack(player, enemy_hp):
    lvl = player["special_lvl"]
    weapon = player["weapon"]

    if "Jousi" in weapon:
        dmg = random.randint(10, 15) + lvl * 2
        print(f"🏹 Tarkka laukaus {dmg}")
        return enemy_hp - dmg, True

    dmg = random.randint(8, 12) + lvl * 2
    print(f"⚔️ Erikoishyökkäys {dmg}")
    return enemy_hp - dmg, False
