import random

BOSSES = {
    "Goblin King": {
        "hp": 120,
        "atk": (10, 18),
        "special": "Myrskysuoja"
    },
    "Luuranko Lordi": {
        "hp": 150,
        "atk": (12, 20),
        "special": "Luupommi"
    }
}

def spawn_boss():
    name = random.choice(list(BOSSES.keys()))
    boss = BOSSES[name].copy()
    boss["name"] = name

    print(f"\n👑 Bossi ilmestyy: {name}!")
    print(f"HP: {boss['hp']}, Erikoiskyky: {boss['special']}")
    return boss
