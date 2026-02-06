class Weapon:
    def __init__(self, name, min_dmg, max_dmg, crit_chance=0.1):
        self.name = name
        self.min_dmg = min_dmg
        self.max_dmg = max_dmg
        self.crit_chance = crit_chance

    def __str__(self):
        return f"{self.name} ({self.min_dmg}-{self.max_dmg} dmg)"

class Armor:
    def __init__(self, name, defense):
        self.name = name
        self.defense = defense

    def __str__(self):
        return f"{self.name} (+{self.defense} def)"

# Example items
RUSTY_SWORD = Weapon("Rusty Sword", 1, 4)
BASIC_SWORD = Weapon("Basic Sword", 2, 5)
IRON_SWORD = Weapon("Iron Sword", 3, 7)
STEEL_SWORD = Weapon("Steel Sword", 5, 10)
LEGEND_SWORD = Weapon("Legendary Sword", 8, 15)

LEATHER_ARMOR = Armor("Leather Armor", 1)
HIDE_ARMOR = Armor("Hide Armor", 2)
IRON_ARMOR = Armor("Iron Armor", 3)
STEEL_ARMOR = Armor("Steel Armor", 5)
LEGEND_ARMOR = Armor("Legendary Armor", 8)
