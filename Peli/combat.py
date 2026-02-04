import random

from enemies import spawn_enemy
from skills import special_attack
from player import equip_item, add_xp
from loot import roll_loot

def show_hp(player, enemy_name, enemy_hp):
    show_hp(player, enemy["name"], enemy_hp)
    print(f"\n❤️ Sinä: {player['hp']}/{player['max_hp']} HP")
    print(f"💀 {enemy_name}: {enemy_hp} HP")

def fight(player, is_boss=False, boss_data=None):
    if is_boss:
        enemy = boss_data
        enemy_hp = enemy["hp"]
        print(f"\n👑 Bossi: {enemy['name']} ({enemy_hp} HP)")
    else:
        enemy = spawn_enemy()
        enemy_hp = enemy["hp"]
        print(f"\n👹 Vastassa: {enemy['name']} ({enemy_hp} HP)")

    while enemy_hp > 0 and player["hp"] > 0:
        print("\nKomennot: hyökkää / erikois / potion / inv")
        cmd = input("> ").lower()
        ranged = False

        if cmd == "hyökkää":
            dmg = random.randint(5, 10)
            enemy_hp -= dmg
            print(f"💥 {dmg} dmg")

        elif cmd == "erikois":
            enemy_hp, ranged = special_attack(player, enemy_hp)

        elif cmd == "potion":
            if "Potion" in player["inventory"]:
                player["hp"] = player["max_hp"]
                player["inventory"].remove("Potion")
                print("🧪 HP täynnä")
            else:
                print("❌ Ei potioneita")
            continue

        elif cmd == "inv":
            print("\n🎒 Inventaario:")
            for i, item in enumerate(player["inventory"], 1):
                print(f"{i}) {item}")

            choice = input("Valitse numero varustettavaksi (tai enter): ")
            if choice.isdigit():
                idx = int(choice) - 1
                if 0 <= idx < len(player["inventory"]):
                    equip_item(player, player["inventory"][idx])
                else:
                    print("❌ Väärä numero")
            continue

        else:
            print("❌ Tuntematon komento")
            continue

        if enemy_hp > 0 and not ranged:
            enemy_dmg = random.randint(*enemy["atk"])
            player["hp"] -= enemy_dmg
            print(f"👹 {enemy_dmg} dmg")

    if player["hp"] > 0:
        print("🏆 Voitto!")
        add_xp(player, 50 if not is_boss else 150)

        loot = roll_loot()
        player["inventory"].append(loot)
        print(f"🎁 Loot: {loot}")

        choice = input("Varustetaanko loot? (k/e): ").lower()
        if choice == "k":
            equip_item(player, loot)
