import random
from items import RUSTY_SWORD, BASIC_SWORD, IRON_SWORD, STEEL_SWORD, LEGEND_SWORD
from items import LEATHER_ARMOR, HIDE_ARMOR, IRON_ARMOR, STEEL_ARMOR, LEGEND_ARMOR

class Enemy:
    def __init__(self, name, hp, min_dmg, max_dmg, defense=0, loot=None, dialogue=None, once_only=False):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.min_dmg = min_dmg
        self.max_dmg = max_dmg
        self.defense = defense
        self.loot = loot or []
        self.dialogue = dialogue or []
        self.once_only = once_only

    def is_alive(self):
        return self.hp > 0

    def attack(self):
        return random.randint(self.min_dmg, self.max_dmg)

    def generate_loot(self):
        drops = []
        for item in self.loot:
            if item not in drops:
                drops.append(item)
        return drops

    def speak(self):
        if self.dialogue:
            return random.choice(self.dialogue)
        return ""

# Create enemies
def create_enemy(name):
    enemies = {
        # Darkwood (forest)
        "Goblin": Enemy(
            "Goblin", 8, 1, 3,
            loot=[HIDE_ARMOR, BASIC_SWORD],
            dialogue=[
                "Goblin snarls: 'You won't leave here alive!'",
                "Goblin laughs wickedly and swings its club!",
                "Goblin hisses: 'Another victim!'"
            ]
        ),
        "Wolf": Enemy(
            "Wolf", 12, 2, 5,
            loot=[HIDE_ARMOR, BASIC_SWORD],
            dialogue=[
                "The wolf growls and bares its teeth!",
                "The wolf lunges with a vicious snarl!",
                "The wolf's eyes glint as it pounces!"
            ]
        ),
        "Forest Spider": Enemy(
            "Forest Spider", 10, 1, 4,
            loot=[HIDE_ARMOR, BASIC_SWORD],
            dialogue=[
                "The spider hisses as it scuttles forward!",
                "You see multiple legs strike from the shadows!",
                "The spider lunges with venomous fangs!"
            ]
        ),

        # Cave
        "Cave Spider": Enemy(
            "Cave Spider", 16, 2, 4,
            loot=[IRON_SWORD, IRON_ARMOR],
            dialogue=[
                "The cave spider hisses and strikes!",
                "A shadow moves as the spider leaps!",
                "You feel the spider's venomous gaze!"
            ]
        ),
        "Bat Swarm": Enemy(
            "Bat Swarm", 14, 1, 3,
            loot=[IRON_SWORD, IRON_ARMOR],
            dialogue=[
                "Bats screech as they dive at you!",
                "The swarm circles above, waiting to strike!",
                "You feel the wings of dozens of bats brush past!"
            ]
        ),
        "Giant Rat": Enemy(
            "Giant Rat", 16, 1, 4,
            loot=[IRON_SWORD, IRON_ARMOR],
            dialogue=[
                "The rat gnashes its teeth and charges!",
                "A large rat lunges from the darkness!",
                "The rat squeaks and bites fiercely!"
            ]
        ),

        # Tundra
        "Ice Bear": Enemy(
            "Ice Bear", 40, 6, 10, defense=3,
            loot=[STEEL_ARMOR, STEEL_SWORD],
            dialogue=[
                "The Ice Bear roars a chilling roar!",
                "The Ice Bear slams the ground with massive paws!",
                "Snow flies as the Ice Bear charges!"
            ]
        ),
        "Frost Wolf": Enemy(
            "Frost Wolf", 35, 3, 6,
            loot=[STEEL_SWORD],
            dialogue=[
                "The Frost Wolf howls into the icy wind!",
                "The Frost Wolf leaps from behind a snowdrift!",
                "You hear snarls echoing across the tundra!"
            ]
        ),
        "Snow Spider": Enemy(
            "Snow Spider", 26, 2, 5,
            loot=[STEEL_ARMOR],
            dialogue=[
                "The spider scuttles silently over the snow!",
                "Sharp fangs glint as the snow spider strikes!",
                "A sudden leap from the spider startles you!"
            ]
        ),

        # Old Castle
        "Castle Guard": Enemy(
            "Castle Guard", 50, 5, 9, defense=2,
            loot=[LEGEND_SWORD, LEGEND_ARMOR],
            dialogue=[
                "The guard bellows: 'Intruder! Face justice!'",
                "The guard swings his halberd with deadly precision!",
                "The guard roars: 'None shall pass!'"
            ]
        ),
        "Armored Knight": Enemy(
            "Armored Knight", 55, 6, 10, defense=3,
            loot=[LEGEND_ARMOR],
            dialogue=[
                "The knight charges with his sword raised!",
                "Clang! The knight swings his blade in a wide arc!",
                "The knight grunts: 'You dare challenge me?!'"
            ]
        ),
        "Dark Archer": Enemy(
            "Dark Archer", 45, 4, 8, defense=1,
            loot=[LEGEND_SWORD],
            dialogue=[
                "The archer looses a volley of arrows!",
                "A dark figure fires arrows from the battlements!",
                "You feel the sting of a shadowed arrow!"
            ]
        ),

        # Abandoned Dungeon (boss)
        "Castle Lord 'Ironhand'": Enemy(
            "Castle Lord 'Ironhand'", 200, 12, 16, defense=9,
            loot=[LEGEND_SWORD, LEGEND_ARMOR],
            dialogue=[
                "Ironhand shouts: 'I will crush your bones!'",
                "Ironhand bellows: 'None shall challenge me and live!'",
                "Ironhand roars: 'Feel the power of the fortress!'",
                "Ironhand swings with unstoppable fury!"
            ]
        )
    }

    if name not in enemies:
        raise ValueError(f"Enemy '{name}' not found!")
    return enemies[name]
