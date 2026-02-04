from config import BASE_HP, XP_START, XP_GROWTH, MAX_LEVEL
from items import ARMORS, WEAPONS

ARMOR_SLOTS = {
    "Hattu": "head",
    "Kypärä": "head",
    "Paita": "body",
    "Panssari": "body",
    "Hanskat": "hands",
    "Kengät": "feet",
    "Kilpi": "shield",
    "Tornikilpi": "shield"
}

def parse_bonus(item):
    if "+" in item:
        try:
            return int(item.split("+")[1])
        except ValueError:
            return 0
    return 0

def calculate_ac(armor_items, two_handed=False):
    ac = 0
    for slot, item in armor_items.items():
        if two_handed and slot == "shield":
            continue

        base = item.split(" +")[0]
        if base in ARMORS:
            ac += ARMORS[base]["AC"] + parse_bonus(item)
    return ac

def create_player(stats):
    armor = {
        "head": "Hattu",
        "body": "Paita",
        "hands": "Hanskat",
        "feet": "Kengät",
        "shield": "Kilpi"
    }

    return {
        "level": 1,
        "xp": 0,
        "xp_next": XP_START,
        "stats": stats,
        "hp": BASE_HP + stats["kestävyys"] * 10,
        "max_hp": BASE_HP + stats["kestävyys"] * 10,
        "inventory": ["Potion"] * 5 + list(armor.values()),
        "weapon": "1H-Miekka",
        "two_handed": False,
        "special_lvl": 1,
        "armor": armor,
        "AC": calculate_ac(armor)
    }

def equip_weapon(player, weapon):
    player["weapon"] = weapon
    player["two_handed"] = weapon in [
        "2H-Miekka", "2H-Sotavasara", "2H-Kirves", "Jousi"
    ]

    if player["two_handed"]:
        print("⚠️ 2H-ase käytössä – kilpi ei anna AC:tä")

    player["AC"] = calculate_ac(player["armor"], player["two_handed"])

def equip_item(player, item):
    base = item.split(" +")[0]

    if base in WEAPONS:
        equip_weapon(player, item)
        print(f"🗡️ Varustit aseen: {item}")
        return True

    if base in ARMORS:
        slot = ARMOR_SLOTS.get(base)
        if not slot:
            print("❌ Tuntematon armor-slot")
            return False

        old = player["armor"].get(slot)
        if old:
            print(f"🔁 {old} → {item}")

        player["armor"][slot] = item
        player["AC"] = calculate_ac(player["armor"], player["two_handed"])
        print(f"🛡️ Varustit {item} | AC nyt {player['AC']}")
        return True

    print("❌ Tätä itemiä ei voi varustaa.")
    return False

def add_xp(player, amount):
    player["xp"] += amount
    print(f"✨ +{amount} XP")

    while player["xp"] >= player["xp_next"] and player["level"] < MAX_LEVEL:
        player["xp"] -= player["xp_next"]
        player["level"] += 1
        player["xp_next"] = int(player["xp_next"] * XP_GROWTH)

        player["max_hp"] += 10
        player["hp"] = player["max_hp"]

        if player["special_lvl"] < 5:
            player["special_lvl"] += 1

        print(f"🆙 Level {player['level']}")
