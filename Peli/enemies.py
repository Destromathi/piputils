import random

ENEMIES = [
    {"name": "Goblin", "hp": (40, 60), "atk": (6, 10)},
    {"name": "Susi", "hp": (50, 70), "atk": (8, 12)},
]

def spawn_enemy():
    e = random.choice(ENEMIES)
    return {
        "name": e["name"],
        "hp": random.randint(*e["hp"]),
        "atk": e["atk"]
    }
