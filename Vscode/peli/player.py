# player.py
from items import RUSTY_SWORD, LEATHER_ARMOR, Weapon, Armor
import random

class Player:
    def __init__(self, name):
        self.name = name
        self.max_hp = 30
        self.hp = self.max_hp

        # Starting equipment
        self.weapon = RUSTY_SWORD
        self.armor = LEATHER_ARMOR

        # Inventory
        self.inventory = [RUSTY_SWORD, LEATHER_ARMOR]

    # =====================
    # Player state
    # =====================
    def is_alive(self):
        return self.hp > 0

    def take_damage(self, dmg):
        reduced = max(0, dmg - self.armor.defense)
        self.hp -= reduced
        return reduced

    # =====================
    # Heal skill
    # =====================
    def heal(self):
        amount = random.randint(8, 16)
        old_hp = self.hp
        self.hp = min(self.max_hp, self.hp + amount)
        print(f"💚 You used your Heal skill! HP {old_hp} → {self.hp}/{self.max_hp}")

    # =====================
    # Show equipped gear
    # =====================
    def show_equipped(self):
        print(f"\n🔹 Equipped Gear:")
        print(f"Weapon: {self.weapon}")
        print(f"Armor: {self.armor}")
        print(f"HP: {self.hp}/{self.max_hp}\n")

    # =====================
    # Show inventory
    # =====================
    def show_inventory(self):
        print("\n📦 Inventory:")
        for i, item in enumerate(self.inventory):
            print(f"{i+1}. {item}")
        print("")

    # =====================
    # Equip an item
    # =====================
    def equip(self, index):
        if index < 0 or index >= len(self.inventory):
            print("⚠️ Invalid choice.")
            return

        item = self.inventory[index]

        if isinstance(item, Weapon):
            old_weapon = self.weapon
            self.weapon = item
            print(f"🗡️ Weapon changed: {old_weapon.name} → {item.name}")
        elif isinstance(item, Armor):
            old_armor = self.armor
            self.armor = item
            print(f"🛡️ Armor changed: {old_armor.name} → {item.name}")
        else:
            print(f"⚠️ {item} cannot be equipped.")
