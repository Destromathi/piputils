from utils import roll_damage, special_hit
import random

# ANSI color codes
RED = "\033[91m"     # enemy damage
YELLOW = "\033[93m"  # enemy yells
GREEN = "\033[92m"   # player damage
BLUE = "\033[94m"    # player action description
RESET = "\033[0m"    # reset color

def fight(player, enemy):
    print(f"\n⚔️ {enemy.name} emerges from the shadows!")

    # Skip fight if boss already defeated
    if getattr(enemy, "once_only", False):
        print(f"{YELLOW}{enemy.name} has already been defeated once!{RESET}")
        return True

    while player.is_alive() and enemy.is_alive():
        # Show HP
        print(f"\n{BLUE}{player.name} HP: {player.hp}/{player.max_hp}{RESET}")
        print(f"{BLUE}{enemy.name} HP: {enemy.hp}/{enemy.max_hp}{RESET}")
        print("Commands: attack, special, inventory, gear, heal")

        cmd = input("> ").lower()

        # ===== Player actions =====
        if cmd == "gear":
            player.show_equipped()
            continue
        if cmd == "heal":
            player.heal()
            continue
        if cmd == "inventory":
            player.show_inventory()
            sub = input("equip / back > ").lower()
            if sub == "equip":
                try:
                    idx = int(input("Choose number > ")) - 1
                    player.equip(idx)
                except ValueError:
                    print("⚠️ Enter a number.")
            continue

        # ===== Player attack =====
        dmg = roll_damage(player.weapon)
        critical = False
        if cmd == "special" and special_hit(player.weapon.crit_chance):
            dmg *= 2
            critical = True

        dmg = max(0, dmg - enemy.defense)
        enemy.hp -= dmg

        # Random player attack text
        attack_texts = [
            f"You swing your {player.weapon.name} with deadly force!",
            f"You strike at {enemy.name}, aiming for a weak spot!",
            f"Your {player.weapon.name} cuts through the air towards {enemy.name}!",
            f"You slash violently, trying to break {enemy.name}'s guard!"
        ]
        if critical:
            attack_texts = [f"💥 CRITICAL STRIKE! {text}" for text in attack_texts]

        print(f"{BLUE}{random.choice(attack_texts)}{RESET} {GREEN}{dmg} damage!{RESET}")

        # ===== Enemy counterattack =====
        if enemy.is_alive():
            taken = player.take_damage(enemy.attack())

            # Random enemy line
            enemy_line = enemy.speak()
            if enemy_line:
                print(f"{YELLOW}{enemy_line}{RESET}")

            # Damage taken message
            print(f"{RED}{enemy.name} hits you for {taken} damage!{RESET}")

    # ===== Loot drop =====
    if not enemy.is_alive():
        loot = enemy.generate_loot()
        if loot:
            print("\n🎁 You found loot:")
            for item in loot:
                if item not in player.inventory:
                    player.inventory.append(item)
                    print(f"- {item}")
                else:
                    print(f"- {item} (already in inventory)")

    return player.is_alive()
